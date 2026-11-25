# Changelog

All notable changes to the AI Evolution Lineage Graph
(AELG) specification will be documented in this file.

The format is based on Keep a Changelog,
and this project follows Semantic Versioning.

---

## [0.1.0] - 2026-11-25

### Initial Release — Evidence-Based Evolution Ledger

The initial release of AI Evolution Lineage Graph (AELG)
establishes a minimal specification for recording AI
evolution events, lineage relationships, and supporting
evidence.

AELG provides a foundation for observing AI evolution
as a network of technological, human, resource,
implementation, and governance factors.

### Added

#### Core Specification

- Initial AELG v0.1 specification.
- Evidence-based evolution ledger structure.
- Evolution event definitions.
- Lineage relationship definitions.
- Evidence record definitions.
- Directed and symmetric relationship semantics.
- Cross-layer evolution relationships.
- Branching and convergence semantics.
- Evidence status revision principles.
- Privacy and attribution boundaries.
- Structural and semantic validation requirements.

#### Evolution Layers

Introduced five evolution layers:

- `technology`
- `implementation`
- `question`
- `resource`
- `governance`

Each evolution event belongs to one primary layer.

Relationships may connect events across different
evolution layers.

#### Relationship Types

Introduced six lineage relationship types:

- `derived_from`
- `influenced_by`
- `responds_to`
- `enabled_by`
- `constrained_by`
- `related_to`

Multiple relationships may connect a single event
to different antecedents or influencing factors.

#### Evidence Statuses

Introduced three evidence classifications:

- `confirmed`
- `inferred`
- `unknown`

Confirmed and inferred relationships require
at least one evidence reference.

Unknown relationships may be retained without
supporting evidence.

Evidence classifications may be revised when
additional information becomes available.

#### Evidence Source Types

Introduced ten evidence source categories:

- `research_paper`
- `technical_report`
- `official_statement`
- `release_note`
- `repository`
- `user_feedback`
- `regulatory_document`
- `incident_report`
- `evaluation_report`
- `other`

#### JSON Schema

Added:

`schemas/evolution-event.schema.json`

Features:

- JSON Schema Draft 2020-12.
- Machine-readable evolution ledger structure.
- Required field definitions.
- Identifier patterns.
- Supported enumeration values.
- Reusable schema definitions.
- Conditional evidence requirements.
- Duplicate array entry restrictions.
- Undefined property restrictions.

#### Sample Evolution Ledger

Added:

`examples/sample-evolution.json`

The fictional sample contains:

| Component | Count |
|---|---:|
| Evolution events | 8 |
| Lineage relationships | 11 |
| Evidence records | 8 |
| Evolution layers | 5 |
| Relationship types | 6 |
| Evidence statuses | 3 |
| Inheritance edges | 3 |

Evidence status distribution:

| Status | Count |
|---|---:|
| Confirmed | 8 |
| Inferred | 2 |
| Unknown | 1 |

The sample demonstrates:

- Technical inheritance.
- Potential human influence.
- Hardware enablement.
- Governance constraints.
- Practical implementation.
- Human feedback after deployment.
- Subsequent technological revision.
- General association without causal attribution.
- Convergence of multiple evolution factors.

All sample events and evidence records are fictional.

Sample evidence URIs are placeholders.

#### Reference Validator

Added:

`scripts/validate.py`

Implemented dependency-free validation using
the Python standard library.

Validation capabilities include:

- Root structure validation.
- Specification version validation.
- Required field validation.
- Data type validation.
- Undefined property rejection.
- Identifier format validation.
- Record identifier uniqueness.
- Evolution layer validation.
- Relationship type validation.
- Evidence status validation.
- Evidence source type validation.
- Gregorian calendar date validation.
- HTTP and HTTPS URI format checks.
- Duplicate actor detection.
- Duplicate evidence reference detection.
- Event reference integrity.
- Evidence reference integrity.
- Self-reference rejection.
- Minimum evidence requirements.
- Temporal consistency checks.
- Inheritance cycle detection.
- Duplicate JSON object key rejection.
- Invalid JSON constant rejection.

Introduced 21 validation error categories:

`E001` through `E021`.

The validator returns:

- Exit code `0` on success.
- Exit code `1` on validation failure.

#### Inheritance Cycle Detection

Implemented Kahn's topological sorting algorithm
for detecting cycles in the `derived_from` subgraph.

Features:

