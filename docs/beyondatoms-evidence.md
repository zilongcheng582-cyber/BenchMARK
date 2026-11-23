# BeyondAtoms CARVE vs. historical Claim-only LR

## Question

How do the archived CARVE predictions compare sample by sample with the historical pooled strict Claim-only logistic regression (LR) out-of-fold predictions?

## Evidence files and provenance

The verified remote CARVE prediction file is `experiments/audit/carve_predictions.csv` (1,550 rows). Its SHA-256 is `ab5b686dabf0157fb2f8e74f2ede0dcf2fe26091064289aad908a88ff1c6e2af`. Its exporter documents that it reads official CARVE debug logs and maps support/refute labels to binary labels; the archive's separate metrics check reports exact agreement with the official aggregate metrics.

The historical LR predictions are the `pooled_strict_lr` rows in `experiments/original_shortcut_audit/OOF_PREDICTIONS.csv`, joined to `ALIGNED_SAMPLES.csv`. There are 1,550 unique IDs, and the ID, fold, component, and gold label fields align exactly. This is the primary comparison. A separate recovered LR ZIP contains exploratory predictions under a different CV protocol; those are not interchangeable with these historical OOF predictions and are excluded from this comparison.

## Results

| Metric | CARVE | Pooled strict Claim-only LR |
|---|---:|---:|
| n | 1,550 | 1,550 |
| Correct | 1,427 | 1,115 |
| Accuracy | 0.920645 | 0.719355 |
| Macro-F1 | 0.920514 | 0.718920 |

| Paired outcome | Count |
|---|---:|
| Both correct | 1,043 |
| CARVE correct, LR wrong | 384 |
| CARVE wrong, LR correct | 72 |
| Both wrong | 51 |

CARVE is correct on 312 more examples overall. Among the 456 discordant examples, 384 favor CARVE and 72 favor LR. The historical audit reports an exact two-sided McNemar p-value of `1.609815026881316e-52` and a dependency-component paired bootstrap 95% interval for the accuracy difference of `[0.1791, 0.2242]`.

The archived LR audit's overall accuracy interval is `[0.6977, 0.7414]`; that interval is component-clustered. Resampling unit and paired dependence matter because examples share evidence and are not independent.

## Interpretation limits

- This is a comparison of archived predictions with verified row alignment, not a retraining experiment.
- The CARVE and LR pipelines have distinct training and inference protocols. Do not describe the result as a controlled architectural ablation.
- The p-value does not remove benchmark, data-selection, or protocol concerns.
- An exploratory ZIP's `pred_strict`/`pred_hybrid` results use another protocol and must not be substituted for `pooled_strict_lr`.
- The component bootstrap and exact McNemar values above are transcribed from the remote audit summary; the public repository does not contain protected/raw inputs.

## File integrity

CARVE CSV SHA-256: `ab5b686dabf0157fb2f8e74f2ede0dcf2fe26091064289aad908a88ff1c6e2af`.

The LR OOF CSV has 20,150 rows: 13 strategies × 1,550 examples. Filtering the `pooled_strict_lr` strategy yields exactly 1,550 unique IDs. The benchmark CARVE output contains 1,550 data rows plus its header.

