# AI Evolution Lineage Graph Specification

## AELG v0.1

| Property | Value |
|---|---|
| Specification | AI Evolution Lineage Graph |
| Abbreviation | AELG |
| Version | 0.1.0 |
| Status | Initial Specification |
| Document Type | Core Specification |
| Implementation Model | Evidence-Based Evolution Ledger |

---

## 1. Purpose

AI Evolution Lineage Graph (AELG) defines a minimal
structure for recording the evolution of artificial
intelligence systems and their influencing factors.

AELG addresses three fundamental questions:

1. What changed?
2. What may have influenced the change?
3. What evidence supports the recorded relationship?

AI evolution may involve interactions between:

- Technological inheritance
- Research discoveries
- Implementation practices
- Human questions
- Computational resources
- Economic conditions
- Governance requirements
- Social expectations
- Operational failures

AELG represents these interactions as structured
events, relationships, and evidence records.

The specification does not assume that AI evolution
can be explained by a single organization,
technology, or causal factor.

---

## 2. Scope

### 2.1 In Scope

Version 0.1 defines:

- Evolution events
- Evolution layers
- Lineage relationships
- Evidence records
- Evidence status classification
- Identifier requirements
- Reference integrity
- Temporal consistency
- Inheritance cycle detection
- Minimum validation requirements

### 2.2 Out of Scope

Version 0.1 does not define:

- Automated causal inference
- Autonomous evidence verification
- Individual contribution scoring
- Financial attribution
- Royalty distribution
- Graph visualization engines
- Real-time monitoring
- Distributed ledger infrastructure
- Model performance ranking
- Predictive evolution simulation

These capabilities may be considered in future
versions when concrete requirements emerge.

---

## 3. Normative Language

The following terms define requirement levels:

- MUST: Mandatory requirement.
- MUST NOT: Prohibited behavior.
- SHOULD: Recommended requirement.
- SHOULD NOT: Discouraged behavior.
- MAY: Optional behavior.

A conforming AELG ledger MUST satisfy all
applicable MUST and MUST NOT requirements.

---

## 4. Core Principles

### 4.1 Multi-Factor Evolution

AI evolution MUST be representable through
multiple interacting factors.

A single evolution event MAY reference
multiple influencing events.

AELG MUST NOT assume that every change
has only one cause.

### 4.2 Evidence Before Attribution

An influence relationship MUST NOT be classified
as confirmed without supporting evidence.

The recorded evidence MUST support the specific
relationship being claimed.

### 4.3 Correlation Is Not Causation

Temporal proximity MUST NOT be treated
as sufficient proof of causality.

A preceding event MAY be recorded as
a potential influence.

However, its evidence status MUST reflect
the available support.

### 4.4 Human Questions as Potential Influence

Human questions, feedback, and requirements
MAY be represented as evolution events.

Their existence MUST NOT automatically establish
influence on AI development.

Specific influence claims require
appropriate supporting evidence.

### 4.5 Preservation of Uncertainty

Unverified relationships MAY be retained
with an unknown evidence status.

Unknown relationships MUST NOT be presented
as confirmed facts.

### 4.6 Cross-Organizational Lineage

Relationships MAY connect events associated
with different organizations or communities.

Organizational ownership MUST NOT be assumed
from technical inheritance alone.

### 4.7 Minimal Extensibility

AELG SHOULD remain structurally minimal.

Additional mechanisms SHOULD be introduced
only in response to observed requirements.

---

## 5. Conceptual Architecture

AELG defines three primary record types:

```text
Evolution Event
      |
      v
Lineage Relationship
      |
      v
Evidence Record
```

These components form an evolution ledger.

```text
+----------------------+
| Evolution Events     |
+----------------------+
           |
           v
+----------------------+
| Lineage Relationships|
+----------------------+
           |
           v
+----------------------+
| Evidence Records     |
+----------------------+
           |
           v
+----------------------+
| Structural Validation|
+----------------------+
           |
           v
+----------------------+
| Evolution Ledger     |
+----------------------+
```

The ledger provides a foundation for future
graph generation and historical analysis.

Version 0.1 does not require a graph database.

---

## 6. Evolution Ledger

### 6.1 Root Structure

An AELG v0.1 ledger MUST contain the following
top-level fields:

| Field | Type | Required |
|---|---|---|
| `spec_version` | String | Yes |
| `events` | Array | Yes |
| `relationships` | Array | Yes |
| `evidence` | Array | Yes |

Example:

```json
{
  "spec_version": "0.1.0",
  "events": [],
  "relationships": [],
  "evidence": []
}
```

