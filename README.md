# Conservative AI Counterfeit Detection (Vision Layer)

This repository implements a **conservative, reference-based computer vision system**
for detecting counterfeit pharmaceutical packaging.

It is designed as the **physical authentication (AI) layer** of a larger
blockchain-based drug traceability and anti-counterfeit system.

This repository focuses **only on vision-based physical inspection**.
Blockchain logic is **mocked** to demonstrate system interaction.

---

## Design Philosophy

This system is intentionally **conservative**.

- It detects **obvious physical deviations**
- It does **not attempt to detect high-quality visual clones**
- It does **not make final authenticity decisions**

The purpose of this layer is to filter physically implausible packages.
Packages that pass visual inspection are expected to be verified by downstream systems.

---

## System Overview

The system operates in two phases:

### 1. Reference Enrollment
A genuine medicine package image is uploaded once and enrolled as a **reference**.

From this reference image, the system extracts:
- Print sharpness
- Global color profile
- Local layout geometry

These features form the baseline for future comparisons.

### 2. Verification
Incoming package images are compared against the enrolled reference.
If no significant physical deviation is detected, the package is forwarded
to blockchain verification.

---

## Sample Images Explained

The `samples/` directory contains controlled examples used to demonstrate system behavior.

### `sample1.png` — Low-Quality Reprint
- Reduced sharpness and reprint artifacts
- **Rejected by the AI layer** due to low print quality

### `sample2.png` — Layout Drift
- Positional mismatch in text and design elements
- **Rejected by the AI layer** due to layout deviation

### `sample3.png` — High-Quality Clone
- Visually similar to the genuine package
- **Passes AI verification**
- Intended to be rejected by blockchain verification

### `sample4.png` — Replayed Identity
- Visually indistinguishable from the genuine package
- **Passes AI verification**
- Intended to be rejected by blockchain verification

---

## Conservative Nature

This system is conservative by design.

Only clear physical deviations are detected.
High-quality visual clones are **not detected** by the AI layer.

---

## Blockchain Mocking

Blockchain behavior is **mocked** in this repository.

The mock simulates:
- Duplicate identity detection
- Identity reuse

This is used to demonstrate how visually plausible packages
can still be flagged after physical inspection.

---

## Scope

- Reference-based computer vision only
- No machine learning models
- Mocked blockchain behavior
- Proof-of-concept system

---

## Relationship to Larger Project

This module is an **extension of a larger anti-counterfeit system**
that combines computer vision with blockchain-based verification.

**This repository contains only the AI vision component**.

---

## Status

Proof of Concept
