# AI Evolution Lineage Graph (AELG)

> Trace not only what AI has become,
> but also what has shaped its evolution.

**Version:** v0.1.0  
**Status:** Initial Specification

## 1. Overview

AI Evolution Lineage Graph (AELG) is a minimal,
evidence-based specification for recording AI evolution,
influencing factors, and lineage relationships.

AI evolution is not determined solely by model developers.

It may also be shaped by:

- Research discoveries
- Technical inheritance
- Open-source contributions
- Human questions and feedback
- Computational resources
- Economic constraints
- Safety requirements
- Regulatory changes
- Operational failures
- Social expectations

AELG provides a structured way to record these changes
and their documented or potential relationships.

The objective is not to determine who owns AI evolution,
but to make its history and influencing factors traceable.

---

## 2. Core Philosophy

Traditional AI histories often focus on:

- Model releases
- Company announcements
- Benchmark improvements
- Parameter counts
- Capability comparisons

AELG focuses on a different question:

> What changed, what influenced the change,
> and what evidence supports that relationship?

AI evolution should be understood as a network
of interacting factors rather than a single
corporate or technological lineage.

### From Tree to Graph

Traditional lineage:

```text
Model A
   |
Model B
   |
Model C
```

AELG conceptual lineage:

```text
Research -----------+
                    |
Human Questions ----+
                    |
Resource Pressure --+--> Evolution Event
                    |          |
Safety Requirements-+          |
                    |          v
Open Source --------+    Future Changes
```

Multiple factors may converge on a single evolution event.

A single factor may also influence multiple events.

AELG therefore uses a graph-oriented conceptual model.

---

## 3. Core Principles

### Principle 1: Evolution Is Multi-Factorial

AI evolution may emerge from interactions between
technical, human, economic, and institutional factors.

No single category is assumed to explain all changes.

### Principle 2: Evidence Before Attribution

Influence must not be treated as established
without sufficient supporting evidence.

### Principle 3: Correlation Is Not Causation

Temporal proximity does not establish causality.

An event occurring before another event does not
necessarily mean that it caused the later event.

### Principle 4: Human Questions Are Potential Evolutionary Pressure

Human questions, feedback, and requirements may
influence the direction of AI development.

However, specific influence claims require evidence.

### Principle 5: Uncertainty Must Be Preserved

Unknown relationships must remain unknown
until adequate evidence becomes available.

### Principle 6: Lineage May Cross Organizational Boundaries

AI evolution may involve research, software,
knowledge, and practices originating outside
the organization releasing a system.

### Principle 7: Minimal and Extensible

AELG begins with the smallest practical structure.

Additional capabilities should be introduced
only when concrete requirements emerge.

---

## 4. Evolution Layers

AELG defines five primary evolution layers.

| Layer | Identifier | Description |
|---|---|---|
| Technology | `technology` | Models, algorithms, architectures, and methods |
| Implementation | `implementation` | Deployment, integration, and practical applications |
| Question | `question` | Human questions, feedback, needs, and requirements |
| Resource | `resource` | Computing, energy, memory, infrastructure, and cost |
| Governance | `governance` | Safety, regulation, rights, accountability, and trust |

These layers are categories for observation.

They do not represent a mandatory hierarchy.

Relationships may cross multiple layers.

---

## 5. Basic Architecture

```text
External Factors
       |
       v
Evolution Events
       |
       v
Lineage Relationships
       |
       v
Evidence Records
       |
       v
Evolution Ledger
       |
       v
Future Graph Visualization
```

Version 0.1 focuses on the evolution ledger
and structured lineage records.

Graph visualization is outside the current scope.

---

## 6. Core Components

### 6.1 Evolution Event

An evolution event represents an identifiable
change or documented development.

Examples include:

- Introduction of a new architecture
- Release of a model
- Addition of a safety mechanism
- Reduction of inference costs
- Introduction of local inference
- Changes to an evaluation framework
- Publication of user requirements
- Changes in governance policies

Each event contains:

- Event identifier
- Event date
- Evolution layer
- Title
- Description
- Associated actors
- Evidence references

### 6.2 Lineage Relationship

A lineage relationship connects two evolution events.

It records a documented or proposed connection
without automatically asserting causality.

Initial relationship types:

| Type | Description |
|---|---|
| `derived_from` | Technical or conceptual inheritance |
| `influenced_by` | Documented or proposed influence |
| `responds_to` | Response to a requirement, issue, or event |
| `enabled_by` | An enabling condition or capability |
| `constrained_by` | A limiting condition or pressure |
| `related_to` | Association without a specific causal claim |

Except for `related_to`, these relationships are directed.

The source event is the event being described.

The target event is the referenced antecedent,
influence, condition, or constraint.

For example:

```text
Event B --derived_from--> Event A
```

This indicates that Event B derives from Event A.

### 6.3 Evidence Record

An evidence record identifies a source supporting
an event or a lineage relationship.

Possible evidence sources include:

- Research papers
- Official technical reports
- Public repositories
- Release notes
- Regulatory documents
- Public feedback records
- Verified incident reports
- Published evaluation results

Evidence records should identify:

- Evidence identifier
- Source type
- Source location
- Description

Evidence must be interpreted within its actual scope.

An official statement may establish that a change
was announced without establishing why it occurred.

---

## 7. Evidence Status

AELG defines three evidence statuses.

| Status | Description |
|---|---|
| `confirmed` | The stated relationship is directly supported by evidence |
| `inferred` | The relationship is plausible and supported indirectly |
| `unknown` | The relationship has not been adequately established |

### Confirmed

Evidence directly supports the specific relationship
being recorded.

Confirmation applies only to the scope of that evidence.

It does not imply that every possible cause
has been identified.

### Inferred

Evidence suggests a relationship,
but the available information is insufficient
for direct confirmation.

Inferred relationships must not be presented
as established facts.

### Unknown

A relationship has been proposed or observed,
but supporting evidence is insufficient.

An unknown relationship must not be treated
as proof of influence or causality.

---

## 8. Example Evolution Record

The following example is fictional.

It illustrates the structure of an evolution ledger
without making claims about real AI systems.

```json
{
  "spec_version": "0.1.0",
  "events": [
    {
      "event_id": "EVT-001",
      "date": "2026-01-01",
      "layer": "question",
      "title": "Demand for lower inference costs",
      "description": "Users request more affordable AI inference.",
      "actors": [
        "example-user-community"
      ],
      "evidence_ids": [
        "EVD-001"
      ]
    },
    {
      "event_id": "EVT-002",
      "date": "2026-02-01",
      "layer": "technology",
      "title": "Introduction of efficient inference",
      "description": "An example developer introduces an optimization.",
      "actors": [
        "example-developer"
      ],
      "evidence_ids": [
        "EVD-002"
      ]
    }
  ],
  "relationships": [
    {
      "relationship_id": "REL-001",
      "source_event_id": "EVT-002",
      "target_event_id": "EVT-001",
      "type": "influenced_by",
      "evidence_status": "unknown",
      "evidence_ids": [],
      "description": "A possible influence that has not been established."
    }
  ],
  "evidence": [
    {
      "evidence_id": "EVD-001",
      "source_type": "user_feedback",
      "source_uri": "https://example.com/feedback",
      "description": "Fictional user feedback record."
    },
    {
      "evidence_id": "EVD-002",
      "source_type": "release_note",
      "source_uri": "https://example.com/release",
      "description": "Fictional technical release announcement."
    }
  ]
}
```

The existence of both events does not establish
an influence relationship.

Therefore, the relationship remains `unknown`.

The example URLs are placeholders and do not
represent verified evidence.

---

## 9. Validation Rules

A conforming AELG v0.1 ledger must satisfy
the following minimum requirements:

1. Required fields must be present.
2. Event identifiers must be unique.
3. Relationship identifiers must be unique.
4. Evidence identifiers must be unique.
5. Evolution layers must use supported values.
6. Relationship types must use supported values.
7. Evidence statuses must use supported values.
8. Event references must resolve to existing events.
9. Evidence references must resolve to existing records.
10. Self-referencing relationships must be rejected.
11. Confirmed relationships must reference evidence.
12. Inferred relationships must reference evidence.
13. Confirmed or inferred antecedent relationships
    must not reference a later event.
14. `derived_from` relationships must not form cycles.

Unknown relationships may be retained
without supporting evidence.

The validator checks structural consistency.

It does not independently establish the truth,
authenticity, or causal sufficiency of evidence.

---

## 10. Repository Structure