### 6.2 Version Requirement

The `spec_version` field MUST equal:

```text
0.1.0
```

A validator implementing only version 0.1
MUST reject unsupported specification versions.

### 6.3 Collection Requirements

The `events` array MUST contain at least one
evolution event.

The `relationships` array MAY be empty.

The `evidence` array MAY be empty if no record
requires an evidence reference.

Every collection entry MUST conform to its
corresponding record definition.

### 6.4 Additional Properties

A conforming v0.1 ledger MUST NOT contain
undefined properties.

This requirement applies to:

- Root objects
- Evolution events
- Lineage relationships
- Evidence records

New properties require a specification update.

---

## 7. Identifier Requirements

### 7.1 Identifier Format

Each record MUST have a unique identifier
within its record collection.

The following identifier formats are defined:

| Record Type | Format | Example |
|---|---|---|
| Evolution Event | `EVT-` followed by digits | `EVT-001` |
| Lineage Relationship | `REL-` followed by digits | `REL-001` |
| Evidence Record | `EVD-` followed by digits | `EVD-001` |

Identifier patterns:

```text
Event:        ^EVT-[0-9]+$
Relationship: ^REL-[0-9]+$
Evidence:     ^EVD-[0-9]+$
```

Identifiers MUST be case-sensitive.

Identifiers MUST NOT contain whitespace.

### 7.2 Identifier Stability

An identifier SHOULD remain stable after
the corresponding record has been published.

An identifier SHOULD NOT be reassigned to
an unrelated record.

### 7.3 Identifier Scope

Identifiers are local to an individual ledger.

Version 0.1 does not define globally unique
identifiers or cross-ledger resolution.

---

## 8. Evolution Event

### 8.1 Definition

An evolution event represents an identifiable
change, development, condition, or occurrence
relevant to AI evolution.

An event does not need to represent
a model release.

It MAY represent:

- A research discovery
- A technical improvement
- A newly expressed human requirement
- A resource limitation
- A governance change
- An operational incident
- An infrastructure development

### 8.2 Event Structure

| Field | Type | Required | Description |
|---|---|---|---|
| `event_id` | String | Yes | Unique event identifier |
| `date` | String | Yes | Event occurrence date |
| `layer` | String | Yes | Evolution layer |
| `title` | String | Yes | Short event title |
| `description` | String | Yes | Event description |
| `actors` | Array of strings | Yes | Associated actors |
| `evidence_ids` | Array of strings | Yes | Supporting evidence references |

### 8.3 Event Example

```json
{
  "event_id": "EVT-001",
  "date": "2026-01-01",
  "layer": "question",
  "title": "Demand for affordable inference",
  "description": "Users express a requirement for lower inference costs.",
  "actors": [
    "example-user-community"
  ],
  "evidence_ids": [
    "EVD-001"
  ]
}
```

This example is fictional.

### 8.4 Date Requirements

The `date` field MUST use the following format:

```text
YYYY-MM-DD
```

The date MUST represent a valid Gregorian
calendar date.

Examples:

```text
2026-01-01
2026-11-24
2028-02-29
```

Invalid examples:

```text
2026-02-30
2026-13-01
26-01-01
```

The date SHOULD represent the occurrence date
of the described event rather than the date
on which the ledger entry was created.

Version 0.1 does not support:

- Approximate dates
- Date ranges
- Time-of-day information
- Uncertain historical dates

Events without a sufficiently established date
cannot be represented conformantly in v0.1.

### 8.5 Actor Requirements

Actors MAY include:

- Organizations
- Research institutions
- Open-source communities
- User communities
- Public institutions
- Standards organizations
- Individuals where appropriate

The `actors` array MAY be empty
when associated actors are unknown.

Each actor entry MUST be a non-empty string.

Duplicate actor entries MUST NOT occur
within the same event.

Actor association does not establish:

- Ownership
- Responsibility
- Intellectual property rights
- Causal contribution
- Financial entitlement

### 8.6 Event Evidence Requirements

An event MAY reference zero or more
evidence records.

Every referenced evidence identifier MUST
resolve to an existing evidence record.

Duplicate evidence references MUST NOT occur
within the same event.

An event without evidence MAY be recorded,
but its presence does not establish
historical accuracy.

Version 0.1 does not assign a separate
evidence status to individual events.

---

## 9. Evolution Layers

AELG defines five evolution layers.

### 9.1 Technology Layer

Identifier:

```text
technology
```

Represents changes involving:

- Model architectures
- Learning methods
- Inference methods
- Algorithms
- Reasoning techniques
- Technical inheritance
- Model optimization

