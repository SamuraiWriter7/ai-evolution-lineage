#!/usr/bin/env python3

"""
AI Evolution Lineage Graph (AELG) v0.1
Reference Validator

Validates structural and semantic consistency
of an AELG evolution ledger.

Requirements:
    Python 3.11+
    Python standard library only

Usage:
    python scripts/validate.py
    python scripts/validate.py path/to/ledger.json

Exit codes:
    0: Validation passed
    1: Validation failed

Validation does not establish historical accuracy,
source authenticity, or causal truth.
"""

from __future__ import annotations

import json
import re
import sys

from collections import deque
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit


# ============================================================
# Specification Constants
# ============================================================

SPEC_VERSION = "0.1.0"

ROOT_DIR = Path(__file__).resolve().parent.parent

DEFAULT_FILE = (
    ROOT_DIR
    / "examples"
    / "sample-evolution.json"
)


EVOLUTION_LAYERS = {
    "technology",
    "implementation",
    "question",
    "resource",
    "governance",
}


RELATIONSHIP_TYPES = {
    "derived_from",
    "influenced_by",
    "responds_to",
    "enabled_by",
    "constrained_by",
    "related_to",
}


ANTECEDENT_TYPES = {
    "derived_from",
    "influenced_by",
    "responds_to",
    "enabled_by",
    "constrained_by",
}


EVIDENCE_STATUSES = {
    "confirmed",
    "inferred",
    "unknown",
}


EVIDENCE_REQUIRED_STATUSES = {
    "confirmed",
    "inferred",
}


EVIDENCE_SOURCE_TYPES = {
    "research_paper",
    "technical_report",
    "official_statement",
    "release_note",
    "repository",
    "user_feedback",
    "regulatory_document",
    "incident_report",
    "evaluation_report",
    "other",
}


EVENT_ID_PATTERN = re.compile(
    r"EVT-[0-9]+"
)

RELATIONSHIP_ID_PATTERN = re.compile(
    r"REL-[0-9]+"
)

EVIDENCE_ID_PATTERN = re.compile(
    r"EVD-[0-9]+"
)

DATE_PATTERN = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}"
)


ROOT_FIELDS = {
    "spec_version",
    "events",
    "relationships",
    "evidence",
}


EVENT_FIELDS = {
    "event_id",
    "date",
    "layer",
    "title",
    "description",
    "actors",
    "evidence_ids",
}


RELATIONSHIP_FIELDS = {
    "relationship_id",
    "source_event_id",
    "target_event_id",
    "type",
    "evidence_status",
    "evidence_ids",
    "description",
}


EVIDENCE_FIELDS = {
    "evidence_id",
    "source_type",
    "source_uri",
    "description",
}


# ============================================================
# Validation Error
# ============================================================

class ValidationError(Exception):
    """Raised when an AELG validation rule is violated."""

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:

        self.code = code
        self.message = message

        super().__init__(
            f"{code}: {message}"
        )


def fail(
    code: str,
    message: str,
) -> None:

    raise ValidationError(
        code,
        message,
    )


# ============================================================
# Basic Validation Helpers
# ============================================================

def require_object(
    value: object,
    context: str,
    code: str = "E004",
) -> None:

    if not isinstance(value, dict):

        fail(
            code,
            f"{context} must be an object.",
        )


def require_array(
    value: object,
    context: str,
) -> None:

    if not isinstance(value, list):

        fail(
            "E004",
            f"{context} must be an array.",
        )


def require_non_empty_string(
    value: object,
    context: str,
) -> None:

    if (
        not isinstance(value, str)
        or not value.strip()
    ):

        fail(
            "E004",
            f"{context} must be a non-empty string.",
        )


def require_fields(
    record: dict,
    required_fields: set[str],
    context: str,
) -> None:

    missing = (
        required_fields
        - set(record.keys())
    )

    if missing:

        fail(
            "E003",
            (
                f"{context} is missing required fields: "
                f"{', '.join(sorted(missing))}"
            ),
        )


def reject_undefined_fields(
    record: dict,
    allowed_fields: set[str],
    context: str,
) -> None:

    undefined = (
        set(record.keys())
        - allowed_fields
    )

    if undefined:

        fail(
            "E020",
            (
                f"{context} contains undefined fields: "
                f"{', '.join(sorted(undefined))}"
            ),
        )


def validate_object_fields(
    record: object,
    fields: set[str],
    context: str,
) -> None:

    require_object(
        record,
        context,
    )

    require_fields(
        record,
        fields,
        context,
    )

    reject_undefined_fields(
        record,
        fields,
        context,
    )


