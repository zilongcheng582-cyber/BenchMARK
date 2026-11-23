# Paper-to-archive file map

This map was assembled from the supplied `E:\main.tex`, `E:\references.bib`, `E:\main.pdf`, and `E:\ACL2027_ARCHIVE_GUIDE_ZH.docx`, then checked against named entries in the master archive's `FILE_INDEX.csv` and `SHA256SUMS.txt`. It identifies the concrete archive packages and files that correspond to the manuscript. The 371-row index has not been exhaustively reconciled, so this is a research-file map rather than a complete package inventory.

## Manuscript source files

| File | Status | Role |
|---|---|---|
| `E:\main.tex` | Found, 53,747 bytes | ACL-compatible paper source; includes the main claims and appendix. |
| `E:\references.bib` | Found, 10,503 bytes | The bibliography explicitly loaded by `\bibliography{references}`. |
| `E:\main.pdf` | Found, 242,657 bytes | Rendered paper PDF; SHA-256 matches the archive's `main.pdf` entry. |

Local file SHA-256: `main.tex` `1c56730dc312b71f35bb0f42cbb57ad7fa9985f2c777cc12a8fe251280cd27c6`; `references.bib` `2300d85032a0412e4574949b9b7ac6be21762db22257649e36aeab86a7dc59fb`; `main.pdf` `94be43407f2f0e1c15fe6c7568fdf9f7e47bd1200931720bf989e8bb88925ba3`.

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

| Case ID | Exact dataset member | Record label | Linked evidence record |
|---|---|---|---|
| `re-anchoring_140` | `beyondatoms/datasets/beyondatoms/re-anchoring_dataset.json` | support | `re-anchoring_evidence_70` |
| `re-anchoring_215` | same Re-anchoring dataset | not_support | `re-anchoring_evidence_107` |
| `re-anchoring_262` | same Re-anchoring dataset | support | `re-anchoring_evidence_131` |
| `re-anchoring_264` | same Re-anchoring dataset | support | `re-anchoring_evidence_132` |
| `re-anchoring_265` | same Re-anchoring dataset | not_support | `re-anchoring_evidence_132` |
| `re-anchoring_267` | same Re-anchoring dataset | not_support | `re-anchoring_evidence_133` |
| `re-anchoring_336` | same Re-anchoring dataset | support | `re-anchoring_evidence_168` |
| `substitution_209` | `beyondatoms/datasets/beyondatoms/substitution_dataset.json` | not_support | `substitution_evidence_104` |
| `substitution_225` | same Substitution dataset | not_support | `substitution_evidence_112` |
| `substitution_260` | same Substitution dataset | support | `substitution_evidence_130` |
| `omission_155` | `beyondatoms/datasets/beyondatoms/omission_dataset.json` | not_support | `omission_evidence_75` |
| `omission_254` | same Omission dataset | support | `omission_evidence_121` |

## Master-archive locator files

The guide identifies these as the authoritative route to an exhaustive inventory and reproducibility metadata:

- `FILE_INDEX.csv`: archive member path, package, and purpose.
- `SHA256SUMS.txt`: package/data/source/document fingerprints.
- `REPO_VERSIONS.json`: fixed upstream repositories, commits, and URLs.
- `E:\main.pdf`: local manuscript PDF, 242,657 bytes; the guide also lists `main.pdf` in the master archive.

The master archive is `/root/ACL2027_COMPLETE_RESEARCH_ARCHIVE.zip` on the remote instance (143,020,087 bytes; uploaded 2026-11-23 20:22 local server time).

The extracted master index has 371 data rows and columns `容器`, `相对路径`, `用途`, `字节数`. Most named entries above were checked against this index; `selection_audit/01_INPUT_AND_PREDICTION_AUDIT.md` and `interaction_audit/01_ARCHIVE_AND_PREDICTION_ALIGNMENT.md` were confirmed by direct reads from their nested ZIPs even though the index does not list them. The case IDs themselves do not appear in indexed member paths, and no path matched `casebook` or `intervention`. The Stage A materials were subsequently located in the remote working tree at `experiments/module_causal_audit/stage_a/`; they are outside the master ZIP index, which explains why the earlier archive-only lookup missed them.