### 9.2 Implementation Layer

Identifier:

```text
implementation
```

Represents changes involving:

- Deployment
- API integration
- Application development
- Local execution
- Agent orchestration
- Software integration
- Operational implementation

### 9.3 Question Layer

Identifier:

```text
question
```

Represents changes involving:

- Human questions
- User feedback
- User requirements
- Unresolved problems
- Operational demands
- Publicly expressed needs

The question layer treats human requirements
as observable potential influences.

It does not assume that all questions
affect model development.

### 9.4 Resource Layer

Identifier:

```text
resource
```

Represents changes involving:

- Computing capacity
- Accelerators
- Memory
- Energy
- Communication infrastructure
- Data centers
- Inference costs
- Resource availability

### 9.5 Governance Layer

Identifier:

```text
governance
```

Represents changes involving:

- Safety requirements
- Regulation
- Permission boundaries
- Accountability
- Auditing
- Trust
- Intellectual property
- Social acceptance

### 9.6 Layer Constraints

Each event MUST declare exactly one
primary evolution layer.

The allowed values are:

```text
technology
implementation
question
resource
governance
```

Unknown layer values MUST be rejected.

A single event MAY be relevant to
multiple conceptual layers.

However, v0.1 requires one primary layer
for each event record.

Cross-layer interactions are represented
through lineage relationships.

---

## 10. Lineage Relationship

### 10.1 Definition

A lineage relationship describes a connection
between two evolution events.

The relationship MAY represent inheritance,
influence, response, enablement, constraint,
or general association.

A relationship does not automatically
establish causality.

### 10.2 Relationship Structure

| Field | Type | Required |
|---|---|---|
| `relationship_id` | String | Yes |
| `source_event_id` | String | Yes |
| `target_event_id` | String | Yes |
| `type` | String | Yes |
| `evidence_status` | String | Yes |
| `evidence_ids` | Array of strings | Yes |
| `description` | String | Yes |

### 10.3 Relationship Direction

For directed relationship types:

- The source event is the event being described.
- The target event is the referenced antecedent,
  influence, condition, or constraint.

```text
Source Event
     |
     | relationship type
     v
Target Event
```

For example:

```text
EVT-002 --derived_from--> EVT-001
```

This means that EVT-002 derives from EVT-001.

The direction of the stored relationship
is from the described event toward
its referenced antecedent.

A chronological visualization MAY display
the inverse direction.

However, the stored relationship MUST NOT
change its defined semantics.

### 10.4 Relationship Example

```json
{
  "relationship_id": "REL-001",
  "source_event_id": "EVT-002",
  "target_event_id": "EVT-001",
  "type": "influenced_by",
  "evidence_status": "unknown",
  "evidence_ids": [],
  "description": "A possible influence that has not been established."
}
```

### 10.5 Endpoint Requirements

Both event identifiers MUST resolve
to existing evolution events.

The source and target identifiers
MUST NOT be identical.

Self-referencing relationships are invalid.

### 10.6 Evidence Reference Requirements

Every referenced evidence identifier MUST
resolve to an existing evidence record.

Duplicate evidence references MUST NOT occur
within the same relationship.

The minimum number of evidence references
depends on the declared evidence status.

---

## 11. Relationship Types

AELG v0.1 defines six relationship types.

### 11.1 Derived From

Identifier:

```text
derived_from
```

Represents technical or conceptual inheritance.

Example:

```text
New architecture
    --derived_from-->
Earlier architecture
```

This relationship MAY represent:

- Architectural inheritance
- Technical adaptation
- Model derivation
- Documented conceptual inheritance

A `derived_from` relationship MUST NOT
participate in an inheritance cycle.

### 11.2 Influenced By

Identifier:

```text
influenced_by
```

Represents an influence or proposed influence
on an evolution event.

Example:

```text
Model optimization
    --influenced_by-->
User requirements
```

Influence MAY be partial.

This relationship does not imply that the target
event was the only cause of the source event.

### 11.3 Responds To

Identifier:

```text
responds_to
```

Represents a response to a requirement,
incident, question, or development.

Example:

```text
Safety mechanism
    --responds_to-->
Operational incident
```

A confirmed response relationship requires
evidence connecting the response
to the referenced event.

### 11.4 Enabled By

Identifier:

```text
enabled_by
```

Represents an enabling condition
or supporting capability.

Example:

```text
Local inference deployment
    --enabled_by-->
Hardware development
```

An enabling condition does not necessarily
constitute the sole cause of a change.