def require_enum(
    value: object,
    allowed_values: set[str],
    context: str,
    code: str,
) -> None:

    if (
        not isinstance(value, str)
        or value not in allowed_values
    ):

        fail(
            code,
            (
                f"{context} has unsupported value "
                f"{value!r}. "
                f"Allowed values: "
                f"{', '.join(sorted(allowed_values))}"
            ),
        )


def validate_identifier(
    value: object,
    pattern: re.Pattern,
    context: str,
) -> None:

    if (
        not isinstance(value, str)
        or pattern.fullmatch(value) is None
    ):

        fail(
            "E005",
            f"{context} has invalid identifier: {value!r}",
        )


def require_unique_entries(
    values: list[str],
    context: str,
) -> None:

    seen = set()

    for value in values:

        if value in seen:

            fail(
                "E019",
                (
                    f"{context} contains duplicate "
                    f"entry: {value!r}"
                ),
            )

        seen.add(value)


# ============================================================
# Date Validation
# ============================================================

def validate_date(
    value: object,
    context: str,
) -> date:

    if (
        not isinstance(value, str)
        or DATE_PATTERN.fullmatch(value) is None
    ):

        fail(
            "E016",
            (
                f"{context} must use "
                f"YYYY-MM-DD format."
            ),
        )

    try:

        return date.fromisoformat(value)

    except ValueError:

        fail(
            "E016",
            (
                f"{context} is not a valid "
                f"Gregorian calendar date: {value!r}"
            ),
        )


# ============================================================
# URI Validation
# ============================================================

def validate_source_uri(
    value: object,
    context: str,
) -> None:

    if (
        not isinstance(value, str)
        or not value
    ):

        fail(
            "E017",
            f"{context} must be a non-empty URI.",
        )

    if any(
        character.isspace()
        or ord(character) < 32
        or ord(character) == 127
        for character in value
    ):

        fail(
            "E017",
            (
                f"{context} must not contain "
                f"whitespace or control characters."
            ),
        )

    if re.search(
        r'[^A-Za-z0-9:/?#\[\]@!$&\'()*+,;=._~%\-]',
        value,
    ):

        fail(
            "E017",
            f"{context} contains invalid URI characters.",
        )

    if re.search(
        r"%(?![0-9A-Fa-f]{2})",
        value,
    ):

        fail(
            "E017",
            f"{context} contains invalid percent encoding.",
        )

    try:

        parsed = urlsplit(value)

        hostname = parsed.hostname

        # Accessing the port also detects
        # malformed or out-of-range port values.
        _ = parsed.port

    except ValueError as error:

        fail(
            "E017",
            f"{context} contains an invalid URI: {error}",
        )

    if parsed.scheme.lower() not in {
        "http",
        "https",
    }:

        fail(
            "E017",
            (
                f"{context} must use "
                f"HTTP or HTTPS."
            ),
        )

    if not parsed.netloc or not hostname:

        fail(
            "E017",
            (
                f"{context} must contain "
                f"a non-empty host."
            ),
        )


# ============================================================
# Actor Validation
# ============================================================

def validate_actors(
    actors: object,
    context: str,
) -> None:

    require_array(
        actors,
        context,
    )

    for index, actor in enumerate(actors):

        require_non_empty_string(
            actor,
            f"{context}[{index}]",
        )

    require_unique_entries(
        actors,
        context,
    )


# ============================================================
# Evidence Reference Validation
# ============================================================

def validate_evidence_ids(
    evidence_ids: object,
    context: str,
) -> None:

    require_array(
        evidence_ids,
        context,
    )

    for index, evidence_id in enumerate(
        evidence_ids
    ):

        validate_identifier(
            evidence_id,
            EVIDENCE_ID_PATTERN,
            f"{context}[{index}]",
        )

    require_unique_entries(
        evidence_ids,
        context,
    )


# ============================================================
# Root Structure Validation
# ============================================================

def validate_root(
    ledger: object,
) -> None:

    require_object(
        ledger,
        "Ledger",
        code="E001",
    )

    require_fields(
        ledger,
        ROOT_FIELDS,
        "Ledger",
    )

    reject_undefined_fields(
        ledger,
        ROOT_FIELDS,
        "Ledger",
    )

    if ledger["spec_version"] != SPEC_VERSION:

        fail(
            "E002",
            (
                "Unsupported specification version: "
                f"{ledger['spec_version']!r}. "
                f"Expected {SPEC_VERSION}."
            ),
        )

    require_array(
        ledger["events"],
        "events",
    )

    require_array(
        ledger["relationships"],
        "relationships",
    )

    require_array(
        ledger["evidence"],
        "evidence",
    )

    if not ledger["events"]:

        fail(
            "E021",
            "The events array must contain at least one event.",
        )