## Current BeyondAtoms primary paired-result files

These are on the remote working tree, outside the nine ZIP packages. They are the primary files for the current `main.tex` CARVE versus pooled-LR comparison, and must not be confused with the earlier LR ZIP's evidence-grouped exploratory predictions:

- `/root/data/beyondatoms-carve/experiments/audit/carve_predictions.csv`
- `/root/data/beyondatoms-carve/experiments/audit/metrics_recomputed.json`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/ALIGNED_SAMPLES.csv`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/OOF_PREDICTIONS.csv`
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/audit_summary.json`

The working tree's `experiments/original_shortcut_audit` is the source for `pooled_strict_lr` in the current draft; the archive's `beyondatoms_lr_recovered/predictions_per_sample_precomputed.csv` is a separate protocol and estimand. The strategy-selection input audit explicitly says the archived bundle lacks same-version per-example pooled-LR predictions aligned to current CARVE. Thus the working-tree files above, rather than that ZIP, are required to substantiate the current paired table; their provenance must stay separate from the earlier archive rows.

## Main-text experiment artifact map

Scope: this section follows the experiments reported in the body of `E:\main.tex`. Per the user's instruction, the Appendix evidence-edited pilot (64 groups) and held-out set (119 groups) are not included here.

### RQ1 — grouped claim-only predictability

The five-fold, dependency-grouped OOF protocol and the two estimands (operation-specific and pooled) map to these remote working-tree files:

- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/FROZEN_MODEL_SETTINGS.json` — saved model and fold settings.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/CLAIM_ONLY_GROUPED_BASELINES.csv` — operation-specific and pooled aggregate results used by Table 1.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/OOF_PREDICTIONS.csv` — row-level OOF predictions.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/audit_summary.json` — audit summary and diagnostics.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/pooled_shortcut_audit.py.b64` — saved analysis script, stored base64-encoded.

### RQ2 — CARVE predictions and paired comparison

- `/root/data/beyondatoms-carve/experiments/audit/carve_predictions.csv` — frozen CARVE predictions on the 1,550-record benchmark.
- `/root/data/beyondatoms-carve/experiments/audit/metrics_recomputed.json` — recomputed standalone metrics for Table 2.
- `/root/data/beyondatoms-carve/experiments/audit/error_intersection.json` — saved joint-error summary.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/CARVE_LR_ALIGNED_PREDICTIONS.csv` — record-aligned CARVE/pooled-LR predictions supporting Table 3.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/ALIGNED_SAMPLES.csv` — aligned analysis rows.
- `/root/data/beyondatoms-carve/experiments/original_shortcut_audit/JOINT_PAIR_ACCURACY.csv` — original-pair joint accuracy reported in the Appendix.

The historical LR ZIP remains a different evidence-grouping estimand and is not a substitute for the aligned file above.

### RQ3 — selected Stage A interventions

The Stage A assets are in `/root/data/beyondatoms-carve/experiments/module_causal_audit/stage_a/`. The roster metadata names `frozen_stage_a_cases.jsonl` and gives SHA-256 `94af955786aae3991246a07c2164a15787dbfcc9e8b3701ccee0c9190f69f21b`; the file exists at that path, is 33,090 bytes, and its computed SHA-256 matches. In the roster, `source_id` maps `re-anchoring_140` to `stage_a_05` and `re-anchoring_265` to `stage_a_08`.

- `frozen_stage_a_cases.jsonl` and `frozen_stage_a_cases.meta.json` — frozen 16-case roster, case IDs, and roster hash.
- `PATCH_EXPERIMENT_MATRIX.csv` — six-condition case-level outcome matrix used for the Appendix Stage A table and the selected body examples.
- `build_patch_specs.log` — patch specification/build log; the two target rows identify the evidence-endpoint patch for `stage_a_05` and the match `direction` edit for `stage_a_08`, alongside wrong-value controls.
- `compare_patch_runs.log` — saved patch-run comparison output.
- `structured_replay_cpu.log` and `structured_replay_cpu.py` — CPU baseline replay output and its script.
- `STAGE_A_CASE_STUDIES.md` — case-level claim/evidence excerpts and narratives; this is where the manuscript's omitted verbatim source excerpt for case 140 can be checked.
- `SEMANTIC_CHECK_265_140.md` — focused semantic/control audit for the two body cases.
- `CARVE_MODULE_CAUSAL_AUDIT_STAGE_A.md` — Stage A report; it points to the matrix, logs, source checks, and validation scripts.
- `SOURCE_CODE_HOOK_MAP.md`, `replay_harness.py`, and `run_gpu_validation.sh`, `run_gpu_validation2.sh`, `run_gpu_validation3.sh` — intervention hook map, replay implementation, and saved GPU-validation command scripts. These are historical artifacts; no inference was run during this file audit.

