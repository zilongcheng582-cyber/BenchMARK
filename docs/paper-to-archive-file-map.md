# Paper-to-archive file map

This map was assembled from the supplied `E:\main.tex`, `E:\references.bib`, `E:\main.pdf`, and `E:\ACL2027_ARCHIVE_GUIDE_ZH.docx`, then checked against named entries in the master archive's `FILE_INDEX.csv`. It identifies the concrete archive packages and files that correspond to the manuscript. `SHA256SUMS.txt` has not been checked, and the 371-row index has not been exhaustively reconciled, so this is a research-file map rather than a complete package inventory.

## Manuscript source files

| File | Status | Role |
|---|---|---|
| `E:\main.tex` | Found, 53,747 bytes | ACL-compatible paper source; includes the main claims and appendix. |
| `E:\references.bib` | Found, 10,503 bytes | The bibliography explicitly loaded by `\bibliography{references}`. |
| `E:\main.pdf` | Found, 242,657 bytes | Rendered paper PDF; also named by the archive guide. |

`main.tex` has no `\input`, `\include`, or `\includegraphics` dependencies. Its only explicit external TeX dependency is `references.bib` (besides the ACL style and LaTeX packages supplied by the build environment).

## The nine experiment packages and manuscript correspondence

| Package ZIP | Confirmed archive member paths | Manuscript sections / claims supported |
|---|---|---|
| `beyondatoms_lr_recovered.zip` | `beyondatoms_lr_recovered/RESEARCH_NOTE.md`; `beyondatoms_lr_recovered/predictions_per_sample_precomputed.csv` | Historical Claim-only LR exploratory baselines. The guide warns these predictions use an Evidence-grouping protocol and are not the current `main.pdf` pooled-LR/CARVE comparison. Keep separate from the later `original_shortcut_audit` OOF files. |
| `ba_dataset_first_audit.zip` | `DATASET_FIRST_THEORY_AUDIT.md`; `pair_stats.json` | Four operation construction, text features, fixed evidence pairing, and theory correspondence. Relates to §RQ1 and appendix deduplication/pair units. |
| `GRACE_AUDIT.zip` | `grace_audit/manifest.json`; `grace_audit/02_GRACE_TRAIN_TEST_RESULTS.md`; `grace_audit/results/judge_predictions.csv`; `grace_audit/results/predictions.csv.gz` | Cross-task evidence cited in Related Work and the study-level synthesis. Preserve the distinction between official test predictions, auxiliary NLI masking, and step-only TF-IDF. |
| `VITAMINC_AUDIT.zip` | `vitaminc_audit/manifest.json`; `vitaminc_audit/03_NATIVE_CONTRASTIVE_RESULTS.md`; `vitaminc_audit/results/neural_rectangles.csv`; `vitaminc_audit/results/paired_prediction_matrix.csv.gz`; `vitaminc_audit/results/pairs.csv.gz`; `vitaminc_audit/results/rectangles.csv.gz`; `vitaminc_audit/results/rows.csv.gz`; `vitaminc_audit/results/albert_predictions.csv.gz`; `vitaminc_audit/results/linear_predictions.csv.gz`; `vitaminc_audit/results/nli_predictions.csv.gz`; `vitaminc_audit/results/real_transfer_predictions.csv.gz`; `vitaminc_audit/results/synthetic_transfer_predictions.csv.gz` | Contrastive evidence-reliance comparison discussed in Related Work and exploratory appendix. `neural_rectangles.csv` defines the common 128-group frozen-prediction comparison. |
| `VITAMINC_RESIDUAL_AUDIT.zip` | `residual_audit/manifest.json`; `residual_audit/03_ALBERT_RESIDUAL_ANALYSIS.md`; `residual_audit/results/predictions.csv.gz`; `residual_audit/results/quartet_success.csv.gz`; `residual_audit/results/sample_success.csv` | Residual and strategy-selection evidence; distinguishes full 11,127 quartets from common 128 groups. |
| `ACL2027_RESEARCH_SYNTHESIS.zip` | `acl_synthesis/EXECUTIVE_SUMMARY_ZH.md`; `acl_synthesis/03_CLAIM_LEVEL_NOVELTY_MATRIX.md` | Cross-task synthesis, literature novelty, and paper framing. Check against the final strategy decision before carrying over claims. |
| `ACL2027_CONSTRUCTION_AUDIT.zip` | `construction_audit/EXECUTIVE_SUMMARY_ZH.md`; `construction_audit/04_STRUCTURAL_IDENTIFIABILITY.md`; `construction_audit/07_RESEARCH_DIRECTION_COMPARISON.md`; `construction_audit/results/construction_profiles.json`; `construction_audit/results/structural_rows.csv.gz`; `construction_audit/results/input_manifest.json`; `construction_audit/results/behavior_replay/audit.json`; `construction_audit/results/behavior_replay/common_metrics.csv`; `construction_audit/results/behavior_replay/input_hashes.json` | Construction profiles, one-sided oracle, graph certificate, concentration, behavior replay, and cross-task assumptions. |
| `ACL2027_INTERACTION_AUDIT.zip` | `interaction_audit/01_ARCHIVE_AND_PREDICTION_ALIGNMENT.md`; `interaction_audit/manifest.json`; `interaction_audit/EXECUTIVE_SUMMARY_ZH.md`; `interaction_audit/03_VITAMINC_CONFOUNDER_ROBUSTNESS.md`; `interaction_audit/results/interaction_bootstrap.csv`; `interaction_audit/results/beyondatoms_pair_cells.csv`; `interaction_audit/results/unified_accuracy.csv.gz` (3,583,889 bytes) | Main interaction comparisons, within-family intervals, common support, ablation claims, and unified frozen predictions. |
| `ACL2027_STRATEGY_SELECTION_AUDIT.zip` | `selection_audit/01_INPUT_AND_PREDICTION_AUDIT.md`; `selection_audit/README.md`; `selection_audit/EXECUTIVE_SUMMARY_ZH.md`; `selection_audit/08_ACL_FINDINGS_DECISION.md`; `selection_audit/replay_interaction.py`; `selection_audit/results/input_manifest.json`; `selection_audit/results/strategy_catalog.csv`; `selection_audit/results/02_ALL_STRATEGIES_CONSTRUCTION_MATRIX.csv`; `selection_audit/results/strategy_pair_reversals.csv`; `selection_audit/results/previous_interaction_bootstrap.csv`; `selection_audit/results/weight_diagnostics.csv`; `selection_audit/results/covariate_balance.csv`; `selection_audit/results/vitaminc_residual_trace.csv`; `selection_audit/results/coverage_curves.csv`; `selection_audit/results/reference_sensitivity.csv` | Final selected estimands, pair reversals, overlap weighting, residual accounting, and current Findings go/no-go. Read this package first when reconciling earlier conclusions. |