# ============================================================
# Evolution Event Validation
# ============================================================

def validate_event(
    event: object,
    index: int,
) -> date:

    context = f"events[{index}]"

    validate_object_fields(
        event,
        EVENT_FIELDS,
        context,
    )

    validate_identifier(
        event["event_id"],
        EVENT_ID_PATTERN,
        f"{context}.event_id",
    )

    context = event["event_id"]

    event_date = validate_date(
        event["date"],
        f"{context}.date",
    )

    require_enum(
        event["layer"],
        EVOLUTION_LAYERS,
        f"{context}.layer",
        "E007",
    )

    require_non_empty_string(
        event["title"],
        f"{context}.title",
    )

    require_non_empty_string(
        event["description"],
        f"{context}.description",
    )

    validate_actors(
        event["actors"],
        f"{context}.actors",
    )

    validate_evidence_ids(
        event["evidence_ids"],
        f"{context}.evidence_ids",
    )

    return event_date


# ============================================================
# Evidence Record Validation
# ============================================================

def validate_evidence_record(
    evidence: object,
    index: int,
) -> None:

    context = f"evidence[{index}]"

    validate_object_fields(
        evidence,
        EVIDENCE_FIELDS,
        context,
    )

    validate_identifier(
        evidence["evidence_id"],
        EVIDENCE_ID_PATTERN,
        f"{context}.evidence_id",
    )

    context = evidence["evidence_id"]

    require_enum(
        evidence["source_type"],
        EVIDENCE_SOURCE_TYPES,
        f"{context}.source_type",
        "E018",
    )

    validate_source_uri(
        evidence["source_uri"],
        f"{context}.source_uri",
    )

    require_non_empty_string(
        evidence["description"],
        f"{context}.description",
    )


# ============================================================
# Relationship Validation
# ============================================================

def validate_relationship(
    relationship: object,
    index: int,
) -> None:

    context = f"relationships[{index}]"

    validate_object_fields(
        relationship,
        RELATIONSHIP_FIELDS,
        context,
    )

    validate_identifier(
        relationship["relationship_id"],
        RELATIONSHIP_ID_PATTERN,
        f"{context}.relationship_id",
    )

    context = relationship["relationship_id"]

    validate_identifier(
        relationship["source_event_id"],
        EVENT_ID_PATTERN,
        f"{context}.source_event_id",
    )

    validate_identifier(
        relationship["target_event_id"],
        EVENT_ID_PATTERN,
        f"{context}.target_event_id",
    )

    require_enum(
        relationship["type"],
        RELATIONSHIP_TYPES,
        f"{context}.type",
        "E008",
    )

    require_enum(
        relationship["evidence_status"],
        EVIDENCE_STATUSES,
        f"{context}.evidence_status",
        "E009",
    )

    validate_evidence_ids(
        relationship["evidence_ids"],
        f"{context}.evidence_ids",
    )

    require_non_empty_string(
        relationship["description"],
        f"{context}.description",
    )

    source_id = relationship[
        "source_event_id"
    ]

    target_id = relationship[
        "target_event_id"
    ]

    if source_id == target_id:

        fail(
            "E012",
            (
                f"{context} contains a prohibited "
                f"self-reference: {source_id}"
            ),
        )

    status = relationship[
        "evidence_status"
    ]

    if (
        status in EVIDENCE_REQUIRED_STATUSES
        and not relationship["evidence_ids"]
    ):

        fail(
            "E013",
            (
                f"{context} has evidence status "
                f"{status!r} but contains no "
                f"evidence references."
            ),
        )


# ============================================================
# Record Identifier Uniqueness
# ============================================================

def build_record_index(
    records: list[dict],
    identifier_field: str,
    context: str,
) -> dict[str, dict]:

    result = {}

    for record in records:

        identifier = record[
            identifier_field
        ]

        if identifier in result:

            fail(
                "E006",
                (
                    f"{context} contains duplicate "
                    f"identifier: {identifier}"
                ),
            )

        result[identifier] = record

    return result


# ============================================================
# Reference Integrity
# ============================================================

def validate_event_references(
    relationships: list[dict],
    event_index: dict[str, dict],
) -> None:

    for relationship in relationships:

        relationship_id = relationship[
            "relationship_id"
        ]

        source_id = relationship[
            "source_event_id"
        ]

        target_id = relationship[
            "target_event_id"
        ]

        if source_id not in event_index:

            fail(
                "E010",
                (
                    f"{relationship_id} references "
                    f"unknown source event: {source_id}"
                ),
            )

        if target_id not in event_index:

            fail(
                "E010",
                (
                    f"{relationship_id} references "
                    f"unknown target event: {target_id}"
                ),
            )