### Negative audits in the body

**B0 temporal-rule audit** (`/root/data/beyondatoms-carve/experiments/module_causal_audit/stage_b0/`): `B0_TEMPORAL_HYPOTHESIS.md`, `B0_TEMPORAL_CANDIDATES.csv`, `b0_semantic_assessment.json`, `CPU_RULE_REPLAY.csv`, `B0_summary.json`, and `STEP5_INPUT_RECONSTRUCTION.csv` are the audit specification, candidate funnel, saved analyst assessments, rule replay, summary, and reconstructed verifier inputs. The corresponding code entry points include `b0_screen.py` and `b0_finalize.py.b64`.

**B0.5 cross-system source screen** (`/root/data/beyondatoms-carve/experiments/module_causal_audit/stage_b05/`): `CROSS_SYSTEM_COMPARABILITY.md` records the no-go/design-only outcome; `P3_SOURCE_SNAPSHOT.json`, `sources/`, and `b05_sources.tar.xz` preserve source provenance; `VERIFICATION.json` and `FROZEN_PROTOCOL.json` capture the audit checks and protocol. This is source-level screening, not behavioral replication.

**Repair-bypass eligibility** (also in `stage_b05`): `P3_SAFETY_ELIGIBILITY.md`, `P3_ELIGIBILITY_TASKS.csv`, and `P3_COUNTS.json` correspond to the saved-state task inventory and the 0/64 negative, 3/28 positive eligibility counts in the body. This is an eligibility audit, not a safety evaluation or a new inference run.

## Official BeyondAtoms code snapshot

The master ZIP includes the fixed BeyondAtoms source snapshot. The exact paths below were located; the component wrapper, verifier, direction helper, default template, and relevant method/import sections were read directly:

- `beyondatoms/scripts/run_carve.py` — CLI entry point; imports `Executor` from `pipeline`.
- `beyondatoms/templates/golden_carve.yaml` — 3,413-byte default template; configures `ClaimDrivenVerification`.
- `beyondatoms/pipeline.py` — defines `Executor` and imports the implementation modules below.
- `beyondatoms/modules/claim_driven_verification.py` — seven-line compatibility wrapper; imports the actual verifier.
- `beyondatoms/modules/claim_driven/verification.py` — actual verifier; `_match_claim_rel_to_pool` is around line 488.
- `beyondatoms/modules/claim_driven/helpers.py` — defines `detect_direction`.
- `beyondatoms/modules/claim_driven/normalizer.py` — `TextNormalizer` imported by the wrapper.
- `beyondatoms/modules/claim_driven/prompts.py` — relation and repair prompt definitions imported by the verifier.
- `beyondatoms/modules/relation_extraction.py` — relation extraction and connective family/symmetry/inverse utilities.
- `beyondatoms/modules/verification.py` — downstream source/claim verification module.
- `beyondatoms/util/util.py` — shared utility dependency imported by the CLI and pipeline.

The manuscript's `direction` field maps to `ClaimDrivenVerification`'s `detect_direction` helper. The helper compares lexical overlap for left-to-left/right-to-right endpoints against left-to-right/right-to-left endpoints, then returns `same`, `reversed`, or `unknown`; it does not inspect the connective. The audit's source-level explanation is therefore tied to this exact helper in `helpers.py`.

The Stage A materials are outside `SHA256SUMS.txt` and the master archive's indexed construction `behavior_replay/audit.json`; they were verified directly in the live remote working tree instead. The roster hash now matches the manuscript's `94af9557…f21b` prefix. The Stage A evidence and replay assets listed above were read individually; no new GPU inference was run.