## Exact rows/cases named in `main.tex`

The manuscript names these case IDs; the exact case-level evidence rows and intervention specification files must be located before reproducing the narrative:

- End-to-end intervention: `re-anchoring_140`, `re-anchoring_265`.
- Repair bypass: `substitution_260`, `re-anchoring_262`.
- Rule-level observations: `omission_155`, `omission_254`.
- Temporal audit: `substitution_209`, `substitution_225`, plus suffixes `_264`, `_267`, `_336`, `_215` in the relevant operation/component tables.
- Cross-system source screen: fixed-commit sources for FDSpotter, VeriFact, and FactReasoner, as identified by `REPO_VERSIONS.json` and the cross-system screen records.

These are case IDs, not literal filesystem paths. The four operation datasets below are located, but the index does not identify which member stores the saved intervention roster, patch values, replay outputs, or source excerpts.

## Master-archive locator files

The guide identifies these as the authoritative route to an exhaustive inventory and reproducibility metadata:

- `FILE_INDEX.csv`: archive member path, package, and purpose.
- `SHA256SUMS.txt`: package/data/source/document fingerprints.
- `REPO_VERSIONS.json`: fixed upstream repositories, commits, and URLs.
- `E:\main.pdf`: local manuscript PDF, 242,657 bytes; the guide also lists `main.pdf` in the master archive.

The extracted master index has 371 data rows and columns `容器`, `相对路径`, `用途`, `字节数`. Most named entries above were checked against this index; `selection_audit/01_INPUT_AND_PREDICTION_AUDIT.md` and `interaction_audit/01_ARCHIVE_AND_PREDICTION_ALIGNMENT.md` were confirmed by direct reads from their nested ZIPs even though the index does not list them. The case IDs themselves do not appear in indexed member paths, and no path matched `casebook` or `intervention`. The exact saved Stage A roster, patch specification, replay output, and source excerpt for `re-anchoring_140` / `re-anchoring_265` are not yet located; those need to be identified by reading the relevant audit specification/report files one at a time.

## Current BeyondAtoms primary paired-result files

These are on the remote working tree, outside the nine ZIP packages. They are the primary files for the current `main.tex` CARVE versus pooled-LR comparison, and must not be confused with the earlier LR ZIP's evidence-grouped exploratory predictions:

- `/root/data/beyondatoms-carve/experiments/audit/carve_predictions.csv`
- `/root/data/beyondatoms-carve/experiments/audit/metrics_recomputed.json`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/ALIGNED_SAMPLES.csv`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/OOF_PREDICTIONS.csv`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/audit_summary.json`

The working tree's `experiments/original_shortcut_audit` is the source for `pooled_strict_lr` in the current draft; the archive's `beyondatoms_lr_recovered/predictions_per_sample_precomputed.csv` is a separate protocol and estimand. The strategy-selection input audit explicitly says the archived bundle lacks same-version per-example pooled-LR predictions aligned to current CARVE. Thus the working-tree files above, rather than that ZIP, are required to substantiate the current paired table; their provenance must stay separate from the earlier archive rows.

## Official BeyondAtoms code snapshot

The master ZIP includes the fixed BeyondAtoms source snapshot. These exact source files were located and read individually:

- `beyondatoms/scripts/run_carve.py` — CLI entry point; imports `Executor` from `pipeline`.
- `beyondatoms/pipeline.py` — defines `Executor` and imports the implementation modules below.
- `beyondatoms/modules/relation_extraction.py` — relation extraction and connective family/symmetry/inverse utilities.
- `beyondatoms/modules/verification.py` — downstream source/claim verification module.
- `beyondatoms/util/util.py` — shared utility dependency imported by the CLI and pipeline.

The manuscript's specific claim about the `direction` field in a match record is not mapped to one of these source files yet. The queried `relation_extraction.py` contains connective handling but does not define that field. The matching implementation and Stage A patch/replay files remain an open file-location item.

All nine package names from the guide were confirmed as entries in the master index. The exact paths shown in the table were matched to index rows; hashes remain unchecked until `SHA256SUMS.txt` is read.

The master index confirms the four operation data files that underlie the case IDs in the manuscript:

- `beyondatoms/datasets/beyondatoms/injection_dataset.json`
- `beyondatoms/datasets/beyondatoms/omission_dataset.json`
- `beyondatoms/datasets/beyondatoms/re-anchoring_dataset.json`
- `beyondatoms/datasets/beyondatoms/substitution_dataset.json`