### 11.5 Constrained By

Identifier:

```text
constrained_by
```

Represents a limiting condition or pressure.

Example:

```text
Inference architecture
    --constrained_by-->
Resource limitations
```

Constraints MAY influence:

- Architecture
- Cost
- Performance
- Deployment
- Safety
- Permissions

### 11.6 Related To

Identifier:

```text
related_to
```

Represents a general association without
asserting a specific causal direction.

Example:

```text
Technology Event
    --related_to--
Governance Event
```

The relationship is semantically symmetric.

The source and target fields are retained
for consistent serialization.

Their ordering does not establish causality
or chronological precedence.

### 11.7 Relationship Type Summary

| Type | Directed | Temporal Rule | Cycle Restriction |
|---|---|---|---|
| `derived_from` | Yes | Yes | Yes |
| `influenced_by` | Yes | Yes | No |
| `responds_to` | Yes | Yes | No |
| `enabled_by` | Yes | Yes | No |
| `constrained_by` | Yes | Yes | No |
| `related_to` | No | No | No |

Temporal rules apply according to Section 14.

Cycle restrictions apply according to Section 15.

---

## 12. Evidence Record

### 12.1 Definition

An evidence record identifies material that
supports an evolution event or relationship.

An evidence record is a reference to evidence.

It does not independently certify
the accuracy or authenticity of that evidence.

### 12.2 Evidence Structure

| Field | Type | Required |
|---|---|---|
| `evidence_id` | String | Yes |
| `source_type` | String | Yes |
| `source_uri` | String | Yes |
| `description` | String | Yes |

### 12.3 Evidence Example

```json
{
  "evidence_id": "EVD-001",
  "source_type": "research_paper",
  "source_uri": "https://example.com/research",
  "description": "Fictional research reference used for demonstration."
}
```

This example uses a placeholder URI.

It does not represent verified historical evidence.

### 12.4 Evidence Source Types

The following source types are supported:

| Source Type | Description |
|---|---|
| `research_paper` | Research publication |
| `technical_report` | Technical documentation or report |
| `official_statement` | Public organizational statement |
| `release_note` | Release documentation |
| `repository` | Source code or public repository |
| `user_feedback` | Appropriately available user feedback |
| `regulatory_document` | Regulation or governance document |
| `incident_report` | Documented operational incident |
| `evaluation_report` | Published evaluation results |
| `other` | Other relevant evidence |

Unknown source types MUST be rejected.

The `other` source type MAY be used when
no more specific supported category applies.

### 12.5 Source URI Requirements

The `source_uri` field MUST contain
an absolute HTTP or HTTPS URI.

It MUST include a non-empty host.

It MUST NOT contain whitespace.

Examples:

```text
https://example.com/report
https://example.com/repository
http://example.org/archive
```

HTTPS SHOULD be preferred.

Relative paths and local filesystem paths
are not supported in version 0.1.

### 12.6 Evidence Description

The evidence description SHOULD explain
what the referenced material supports.

For example:

```text
Documents the introduction of a safety mechanism.
```

Or:

```text
Directly identifies user feedback as one reason
for the implementation change.
```

A source documenting an event does not
necessarily document its causes.

### 12.7 Evidence Limitations

A structural validator MUST NOT interpret
the presence of an evidence URI as proof
of authenticity or causal validity.

Version 0.1 does not require:

- Network access
- Source availability checks
- Content retrieval
- Cryptographic signatures
- Content hashing
- Independent source verification

---

## 13. Evidence Status

### 13.1 Supported Statuses

AELG defines three evidence statuses:

```text
confirmed
inferred
unknown
```

### 13.2 Confirmed

Identifier:

```text
confirmed
```

The recorded relationship is directly
supported by appropriate evidence.

Requirements:

- MUST reference at least one evidence record.
- MUST describe the specific supported relationship.
- MUST NOT exceed the actual scope of the evidence.

For example, a release announcement
confirming a feature does not automatically
confirm the reasons for introducing that feature.

A confirmed status represents an assertion
made by the ledger maintainer.

It does not represent independent certification
by the structural validator.

### 13.3 Inferred

Identifier:

```text
inferred
```

Available evidence indirectly supports
a plausible relationship.

Requirements:

- MUST reference at least one evidence record.
- MUST preserve uncertainty.
- MUST NOT be represented as a confirmed fact.

An inferred relationship MAY be revised
when additional evidence becomes available.

### 13.4 Unknown

Identifier:

```text
unknown
```

The relationship has not been
adequately established.

Requirements:

- MAY reference zero or more evidence records.
- MUST NOT be presented as confirmed.
- MUST NOT be used as proof of causality.

Unknown relationships preserve
unresolved observations and hypotheses.

### 13.5 Evidence Status Summary

| Status | Minimum Evidence References | Interpretation |
|---|---:|---|
| `confirmed` | 1 | Directly supported assertion |
| `inferred` | 1 | Indirectly supported inference |
| `unknown` | 0 | Unresolved relationship |

The number of evidence records alone
does not determine evidence quality.

Multiple weak sources MUST NOT automatically
be treated as stronger than one relevant
and reliable source.

### 13.6 Evidence Status Revision

Evidence status MAY change when
additional information becomes available.

```text
unknown <--> inferred <--> confirmed
```

Status changes are not necessarily progressive.

A confirmed relationship MAY be downgraded
if its evidence is corrected, withdrawn,
or found insufficient.

An unknown relationship MAY become
confirmed directly.

Version 0.1 does not require a status
transition history or automated promotion.

---

## 14. Temporal Consistency

### 14.1 General Rule

AELG distinguishes chronological precedence
from causal evidence.

An earlier event is not necessarily
the cause of a later event.

### 14.2 Antecedent Relationship Types

The following relationship types
are considered antecedent relationships:

```text
derived_from
influenced_by
responds_to
enabled_by
constrained_by
```

### 14.3 Confirmed and Inferred Relationships

For confirmed or inferred antecedent
relationships, the following rule MUST hold:

```text
target_event.date <= source_event.date
```

The target event MUST NOT occur
after the source event.

Valid example:

```text
Source: 2026-02-01
Target: 2026-01-01
Status: confirmed
Result: PASS
```

Invalid example:

```text
Source: 2026-01-01
Target: 2026-02-01
Status: confirmed
Result: FAIL
```

### 14.4 Same-Day Events

Relationships between events occurring
on the same date MAY be recorded.

Version 0.1 does not represent
time-of-day information.

Same-day dates do not establish
the internal ordering of events.

### 14.5 Unknown Relationships

Unknown relationships are exempt from
the mandatory temporal ordering rule.

This exemption permits the retention
of unresolved or inconsistent hypotheses.

An unknown antecedent relationship
whose target occurs after its source
SHOULD be reviewed before promotion.

The exemption does not permit:

- Invalid date formats
- Unresolved event references
- Self-referencing relationships
- Inheritance cycles

Unknown status MUST NOT be interpreted
as evidence that a future event caused
an earlier event.

### 14.6 General Associations

The `related_to` relationship type
has no temporal ordering requirement.

An association MAY connect events
in either chronological direction.

### 14.7 Temporal Rule Summary

| Relationship | Status | Target Later Than Source |
|---|---|---|
| Antecedent | `confirmed` | Invalid |
| Antecedent | `inferred` | Invalid |
| Antecedent | `unknown` | Structurally permitted |
| `related_to` | Any supported status | Permitted |

---

## 15. Inheritance Cycle Detection

### 15.1 Purpose

Technical or conceptual inheritance
MUST NOT be circular.

The `derived_from` subgraph MUST be
a directed acyclic graph (DAG).

### 15.2 Valid Inheritance

```text
EVT-003
   |
   v
EVT-002
   |
   v
EVT-001
```

Multiple inheritance is also permitted.

```text
EVT-003
   |  |
   |  +------> EVT-002
   |
   +---------> EVT-001
```

### 15.3 Invalid Inheritance

Direct cycle:

```text
EVT-001 ---> EVT-002
   ^            |
   |            |
   +------------+
```

Indirect cycle:

```text
EVT-001 ---> EVT-002 ---> EVT-003
   ^                        |
   |                        |
   +------------------------+
```

Both structures MUST be rejected.

### 15.4 Detection Scope

Cycle detection MUST examine every
`derived_from` relationship.

The requirement applies regardless
of evidence status.

A cycle containing an unknown inheritance
relationship is still invalid.

### 15.5 Other Relationship Types

Version 0.1 does not impose a general
cycle restriction on:

```text
influenced_by
responds_to
enabled_by
constrained_by
related_to
```

This allows the representation of
feedback and reciprocal interactions,
subject to temporal consistency rules.

For example, a historical feedback sequence
may be represented using separate events:

```text
EVT-001: Initial user requirement
EVT-002: Technical response
EVT-003: Subsequent user feedback
EVT-004: Further technical revision
```

Each development SHOULD be recorded
as a separate event where appropriate.

### 15.6 Implementation

A validator MAY use:

- Depth-first search
- Topological sorting
- Another equivalent cycle detection algorithm

The implementation method is not prescribed.

The resulting inheritance graph MUST
contain no directed cycle.

---

## 16. Graph Semantics

### 16.1 Nodes

Every evolution event is a graph node.

### 16.2 Edges

Every lineage relationship is a graph edge.

### 16.3 Evidence References

Evidence records support nodes or edges.

Evidence records are not evolution graph
nodes in version 0.1.

### 16.4 Branching

A single event MAY be referenced
by multiple events.

```text
EVT-002 ----+
            |
            v
         EVT-001
            ^
            |
EVT-003 ----+
```

### 16.5 Convergence

A single event MAY reference
multiple antecedent events.

```text
             +----> Research
             |
New Model ---+----> User Requirement
             |
             +----> Resource Constraint
```

### 16.6 Cross-Layer Relationships

Relationships MAY connect events
belonging to different evolution layers.

Example:

```text
Technology
    --influenced_by-->
Question
```

Another example:

```text
Implementation
    --enabled_by-->
Resource
```

No mandatory layer hierarchy is defined.

### 16.7 Disconnected Events

A ledger MAY contain events
without relationships.

Disconnected events are not invalid.

Their relationships may become known
at a later stage.

### 16.8 Parallel Relationships

Multiple relationships MAY connect
the same pair of events.

Each relationship MUST have
a unique relationship identifier.

For example:

```text
EVT-002 --influenced_by--> EVT-001

EVT-002 --enabled_by-----> EVT-001
```

Version 0.1 does not require semantic
deduplication of relationship records.

---

## 17. Complete Ledger Example

The following ledger is fictional.

It demonstrates multiple evolution layers
and different evidence statuses.

```json
{
  "spec_version": "0.1.0",
  "events": [
    {
      "event_id": "EVT-001",
      "date": "2026-01-01",
      "layer": "question",
      "title": "Demand for affordable inference",
      "description": "Users request lower inference costs.",
      "actors": [
        "example-user-community"
      ],
      "evidence_ids": [
        "EVD-001"
      ]
    },
    {
      "event_id": "EVT-002",
      "date": "2026-01-15",
      "layer": "resource",
      "title": "Improved computing efficiency",
      "description": "An example hardware improvement becomes available.",
      "actors": [
        "example-hardware-provider"
      ],
      "evidence_ids": [
        "EVD-002"
      ]
    },
    {
      "event_id": "EVT-003",
      "date": "2026-02-01",
      "layer": "technology",
      "title": "Efficient inference architecture",
      "description": "An example developer introduces a lower-cost inference method.",
      "actors": [
        "example-developer"
      ],
      "evidence_ids": [
        "EVD-003"
      ]
    }
  ],
  "relationships": [
    {
      "relationship_id": "REL-001",
      "source_event_id": "EVT-003",
      "target_event_id": "EVT-001",
      "type": "influenced_by",
      "evidence_status": "unknown",
      "evidence_ids": [],
      "description": "User requirements may have influenced the optimization."
    },
    {
      "relationship_id": "REL-002",
      "source_event_id": "EVT-003",
      "target_event_id": "EVT-002",
      "type": "enabled_by",
      "evidence_status": "confirmed",
      "evidence_ids": [
        "EVD-003"
      ],
      "description": "The fictional technical report directly identifies the hardware improvement as an enabling condition."
    }
  ],
  "evidence": [
    {
      "evidence_id": "EVD-001",
      "source_type": "user_feedback",
      "source_uri": "https://example.com/feedback",
      "description": "Fictional user requirements."
    },
    {
      "evidence_id": "EVD-002",
      "source_type": "technical_report",
      "source_uri": "https://example.com/hardware",
      "description": "Fictional hardware development report."
    },
    {
      "evidence_id": "EVD-003",
      "source_type": "technical_report",
      "source_uri": "https://example.com/inference",
      "description": "Fictional report describing inference optimization and its enabling hardware condition."
    }
  ]
}
```

The example demonstrates the distinction
between a documented enabling relationship
and an unverified potential influence.

The example URIs are placeholders.

The confirmed status is illustrative
and does not establish any real-world claim.

---

## 18. Validation Model

### 18.1 Validation Layers

AELG defines two validation layers:

```text
Input Ledger
     |
     v
Structural Validation
     |
     v
Semantic Validation
     |
     v
Validation Result
```

### 18.2 Structural Validation

Structural validation MUST check:

- Root object structure
- Specification version
- Required fields
- Supported field types
- Supported enumeration values
- Identifier formats
- Collection requirements
- Non-empty string values
- Undefined properties