def validate_evidence_references(
    events: list[dict],
    relationships: list[dict],
    evidence_index: dict[str, dict],
) -> None:

    for event in events:

        event_id = event["event_id"]

        for evidence_id in event[
            "evidence_ids"
        ]:

            if evidence_id not in evidence_index:

                fail(
                    "E011",
                    (
                        f"{event_id} references "
                        f"unknown evidence: {evidence_id}"
                    ),
                )

    for relationship in relationships:

        relationship_id = relationship[
            "relationship_id"
        ]

        for evidence_id in relationship[
            "evidence_ids"
        ]:

            if evidence_id not in evidence_index:

                fail(
                    "E011",
                    (
                        f"{relationship_id} references "
                        f"unknown evidence: {evidence_id}"
                    ),
                )


# ============================================================
# Temporal Consistency
# ============================================================

def validate_temporal_consistency(
    relationships: list[dict],
    event_dates: dict[str, date],
) -> None:

    for relationship in relationships:

        relationship_type = relationship[
            "type"
        ]

        status = relationship[
            "evidence_status"
        ]

        if relationship_type not in ANTECEDENT_TYPES:

            continue

        if status == "unknown":

            continue

        source_id = relationship[
            "source_event_id"
        ]

        target_id = relationship[
            "target_event_id"
        ]

        source_date = event_dates[
            source_id
        ]

        target_date = event_dates[
            target_id
        ]

        if target_date > source_date:

            fail(
                "E014",
                (
                    f"{relationship['relationship_id']} "
                    f"violates temporal consistency. "
                    f"Source {source_id}: {source_date}; "
                    f"target {target_id}: {target_date}."
                ),
            )


# ============================================================
# Inheritance Cycle Detection
# ============================================================

def validate_inheritance_cycles(
    event_index: dict[str, dict],
    relationships: list[dict],
) -> None:

    """
    Validate the derived_from subgraph using
    Kahn's topological sorting algorithm.

    All derived_from relationships are included,
    regardless of evidence status.

    Other relationship types are excluded.
    """

    graph = {
        event_id: []
        for event_id in event_index
    }

    indegree = {
        event_id: 0
        for event_id in event_index
    }

    for relationship in relationships:

        if relationship["type"] != "derived_from":

            continue

        source_id = relationship[
            "source_event_id"
        ]

        target_id = relationship[
            "target_event_id"
        ]

        graph[source_id].append(
            target_id
        )

        indegree[target_id] += 1

    queue = deque(
        event_id
        for event_id, degree in indegree.items()
        if degree == 0
    )

    processed_count = 0

    while queue:

        event_id = queue.popleft()

        processed_count += 1

        for target_id in graph[event_id]:

            indegree[target_id] -= 1

            if indegree[target_id] == 0:

                queue.append(target_id)

    if processed_count != len(event_index):

        unresolved = sorted(
            event_id
            for event_id, degree in indegree.items()
            if degree > 0
        )

        fail(
            "E015",
            (
                "Inheritance cycle detected "
                "in derived_from subgraph. "
                "Unresolved nodes: "
                + ", ".join(unresolved)
            ),
        )


# ============================================================
# Complete Ledger Validation
# ============================================================

def validate_ledger(
    ledger: object,
) -> dict[str, int]:

    # Step 1: Validate root structure.

    validate_root(ledger)

    events = ledger["events"]

    relationships = ledger[
        "relationships"
    ]

    evidence = ledger["evidence"]

    # Step 2: Validate evolution events.

    event_dates = {}

    for index, event in enumerate(events):

        event_date = validate_event(
            event,
            index,
        )

        event_dates[
            event["event_id"]
        ] = event_date

    # Step 3: Validate evidence records.

    for index, record in enumerate(evidence):

        validate_evidence_record(
            record,
            index,
        )

    # Step 4: Validate relationships.

    for index, relationship in enumerate(
        relationships
    ):

        validate_relationship(
            relationship,
            index,
        )

    # Step 5: Validate identifier uniqueness.

    event_index = build_record_index(
        events,
        "event_id",
        "events",
    )

    build_record_index(
        relationships,
        "relationship_id",
        "relationships",
    )

    evidence_index = build_record_index(
        evidence,
        "evidence_id",
        "evidence",
    )

    # Step 6: Validate reference integrity.

    validate_event_references(
        relationships,
        event_index,
    )

    validate_evidence_references(
        events,
        relationships,
        evidence_index,
    )

    # Step 7: Validate temporal consistency.

    validate_temporal_consistency(
        relationships,
        event_dates,
    )

    # Step 8: Detect inheritance cycles.

    validate_inheritance_cycles(
        event_index,
        relationships,
    )

    # Step 9: Return ledger statistics.

    return {
        "events": len(events),
        "relationships": len(relationships),
        "evidence": len(evidence),
        "confirmed": sum(
            relationship["evidence_status"]
            == "confirmed"
            for relationship in relationships
        ),
        "inferred": sum(
            relationship["evidence_status"]
            == "inferred"
            for relationship in relationships
        ),
        "unknown": sum(
            relationship["evidence_status"]
            == "unknown"
            for relationship in relationships
        ),
        "inheritance_edges": sum(
            relationship["type"]
            == "derived_from"
            for relationship in relationships
        ),
    }