- Direct cycle detection.
- Indirect cycle detection.
- Multi-level inheritance validation.
- Multiple inheritance support.
- Non-recursive graph traversal.
- Validation regardless of evidence status.

The inheritance subgraph must remain a directed
acyclic graph (DAG).

Other relationship types are not subject to
the inheritance cycle restriction.

#### Temporal Consistency

Introduced chronological constraints for
confirmed and inferred antecedent relationships.

The target event must not occur after
the source event.

Exceptions:

- Unknown relationships.
- General `related_to` relationships.

Same-day relationships are permitted.

Chronological precedence alone does not
establish causality.

#### Continuous Integration

Added:

`.github/workflows/validate.yml`

GitHub Actions workflow features:

- Python 3.11 execution environment.
- Required file checks.
- JSON syntax checks.
- Python syntax checks.
- Reference validator execution.
- Push-triggered validation.
- Pull request validation.
- Manual workflow execution.
- Read-only repository permissions.
- Five-minute execution timeout.

Initial GitHub Actions validation passed.

No external Python dependencies are required.

#### Documentation

Added:

- `README.md`
- `specs/aelg-v0.1.md`
- `CHANGELOG.md`

Documentation covers:

- Project purpose.
- Core design principles.
- Evolution layers.
- Lineage semantics.
- Evidence classifications.
- Validation requirements.
- Privacy considerations.
- Security considerations.
- Interoperability concepts.
- Future extension areas.

### Security

- Ledger content is treated as data.
- Ledger descriptions are not executed.
- Actor names are not interpreted as commands.
- Evidence URIs are not automatically accessed.
- Validation does not require network access.
- GitHub Actions uses read-only repository permissions.
- Undefined record properties are rejected.
- Malformed JSON input is rejected.
- Duplicate JSON object keys are rejected.

### Design Decisions

- AI evolution is represented as a graph
  rather than a single lineage tree.
- Human questions are recognized as potential
  evolutionary influences.
- Evidence status is separated from
  structural validity.
- Temporal proximity is not treated
  as proof of causation.
- Uncertainty is preserved as an explicit state.
- Evidence classifications may be downgraded
  when supporting information changes.
- Only technical and conceptual inheritance
  is subject to mandatory cycle restrictions.
- Each event has one primary evolution layer.
- Identifiers are local to an individual ledger.
- External runtime dependencies are avoided.
- Future expansion is driven by observed needs.

### Interoperability

AELG may conceptually complement:

- QuestionTube
- Dialogue Archive
- Shared Trace
- Reasoning Recycling
- Royalty OS

These integrations are optional and conceptual.

No external specification is required
for AELG v0.1 conformance.

### Known Limitations

- No automated causal inference.
- No independent evidence verification.
- No evidence authenticity certification.
- No evidence content retrieval.
- No complete URI standards conformance checker.
- No event-level evidence status classification.
- No approximate date or date range support.
- No cross-ledger identifier resolution.
- No interactive graph visualization.
- No automated historical data collection.
- No real-time evolution monitoring.
- No contribution scoring.
- No financial attribution or royalty calculation.
- No dedicated automated negative test suite.
- No independent JSON Schema engine validation
  in the default CI workflow.

Passing structural and semantic validation
does not establish historical accuracy,
source authenticity, evidence sufficiency,
or causal truth.

---

## Potential Future Extensions

The following areas may be considered
when practical requirements emerge.

### Evolution Graph Visualization

- Graph generation from evolution ledgers.
- Cross-layer visualization.
- Branching and convergence analysis.
- Evidence status visualization.
- Chronological evolution mapping.

### Evidence Management

- Evidence revision history.
- Independent evidence verification.
- Evidence content hashing.
- Contradictory evidence management.
- Event-level verification status.

### Question-Driven Evolution

- Question lineage integration.
- Human feedback traceability.
- Question-to-change relationship analysis.
- Evolutionary pressure observation.

### Extended Interoperability

- Cross-ledger references.
- Contribution provenance.
- Shared Trace integration.
- Reasoning asset lineage.
- Independent attribution mechanisms.
- Value circulation interoperability.

These extensions are not committed features.

Future development should respond to
observed limitations and practical needs.

---

## Version History

| Version | Release Date | Description |
|---|---|---|
| v0.1.0 | 2026-11-25 | Initial evidence-based evolution ledger specification |

---

## Guiding Principle

> Record the change.
> Preserve the evidence.
> Respect uncertainty.
> Reveal the lineage.

---

AI Evolution Lineage Graph (AELG)

From model history to evidence-based evolution history.