Required string values MUST NOT be empty
or consist only of whitespace.

### 18.3 Semantic Validation

Semantic validation MUST check:

- Valid Gregorian calendar dates
- Unique record identifiers
- Unique actor entries within each event
- Unique evidence references within each record
- Event reference integrity
- Evidence reference integrity
- Evidence URI requirements
- Prohibited self-references
- Evidence status requirements
- Temporal consistency
- Inheritance cycle restrictions

### 18.4 JSON Schema

The machine-readable schema is located at:

```text
schemas/evolution-event.schema.json
```

The schema SHOULD describe structural
constraints using JSON Schema Draft 2020-12.

Despite its filename, the schema describes
the complete AELG evolution ledger.

JSON Schema alone is not sufficient
to enforce every semantic requirement.

### 18.5 Reference Validator

The reference validator is located at:

```text
scripts/validate.py
```

The validator MUST implement the mandatory
structural and semantic requirements.

The reference implementation SHOULD use:

- Python 3.11 or later
- Python standard library
- No external Python dependencies

A dependency-free validator MAY implement
the required structural checks directly
rather than invoking a JSON Schema engine.

The schema and reference validator
MUST remain semantically consistent.

---

## 19. Validation Error Categories

The following error categories define
a recommended reporting vocabulary.

| Error Code | Description |
|---|---|
| `E001` | Invalid root structure |
| `E002` | Unsupported specification version |
| `E003` | Missing required field |
| `E004` | Invalid field type or value |
| `E005` | Invalid identifier format |
| `E006` | Duplicate record identifier |
| `E007` | Invalid evolution layer |
| `E008` | Invalid relationship type |
| `E009` | Invalid evidence status |
| `E010` | Unresolved event reference |
| `E011` | Unresolved evidence reference |
| `E012` | Self-referencing relationship |
| `E013` | Insufficient evidence references |
| `E014` | Invalid temporal relationship |
| `E015` | Inheritance cycle detected |
| `E016` | Invalid date |
| `E017` | Invalid evidence URI |
| `E018` | Invalid evidence source type |
| `E019` | Duplicate array entry |
| `E020` | Undefined property |
| `E021` | Invalid collection size |

The exact error message format
is implementation-specific.

Validators SHOULD provide sufficient context
to identify the invalid record or field.

---

## 20. Validation Results

### 20.1 PASS

A ledger passes validation when
all mandatory requirements are satisfied.

```text
PASS: AELG ledger is structurally valid.
```

PASS indicates structural and semantic
consistency with this specification.

PASS does not establish:

- Historical accuracy
- Source authenticity
- Causal truth
- Evidence sufficiency
- Legal responsibility
- Contribution ownership

### 20.2 FAIL

A ledger fails validation when
one or more mandatory requirements
are violated.

```text
FAIL: Invalid AELG ledger.
E010: Unresolved event reference.
```

### 20.3 Process Exit Codes

The reference command-line validator MUST
use the following exit codes:

| Exit Code | Meaning |
|---|---|
| `0` | Validation passed |
| `1` | Validation failed or input could not be processed |

Unreadable files and malformed JSON
MUST NOT produce a successful result.

### 20.4 Default Validation Target

When executed without a file argument,
the reference validator MUST validate:

```text
examples/sample-evolution.json
```

An implementation MAY support
additional command-line arguments
for validating other ledger files.

---

## 21. Continuous Integration

The repository SHOULD include automated
validation through GitHub Actions.

Workflow location:

```text
.github/workflows/validate.yml
```

The workflow SHOULD run when:

- Changes are pushed.
- Pull requests are created or updated.

The workflow MUST report failure
when the reference validator returns
a non-zero exit code.

Example execution:

```bash
python scripts/validate.py
```

Continuous integration verifies
specification conformance.

It does not verify the real-world truth
of the recorded history.

---

## 22. Privacy and Governance

### 22.1 Evidence Collection

AELG implementations SHOULD prefer:

- Public documentation
- Appropriately authorized records
- Published research
- Public technical repositories
- Public institutional documents

AELG MUST NOT be interpreted
as permission to collect or publish
otherwise restricted information.

### 22.2 Personal Information

Unnecessary personal information
SHOULD NOT be included.

Actor identifiers MAY represent
communities or organizations
instead of identifiable individuals.

Personal dialogue records and user feedback
require appropriate authorization
before collection or publication.

### 22.3 Attribution Boundaries

A recorded relationship MUST NOT
automatically establish:

