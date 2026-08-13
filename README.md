# curated-vintage-intelligence
AI-assisted market intelligence and valuation prototype for designer vintage jewelry.
# Curated Vintage Intelligence

Curated Vintage Intelligence is an independent AI and data engineering
initiative exploring data-driven identification and valuation of designer
vintage jewelry.

## Project Goal

The project aims to transform fragmented vintage jewelry market information
into structured and measurable insights for:

- identification
- valuation
- comparable-item analysis
- sourcing
- curation
- resale intelligence

## Current Status

🚧 Prototype in development

Current focus:
- domain data modeling
- market observation dataset
- backend architecture
- data quality
- automated testing

## Planned Architecture

User / Dataset
      ↓
FastAPI
      ↓
Pricing Engine
      ↓
PostgreSQL + pgvector
      ↓
Comparable Sales / ML Model

## Planned Tech Stack

- Python
- FastAPI
- PostgreSQL
- pgvector
- CatBoost
- pytest
- GitHub Actions

## Quality Engineering

A central goal of the project is to explore quality assurance for
data-driven and ML-based systems, including:

- data validation
- API testing
- integration testing
- prediction accuracy
- confidence evaluation
- model quality gates
- CI/CD

## Project Status

Version 0.1 – Data model and architecture

# Curated Vintage Intelligence – Vertical Slice

A small evidence-first valuation service for structured resale-market observations.

## Current vertical slice

Implemented:

- Pydantic validation for market observations
- Explicit SOLD vs ASKING semantics
- Deterministic evidence weighting
- Median-based baseline valuation
- Anti-anchoring invariant
- FastAPI `/valuation` endpoint
- Automated pytest suite
- Coverage quality gate
- GitHub Actions CI
- Dockerized FastAPI service
- Container health and `/docs` checks

## Core architectural invariant

The expected valuation must not influence the evidence-derived baseline.

Same evidence + different external anchor → same baseline.

New verified evidence → baseline may change.