All nine package names from the guide were confirmed as entries in the master index. The exact paths shown in the table were matched to index rows. The following SHA-256 values were read from the single `SHA256SUMS.txt` member:

| Package ZIP | SHA-256 |
|---|---|
| `beyondatoms_lr_recovered.zip` | `c6c19ced687bfac9b261dca584e7f6ef8dac37a09820c8333cc65540c258527a` |
| `ba_dataset_first_audit.zip` | `50ecc6a0cadab33b73890159a0bfd740dfa3e49b43bed16c54e4c0f0a2e4be38` |
| `GRACE_AUDIT.zip` | `5543d4dae9434c93a1647970e732d5e34ad4b09a7bfbb05a762e4ce24299e943` |
| `VITAMINC_AUDIT.zip` | `18793908e5b5dd5a45b5220c8376ec0534b47b8f5af70e9ca5267c1fa2ab9213` |
| `VITAMINC_RESIDUAL_AUDIT.zip` | `dbf92c1b493eb49a946bbb286e9cc67003cf4ad8fe46ab14d8d423329c71307b` |
| `ACL2027_RESEARCH_SYNTHESIS.zip` | `772754265b80f7b0b2be390192e75051a574448100f52100ab92cef219471a45` |
| `ACL2027_CONSTRUCTION_AUDIT.zip` | `a3ecc1516aee43fdb81e2ca9274dd7cbb5af0f663ffb45a6df80224df7a27ccb` |
| `ACL2027_INTERACTION_AUDIT.zip` | `babe03633ca9002fdfffea01a91b80c9556ce978acd70b023c14937673899495` |
| `ACL2027_STRATEGY_SELECTION_AUDIT.zip` | `219314a070705d69a5d82ef22600859bd97514c5621adc8c6d4b69c1c96b3f7f` |

`FILE_INDEX.csv` SHA-256: `5b57e3764cc7fc9ab6a1b96809e04405b0c3fa9e73ad1defc3360e2eff84deac`. `REPO_VERSIONS.json` SHA-256: `84c1046738f18b8d1994f5eb0778413f2c1c82ca157d1b370bbdf529318670df`. The archived `main.pdf` SHA-256 `94be43407f2f0e1c15fe6c7568fdf9f7e47bd1200931720bf989e8bb88925ba3` matches local `E:\main.pdf` byte-for-byte.

## Fixed upstream source snapshots

`REPO_VERSIONS.json` records these four upstream code snapshots. These are reference sources, not the user's uploaded research repo:

| Snapshot | Origin | Commit |
|---|---|---|
| BeyondAtoms | `https://github.com/lzy248/beyondatoms.git` | `172dced0a1e98a8544101ecd48754bb7bd8c4659` |
| GRACE-benchmark | `https://github.com/pvhoang14/GRACE-benchmark.git` | `63b6b2d57839bf4a44e9f74572b2f8c5898e3f39` |
| VitaminC | `https://github.com/TalSchuster/VitaminC.git` | `eb532922b88b199df68ed26afeb58dca5501b52f` |
| Benchmark-Profiling | `https://github.com/junkim100/Benchmark-Profiling.git` | `bf2bc43b1fb1f19bf3496f1d9180812e9da78e81` |

The master index confirms the four operation data files that underlie the case IDs in the manuscript:

- `beyondatoms/datasets/beyondatoms/injection_dataset.json`
- `beyondatoms/datasets/beyondatoms/omission_dataset.json`
- `beyondatoms/datasets/beyondatoms/re-anchoring_dataset.json`
- `beyondatoms/datasets/beyondatoms/substitution_dataset.json`

## GitHub repository discovery

The connected GitHub account's repository listing contains `zilongcheng582-cyber/BenchMARK` but no separately named ACL27, BeyondAtoms, CARVE, benchmark-audit, strategy-exclusion, or paper-consolidation research repository. A public repository search result, `zzz-go-up/acl27`, is unrelated: its README identifies it as the official `acl-style-files` template repository. Therefore no user research-code repository has been identified through the connected GitHub account. This does not rule out code stored on the remote cloud instance or an unconnected account.