- Legal ownership
- Intellectual property rights
- Individual contribution entitlement
- Financial compensation
- Institutional responsibility

These determinations require
additional evidence and governance.

### 22.4 Evidence Integrity

Ledger maintainers SHOULD preserve
the original context of evidence.

Evidence SHOULD NOT be selectively
represented in a misleading manner.

Known corrections SHOULD be reflected
in the corresponding records.

### 22.5 Record Correction

Incorrect relationships MAY be corrected,
downgraded, or removed.

AELG does not require immutable records.

Version control MAY be used
to preserve correction history.

Version 0.1 does not define a mandatory
record revision or deletion protocol.

---

## 23. Security Considerations

AELG ledgers are data records.

They MUST NOT be interpreted
as executable instructions.

Validators MUST NOT execute:

- Content contained in descriptions
- Commands contained in actor names
- Code referenced by evidence URIs
- Instructions embedded in evidence material

The reference validator SHOULD operate
without network access.

Evidence URIs are references only.

Automatic retrieval and execution
are outside the scope of version 0.1.

---

## 24. Interoperability

AELG MAY complement other specifications,
including:

### 24.1 QuestionTube

Potential integration:

```text
Question Record
      |
      v
Question Layer Event
      |
      v
Potential Evolution Relationship
```

Question derivation may provide
context for evolution observations.

### 24.2 Dialogue Archive

Potential integration:

```text
Authorized Dialogue Record
      |
      v
Evidence Reference
      |
      v
Evolution Ledger
```

Archived dialogue does not automatically
establish influence on development.

### 24.3 Shared Trace

Potential integration:

```text
Shareable Trace
      |
      v
Evidence Record
      |
      v
Documented Relationship
```

### 24.4 Reasoning Recycling

Potential integration:

```text
Reusable Reasoning Asset
      |
      v
Technical or Conceptual Development
      |
      v
Evolution Event
```

### 24.5 Royalty OS

Potential integration:

```text
Documented Evolution Relationship
      |
      v
Independent Contribution Verification
      |
      v
Future Attribution Mechanism
```

AELG v0.1 does not define or authorize
financial attribution.

All integrations described in this section
are conceptual and optional.

No external specification is required
for AELG v0.1 conformance.

---

## 25. Version 0.1 Conformance

A conforming AELG v0.1 implementation MUST:

1. Support the defined ledger structure.
2. Recognize all five evolution layers.
3. Recognize all six relationship types.
4. Recognize all three evidence statuses.
5. Validate all required fields.
6. Validate identifiers and uniqueness.
7. Validate calendar dates.
8. Resolve event references.
9. Resolve evidence references.
10. Reject self-referencing relationships.
11. Enforce evidence reference requirements.
12. Enforce applicable temporal constraints.
13. Reject inheritance cycles.
14. Preserve the distinction between evidence
    status and structural validity.
15. Reject unsupported specification versions.
16. Reject undefined properties.
17. Avoid executing ledger content.

A conforming validator MUST NOT claim
that structural validation establishes
causal or historical truth.

---

## 26. Future Extension Areas

Potential future versions MAY introduce:

- Cross-ledger identifiers
- Graph visualization
- Evidence revision history
- Event verification status
- Evidence content hashes
- Independent verification
- Approximate historical dates
- Time ranges
- Multi-layer event classification
- Question lineage integration
- Contribution provenance
- Contradictory evidence management
- Evolutionary pressure analysis

These extensions are not requirements
of version 0.1.

No future version is mandatory.

Extensions SHOULD be driven by
observed limitations and practical needs.

---

## 27. Design Philosophy

AI evolution is not necessarily
a single technological lineage.

It may emerge from the interaction
of multiple evolving systems.

```text
Research
Human Questions
Resources
Implementation
Governance
       |
       v
Evolution Events
       |
       v
Evidence-Based Relationships
       |
       v
Evolution Lineage
```

AELG does not attempt to determine
the direction of AI evolution.

It attempts to preserve the observable
traces of that evolution.

```text
Observe the change.

Record the relationship.

Preserve the evidence.

Respect uncertainty.
```

---

## 28. Conclusion

AI evolution cannot always be understood
through model release histories alone.

Technological inheritance, human questions,
resource conditions, implementation practices,
and governance may interact to shape
the development of AI systems.

AELG provides a minimal foundation
for recording these interactions.

The specification begins with
three fundamental components:

```text
Event
Relationship
Evidence
```

From these components, an evidence-based
evolution lineage may gradually emerge.

---

**End of Specification**

AI Evolution Lineage Graph (AELG)

Version 0.1.0