# ============================================================
# Strict JSON Loading
# ============================================================

def reject_duplicate_json_keys(
    pairs: list[tuple],
) -> dict:

    result = {}

    for key, value in pairs:

        if key in result:

            fail(
                "E019",
                f"Duplicate JSON object key: {key!r}",
            )

        result[key] = value

    return result


def reject_invalid_json_constant(
    value: str,
) -> None:

    fail(
        "E004",
        f"Invalid JSON constant: {value}",
    )


def load_ledger(
    file_path: Path,
) -> object:

    try:

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(
                file,
                object_pairs_hook=(
                    reject_duplicate_json_keys
                ),
                parse_constant=(
                    reject_invalid_json_constant
                ),
            )

    except json.JSONDecodeError as error:

        fail(
            "E001",
            (
                f"Invalid JSON in {file_path}. "
                f"Line {error.lineno}, "
                f"column {error.colno}: "
                f"{error.msg}"
            ),
        )

    except UnicodeError as error:

        fail(
            "E001",
            f"Invalid UTF-8 input: {error}",
        )

    except OSError as error:

        fail(
            "E001",
            f"Unable to read {file_path}: {error}",
        )

    except RecursionError:

        fail(
            "E001",
            "JSON input is nested too deeply.",
        )


# ============================================================
# Validation Output
# ============================================================

def print_summary(
    file_path: Path,
    statistics: dict[str, int],
) -> None:

    print(
        "=" * 60
    )

    print(
        "AI Evolution Lineage Graph (AELG)"
    )

    print(
        f"Specification Version: {SPEC_VERSION}"
    )

    print(
        "=" * 60
    )

    print(
        f"File: {file_path}"
    )

    print()

    print(
        "Validation Summary"
    )

    print(
        "-" * 60
    )

    print(
        f"Evolution events:       "
        f"{statistics['events']}"
    )

    print(
        f"Lineage relationships:  "
        f"{statistics['relationships']}"
    )

    print(
        f"Evidence records:       "
        f"{statistics['evidence']}"
    )

    print(
        f"Inheritance edges:      "
        f"{statistics['inheritance_edges']}"
    )

    print()

    print(
        "Evidence Status"
    )

    print(
        "-" * 60
    )

    print(
        f"Confirmed:              "
        f"{statistics['confirmed']}"
    )

    print(
        f"Inferred:               "
        f"{statistics['inferred']}"
    )

    print(
        f"Unknown:                "
        f"{statistics['unknown']}"
    )

    print()

    print(
        "PASS: AELG ledger is structurally valid."
    )

    print()

    print(
        "Note: Validation does not establish "
        "historical accuracy,"
    )

    print(
        "source authenticity, evidence sufficiency, "
        "or causal truth."
    )

    print(
        "=" * 60
    )


# ============================================================
# Command-Line Entry Point
# ============================================================

def main() -> int:

    arguments = sys.argv[1:]

    if len(arguments) > 1:

        print(
            "Usage: python scripts/validate.py "
            "[ledger.json]",
            file=sys.stderr,
        )

        return 1

    if arguments:

        file_path = Path(
            arguments[0]
        )

    else:

        file_path = DEFAULT_FILE

    try:

        ledger = load_ledger(
            file_path
        )

        statistics = validate_ledger(
            ledger
        )

    except ValidationError as error:

        print(
            "FAIL: Invalid AELG ledger.",
            file=sys.stderr,
        )

        print(
            str(error),
            file=sys.stderr,
        )

        return 1

    print_summary(
        file_path,
        statistics,
    )

    return 0


if __name__ == "__main__":

    sys.exit(main())