```text
ai-evolution-lineage/
├── README.md
├── specs/
│   └── aelg-v0.1.md
├── schemas/
│   └── evolution-event.schema.json
├── examples/
│   └── sample-evolution.json
├── scripts/
│   └── validate.py
├── .github/
│   └── workflows/
│       └── validate.yml
└── CHANGELOG.md
```

---

## 11. Quick Start

### Requirements

- Python 3.11 or later
- No external Python dependencies

### Clone Repository

```bash
git clone <repository-url>
cd ai-evolution-lineage
```

Replace `<repository-url>` with the actual
GitHub repository URL.

### Validate Example

```bash
python scripts/validate.py
```

The reference validator is intended to check:

- Required fields and supported values
- Identifier uniqueness
- Reference integrity
- Evidence requirements
- Temporal consistency
- Inheritance cycle detection

The JSON Schema provides a machine-readable
description of the ledger structure.

The dependency-free reference validator implements
the required structural and semantic checks
without relying on an external JSON Schema engine.

---

## 12. GitHub Actions

The repository is designed to support
automated validation through GitHub Actions.

```text
Push or Pull Request
          |
          v
Set Up Python
          |
          v
Validate Evolution Ledger
          |
          v
     PASS / FAIL
```

Continuous integration checks structural validity.

Passing validation does not certify historical
accuracy or the truth of recorded influence claims.

---

## 13. Relationship to Other Specifications

AELG is designed as an independent
evolution observation layer.

It may complement the following conceptual
specifications:

| Specification | Potential Role |
|---|---|
| QuestionTube | Question origin and derivation |
| Dialogue Archive | Human-AI dialogue records |
| Shared Trace | Shareable evidence and trace records |
| Reasoning Recycling | Reuse of reasoning assets |
| Royalty OS | Future contribution and value attribution |

These integrations are conceptual.

AELG v0.1 does not require any of these
specifications as runtime dependencies.

---

## 14. Privacy and Attribution

AELG must not be used to justify unauthorized
collection or publication of personal information.

Public records and appropriately authorized
evidence should be preferred.

The existence of a human question,
feedback record, or dialogue does not automatically
establish its contribution to a model update.

AELG does not determine:

- Intellectual property ownership
- Legal responsibility
- Financial entitlement
- Individual contribution scores
- Royalty distribution

Such determinations require additional evidence,
governance, and appropriate authorization.

---

## 15. Non-Goals

Version 0.1 does not attempt to provide:

- Automated causal inference
- Automatic contribution attribution
- Real-time AI evolution monitoring
- Large-scale knowledge graph infrastructure
- Interactive graph visualization
- Model performance rankings
- Royalty calculation
- Autonomous evidence verification
- Blockchain-based record storage

These capabilities are intentionally excluded
from the initial specification.

---

## 16. Roadmap

### v0.1 — Evolution Ledger

- Evolution event definition
- Five evolution layers
- Lineage relationship types
- Evidence status classification
- JSON Schema
- Reference validation
- Continuous integration

### Potential v0.2 — Evolution Graph

- Graph generation
- Cross-layer lineage visualization
- Branching and convergence analysis

### Potential v0.3 — Question-Driven Evolution

- Question lineage integration
- Human feedback traceability
- Evolutionary pressure analysis

### Future Exploration

- Independent evidence verification
- Historical evolution comparison
- Contribution provenance
- Interoperability with value circulation systems

Future versions are exploratory.

Expansion depends on observed requirements
and available evidence.

---

## 17. Design Philosophy

AI evolution is not necessarily a single tree.

It may be a network of converging technologies,
human questions, resource constraints,
social pressures, and institutional decisions.

AELG does not attempt to control that evolution.

It attempts to observe and document it.

```text
Questions create pressure.

Pressure may influence direction.

Direction produces change.

Change leaves traces.

Traces reveal lineage.
```

The purpose of AELG is to preserve those traces
without overstating what they prove.

---

## 18. Conclusion

AI systems may be developed by organizations,
but their evolution can be shaped by a wider
network of knowledge, resources, and social forces.

Understanding AI evolution requires more than
tracking model releases and performance scores.

It requires examining the relationships
behind technological change.

AELG begins with a simple principle:

> Record the change.
> Preserve the evidence.
> Respect uncertainty.
> Reveal the lineage.

---

**AI Evolution Lineage Graph — AELG**

From model history to evidence-based evolution history.
