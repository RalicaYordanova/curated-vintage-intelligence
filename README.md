# Curated Vintage Intelligence 💎

**Evidence-first market intelligence and valuation architecture for designer vintage jewelry.**

Curated Vintage Intelligence (CVI) is an independent AI and data engineering project exploring how fragmented, heterogeneous resale-market data can be transformed into structured and testable valuation evidence.

The project combines domain modeling, data quality, valuation logic and Quality Engineering with a particular focus on a fundamental problem:

> How can a valuation system reason from imperfect market evidence without allowing an expected answer to influence the evidence itself?

## Project Goal

Designer vintage jewelry presents an unusually difficult valuation problem.

Market information is fragmented across platforms, comparable items are often sparse, and superficially similar price observations may represent fundamentally different market events.

For example:

```text
€224 → SOLD   → price actually realized in a transaction
€90  → ASKING → price currently requested by a seller
```

Both are prices.

They are not equivalent evidence.

CVI aims to build a structured foundation for:

- market observation modeling
- comparable-item analysis
- evidence-based valuation
- identification and curation
- sourcing and resale intelligence
- data quality and provenance
- future ML-assisted valuation

---

# Vertical Slice — V0.1 ✅

The first end-to-end vertical slice is complete.

It implements a small deterministic valuation service from domain data validation through REST API and automated CI verification.

```text
MarketObservation
        ↓
Pydantic validation
        ↓
Evidence semantics
        ↓
Evidence weighting / ranking
        ↓
Deterministic baseline valuation
        ↓
Valuation service
        ↓
FastAPI
        ↓
Automated tests
        ↓
Coverage quality gate
        ↓
GitHub Actions
        ↓
Docker
```

## Implemented

### Domain & Data Quality

- Pydantic-based `MarketObservation` model
- explicit SOLD vs ASKING semantics
- validation of inconsistent market observations
- separation of realized-sale and asking-price evidence

### Evidence Layer

- deterministic evidence weighting
- SOLD evidence ranked above ASKING evidence
- explicit behavior for empty evidence collections
- separation of observation semantics from valuation logic

### Baseline Valuation

The V0.1 baseline deliberately uses a simple and explainable rule:

> **Median of qualified realized-sale observations**

ASKING prices do not silently enter the realized-sale baseline.

If no realized-sale evidence exists, the system explicitly rejects baseline calculation rather than fabricating a valuation.

This is intentionally a baseline — not the final CVI valuation algorithm.

---

# Core Architectural Invariant 🔒

A central Quality Engineering requirement is protection against **anchoring**.

An external expected valuation may be available to the system, but it must not influence the evidence-derived baseline.

```text
Same evidence
+ different external expectation
        ↓
Same baseline
```

Implemented as an executable invariant:

```python
baseline_a = valuate(
    observations,
    external_anchor=15,
)

baseline_b = valuate(
    observations,
    external_anchor=80,
)

assert baseline_a == baseline_b
```

At the same time:

```text
New verified evidence
        ↓
Baseline may change
```

This establishes an important architectural distinction:

> **Expectations do not change evidence. New evidence can change the valuation.**

The expected valuation is therefore not used as an input for deciding whether an observation deserves to influence the evidence-derived baseline.

---

# API

The valuation logic is exposed through FastAPI.

Implemented endpoints:

```text
GET  /health
POST /valuation
GET  /docs
```

`POST /valuation` uses the same underlying valuation service as the Python application rather than implementing separate pricing logic inside the API layer.

Example response:

```json
{
  "baseline": 16.5,
  "evidence_count": 2,
  "anchor_used_for_baseline": false
}
```

API tests verify:

- successful valuation requests
- Pydantic validation at the API boundary
- HTTP 422 for invalid observations
- consistency between API and service-layer results
- anti-anchoring behavior through the REST interface

---

# Quality Engineering

Quality is treated as part of the architecture rather than as a final testing phase.

The current vertical slice includes:

- unit testing with pytest
- API testing with FastAPI TestClient
- semantic data validation
- boundary-condition testing
- executable architectural invariants
- service/API consistency tests
- measured code coverage
- CI-enforced coverage threshold of **≥ 86%**
- automated GitHub Actions pipeline
- Docker build verification
- container startup verification
- automated `/health` check
- automated FastAPI `/docs` availability check

A change that drops coverage below the configured threshold causes CI to fail.

---

# Technology Stack

Implemented in V0.1:

- Python
- Pydantic
- FastAPI
- pytest
- pytest-cov
- httpx
- GitHub Actions
- Docker
- Uvicorn

---

# Engineering Principles

CVI V0.1 deliberately favors explicit and testable behavior over premature model complexity.

### 1. Preserve evidence

Unexpected observations should not automatically be deleted because they disagree with an expected valuation.

### 2. Separate observation from interpretation

A realized transaction is ground truth for what happened in that transaction.

It is not automatically ground truth for an item's latent market value.

### 3. Avoid anchoring

Expected valuation must not determine which observations are considered trustworthy.

### 4. Earn model complexity

Transaction context, bidder competition, exposure, timing and similar variables may become useful features.

They should become model features when repeated evidence justifies them — not because one unusual transaction makes them intuitively attractive.

### 5. Make assumptions executable

Important architectural assumptions should become automated tests wherever possible.

---

# Current Architecture

```text
                     Market observations
                            │
                            ▼
                   MarketObservation
                       (Pydantic)
                            │
                            ▼
                Semantic data validation
                            │
                            ▼
                Evidence classification
                  SOLD / ASKING / ...
                            │
                            ▼
               Evidence weighting/ranking
                            │
                            ▼
              Deterministic SOLD baseline
                       (median)
                            │
                            ▼
                    Valuation service
                            │
                            ▼
                       FastAPI
                     /valuation
                            │
                            ▼
                 Automated API tests
                            │
                            ▼
                    GitHub Actions
                  tests + coverage
                            │
                            ▼
                         Docker
```

---

# What V0.1 Does Not Claim

The current implementation is an architectural vertical slice, not a production-ready AI pricing engine.

It does **not** yet claim to provide:

- final market-value predictions
- statistically calibrated confidence scores
- production-grade comparable selection
- learned transaction-context effects
- causal interpretation of auction outcomes
- trained ML valuation models

These capabilities are deliberately separated from the first vertical slice.

The purpose of V0.1 is to establish a reliable and testable foundation on which more sophisticated valuation methods can later be evaluated.

---

# Why This Matters

In sparse and noisy markets, producing a number is relatively easy.

Producing a number while being able to explain:

- what evidence generated it,
- what each observation means,
- which assumptions were applied,
- what information was deliberately excluded,
- and which architectural properties are automatically protected

is a different engineering problem.

CVI explores that problem at the intersection of:

**AI/Data Engineering × Quality Engineering × Vintage Market Intelligence**

---

# Status

**V0.1 — First end-to-end vertical slice complete ✅**

Current capability:

```text
Validated market data
        ↓
Deterministic valuation baseline
        ↓
REST API
        ↓
Automated tests
        ↓
≥86% coverage gate
        ↓
GitHub Actions CI
        ↓
Docker
```

## Next Phase

Expand the evidence base and comparable-item architecture before introducing additional model complexity.

The next development phase will focus on:

- richer real-world market observations
- comparable-item selection
- provenance and evidence quality
- robust handling of sparse and unusual market observations
- valuation uncertainty
- evaluation methodology
- additional executable quality invariants

> **Complexity should be earned by evidence.**
