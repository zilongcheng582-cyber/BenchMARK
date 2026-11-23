# Paper-to-archive file map

This map was assembled from the supplied `E:\main.tex` and `E:\ACL2027_ARCHIVE_GUIDE_ZH.docx`. It identifies the concrete archive packages and named entry files that correspond to the manuscript. The complete `FILE_INDEX.csv` and `SHA256SUMS.txt` are inside the remote master archive and have not yet been read here; therefore package-internal completeness is not certified.

## Manuscript source files

| File | Status | Role |
|---|---|---|
| `E:\main.tex` | Found, 53,747 bytes | ACL-compatible paper source; includes the main claims and appendix. |
| `E:\references.bib` | Found, 10,503 bytes | The bibliography explicitly loaded by `\bibliography{references}`. |
| `E:\main.pdf` | Found, 242,657 bytes | Rendered copy corresponding to the supplied source; also named by the archive guide. |

`main.tex` has no `\input`, `\include`, or `\includegraphics` dependencies. Its only explicit external TeX dependency is `references.bib` (besides the ACL style and LaTeX packages supplied by the build environment).

## The nine experiment packages and manuscript correspondence

| Package ZIP | Named files to retrieve | Manuscript sections / claims supported |
|---|---|---|
| `beyondatoms_lr_recovered.zip` | `RESEARCH_NOTE.md`; `predictions_per_sample_precomputed.csv` | Historical Claim-only LR exploratory baselines. The guide warns these predictions use an Evidence-grouping protocol and are not the current `main.pdf` pooled-LR/CARVE comparison. Keep separate from the later `original_shortcut_audit` OOF files. |
| `ba_dataset_first_audit.zip` | `DATASET_FIRST_THEORY_AUDIT.md`; `pair_stats.json` | Four operation construction, text features, fixed evidence pairing, and theory correspondence. Relates to §RQ1 and appendix deduplication/pair units. |
| `GRACE_AUDIT.zip` | `02_GRACE_TRAIN_TEST_RESULTS.md`; `results/judge_predictions.csv`; `results/predictions.csv.gz` | Cross-task evidence cited in Related Work and the study-level synthesis. Preserve the distinction between official test predictions, auxiliary NLI masking, and step-only TF-IDF. |
| `VITAMINC_AUDIT.zip` | `03_NATIVE_CONTRASTIVE_RESULTS.md`; `results/neural_rectangles.csv`; `results/pairs.csv.gz`; `results/rectangles.csv.gz`; `results/rows.csv.gz` | Contrastive evidence-reliance comparison discussed in Related Work and exploratory appendix. `neural_rectangles.csv` defines the common 128-group frozen-prediction comparison. |
| `VITAMINC_RESIDUAL_AUDIT.zip` | `03_ALBERT_RESIDUAL_ANALYSIS.md`; `results/predictions.csv.gz`; `results/quartet_success.csv.gz`; `results/sample_success.csv` | Residual and strategy-selection evidence; distinguishes full 11,127 quartets from common 128 groups. |
| `ACL2027_RESEARCH_SYNTHESIS.zip` | `EXECUTIVE_SUMMARY_ZH.md`; `03_CLAIM_LEVEL_NOVELTY_MATRIX.md` | Cross-task synthesis, literature novelty, and paper framing. Check against the final strategy decision before carrying over claims. |
| `ACL2027_CONSTRUCTION_AUDIT.zip` | `results/construction_profiles.json`; `04_STRUCTURAL_IDENTIFIABILITY.md` | Construction profiles, one-sided oracle, graph certificate, concentration, and cross-task assumptions. |
| `ACL2027_INTERACTION_AUDIT.zip` | `03_VITAMINC_CONFOUNDER_ROBUSTNESS.md`; `results/interaction_bootstrap.csv`; `results/beyondatoms_pair_cells.csv`; `manifest.json` | Main interaction comparisons, within-family intervals, common support, and ablation claims. |
| `ACL2027_STRATEGY_SELECTION_AUDIT.zip` | `EXECUTIVE_SUMMARY_ZH.md`; `08_ACL_FINDINGS_DECISION.md`; `results/02_ALL_STRATEGIES_CONSTRUCTION_MATRIX.csv`; `results/strategy_pair_reversals.csv`; `results/weight_diagnostics.csv`; `results/covariate_balance.csv`; `results/vitaminc_residual_trace.csv`; `results/coverage_curves.csv`; `results/reference_sensitivity.csv` | Final selected estimands, pair reversals, overlap weighting, residual accounting, and current Findings go/no-go. Read this package first when reconciling earlier conclusions. |

## Exact rows/cases named in `main.tex`

The manuscript names these cases, which must be located in the archived casebook or saved intermediate-state tables before reproducing the narrative:

- End-to-end intervention: `re-anchoring_140`, `re-anchoring_265`.
- Repair bypass: `substitution_260`, `re-anchoring_262`.
- Rule-level observations: `omission_155`, `omission_254`.
- Temporal audit: `substitution_209`, `substitution_225`, plus suffixes `_264`, `_267`, `_336`, `_215` in the relevant operation/component tables.
- Cross-system source screen: fixed-commit sources for FDSpotter, VeriFact, and FactReasoner, as identified by `REPO_VERSIONS.json` and the cross-system screen records.

These are case IDs, not literal filesystem paths. Their exact member filenames still need to be taken from `FILE_INDEX.csv` and the matching package casebook.

## Master-archive locator files

The guide identifies these as the authoritative route to an exhaustive inventory and reproducibility metadata:

- `FILE_INDEX.csv`: archive member path, package, and purpose.
- `SHA256SUMS.txt`: package/data/source/document fingerprints.
- `REPO_VERSIONS.json`: fixed upstream repositories, commits, and URLs.
- `main.pdf`: manuscript copy in the archive.

The supplied guide names nine packages. No additional archive members are inferred beyond the listed names. The exact internal paths, hashes, and all casebook filenames remain unverified until the index is retrieved.

