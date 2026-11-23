# ACL 2027 paper-code evidence archive

This repository is a compact research audit of archived NLP paper code and its prediction outputs. It records which files support each result, what can be reproduced on CPU, and where protocols differ. It is not a replacement for the upstream implementations.

## Current status

The BeyondAtoms CARVE prediction audit is verified against the exact remote prediction exports and the historical pooled strict Claim-only LR OOF predictions. The underlying source archive and row-level predictions are intentionally excluded from this public repository. Other archived packages (GRACE, VitaminC, construction, interaction, strategy selection, and synthesis) have not yet been audited in this checkout; no cross-package conclusion is claimed yet.

## Verified BeyondAtoms result

On 1,550 matched examples, CARVE has 1,427 correct predictions (92.06% accuracy) and the historical pooled strict LR has 1,115 (71.94%). The matched four-cell table is:

| | LR correct | LR wrong | Total |
|---|---:|---:|---:|
| CARVE correct | 1,043 | 384 | 1,427 |
| CARVE wrong | 72 | 51 | 123 |
| Total | 1,115 | 435 | 1,550 |

The exact two-sided McNemar p-value reported by the audit is `1.609815026881316e-52`. This is a paired comparison of these specific archived outputs; it does not establish that the models were trained under identical protocols or that CARVE's performance generalizes beyond this benchmark.

## Reproduction

`scripts/recompute_paired.py` recomputes the matched table from the two CSVs when the user supplies them locally. It does not download or extract archives. Input paths are explicit command-line arguments. The expected schemas and file fingerprints are documented in `docs/beyondatoms-evidence.md`.

Raw archives, credentials, and row-level predictions are not committed. The `inputs/` directory is local-only.

