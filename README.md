# Awesome Frontier Models (LLMs / VLMs) as Robot Policies [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![entries](https://img.shields.io/badge/entries-140-blue?style=flat-square) ![newest](https://img.shields.io/badge/newest%20entry-2026--11--26-green?style=flat-square) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)

> **Can a general-purpose frontier model (GPT, Claude, Gemini, Qwen…) *be* the robot policy, and if so, what is left for the learned System 1?**
>
> A curated, data-driven list of papers, reports, benchmarks and critiques on frontier LLMs/VLMs controlling robots directly, through code, or on top of learned low-level controllers. Every entry records **what sits below the frontier model**, **how success was judged**, and **how fast and expensive it is**.

<p align="center"><img src="assets/question-in-one-picture.jpg" width="100%" alt="The question in one picture. Left, classic dual-system VLA: System 2, an onboard VLM at about 1 to 10 Hz, passes a latent or subtask to System 1, a learned policy at 50 to 200 Hz, which drives System 0, joint and torque control. Right, frontier model as policy (2026): a cloud frontier model at about 0.05 to 0.5 Hz emits code, end-effector waypoints or skill calls to System 1, which is either a learned VLA or WAM, or nothing, above System 0: IK, tracker and reflexes."></p>

<details><summary>Text version of the figure</summary>

```text
         classic dual-system VLA                      frontier model as policy (2026)       
 +--------------------------------------+      +-------------------------------------------+
 | System 2   VLM, ~1-10 Hz, onboard    |      | Frontier model (cloud), ~0.05-0.5 Hz      |
 |    | latent / subtask                |      |    | code / EEF waypoints / skill calls   |
 | System 1   learned policy, 50-200 Hz | ---> | System 1?  learned VLA/WAM  -or-  nothing |
 |    |                                 |      |    |                                      |
 | System 0   joint / torque control    |      | System 0   IK / tracker / reflexes        |
 +--------------------------------------+      +-------------------------------------------+
```

</details>

**Scope.** In: a general-purpose model that was *not* trained for robotics acts as, or directly steers, the policy. Also in, as context: the dual-system VLAs being challenged, the benchmarks both sides are scored on, and critiques. Out: robot-specific VLAs with no frontier-model angle, and pure task planners with no closed-loop control.

<a id="latest-updates"></a>
## 📰 Latest updates

- **2026-11-26** · ➕ [RoboLiveMem](#robolivemem), [ICLWorld](#iclworld), [WorldLeague](#worldleague), [RUIBench](#ruibench), [RoboUniverse-10K](#robouniverse-10k), [X-Harness](#x-harness), [RoboHarness-Zero](#roboharness-zero), [RegHarness](#regharness), [RoboEvo²](#roboevo2), [Agent on Guard (AoG)](#agent-on-guard), [EvoMisty](#evomisty), [AA-Robotics-Sim](#aa-robotics-sim), [MARGIN](#margin), [RoboClock](#roboclock), [ReWeave](#reweave), [Next-Manip](#next-manip), [Atomic Policy](#atomic-policy), [Boundary-Aware Policy Learning](#boundary-aware-policy), [SkillHarness](#skillharness), [JiL (Judgment-in-the-Loop)](#jil-wam-calibration), [Weight-Space Programming for RFMs](#wsp-robot-repair), [Mibot-RUA](#mibot-rua), [RoboSpoof](#robospoof) · ✏️ [AA-Robotics](#aa-robotics), [RoboDojo](#robodojo) · 🏁 [RoboLiveMem](#robolivemem) (added) · RoboLiveMem runs the same robot-memory tasks with the world paused and running: 8 Claude and GPT models drop from 97% to 50% success. Artificial Analysis launched AA-Robotics-Sim (simulated Unitree G1; GPT-6.2 Astra 71.0) and reported GPT-6.2 Astra at 79 on AA-Robotics. Later run: Roboclock charges model thinking time to the task clock, and GPT-6 Astra falls from 19.0% to 3.0% while the fine-tuned π0.5 keeps 8.3%; Xiaomi Robotics' Mibot-RUA (GPT-6 Astra) now tops the RoboDojo agent track at 79.33% SR, starred for task-specific priors. · <sub>88 candidates screened</sub>
- **2026-11-24** · ➕ [Astra on Codex (Robocurve)](#codex-vs-inspect-robots), [Embo-Harness](#embo-harness), [Contact Harness](#contact-harness), [TRIP (Tripwire)](#trip-tripwire), [ACAP](#acap), [NavRSI](#navrsi), [Embodied-Harness](#embodied-harness), [EvoTER](#evoter), [Real2Worlds2Real](#real2worlds2real), [RoboColiseum](#robocoliseum), [ROSWorld](#rosworld), [γ-Scape](#gamma-scape), [DualManip](#dualmanip) · ✏️ [RoboDojo-RC Tier 1](#robodojo-rc-tier1) · 🏁 [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) (added) · Same model, new harness: GPT-6.2 Astra scores 97% on RoboDojo-RC Tier 1 through Codex vs 65.7% through Inspect Robots; Robocurve is retiring RoboDojo. From the arXiv scan: Embo-Harness, a controlled harness study, puts a directly-acting GPT-6-Astra at 83.3% on RoboLab-120 (second to AMP1's 86.0%). · <sub>61 candidates screened</sub>
- **2026-11-23** · ➕ [Waddle-1](#waddle-1), [RoboDojo-RC Tier 1](#robodojo-rc-tier1), [HuGo](#hugo), [DiMuRe](#dimure), [SPARK](#spark-bt), [Recursia](#recursia), [SCOPE](#scope-program-edits), [UniManip](#unimanip) · Waddle-1, a robot-use agent directing local lower-level policies, tops Robocurve's RoboDojo-RC Tier 1 at 81.4% vs 65.7% for GPT-6.2 Astra (not like-for-like: no call cap). From the arXiv scan: HuGo has gpt-5.4 write closed-loop policy code over a frozen whole-body controller on a Unitree G1 (93.3% zero-shot on hardware for its best push-button policy). · <sub>62 candidates screened</sub>
- **2026-11-22** · ➕ [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2), [Mind2Act World](#mind2act-world), [UniCraft](#unicraft), [SO-101 Bench](#so101-bench), [Real2Gym](#real2gym), [BiCICLe](#bicicle), [InSight](#insight-steerable-vla), [NovaPlan](#novaplan), [STeP](#step-stl), [AquaCap](#aquacap), [ScaleVLA](#scalevla), [CoEnv / CoEx](#coenv-coex) · Anthropic reports Claude Fable 5.2 at 64.9% on RoboDojo Sim in its own runs, more than double GPT-6 Astra (29.8%). · <sub>75 candidates screened</sub>
- **2026-11-21** · ➕ [AgentRoboCritic](#agentrobocritic), [ForceHarness](#forceharness), [RoboTeam](#roboteam), [PhysEvo](#physevo), [Push-T, revisited](#push-t-agentic), [EmbodyAgent](#embodyagent), [Astra as visuo-tactile policy](#astra-visuotactile), [RoC](#reasoning-on-call), [LEXP](#lexp), [ReTrace](#retrace), [LADDER](#ladder), [Gemini 4 Hydrogen](#gemini-4-hydrogen) · ✏️ [Hi Robot](#hi-robot), [Efficient VLA survey](#efficient-vla-survey), [FAEA](#faea) · ForceHarness lets frozen frontier models use force without a wrist sensor, lifting GPT-6 Astra from 2/60 to 54/60 on six real contact tasks. · <sub>43 candidates screened</sub>
- **2026-11-21** · List published with 72 entries; daily automated maintenance switched on.

## Contents

- [📰 Latest updates](#latest-updates)
- [🏁 Milestones](#milestones)
- [📊 Leaderboards: who measured what](#leaderboards)
- [🗂️ At a glance: what sits below the frontier model?](#at-a-glance)
- [🎯 Frontier Model as Direct Policy](#direct) (10)
- [🧑‍💻 Agentic & Code-Writing Policies](#agentic) (21)
- [🎛️ Frontier Model over a Learned System 1 / System 0](#orchestrated) (20)
- [📈 Getting Better Without Weight Updates](#self-improving) (21)
- [⚡ Making It Fast & Cheap](#fast) (8)
- [🧠 The Incumbent: Dual-System VLAs](#dual-system) (17)
- [📊 Benchmarks & Evaluation Reports](#benchmarks) (24)
- [🔍 Analyses, Critiques & Reproducibility](#critiques) (5)
- [🗺️ Surveys, Essays & Perspectives](#perspectives) (9)
- [🏛️ Foundations (pre-2025)](#foundations) (5)
- [Legend](#legend) · [Maintenance](#how-this-list-is-maintained) · [Related lists](#related-lists) · [Contributing](#contributing) · [Citation](#citation)

<a id="milestones"></a>
## 🏁 Milestones

| Date | Work | Why it matters |
|---|---|---|
| 2022-09-16 | [Code as Policies](#code-as-policies) | Introduced code as the interface between an LLM and a robot. |
| 2025-02-20 | [Helix](#helix) | Popularized the 'System 1 / System 2' framing for robot foundation models. |
| 2026-01-28 | [FAEA](#faea) | Early evidence that unmodified coding-agent infrastructure transfers to manipulation. |
| 2026-03-23 | [CaP-X](#cap-x) | The shared benchmark that made agent-vs-VLA comparisons routine. |
| 2026-06-18 | [ENPIRE](#enpire) | An alternative answer: the frontier model builds System 1 instead of replacing it. |
| 2026-07-09 | [Harness VLA](#harness-vla) | The canonical 'keep System 1 for contact' design. |
| 2026-07-09 | [Claude on robotics](#anthropic-robotics) | Direct evidence that a frontier model on top of System 1 can hurt in-distribution and help out-of-distribution. |
| 2026-09-07 | [Robot-Use Agents](#isola-rua) | Named and framed the 'robot-use agent' paradigm. |
| 2026-09-21 | [LLM as Policy on RoboDojo](#robodojo-astra) | First time an LLM topped a public robot-policy leaderboard. |
| 2026-09-24 | [RACaP](#racap) | One of the first concrete distillations of a frontier-agent policy into a small on-robot model. |
| 2026-10-01 | [OpenRUA](#openrua) | Showed that bespoke harness engineering may be unnecessary: native ROS 2 is enough. |
| 2026-10-14 | [Astranomy](#astranomy) | First controlled study comparing the three roles a frontier model can take: direct, agentic, and orchestrator. |
| 2026-10-18 | [Bitter Lesson → Robotics](#bitter-lesson-robotics) | First 'scaling-trend' measurement for frontier models as robot policies. |
| 2026-11-06 | [AMP1](#amp1) | A generalist model beats specialist VLAs and WAMs by a wide margin in the real world as well as in sim. |
| 2026-11-11 | [JustRUA](#justrua) | First controlled ablation showing which harness choices actually produce robot-use-agent gains. |
| 2026-11-13 | [ATLAS](#atlas) | Clearest example of a frontier agent steering a frozen System 0 rather than replacing it. |
| 2026-11-13 | [PEAR / RURL](#pear-rurl) | Robot use as an ordinary foundation-model post-training skill, with no general-capability regression. |
| 2026-11-14 | [RoboDojo leaderboard retest](#openrua-retest) | Benchmark-integrity wake-up call for LLM-as-policy leaderboards. |
| 2026-11-17 | [InteractVLA](#interactvla) | A richer System 2 → System 1 contract: geometric steering instead of language commands. |
| 2026-11-22 | [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) | The top real-world RoboDojo-RC score (97%) came from swapping the harness, not the model: the same GPT-6.2 Astra had scored 65.7% under the benchmark's own harness. |
| 2026-11-23 | [RoboLiveMem](#robolivemem) | Paused-simulator results overstated frontier robot memory: with the world running instead of paused, the same 8 Claude and GPT models fell from 97% to 50% success (Claude Opus 5.5: 100% to 44%). |

<a id="leaderboards"></a>
## 📊 Leaderboards: who measured what

> Numbers are quoted from the cited source. 'measured_by' = whose run produced the number; 'source' = entry id where it is reported. Rows with different settings are NOT directly comparable; read the 'setting' column.

### RoboLab-120 (simulation, zero-shot, DROID-style arm)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1 | frontier agent | frontier: agentic | **86.0%** | 2579 / 3000, 25 eps/task; leaderboard Score 93.5 | RoboLab leaderboard | [AMP1](#amp1) |
| AMP1 | frontier agent (best config) | frontier: agentic | **85.6%** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| Embo-Harness | GPT-6-Astra (xhigh) + VLA refinement | frontier: direct | **83.3%** | full RoboLab-120, zero-shot; Score 89.2; episodes per task not stated | Wu et al. (Embo-Harness) | [Embo-Harness](#embo-harness) |
| Astra — Agentic | GPT-6 Astra (Codex) | frontier: agentic | **74.8%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Orchestrated | GPT-6 Astra + Cosmos3-Nano-Policy | frontier over System 1 | **66.5%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Direct (EEF) | GPT-6 Astra | frontier: direct | **66.3%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| SenseNova-RoboRSI | GPT-6-Astra (per Embo-Harness) | frontier: self-improving | **57.1%** | 685 / 1200, 10 eps/task; leaderboard Score 69.9 | RoboLab leaderboard | [Embo-Harness](#embo-harness) |
| Lakeside | LWM | learned System 1 | **51.0%** | 1531 / 3000, 25 eps/task; leaderboard Score 65.3; best learned policy on the board | RoboLab leaderboard | [RoboLab](#robolab) |
| π0.5 | VLA | learned System 1 | **49.2%** | leaderboard number cited by AMP1 | RoboLab leaderboard (via AMP1) | [AMP1](#amp1) |
| FLUX 3 Action | WAM | learned System 1 | **42.9%** | leaderboard number cited by AMP1 | RoboLab leaderboard (via AMP1) | [AMP1](#amp1) |
| Cosmos3-Nano-Policy | WAM (DROID-finetuned) | learned System 1 | **36.8%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| π0.5 | VLA | learned System 1 | **28.0%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| π0.5 | VLA | learned System 1 | **28.0%** | 336 / 1200, 10 eps/task; leaderboard Score 43.4 | RoboLab leaderboard | [RoboLab](#robolab) |

> π0.5 appears twice: 49.2% (leaderboard, cited by AMP1) vs 28.0% (Astranomy's own run). That 21-point gap on one benchmark is why every row says who measured it.

### RoboDojo (simulation, 42 tasks)

| System | Model | Type | Success rate / robodojo score | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1+ (after practice) | frontier agent + memory | frontier: agentic + memory | **84.1% SR** | few-shot practice, no weight updates | Apple (AMP1) | [AMP1](#amp1) |
| Mibot-RUA* | GPT-6 Astra (per adapter PR) | frontier: self-improving | **79.33% SR · Score 83.94** | official leaderboard agent track, Avg. (w/o Open); starred: task-specific briefs, skills, experience and scene priors beyond the official Detail Description | RoboDojo leaderboard (contributed by Xiaomi Robotics) | [Mibot-RUA](#mibot-rua) |
| Boundary-Aware Policy Learning | Claude Opus 5.5 (high) + boundary-trained π0.5 | frontier over System 1 | **69.2%** | 26 Generalization/Memory/Open-vocabulary tasks only, 10 episodes per task; Harness VLA (VPP2) 40.8% under the same subset | Fang et al. (Boundary-Aware) | [Boundary-Aware Policy Learning](#boundary-aware-policy) |
| Claude Fable 5.2 | Claude Fable 5.2 (Max effort) | frontier: model launch | **64.9% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| X-Harness (model pool, Semi-online rescue) | Claude Opus 5.5 + GPT-6 Astra + Gemini 4 Argon over WALL-OSS-1.0-lite | frontier over System 1 | **62.2%** | Pure-RGB RoboDojo, 42 tasks × 20 layouts (seed 0), five-axis macro mean; code evolved on training layouts; WALL-OSS-1.0-lite official 35.0 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| PhysEvo | Astra (frozen) | frontier: self-improving | **62.00% SR · Score 68.14** | held-out layouts; retained task-specific deployment versions; five-dimension weighting | Tian et al. | [PhysEvo](#physevo) |
| Next-Manip | GPT-6 Astra (medium) + Simate VLA, GPT-6 Luna allocator | frontier over System 1 | **59.58% SR · Score 67.88** | 12 representative tasks only (3 per Generalization/Precision/Long-Horizon/Memory), 20 trials per task; published standalone Astra 14.83% and Simate 38.56% on the same 12 tasks | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| ReWeave | GPT-6.1 Sol (xhigh) controller + frozen π0.5 | frontier: self-improving | **58.25% SR · Score 63.43** | 42 tasks, held-out seeds 1–10, native step limits; harness optimized on seed 0 (≤10 rounds per task); seed harness H0 25.50% | Xu et al. (ReWeave) | [ReWeave](#reweave) |
| UniCraft (frozen skills) | GPT-6 Astra (high effort, Codex harness) | frontier: self-improving code | **54.8% SR (115/210)** | zero-shot transfer of skills learned on other benchmarks; seed and layout 0, 42 tasks × 5 rollouts | Wang et al. (UniCraft) | [UniCraft](#unicraft) |
| AoG | GPT-6 Astra (xhigh) + frozen VPP2 WAM | frontier over System 1 | **50.57% SR · Score 57.26** | 42 tasks × 50 eps; harness frozen after 5 self-improvement rounds; world keeps running while the agent reasons | Cui et al. (AoG) | [Agent on Guard (AoG)](#agent-on-guard) |
| InteractVLA | VL agent + steerable VLA | frontier over System 1 | **48.62%** | with recursive self-improvement | Zhao et al. | [InteractVLA](#interactvla) |
| Claude Opus 5.5 | Claude Opus 5.5 (Max effort) | frontier: model launch | **39.4% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| Gemini 4 Argon | Gemini 4 Argon (High effort) | frontier: model launch | **34.2% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| VPP2 (standalone) | world action model | learned System 1 | **32.26% SR · Score 39.26** | same protocol, AoG's baseline table | Cui et al. (AoG) | [Agent on Guard (AoG)](#agent-on-guard) |
| GPT-6 Astra | GPT-6 Astra (Max effort) | frontier: model launch | **29.8% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| X-Harness (Offline) | Claude Opus 5.5 over π0.5 | frontier over System 1 | **28.1%** | 42 tasks, 2D detections only, 8 evolution rounds, 0 test-time VLM calls; π0.5 official 6.9 / rerun 9.6 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| AMP1 (zero-shot) | frontier agent | frontier: agentic | **26.4% SR** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| LLM as policy | GPT-6 Astra | frontier: direct | **22.48% SR · Score 28.97** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | DeepSeek-Flash | frontier: direct | **1.92% SR** | 10 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | GPT-5.5 | frontier: direct | **0.88% SR** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| JustRUA | GPT-6 Astra | frontier: agentic (lean harness) | **Score 50.3** | no learned policy / self-improvement / task tuning; official L3 harness = 29.7 | Wang et al. | [JustRUA](#justrua) |
| uni-robot-agent | Qwen3.8-Flash-Next (open) | open model: agentic | **Score 31.39** | no privileged inputs | Yuan et al. | [uni-robot-agent](#democratizing-rua) |

> On the official leaderboard's agent track, Xiaomi Robotics' Mibot-RUA (GPT-6 Astra) leads at Avg. (w/o Open) 83.94 / 79.33% (added 2026-11-26), but RoboDojo stars it, like every other agent entry tested before its 2026-11-14 rules, for injecting task-specific information beyond the official Detail Description. The Astra direct-policy entry ranked above all 40 public policies at the time. See Critiques for leaderboard entries that did not survive retesting.

### LIBERO-PRO (perturbed LIBERO)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| ASPIRE | Claude Opus 5.5 | frontier: self-improving code | **99%** | all 80 tasks; with skill learning | NVIDIA GEAR | [ASPIRE](#aspire) |
| AMP1 | frontier agent | frontier: agentic | **95.2%** | zero-shot via CaP-Gym (project page) | Apple (AMP1) | [AMP1](#amp1) |
| OpenRUA | Claude Code + Opus 5 | frontier: agentic | **87.0%** | zero-shot | Chu et al. | [OpenRUA](#openrua) |
| RACaP | GPT-5.6 ReAct | frontier: agentic | **45.0%** | zero-shot | Li et al. | [RACaP](#racap) |
| PEAR / RURL | open 27B, RL in sim | open model: direct | **57.4%** | new task in familiar scene (π0.5: 0.75%) | Tang et al. | [PEAR / RURL](#pear-rurl) |
| UniCraft | GPT-6 Astra (high effort, Codex harness) | frontier: self-improving code | **86.00%** | pooled unseen scenarios and tasks after 3 learning epochs (X-VLA 96.00 in the same table) | Wang et al. (UniCraft) | [UniCraft](#unicraft) |
| ScaleVLA | DeepSeek-V4.1-Flash 552B (frozen) + action DiT | VLA with frontier backbone | **45.1%** | mean of three perturbation settings, 500 episodes per setting; smaller backbones at most 31.3% | Yu et al. (ScaleVLA) | [ScaleVLA](#scalevla) |
| SCOPE | GLM-5.3-Flash | frontier: self-improving code | **80.66%** | 6 Object/Goal/Spatial Pos & Task settings, mean of 3 runs | Shu et al. (SCOPE) | [SCOPE](#scope-program-edits) |
| SPARK | Qwen3.8-27B (4-bit, open) | open model: agentic | **75.1%** | 6 Object/Goal/Spatial Pos & Task settings, 50 eps/task, no practice; benchmark success check read to trigger retries (67.5% without) | Grant et al. (SPARK) | [SPARK](#spark-bt) |
| Recursia (frozen stack) | coding agent (not specified for sim) | frontier: self-improving code | **28.4% Pos · 53.4% Task** | LIBERO-Pro Long only, 10 tasks × 50 seeds per axis, zero-shot transfer | Chen et al. (Recursia) | [Recursia](#recursia) |
| Real2Worlds2Real (136-skill library) | GPT-6 Astra | frontier: self-improving code | **82.2%** | LIBERO-Pro Long only, 20 tasks (10 position, 10 task perturbation) × 50 held-out initial states; 52.9% with no skills; mean over all candidate programs 69.1% | Gu et al. (Real2Worlds2Real) | [Real2Worlds2Real](#real2worlds2real) |
| X-Harness (Offline) | Claude Opus 5.5 over π0.5 | frontier over System 1 | **95.4%** | 40 tasks × 4 shifts pooled; code evolved on training initial states; π0.5 rerun 58.6 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| RegHarness | DeepSeek-Flash (run time); skills refined by Claude Opus 5.5 | frontier: self-improving code | **87.8% (158/180)** | 60 Object/Goal/Spatial tasks × initial states 0–2; state 0 used for development; task check read during execution | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RATs (rerun) | DeepSeek-Flash | frontier: agentic | **39.4% (71/180)** | same 180 paired trials as RegHarness | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RoboEvo² (hybrid) | GPT-6 Astra coding agent + agent-trained π0.5 | frontier: self-improving | **90.5%** | all 8 settings, 100 eps each on unseen initial states, after co-evolution; standalone policy 84.1% | Liu et al. (RoboEvo²) | [RoboEvo²](#roboevo2) |
| MARGIN | Claude Opus 5.5 | frontier: self-improving code | **98.2%** | all 80 tasks, eight-category mean (six-category 99.1%); ASPIRE incumbents plus margin-refined programs; authors' ASPIRE reproduction 98.175% on 4,000 held-out episodes | Duan et al. (MARGIN) | [MARGIN](#margin) |
| ReWeave | GPT-6 Astra (low) controller + frozen π0.5; harness optimized by GPT-6.1 Sol | frontier: self-improving | **98.75%** | 80 tasks, held-out seeds 1–10; harness optimized on seed 0 (≤10 rounds per task); seed harness H0 89.00% | Xu et al. (ReWeave) | [ReWeave](#reweave) |

> Papers use different LIBERO-PRO conditions and subsets. Treat as indicative, not a single leaderboard.

### AA-Robotics (real 6-axis arm, 8 tasks, human-graded)

| System | Model | Type | Score / 100 | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| Codex | GPT-6 Astra | frontier: agentic | **69.4** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Codex | GPT-6.1 Sol | frontier: agentic | **64.6** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Antigravity + Robotics plugin | Gemini 4 Hydrogen | frontier: agentic | **58** | not stated | Google (launch post; not yet on AA's own page) | [Gemini 4 Hydrogen](#gemini-4-hydrogen) |
| Antigravity | Gemini 4 Argon | frontier: agentic | **55.3** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Claude Code | Claude Opus 5.5 | frontier: agentic | **48.8** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Claude Code | Claude Fable 5.1 | frontier: agentic | **46.3** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | GPT-6.2 Astra | frontier: agentic | **79** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | GPT-6.2 Sol | frontier: agentic | **78** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | Claude Fable 5.2 | frontier: agentic | **75** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |

> Independent third party, but no VLA baseline. AA's 2026-11-17 article puts GPT-6.2 Astra (79) on top, ahead of GPT-6.2 Sol (78) and Claude Fable 5.2 (75); those three scores give no harness or effort and are not yet on the AA-Robotics page.

### RoboDojo-RC Tier 1 (real bimanual YAM, 6 tasks × 20 trials, human-graded)

| System | Model | Type | Mean progress score | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| Codex | GPT-6.2 Astra (ultrafast) | frontier: agentic | **97.3%** | Codex harness (self-written tools, several moves per turn), no call cap, 20-min limit · $9.46 (estimate) · 5.6 min | Robocurve | [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) |
| Antigravity | Gemini 4 Neon (high) | frontier: agentic | **89.7%** | coding agent, no call cap, 60-min limit · $5.46 (estimate) · 37.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Claude Code | Claude Fable 5.2 (high, fast) | frontier: agentic | **89.0%** | coding agent, no call cap, 20-min limit · $12.08 (recorded) · 9.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Waddle-1 | undisclosed cloud LLMs + local policies | frontier over System 1 | **81.4%** | full system, no call cap, 10-min limit · $2.46 · 7.4 min | Robocurve | [Waddle-1](#waddle-1) |
| Inspect Robots agent | GPT-6.2 Astra (high, ultrafast) | frontier: direct | **65.7%** | 40 calls · $10.51 · 2.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Dream-1 (Dream Labs) | world action model (hosted API) | learned System 1 | **59.5%** | 3,600 steps · $0.15 · 1.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Fable 5.2 (high, fast) | frontier: direct | **57.5%** | 40 calls · $5.93 · 4.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 4 Carbon (high) | frontier: direct | **54.5%** | 40 calls · $2.16 · 32.1 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 4 Argon (high, priority) | frontier: direct | **48.2%** | 40 calls · $2.34 · 20.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Astra (high, fast) | frontier: direct | **42.5%** | 40 calls · $3.48 · 4.0 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6.1 Sol (high, fast) | frontier: direct | **41.7%** | 40 calls · $2.15 · 4.0 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Opus 5.5 (high, fast) | frontier: direct | **38.2%** | 40 calls · $2.23 · 3.1 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Astra (medium) | frontier: direct | **36.7%** | 40 calls · $1.14 · 4.2 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 3.8 Flash (high) | frontier: direct | **36.2%** | 40 calls · $0.66 · 7.2 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Opus 5.5 (medium) | frontier: direct | **36.0%** | 40 calls · $0.90 · 4.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Sol (high, fast) | frontier: direct | **22.0%** | 40 calls · $0.95 · 3.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| MolmoAct2 | open VLA | learned System 1 | **19.5%** | 3,600 steps · $0.07 (GPU rental) · 0.8 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-5.6 Sol (high, fast) | frontier: direct | **14.9%** | 40 calls · $1.77 · 3.6 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| GR00T N1.7 | open VLA | learned System 1 | **9.5%** | 3,600 steps · $0.05 (GPU rental) · 0.9 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |

> Frontier LLMs, coding agents, a full agent system and learned VLAs/WAMs on one rig, all measured by Robocurve. Setting = call or step cap · cost per attempt · wall-clock per attempt. Graders were not blinded. Caps are not like-for-like: plain LLMs get 40 calls, while coding agents (Codex, Claude Code, Antigravity) and Waddle-1 run with no call cap under 20-, 60- and 10-minute limits. Harness matters: the same GPT-6.2 Astra scores 97.3% through Codex vs 65.7% through Robocurve's 40-call Inspect Robots harness; all three coding agents (89.0–97.3%) top Waddle-1 (81.4%). Robocurve is retiring RoboDojo from future evaluations.

### LIBERO-10 (direct EEF control via tool calls)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| direct EEF | GPT-6 Astra | frontier: direct | **44%** | best effort level | Espinola et al. | [Frontier models on LIBERO-10](#libero10-frontier) |
| direct EEF | Gemini-4 Argon | frontier: direct | **43%** | best effort level | Espinola et al. | [Frontier models on LIBERO-10](#libero10-frontier) |

> 6 models × 3 effort levels, 1,800 episodes total; only the top two are quoted in the abstract.

### Real-world head-to-heads

| System | Model | Type | Successes / trials | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1 | Claude Opus 5.5 (main) | frontier: agentic | **104 / 108** | 12 tasks × 3 robots | Apple (AMP1) | [AMP1](#amp1) |
| FLUX 3 Action | WAM | learned System 1 | **49 / 108** | same tasks | Apple (AMP1) | [AMP1](#amp1) |
| π0.5 | VLA | learned System 1 | **30 / 108** | same tasks | Apple (AMP1) | [AMP1](#amp1) |
| ACE-CaP-0 (frozen programs) | coding agent at dev time only | frontier-developed code | **221 / 240** | 8 tasks; no model in loop at runtime | ACE-CaP Team | [ACE-CaP-0](#ace-cap-0) |
| Reins | GPT-6.1 Sol | frontier: agentic | **88% of episodes** | 5 long-horizon dual-arm tasks | Ye et al. | [Reins](#reins) |
| PEAR / RURL | open 27B, RL in sim | open model: direct | **60% of trials** | real dual-arm; base model 0% | Tang et al. | [PEAR / RURL](#pear-rurl) |
| Inspect Robots agent | GPT-6 Astra | frontier: agentic | **19 / 20 bowl · 2 / 20 puzzle** | bimanual YAM; unblinded graders | Robocurve | [Robocurve Astra eval](#robocurve-astra) |
| GTA-2 | Gemini 3.1 Pro | frontier: agentic | **73.9% avg** | 14 tasks, zero-shot; vs π0.5 + CaP baselines (best baseline 31.4 pp lower) | Seker et al. | [GTA-2](#gta-2) |
| ForceHarness | GPT-6 Astra | frontier: agentic | **54 / 60** | Franka FR3, 6 contact tasks × 10; operator-judged | Sun et al. | [ForceHarness](#forceharness) |
| ForceHarness | GPT-6.1 Sol | frontier: agentic | **47 / 60** | same tasks | Sun et al. | [ForceHarness](#forceharness) |
| Same harness, no force | GPT-6 Astra | frontier: agentic | **2 / 60** | same tasks | Sun et al. | [ForceHarness](#forceharness) |
| LEXP | GPT-6 Astra | frontier: direct + experience | **23 / 36** | bimanual YAM, 12 tasks × 3; human-annotated; vanilla Astra 2 / 36 | Zeng et al. | [LEXP](#lexp) |
| RoC | frontier agent over FastWAM | frontier over System 1 | **73.3% avg** | SO-ARM101, 3 tasks × 10; FastWAM alone 30.0% | Cen et al. | [RoC](#reasoning-on-call) |
| SCOPE (frozen programs) | GLM-5.3-Flash | frontier: self-improving code | **40 / 60** | Quanta X2, 3 tasks × 20 held-out placements; ASPIRE 24 / 60 | Shu et al. (SCOPE) | [SCOPE](#scope-program-edits) |
| HuGo | gpt-5.4 over frozen whole-body policy | frontier over System 1 | **93.3% PBT · 66.7% LBX** | Unitree G1, best policy per task, zero-shot sim-to-real, 15 trials each | Choi et al. (HuGo) | [HuGo](#hugo) |
| Embo-Harness | GPT-6-Astra | frontier: direct | **15/20** | Franka FR3, 4 tasks x 5 zero-shot trials (block stacking 5/5, fruit packing 5/5, dish washing 2/5, flower arranging 3/5); paper's baseline harness 7/20 | Wu et al. (Embo-Harness) | [Embo-Harness](#embo-harness) |
| Contact Harness | GPT-6 Astra (high) | frontier: direct | **136/150 (90.7%)** | Rokae arm, connector insertion, 15 connector types x 10 trials, full insertion to mechanical limit, zero-shot | Shan et al. (Contact Harness) | [Contact Harness](#contact-harness) |
| TRIP + π0.5 | GPT-6.1-sol (medium) + Qwen3.5-9B tripwire VLM | frontier over System 1 | **25/40** | xArm 7, mug + towel hanging, 10 setups each, 'block' and 'move target' human disturbances; turn-based agentic harness 5/40, π0.5 alone 1/40; contact = failure | Chen et al. (TRIP) | [TRIP (Tripwire)](#trip-tripwire) |
| Embodied-Harness | GPT-6 Astra | frontier: direct + self-improving harness | **96.7% avg** | Piper arm, 3 tasks × 10 episodes; π0.5 40.0% on same tasks | Fan et al. (Embodied-Harness) | [Embodied-Harness](#embodied-harness) |
| EvoTER (real-world evolved) | gpt-6.1-sol over frozen π0.5-based policy + Tether | frontier over System 1 | **4/5 · 5/5 · 5/5** | Franka, table setting · drawer storage · two-cup hanging, 5 trials each; direct transfer of sim library 1/5 each | Zhou et al. (EvoTER) | [EvoTER](#evoter) |
| DualManip | GPT-5.6 Terra + shape-adaptive correspondence net | frontier over System 1 | **53.3%** | KUKA iiwa, 3 general tasks under continuous scene change, 15 trials each (CLEA agentic VLM replanning 0.0%, ReKep 28.9%) | Li et al. | [DualManip](#dualmanip) |
| RegHarness | DeepSeek-Flash | frontier: self-improving code | **28 / 45** | Kinova Gen3, 3 tasks × 15; RATs 21 / 45; difference not significant | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RoboEvo² (hybrid) | GPT-6 Astra harness + agent-trained π0.5 | frontier: self-improving | **95.0%** | Unitree G1-D, 4 tasks × 10; standalone policy (120 auto-collected demos) 85.0% vs π0.5 on 200 teleop demos 80.0% | Liu et al. (RoboEvo²) | [RoboEvo²](#roboevo2) |
| Next-Manip | GPT-6 Astra (medium) + fine-tuned π0.5 | frontier over System 1 | **77.50%** | xArm7, 4 tasks × 20 trials, operator labels; average success rate | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| π0.5 (policy only) | VLA | learned System 1 | **28.75%** | same tasks and layouts as Next-Manip | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| GPT-6-Astra agent (100% control) | GPT-6 Astra | frontier: direct | **89.3%** | AgileX Piper, 3 tasks × 50 trials (average success) | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |
| JiL System 1 & 2 | GPT-6 Astra over Fast-WAM (30% agent calls) | frontier over System 1 | **82.0%** | same tasks; 86.0% over LingBot-VA | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |
| Fast-WAM (base) | WAM | learned System 1 | **44.0%** | same tasks; LingBot-VA base 50.7% | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |

### ⏱️ The speed gap (the open problem)

| System | Rate / latency | Cost | Source |
|---|---|---|---|
| Helix System 1 | 200 Hz | onboard | [Helix](#helix) |
| GR00T N1 action module | ≈120 Hz | onboard | [GR00T N1](#gr00t-n1) |
| Fast-in-Slow | 117.7 Hz | onboard | [Fast-in-Slow](#fast-in-slow) |
| DASH System 1 | 20 Hz, independent of 0.8B–8B backbone | onboard | [DASH](#dash) |
| π0.5 | 46.96 ms / call | — | [Astranomy](#astranomy) |
| Cosmos3-Nano-Policy | 713.76 ms / call | — | [Astranomy](#astranomy) |
| Claude models (non-reasoning) | ≈0.2–0.4 Hz | — | [Claude on robotics](#anthropic-robotics) |
| GPT-6 Astra — Direct | 18.56 s / call | $1.96 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra — Orchestrated | 11.50 s / 2.74 s (as listed) | $17.72 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra — Agentic | 13.37 s | $36.40 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra (Robocurve bowl) | ≈2.5 min / run | $0.94 / run | [Robocurve Astra eval](#robocurve-astra) |
| AA-Robotics agents | ≈30 min / task (human ≈20 s) | ≈10× human hourly wage | [AA-Robotics](#aa-robotics) |
| RACaP distilled (Qwen3-VL-8B) | 13.2× faster per decision than GPT-5.6 teacher | — | [RACaP](#racap) |
| ACE-CaP-0 frozen programs | 0.97–2.27 min / task, zero model calls | dev-time only | [ACE-CaP-0](#ace-cap-0) |
| H2E distilled VLA | 3.7× faster than agent + VLA | zero LLM tokens | [H2E](#h2e) |
| GPT-6 Astra direct control | median 31.9 s per decision (π0.5: 0.11 s) | API | [AgentRoboCritic](#agentrobocritic) |

<a id="at-a-glance"></a>
## 🗂️ At a glance: what sits below the frontier model?

| Work | Date | Frontier model | Role | Below it | Eval | Judged by |
|---|---|---|---|---|---|---|
| [Mibot-RUA](#mibot-rua) | 2026-11-26 | GPT-6 Astra | self-improving | none | sim | RoboDojo simulator checker (official leaderboard) |
| [X-Harness](#x-harness) | 2026-11-25 | Claude Opus 5.5, Claude Sonnet 5.5, GPT-6 Astra, Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.5 Flash-Lite | orchestrator | frozen learned policy | sim+real | each benchmark's own success check (sim); real: replay on held-out recordings plus live chunk checks |
| [RegHarness](#regharness) | 2026-11-25 | DeepSeek-Flash (provider alias deepseek-flash), Claude Opus 5.5 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark task check (LIBERO-PRO / MolmoSpaces), also read by the controller during execution; real: operator on site |
| [RoboEvo²](#roboevo2) | 2026-11-25 | GPT-6 Astra, Qwen3.8-27B | self-improving | trained by the agent | sim+real | task-level success check (simulator) for selecting training data and for evaluation; real-world judge not stated |
| [MARGIN](#margin) | 2026-11-24 | Claude Opus 5.5 | self-improving | analytic (IK / waypoints / scripted) | sim | benchmark success check (LIBERO-Pro / LIBERO-90 / Robosuite) on held-out and fresh seeds; acceptance uses development seeds only |
| [Next-Manip](#next-manip) | 2026-11-24 | GPT-6 Astra (medium), GPT-6 Luna (Decisions API, classifier) | orchestrator | frozen learned policy | sim+real | benchmark native success criteria (sim); real: recorded operator labels |
| [Atomic Policy](#atomic-policy) | 2026-11-24 | gpt-6-astra, gemini-3.8-flash, claude-opus-5.5, gemini-2.5-flash, Qwen3-VL-235B | orchestrator | frozen learned policy | sim+real | benchmark success checks (sim); real: task score from completed grasp/place steps (scorer not stated) |
| [Boundary-Aware Policy Learning](#boundary-aware-policy) | 2026-11-24 | Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra, Kimi K3.1 Pro, DeepSeek-V4.1-Flash, GPT-6.1 Terra (data collection) | orchestrator | frozen learned policy | sim+real | benchmark success checks (RoboTwin 2.0, RoboDojo official implementation); real: single qualitative episode |
| [SkillHarness](#skillharness) | 2026-11-24 | DeepSeek V4.1 Flash (non-thinking), Gemma 4 E2B (local monitor) | orchestrator | frozen learned policy | sim+real | route success criteria (clear all obstacles in order, permitted contacts only, stop within tolerance before deadline); scorer not stated |
| [Weight-Space Programming for RFMs](#wsp-robot-repair) | 2026-11-24 | Claude Opus 5.5 | self-improving | trained by the agent | sim | simulator success on new seeded scenes against a pass mark set in advance; failures identified from the simulator's exact measurements |
| [Embo-Harness](#embo-harness) | 2026-11-23 | GPT-6-Astra, GPT-6.1-Sol, GPT-6.1-Terra | direct | analytic (IK / waypoints / scripted) | sim+real | RoboLab-120 SR/Score metrics (sim); real-world judge not stated |
| [ACAP](#acap) | 2026-11-23 | Astra (lead xhigh, members medium; paper does not give the full model name) | agentic / code | analytic (IK / waypoints / scripted) | real | human annotators with task-specific rubrics (physical progress, completion); operators monitor safety |
| [Real2Worlds2Real](#real2worlds2real) | 2026-11-23 | GPT-6 Astra | self-improving | trained by the agent | sim+real | real: not stated; LIBERO-Pro: benchmark checker on 50 held-out initial states |
| [RoboHarness-Zero](#roboharness-zero) | 2026-11-23 | GPT-6 Astra, GPT-6.1 Sol | orchestrator | frozen learned policy | sim | RoboCasa365 environment success predicate |
| [Agent on Guard (AoG)](#agent-on-guard) | 2026-11-23 | GPT-6 Astra, GPT-6.1 Sol | orchestrator | frozen learned policy | sim+real | benchmark success criteria and Score (RoboDojo-Sim, RoboCasa365); real: full task completion without human intervention (judge not named) |
| [EvoMisty](#evomisty) | 2026-11-23 | Claude Opus 5.5, GPT-6 Astra | agentic / code | analytic (IK / waypoints / scripted) | real | agent-written automatic checks plus human checks for anything seen or heard; optimisation metrics measured by the authors on held-out data |
| [ReWeave](#reweave) | 2026-11-23 | GPT-6 Astra (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (high), Claude Sonnet 5.5, DeepSeek V4.1 Flash | self-improving | frozen learned policy | sim+real | official benchmark success labels (sim); real: on-site operator using physical endpoint criteria |
| [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) | 2026-11-23 | GPT-6 Astra | orchestrator | frozen learned policy | sim+real | benchmark success checks (RoboTwin 2.0, LIBERO-Plus); real-world scorer not stated |
| [Contact Harness](#contact-harness) | 2026-11-22 | GPT-6 Astra, Claude Fable 5.1, Claude Fable 5.2 | direct | analytic (IK / waypoints / scripted) | sim+real | task-specific success criteria (real: insertion counts only at the mechanical limit; judge not named); sim: task checks, Write judged by a person (VLA Write runs judged by GPT-6 Astra) |
| [Waddle-1](#waddle-1) | 2026-11-20 | a set of cloud LLMs (not named) | orchestrator | frozen learned policy | real | Robocurve human grader (not blinded) |
| [TRIP (Tripwire)](#trip-tripwire) | 2026-11-20 | GPT-6.1-sol, GPT-6 Astra, Claude Opus 5.5, Qwen3.5-9B (tripwire VLM) | orchestrator | frozen learned policy | sim+real | RoboCasa365 task check + geometric capsule-box human-contact check (sim); task outcome with no contact with the person (real) |
| [NavRSI](#navrsi) | 2026-11-20 | GPT-6-Astra, GPT-6-Luna, GPT-5.6-Sol, GPT-6.1-Terra, GPT-6.1-Sol, GPT-6.2-Sol, GPT-6.2-Astra, Claude Sonnet-5, Claude Opus-5, Claude Opus-5.5, Claude Fable-5, Claude Fable-5.2, Gemini-3.8-Flash, Gemini-4-Hydrogen, Qwen3.7-Flash, Qwen3.8-Flash, Qwen3.8-27B | self-improving | none | sim+real | VLN-CE standard metrics in simulator (NE/OSR/SR/SPL); real-world judging not stated |
| [Embodied-Harness](#embodied-harness) | 2026-11-20 | GPT-6 Astra | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark success checks (RoboTwin 2.0, RoboSPA, RMBench); real-world judging not stated |
| [EvoTER](#evoter) | 2026-11-20 | gpt-6.1-sol | self-improving | frozen learned policy | sim+real | 'externally evaluated task outcome' (RoboCasa365 checker in sim); real-world judge not stated |
| [EmbodyAgent](#embodyagent) | 2026-11-19 | Astra Medium (black-box teacher), Qwen3.5-9B (student) | agentic / code | none | sim | LIBERO BDDL success predicate |
| [RoC](#reasoning-on-call) | 2026-11-19 | GPT-6.1 Sol (xhigh), FastWAM (low-level) | orchestrator | frozen learned policy | sim+real | — |
| [UniCraft](#unicraft) | 2026-11-19 | GPT-6 Astra, Gemini 3.8 Flash, DeepSeek-V4.1-Flash, transfer: GPT-6.1 Sol, GPT-6.1 Terra, MiniMax M3.1 Flash | self-improving | analytic (IK / waypoints / scripted) | sim | native benchmark success checks |
| [InteractVLA](#interactvla) | 2026-11-17 | vision-language agent | orchestrator | frozen learned policy | sim | benchmark checkers |
| [Gemini 4 Hydrogen](#gemini-4-hydrogen) | 2026-11-17 | Gemini 4 Hydrogen (gemini-4-hydrogen) | agentic / code | — | real | — |
| [ForceHarness](#forceharness) | 2026-11-16 | GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | human operator (real); ForceBench public evaluator; HiddenPhys code check on final state |
| [ATLAS](#atlas) | 2026-11-13 | VLM agent (unnamed on page) | orchestrator | frozen learned policy | sim+real | authors |
| [PEAR / RURL](#pear-rurl) | 2026-11-13 | open-weight 27B reasoning model (RL-trained) | direct | analytic (IK / waypoints / scripted) | sim+real | — |
| [Reins](#reins) | 2026-11-12 | GPT-6.1 Sol, GPT-6 Astra, Claude Opus 5.5 | agentic / code | analytic (IK / waypoints / scripted) | real | — |
| [ACE-CaP-0](#ace-cap-0) | 2026-11-12 | coding agent (development time only) | self-improving | analytic (IK / waypoints / scripted) | real | — |
| [H2E](#h2e) | 2026-11-12 | LLM planner (teacher) + 8B VLA (student) | self-improving | trained by the agent | sim | benchmark |
| [AMP1](#amp1) | 2026-11-06 | Claude Opus 5.5 (main real-world), Gemini 4 Argon, 13 models incl. 6 open-weight | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); experimenters (real) |
| [DiMuRe](#dimure) | 2026-11-03 | DeepSeek V4.1 Flash (terminal replanning) | agentic / code | analytic (IK / waypoints / scripted) | sim | LIBERO-Disturb task checks |
| [uni-robot-agent](#democratizing-rua) | 2026-11-01 | Qwen3.8-Flash-Next (open-weight) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | — |
| [LEXP](#lexp) | 2026-10-30 | GPT-6 Astra, Opus 5.5, Sol 5.6 | self-improving | none | real | human annotation against predefined completion criteria, independent of the actor's own declaration |
| [Frontier models on LIBERO-10](#libero10-frontier) | 2026-10-21 | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5, Claude Opus 5.5, Gemini-4 Argon | direct | analytic (IK / waypoints / scripted) | sim | LIBERO checker |
| [Astra as visuo-tactile policy](#astra-visuotactile) | 2026-10-19 | GPT-6 Astra (xhigh) | direct | none | sim | simulator checker (official success criteria; one task's criterion relaxed) |
| [Bitter Lesson → Robotics](#bitter-lesson-robotics) | 2026-10-18 | 9 frontier multimodal LMs at multiple effort / service tiers | direct | analytic (IK / waypoints / scripted) | real | — |
| [Recursia](#recursia) | 2026-10-17 | GPT-6 Astra (physical runs), Claude Opus 5.5 (low effort, verifier calls) | self-improving | analytic (IK / waypoints / scripted) | sim+real | official LIBERO-Pro evaluator (sim); manual assessment (real) |
| [SCOPE](#scope-program-edits) | 2026-10-16 | GLM-5.3-Flash (local) | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); held-out physical placements (real) |
| [Astranomy](#astranomy) | 2026-10-14 | GPT-6 Astra | direct | analytic (IK / waypoints / scripted) | sim | RoboLab task checkers |
| [SEAR](#sear) | 2026-10-13 | 7 frontier LMs | self-improving | trained by the agent | sim+real | benchmark with controls |
| [ReTrace](#retrace) | 2026-10-11 | GPT-6 Astra (high, learner), GPT-6 Astra-low, GPT-6 Sol-xhigh | self-improving | none | real | — |
| [PhysEvo](#physevo) | 2026-10-06 | Astra (frozen; task agent and meta-agent) | self-improving | none | sim+real | RoboDojo native evaluator (sim); authors' rubric (real) |
| [OpenRUA](#openrua) | 2026-10-01 | Claude Code + Claude Opus 5 | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [Real2Gym](#real2gym) | 2026-09-29 | GPT-6 Astra (medium reasoning), baselines: GPT-6 Astra Direct Mode, GPT-5.6 Sol xhigh | self-improving | analytic (IK / waypoints / scripted) | sim+real | predefined completion criteria and human inspection |
| [DualManip](#dualmanip) | 2026-09-25 | GPT-5.6 Terra, Qwen3.5-2B | orchestrator | frozen learned policy | real | not stated (success counts per task) |
| [RAPID](#rapid) | 2026-09-24 | coding agent | agentic / code | analytic (IK / waypoints / scripted) | sim+real | — |
| [HarnessPAI](#harnesspai) | 2026-09-24 | — | orchestrator | frozen learned policy | sim+real | — |
| [RACaP](#racap) | 2026-09-24 | GPT-5.6 (teacher), Qwen3-VL-8B-Instruct (distilled) | self-improving | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [HuGo](#hugo) | 2026-09-24 | gpt-5.4 | orchestrator | frozen learned policy | sim+real | simulator task checks; hardware trials on a Unitree G1 |
| [LLM as Policy on RoboDojo](#robodojo-astra) | 2026-09-21 | GPT-6 Astra, GPT-5.5, DeepSeek-Flash | direct | analytic (IK / waypoints / scripted) | sim | RoboDojo checker |
| [AquaCap](#aquacap) | 2026-09-19 | DeepSeek-V4-Pro (policy), DeepSeek-V4-Flash (coding), Qwen3.7-Flash (VLM) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | task-specific success criterion (lift held, transport within distance) |
| [GPT-Policy](#gpt-policy) | 2026-09-16 | GPT-6 Astra and others | self-improving | analytic (IK / waypoints / scripted) | real | — |
| [AGP](#agent-as-policy) | 2026-09-11 | general-purpose agent | agentic / code | analytic (IK / waypoints / scripted) | real | authors |
| [Show-Harness](#show-harness) | 2026-09-09 | closed frontier VLMs, small open VLMs (fine-tuned) | direct | analytic (IK / waypoints / scripted) | sim+real | — |
| [GTA-2](#gta-2) | 2026-09-09 | Gemini 3.1 Pro (all agents) | agentic / code | analytic (IK / waypoints / scripted) | real | authors |
| [EMERGE-Policy](#emerge-policy) | 2026-08-30 | — | orchestrator | frozen learned policy | sim+real | — |
| [Push-T, revisited](#push-t-agentic) | 2026-08-18 | Claude Code with Fable 5 | agentic / code | analytic (IK / waypoints / scripted) | sim | gym_pusht coverage threshold (simulator checker) |
| [Gemini Robotics 2](#gemini-robotics-2) | 2026-07-30 | Gemini Robotics ER 2, Gemini Robotics 2 (VLA), Gemini Robotics On-Device 2 | orchestrator | jointly trained | real | — |
| [STeP](#step-stl) | 2026-07-20 | GPT-5.4 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | simulator checker (LIBERO / LIBERO-PRO); not stated (real) |
| [Harness VLA](#harness-vla) | 2026-07-09 | LLM coding agent | orchestrator | frozen learned policy | sim+real | benchmark checkers |
| [Claude on robotics](#anthropic-robotics) | 2026-07-09 | Claude Mythos Preview, Opus 4.5–4.7, GPT-5.4, Gemini 3.1 Pro, Kimi K2.6, Qwen 3.6+ | direct | frozen learned policy | sim+real | simulator; informal real Go2 runs |
| [ASPIRE](#aspire) | 2026-06-30 | Claude Opus 5.5 (best), other frontier models | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers |
| [SPARK](#spark-bt) | 2026-06-29 | Qwen3.8-27B (4-bit, local; sim main table), Gemini 3.5 Flash (hardware), gemini-3.1-pro-preview (ablation) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); hardware trials |
| [InSight](#insight-steerable-vla) | 2026-06-23 | Gemini 3 Flash | self-improving | trained by the agent | sim+real | ground-truth state (sim); human against binary criteria (real); VLM filters acquisition rollouts |
| [ENPIRE](#enpire) | 2026-06-18 | frontier coding agents | self-improving | trained by the agent | real | automatic verifier |
| [BiCICLe](#bicicle) | 2026-04-22 | GPT-5-mini (gpt-5-mini-2025-08-07), Qwen 2.5 7B (replication) | direct | analytic (IK / waypoints / scripted) | sim+real | TWIN simulator checker (sim); not stated (real) |
| [CoEnv / CoEx](#coenv-coex) | 2026-04-07 | Claude Code (code agent), GPT-5.6 Sol (planner) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | twin verifier (privileged state) during exploration; task milestones on the real robots |
| [CaP-X](#cap-x) | 2026-03-23 | 12 models incl. Gemini 3 Pro, GPT-5.2, Claude Opus 4.5 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers |
| [NovaPlan](#novaplan) | 2026-02-23 | GPT-5.2 | orchestrator | analytic (IK / waypoints / scripted) | real | human |
| [UniManip](#unimanip) | 2026-02-13 | Qwen3-VL-4B | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); trial success criterion on hardware (object in receptacle, no e-stop or intervention) |
| [FAEA](#faea) | 2026-01-28 | Claude Agent SDK (unmodified) | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [ALRM](#alrm) | 2026-01-27 | 10 LLMs; best closed: Claude-4.1-Opus; best open: Falcon-H1-7B | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [Gemini Robotics 1.5](#gemini-robotics-1-5) | 2025-10-02 | Gemini Robotics-ER 1.5 (orchestrator), Gemini Robotics 1.5 (VLA) | orchestrator | jointly trained | real | — |

<a id="direct"></a>
## 🎯 Frontier Model as Direct Policy

*The general-purpose model itself emits the next action (end-effector pose, joint target, trajectory) at every step. No learned System 1 underneath; the only thing below it is IK / a position controller.*

<details open><summary><b>10 entries</b> + 18 cross-listed</summary>

<a id="embo-harness"></a>
- **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)**
  S-Lab, Nanyang Technological University; ACE Robotics; SenseTime Research · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31201)] [[Project](https://dravenalg.github.io/projects/Embo-Harness/)]  
  Controlled study of frontier-model-as-policy harnesses, varying prompting, planning, action execution and tool use one factor at a time on GPT-6-Astra. 'On RoboLab-120, Embo-Harness achieves an 83.3% success rate' (Score 89.2) 'compared with 57.1% for SenseNova-RoboRSI, the strongest existing baseline'; real robot (Franka FR3): 'succeeds in 15 of 20 zero-shot trials across four real-world manipulation tasks'. Probes suggest the model relies on spatial target estimation more than low-level joint/trajectory generation.  
  <sub>**Model:** GPT-6-Astra, GPT-6.1-Sol, GPT-6.1-Terra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** GPT-6-Astra (xhigh) emits short fixed-length chunks (8) of absolute end-effector targets executed via IK, plus a short multi-action-sequence tool and a VLA-refinement tool (a VLA proposes an action each step, the model refines and executes it); 640x360 two-view images · **Eval:** sim+real · **Judged by:** RoboLab-120 SR/Score metrics (sim); real-world judge not stated · **Trials:** ablations: 20 RoboLab tasks x 3 runs; full RoboLab-120: per-task episode count not stated; real: 4 tasks x 5 zero-shot trials · **Speed/cost:** harness time 10.5-14.8 min per (ablation) configuration on 20 tasks x 3 runs (Table 1); not reported for full RoboLab-120; dropping visual history cuts KV-cache hit rate from over 95% to ~25%, a '7–8× increase in uncached token consumption'</sub>  
  ⚠️ <sub>Authors: 'Our findings depend on the capabilities of current frontier models and may evolve with future advances.' and 'dexterous manipulation, locomotion, and tactile perception require additional low-level and dynamic capabilities'. Real-world failures 'primarily stem from limitations in fine-grained spatial perception'. AMP1 is excluded from the comparison because of its 'external high-accuracy depth estimator'; NVIDIA's Astranomy (74.8% on RoboLab-120) is cited only as a concurrent blog, not compared. The final recipe includes VLA refinement but the paper does not name which VLA. Recipe chosen on a 20-task RoboLab subset that is part of RoboLab-120. SenseNova-RoboRSI (the 'strongest baseline') is by the SenseNova joint team, which shares several authors with this paper.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="contact-harness"></a>
- **[Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation](https://arxiv.org/abs/2611.29377)**
  MARS Lab, Nanyang Technological University · *Paper* · 2026-11-22 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.29377)] [[Project](https://ntumars.github.io/ContactHarness/)]  
  Textual skills plus compliant force-limited execution let a frozen GPT-6 Astra do contact-rich manipulation zero-shot on Rokae and Franka arms. 'With a single prompt skill, Contact Harness achieves a full-insertion rate of 90.7% across 15 connector types' (136/150), and wiping, writing, peeling and pivoting succeed in all 40 trials. In simulation it 'reaches 96.7% success, compared with at most 68.3% for pretrained VLA baselines fine-tuned on task demonstrations' (Fable 5.1/5.2: 98.3%).  
  <sub>**Model:** GPT-6 Astra, Claude Fable 5.1, Claude Fable 5.2 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Guided by textual skills, the VLM requests vision/force/tactile/proprioception observations and issues a single command or short batch (target displacement + duration); an impedance controller with soft/hard contact-force limits executes it, regulating motion between agent decisions · **Eval:** sim+real · **Judged by:** task-specific success criteria (real: insertion counts only at the mechanical limit; judge not named); sim: task checks, Write judged by a person (VLA Write runs judged by GPT-6 Astra) · **Trials:** real: 15 connectors x 10 (150) + 4 other contact tasks x 10 + real-PC 3 x 10 + speed tests 3 x 10; sim: 6 tasks x 10 per method · **Speed/cost:** connector insertion 378 s on average, ~90% spent on model inference and observation; 96 s with fast mode + memory (IEC); 'a real-robot USB-A insertion using about 1.6 million tokens on average'</sub>  
  ⚠️ <sub>Authors: 'The main limitation is long execution time, primarily due to the agent’s reasoning latency.' Supplement: depends on a remote model service whose 'interruptions or stalls put the execution on hold and sometimes cause a failure directly'; small/occluded plugs are hard to see; 'token usage is high' (~1.6M tokens per USB-A insertion); some sockets (e.g. HDMI hidden ring) remain unsolved; uneven connector surfaces need connector-specific prompting; requires wrist force or joint-torque sensing with compliant control. Task prompts are per-task and hand-written; sim benchmark is the authors' own six tasks.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="libero10-frontier"></a>
- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051)**
  — · *Paper* · 2026-10-21 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.30051)]  
  Best is Astra at 44%, then Gemini-4 Argon at 43%. More reasoning effort generally helps, at extra cost. Models do well on placement and struggle with precise spatial arrangement and multi-step interaction.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5, Claude Opus 5.5, Gemini-4 Argon · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Structured tool calls specifying target EEF poses and gripper commands · **Eval:** sim · **Judged by:** LIBERO checker · **Trials:** 18 configurations, 1,800 episodes</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="astra-visuotactile"></a>
- **[GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2610.26846)**
  Tsinghua University / Alibaba (Amap) · *Paper* · 2026-10-19 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2610.26846)] [[Project](https://tactalent.github.io/)] [[Code](https://github.com/ccyydd/TacTalent)] ![stars](https://img.shields.io/github/stars/ccyydd/TacTalent?style=flat-square&label=%E2%98%85)  
  First demonstration that a frontier model reads vision-based tactile images and uses contact cues, few-shot and closed loop. With visuo-tactile input Astra reaches 93.8% (UniVTAC) and 81.8% (OpenViTac), 22.9 and 13.1 points above the strongest reported specialist baselines; vision-only reaches 76.3% and 80.6%.  
  <sub>**Model:** GPT-6 Astra (xhigh) · **Below it:** none · **Interface:** Scene + tactile RGB images and in-context demos in; ordered 7-D EEF-delta + gripper commands out, converted by a benchmark adapter · **Eval:** sim · **Judged by:** simulator checker (official success criteria; one task's criterion relaxed) · **Trials:** 19 tasks (UniVTAC + OpenViTac), 210 sampled scene seeds per setting · **Speed/cost:** median response 15.4 s (vision) / 14.0 s (visuo-tactile); 335.97 million tokens, CNY 7,505.05 for both phases</sub>  
  ⚠️ <sub>Authors: simulation only; cost limits most tasks to ten episodes instead of the full 100-episode evaluation, while baselines are published full-benchmark numbers. Uses task-specific successful demonstrations in context. Tactile input hurts on some tasks.</sub>  

<a id="bitter-lesson-robotics"></a>
- **[The Bitter Lesson Comes to Robotics](https://arxiv.org/abs/2610.25287)**
  — · *Paper* · 2026-10-18 · `📝 preprint` · 🏷️ CoRL 2026 Action Gap workshop  
  [[Paper](https://arxiv.org/abs/2610.25287)] [[Post](https://lesswrong.com/posts/ndS9Xn8Qx5PppHJ3Q/the-ability-of-frontier-models-to-control-robots-is-rapidly)]  
  First broad comparison of frontier LMs on a common real-hardware manipulation suite. Models can directly control real arms but are not yet precise or efficient enough to finish within a practical action budget. Performance doubling time of 53.9 days over July–October 2026.  
  <sub>**Model:** 9 frontier multimodal LMs at multiple effort / service tiers · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Direct end-effector pose commands · **Eval:** real · **Trials:** 6 RoboDojo tasks on physical hardware · **Speed/cost:** best execution rate improved 4.4× (Jul–Oct 2026); lowest execution cost fell 6.2× (Jul–Oct 2026)</sub>  
  ⚠️ <sub>Short window (4 months) and 6 tasks: a weak basis for extrapolation. The LessWrong companion post says each trial is graded by GPT-6 Astra (H) from the three camera feeds, i.e. an LLM judge that is also one of the evaluated models; trials have a 40-action budget, and the authors call the doubling-time CI (36.1–59.5 days) 'relatively wide'.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="astranomy"></a>
- **[Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy](https://research.nvidia.com/labs/srl/projects/astranomy/)**
  NVIDIA Seattle Robotics Lab · *Report* · 2026-10-14 · `💬 post only` · 🏷️ CoRL 2026 LBR  
  [[Project](https://research.nvidia.com/labs/srl/projects/astranomy/)]  
  Zero-shot on RoboLab-120: Agentic 74.8%, Orchestrated 66.5%, Direct (EEF) 66.3%, against Cosmos3-Nano-Policy 36.8% and π0.5 28.0%. Ablations: the action space and the geometry in the prompt matter hugely for Direct (19.3% → 72.7% with gripper/camera geometry) but barely for Agentic.  
  <sub>**Model:** GPT-6 Astra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Three roles: Direct (EEF / joint / B-spline chunks per API call), Agentic (persistent Codex session with tools), Orchestrated (reviews or overrides Cosmos3-Nano-Policy proposals) · **Eval:** sim · **Judged by:** RoboLab task checkers · **Trials:** 120 tasks × 5 seeds · **Speed/cost:** Direct 18.56 s/call; Agentic 13.37 s; π0.5 46.96 ms; Direct $1.96, Orchestrated $17.72, Agentic $36.40 per episode</sub>  
  ⚠️ <sub>Sim only; 5 episodes per task (authors flag this); no arXiv yet. Putting Astra on top of a weak System 1 (Orchestrated) did not beat Astra alone.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="robodojo-astra"></a>
- **[An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](https://arxiv.org/abs/2609.24170)**
  — · *Paper* · 2026-09-21 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.24170)] [[Post](https://robodojo-benchmark.com/report/gpt-6-astra-eval)]  
  Frames the question in System 1 / System 2 terms. Astra: 22.48% success, Score 28.97, ranking above all 40 public policies; GPT-5.5 0.88% and DeepSeek-Flash 1.92%. Capability is sharply polarized: good at semantic generalization, poor at precision, dynamic control, and bimanual coordination. One-shot demos give no aggregate gain.  
  <sub>**Model:** GPT-6 Astra, GPT-5.5, DeepSeek-Flash · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** LLM as policy with shared post-processing · **Eval:** sim · **Judged by:** RoboDojo checker · **Trials:** 42 tasks × 50 episodes (Astra, GPT-5.5); 10 (DeepSeek)</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="show-harness"></a>
- **[Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)**
  Show Lab, NUS · *Paper* · 2026-09-09 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.10522)] [[Project](https://showlab.github.io/Show-Harness/)] [[Code](https://github.com/showlab/Show-Harness)] ![stars](https://img.shields.io/github/stars/showlab/Show-Harness?style=flat-square&label=%E2%98%85)  
  Argues the right interface unlocks VLM capability without extra capacity: zero-shot control with closed frontier VLMs, and small open VLMs adapted with a few GPU-hours. GUMI extends the same action space to GUI-based demonstration collection.  
  <sub>**Model:** closed frontier VLMs, small open VLMs (fine-tuned) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Discrete semantic action units that embodiment-specific interpreters ground deterministically; the VLM stays responsible for fine-grained physical decisions · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="anthropic-robotics"></a>
- **[How Claude performs on robotics tasks](https://www.anthropic.com/research/claude-plays-robotics)**
  Anthropic (Frontier Red Team) · *Report* · 2026-07-09 · `💬 post only`  
  [[Post](https://www.anthropic.com/research/claude-plays-robotics)]  
  'Interface matters as much as the model.' Direct joint control mostly fails: best LIBERO full-task success is 5.5%, and no model stands a collapsed G1 up. Supervising pretrained controllers works far better. However, every model did worse supervising MolmoAct than MolmoAct alone on its own tasks, while beating it on novel tasks.  
  <sub>**Model:** Claude Mythos Preview, Opus 4.5–4.7, GPT-5.4, Gemini 3.1 Pro, Kimi K2.6, Qwen 3.6+ · **Below it:** frozen learned policy · **Interface:** Four interfaces compared: direct torques/commands, programmatic controller, model-designed RL, high-level steering of a gait or VLA (MolmoAct) · **Eval:** sim+real · **Judged by:** simulator; informal real Go2 runs · **Trials:** 35 per cell (200 for LIBERO-40) · **Speed/cost:** ≈0.2–0.4 Hz non-reasoning calls vs ≈83 Hz needed for quadruped control</sub>  
  ⚠️ <sub>Simulator paused between calls (best-case capability); prompts not tuned per model.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="bicicle"></a>
- **[Bimanual Robot Manipulation via Multi-Agent In-Context Learning](https://arxiv.org/abs/2604.20348)**
  Sapienza University of Rome · TU Darmstadt · *Paper* · 2026-04-22 · `📄 peer-reviewed` · 🏷️ CoRL 2026  
  [[Paper](https://arxiv.org/abs/2604.20348)] [[Project](https://alesspalma.github.io/bicicle)]  
  Off-the-shelf text LLMs control two arms through in-context learning with no fine-tuning. 'Evaluated on 13 tasks from the TWIN benchmark, BiCICLe achieves 70.5% average success rate, outperforming the best training-free baseline by 6.1 percentage points'; real bimanual Franka: 60.0% Lift Box, 40.0% Open Pot, 60.0% Cleanup.  
  <sub>**Model:** GPT-5-mini (gpt-5-mini-2025-08-07), Qwen 2.5 7B (replication) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Text-serialized object poses and few-shot demos in the prompt; a leader LLM agent predicts one arm's discretized end-effector keyframes, a follower agent predicts the other arm conditioned on the leader; executed keyframe by keyframe with re-observation · **Eval:** sim+real · **Judged by:** TWIN simulator checker (sim); not stated (real) · **Trials:** 13 TWIN tasks × 3 seeds × 100 episodes; 3 real tasks × 10 trials · **Speed/cost:** median 125.3s LLM wall time per episode (Lift Ball, GPT-5-mini)</sub>  
  ⚠️ <sub>Simulation uses ground-truth segmentation masks; the discrete keypose interface caps precision; bounded by context window and API latency.</sub>  

**Cross-listed here:**

- ↪ **[ICLWorld](#iclworld)**: ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Atomic Policy](#atomic-policy)**: Atomic Policy: Composing Atomic Manipulation Skills with Agentic Reasoning <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[WorldLeague](#worldleague)**: WorldLeague: Benchmarking Physical Agency <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[NavRSI](#navrsi)**: NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Embodied-Harness](#embodied-harness)**: Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboColiseum](#robocoliseum)**: RoboColiseum: Co-evolution of Simulation, Evaluation, and Models <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[ROSWorld](#rosworld)**: ROSWORLD: When Digital Task Competence Meets Physical Execution <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[AgentRoboCritic](#agentrobocritic)**: AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[Gemini 4 Hydrogen](#gemini-4-hydrogen)**: Gemini 4 Hydrogen: a faster model for general purpose robotics <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[ForceHarness](#forceharness)**: ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[PEAR / RURL](#pear-rurl)**: Training Reasoning Models in Simulation to Natively Use Real Robots <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2)**: Introducing Claude Fable 5.2 and Claude Mythos 5.2 <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[LEXP](#lexp)**: Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[ReTrace](#retrace)**: ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[PhysEvo](#physevo)**: PhysEvo: Astra Can Act, Let It <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboDojo-RC Tier 1](#robodojo-rc-tier1)**: RoboDojo-RC Tier 1: real-world leaderboard of frontier models, agents and VLAs (Robocurve) <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Robocurve Astra eval](#robocurve-astra)**: GPT-6 Astra vs Claude Fable 5 / 5.1 on bimanual YAM arms <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[RoboSpoof](#robospoof)**: You Can't See Everything: Perceptual Attacks on Embodied AI <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>

</details>

<a id="agentic"></a>
## 🧑‍💻 Agentic & Code-Writing Policies

*The model acts through a harness: it writes and runs code against sensing/perception/motion APIs, observes the outcome, and repairs. Learned System 1 is absent; motion is analytic (IK, waypoints, ROS).*

<details open><summary><b>21 entries</b> + 25 cross-listed</summary>

<a id="regharness"></a>
- **[RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills](https://arxiv.org/abs/2611.33739)**
  Xiamen University Malaysia; Beijing Zhongke Huiling Robot Technology; Institute of Automation, CAS · *Paper* · 2026-11-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.33739)]  
  With 'a single low-cost model across all run-time roles, RegHarness achieves an 87.8% success rate (158/180) on paired LIBERO-PRO trials, compared with 39.4% for RATs, and a 72.0% success rate on MolmoSpaces trials'. A 2×2 ablation 'shows that its skill refinement alone increases RATs' successful trials from 71 to 135, whereas run-time governance alone achieves 105 and RATs' native stepwise reset-and-replay mode achieves only 46'. Real Kinova Gen3: 28 of 45 vs 21 for RATs, 'a difference not significant at this sample size'.  
  <sub>**Model:** DeepSeek-Flash (provider alias deepseek-flash), Claude Opus 5.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Two-level harness around the RATs Code-as-Policy agent team: within a trial, each proposed step is tested from a reset scene with committed steps replayed, and a fixed-rule controller commits it only if the verifier and a task-long LLM auditor approve (all run-time roles on deepseek-flash); between runs, Claude Opus 5.5 in Claude Code turns logged failures into default-off revisions of skills, primitives and rules that the authors choose to enable · **Eval:** sim+real · **Judged by:** benchmark task check (LIBERO-PRO / MolmoSpaces), also read by the controller during execution; real: operator on site · **Trials:** LIBERO-PRO: 180 paired trials (60 tasks × 3 initial states), 300 over 5 states; MolmoSpaces: 200; real Kinova Gen3: 3 tasks × 15 trials · **Speed/cost:** 'takes 66 minutes on average against 50' per LIBERO-PRO trial (vs RATs); 'an estimated CNY 2.16 (US$0.32)' per trial in run-time model calls</sub>  
  ⚠️ <sub>Authors: 'Reset-and-replay is currently limited to simulation'; both levels were debugged on initial state 0, so 'the observed gain from skill refinement may be an upper estimate'; refinement 'is gated by the authors and lacks the automatic acceptance test'; the coding agent 'reads success checks, full logs and, on MolmoSpaces during design, the benchmark's ground truth'; all systems read the task check during execution. Perception uses simulator camera extrinsics and noise-free depth. All MolmoSpaces trials are in-sample. LIBERO-PRO here is the 60 Object/Goal/Spatial tasks only.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="acap"></a>
- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)**
  S-Lab, Nanyang Technological University; University of Oxford; ACE Robotics · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31205)] [[Project](https://projects.zxhezexin.com/acap)]  
  Splits a robot across asynchronous coding agents per control group, coordinated by a lead hyper-agent, on Galaxea R1 Pro and AgileX PiPER robots. 'Across 72 real-world rollouts covering 25 task/platform settings, ACAP reduces task-balanced time cost by 28.2% compared with a single-agent Direct Policy'; on repeated trials it lowers mean 30-min-capped cost on all six tasks (−29.4%), and on Collaborative tasks 'ACAP completes ten of ten runs, compared with eight for Direct and three for Fixed.'  
  <sub>**Model:** Astra (lead xhigh, members medium; paper does not give the full model name) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** One robot run as a team of persistent coding agents: each member owns a control group (arm+gripper, torso+chassis) and runs its own observe–reason–code–execute loop issuing end-effector/joint targets; a lead 'hyper-agent' assigns work, sets event-based waits, and can take over groups for coupled actions under exclusive control ownership · **Eval:** real · **Judged by:** human annotators with task-specific rubrics (physical progress, completion); operators monitor safety · **Trials:** task-coverage: 72 rollouts over 25 task/platform settings; repeated-trial: 90 rollouts (6 tasks x 5 trials x 3 policies) · **Speed/cost:** task-balanced mean 13.67 min (ACAP) vs 19.04 min (Direct) per task over 25 settings</sub>  
  ⚠️ <sub>Authors: 'The current framework does not include a dedicated motion-level collision-checking layer.' Evaluation is about time cost vs. the authors' own single-agent and fixed-delegation baselines; no learned-policy (VLA) comparison. Progress is human-annotated; operators monitor safety. The model is named only as 'Astra'. Releases a real-world rollout dataset.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="evomisty"></a>
- **[EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot](https://arxiv.org/abs/2611.31341)**
  University at Buffalo · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31341)] [[Project](https://wangxiaoshawn.github.io/projects/evomisty/index.html)]  
  Coding agents build a social robot's capabilities from its documentation and verify them on hardware. 'The two agents construct 109 and 107 verified atomic capabilities, respectively. Both complete all 28 AutoMisty benchmark tasks and seven additional tasks beyond AutoMisty's capabilities.' 'Optimization improves all seven evaluated metrics across five tasks', e.g. 'dialogue response latency decreases by 52% and 71%'.  
  <sub>**Model:** Claude Opus 5.5, GPT-6 Astra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Plugin for Claude Code (Opus 5.5) and Codex (GPT-6 Astra): the agent reads Misty II documentation, writes a control program, verifies each capability on the physical robot, writes task programs from the capability and skill libraries, and optimizes them on user-specified metrics · **Eval:** real · **Judged by:** agent-written automatic checks plus human checks for anything seen or heard; optimisation metrics measured by the authors on held-out data · **Trials:** 28 AutoMisty tasks + 7 new tasks on one physical Misty II; attempts per task not stated</sub>  
  ⚠️ <sub>Authors: 'the applicability of EvoMisty to other robot platforms remains to be validated'; 'Capability verification and task completion checks still rely on human observation and feedback'. Tasks are mostly speech, display and base motion, with no manipulation. The AutoMisty baseline was rerun by the authors. Code 'coming soon'.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="gemini-4-hydrogen"></a>
- **[Gemini 4 Hydrogen: a faster model for general purpose robotics](https://developers.googleblog.com/gemini-hydrogen-for-robotics/)**
  Google DeepMind · *Blog* · 2026-11-17 · `💬 post only`  
  [[Code](https://github.com/google-deepmind/robotics-antigravity-plugin)] [[Post](https://developers.googleblog.com/gemini-hydrogen-for-robotics/)] ![stars](https://img.shields.io/github/stars/google-deepmind/robotics-antigravity-plugin?style=flat-square&label=%E2%98%85)  
  A general-purpose fast Gemini 4 model that replaces Gemini Robotics ER 2 for embodied reasoning and ships a Robotics plugin for Google Antigravity (I2RT YAM, SO-ARM101, FR3 Duo, YAM Pro). On Artificial Analysis Robotics 0.1, 'Hydrogen scores 58', similar to Argon at a lower cost per token; a new arm is 'calibrated and ready for tasks in about 10 minutes'.  
  <sub>**Model:** Gemini 4 Hydrogen (gemini-4-hydrogen) · **Interface:** Plain-language goal + camera view; the model plans, writes and runs control code (Google Antigravity Robotics plugin, MuJoCo, Gemini API); can also drive arms directly from images. Low-level controller not described. · **Eval:** real · **Speed/cost:** 'faster' (qualitative only); 'lower cost per token' than Argon (no figure)</sub>  
  ⚠️ <sub>Vendor blog; no success rates, trial counts or latency figures. The AA score is Google-reported. Antigravity requires a paid Google AI Pro or Ultra subscription.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="forceharness"></a>
- **[ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](https://arxiv.org/abs/2611.21099)**
  Show Lab, NUS · *Paper* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.21099)] [[Project](https://showlab.github.io/ForceHarness)]  
  Gives API-only frozen models force sensing without demos or finetuning, on a Franka FR3 with no wrist F/T sensor. Real robot: GPT-6 Astra goes from 2/60 without force to 54/60, GPT-6.1 Sol reaches 47/60. ForceBench: Astra and Sol 87.5% (Fable 75.0%) vs 35.31% for the best trained policy; HiddenPhys: Astra 87/140 → 135/140, matching the hand-written expert at 136/140.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** One tool call per turn picking a self-terminating force primitive (move_until_contact, push, insert, screw, …) run by admittance control on the stock impedance controller; a physics translation layer returns mass, friction, contact height with uncertainty · **Eval:** sim+real · **Judged by:** human operator (real); ForceBench public evaluator; HiddenPhys code check on final state · **Trials:** real: 6 tasks × 10 episodes per condition; ForceBench 8 tasks × 10; HiddenPhys 7 tasks × 20 seeds · **Speed/cost:** 'Model queries add seconds between primitives'; cuts Astra's cost per episode by 45% (HiddenPhys)</sub>  
  ⚠️ <sub>Authors: 'Model queries add seconds between primitives and preclude reactive coordination, a fixed menu limits new motion laws, and our ablations run only in simulation.' Primitive menu, physics estimators and per-task instructions are hand-written; ForceBench tools were tuned on 8 of 10 seeds; HiddenPhys gives object poses as noisy text (privileged state). Code to be released on publication.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="reins"></a>
- **[Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot](https://arxiv.org/abs/2611.16632)**
  — · *Paper* · 2026-11-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.16632)]  
  Targets the 'blind while the arm moves and while it thinks' problem. GPT-6.1 Sol succeeds in 88% of real episodes with no task-specific code; without the harness it fails every shell game and takes 8× as long. Three frontier models perform alike but differ in tracking a scene that changes while the actor thinks. Also builds a sim-ready twin of the scene for continual learning.  
  <sub>**Model:** GPT-6.1 Sol, GPT-6 Astra, Claude Opus 5.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** 3D perception tools plus atomic actions that report contact and grip; actions chained in one call with per-step conditions; a second 'narrator' instance watches the cameras continuously · **Eval:** real · **Trials:** 5 real long-horizon tasks (dual-arm)</sub>  
  ⚠️ <sub>Code to be released on publication.</sub>  

<a id="amp1"></a>
- **[On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)**
  Apple · *Paper* · 2026-11-06 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2611.09892)] [[Project](https://apple-aiml-research.github.io/ml-amp/)] [[Code](https://github.com/apple-aiml-research/ml-amp)] ![stars](https://img.shields.io/github/stars/apple-aiml-research/ml-amp?style=flat-square&label=%E2%98%85)  
  Reference harness that runs unchanged on single-arm, bimanual, and mobile manipulation with no grasp/push/place skills. Zero-shot 85.6% on RoboLab-120 (vs 49.2% leading VLA, 42.9% leading WAM); 104/108 real-world successes. AMP1+ adds a persistent notes/code memory that lifts RoboDojo from 26.4% to 84.1% after practice.  
  <sub>**Model:** Claude Opus 5.5 (main real-world), Gemini 4 Argon, 13 models incl. 6 open-weight · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Python in a persistent interpreter; SDK for sensing, a segmented scene model, and timed TCP waypoints (harness does IK + limit checks) · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); experimenters (real) · **Trials:** 108 real trials over 12 tasks × 3 robots · **Speed/cost:** avg 34.8 model calls per RoboLab episode</sub>  
  ⚠️ <sub>Authors: 'AMPs are not yet practical, as the robot spends much of each episode waiting for the model.' Quasi-static scenes only; no mid-trajectory revision. Proposed fix is to distill AMP experience into fast local controllers.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="dimure"></a>
- **[DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226)**
  Beijing Institute of Technology · *Paper* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.04226)]  
  A recovery layer for program-based robot-use agents, plus LIBERO-Disturb, a benchmark of mid-execution disturbances for both program agents and VLAs. On 801 disturbed Encore cases, Local DiMuRe reaches 77.65% complete-task success vs 58.68% for the original program under the same physical-step allowance; Full DiMuRe reaches 81.90% with terminal MLLM replanning, an additional step allowance and early handoff.  
  <sub>**Model:** DeepSeek V4.1 Flash (terminal replanning) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Diagnosis selects reuse of the robot-use agent's task program, predefined recovery skills (including bounded GraspVLA grasping), or, after the program exits, MLLM-generated corrective code from images and execution feedback; each recovery is locally verified · **Eval:** sim · **Judged by:** LIBERO-Disturb task checks · **Trials:** 801 scheduled disturbed Encore cases (30 fixed Encore programs × 3 reset seeds)</sub>  
  ⚠️ <sub>Authors: current evidence is limited to simulation; Full's extra allowance and early handoff mean its gain over Local cannot be attributed to MLLM replanning alone; Encore and VLA evaluations use different disturbance versions and protocols, so they are not directly comparable.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="openrua"></a>
- **[OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies](https://arxiv.org/abs/2610.02459)**
  — · *Paper* · 2026-10-01 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.02459)]  
  An off-the-shelf coding agent, with no bespoke primitives, reaches 99.0% on CaP-Bench and 87.0% on LIBERO-PRO. Emergent behaviour: the agent writes its own metric-perception code in 96.8% of episodes and its own motion-control clients in 95.9%.  
  <sub>**Model:** Claude Code + Claude Opus 5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Zero-abstraction: terminal access to native ROS 2 plus its docs only; perception becomes file I/O, manipulation becomes coding · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Secondary critiques note the simulator is paused while the agent thinks, episodes take ~100 turns, and baselines are copied from original papers. The OpenRUA team also published retests of RoboDojo leaderboard entries (see Critiques).</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="rapid"></a>
- **[RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249)**
  — · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.30249)] [[Project](https://yuyaoliu.me/projects/rapid)]  
  From one visual human demonstration, infers a testable spec, primitives, and an environment, then generates, verifies, and refines robot programs. Covers 8 contact-rich nonprehensile tasks (sim and a real Franka) plus LIBERO-Pro.  
  <sub>**Model:** coding agent · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Object-centric relational programs whose primitives are trajectory-optimization programs · **Eval:** sim+real</sub>  

<a id="aquacap"></a>
- **[AquaCap: A Training-Free Underwater Embodied Agent with Code-as-Policy](https://arxiv.org/abs/2609.23133)**
  Sun Yat-sen University · Dalian University of Technology · *Paper* · 2026-09-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.23133)]  
  Closed-loop code-as-policy for an underwater ROV with no training, using only onboard camera images and robot state. 'AquaCap achieves an overall SR of 66.43%, outperforming U0 by 19.29 percentage points' in simulation; real ROV grasping and transport are demonstrated.  
  <sub>**Model:** DeepSeek-V4-Pro (policy), DeepSeek-V4-Flash (coding), Qwen3.7-Flash (VLM) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Policy agent plans condition-aware stages; coding agent writes control programs over high-level ROV / arm APIs; failure-aware memory drives replanning and code revision · **Eval:** sim+real · **Judged by:** task-specific success criterion (lift held, transport within distance) · **Trials:** Sim: 20 Stonefish tasks; real: 10 grasping + 10 transport trials</sub>  
  ⚠️ <sub>Authors: 'Execution efficiency, however, remains a key bottleneck'; controls the ROV only through high-level APIs, not thruster dynamics; real-world success is much lower than in sim.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="agent-as-policy"></a>
- **[Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541)**
  — · *Paper* · 2026-09-11 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.12541)] [[Project](https://agent-as-policy-2026.github.io/)] [[Code](https://github.com/agent-as-policy-2026/agent-as-policy)] [[Data](https://huggingface.co/datasets/Agent-as-Policy/agent-as-policy)] ![stars](https://img.shields.io/github/stars/agent-as-policy-2026/agent-as-policy?style=flat-square&label=%E2%98%85)  
  A general agent drives a physical robot through the whole task, including dynamic and deformable ones (dice flipping, targeted throwing, bimanual towel folding, assembly from human video). At least 80% success on 7 of 8 task configurations. Reusing saved procedures shortens execution over repeated trials.  
  <sub>**Model:** general-purpose agent · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Agent reads visual evidence, writes programs, issues motion commands, revises on physical outcomes · **Eval:** real · **Judged by:** authors</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="gta-2"></a>
- **[GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808)**
  — · *Paper* · 2026-09-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.09808)] [[Project](https://gta2-project.github.io/)]  
  Zero-shot 73.9% average on 14 real-robot tasks, 31.4 pp above the strongest baseline (π0.5 and two Code-as-Policies variants); targeted human feedback raises it to 90.7%.  
  <sub>**Model:** Gemini 3.1 Pro (all agents) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Four VLM agents build task-axis skills: keypoints/axes, controller compositions, scene parameters · **Eval:** real · **Judged by:** authors · **Trials:** 14 real tasks</sub>  

<a id="push-t-agentic"></a>
- **[Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227)**
  UC Berkeley · *Paper* · 2026-08-18 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2608.18227)]  
  A demonstration-free code-as-policy for Push-T, built by Claude Code with Fable 5. The state controller reaches 100.0% success (vision controller 97.2%) vs 62.5% for the LeRobot Diffusion Policy checkpoint over 200 seeds, at 120.1 vs 223.7 mean steps. A self-generated curriculum extends it to Push-A–Z (99.4% overall) and to simulated Franka (vision 89.8%) and UR5e (vision 98.5%).  
  <sub>**Model:** Claude Code with Fable 5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Coding agent writes, runs and revises a state-machine / MPC controller and vision pipeline offline in simulation; the generated code is the runtime policy (no LLM in the 10 Hz loop) · **Eval:** sim · **Judged by:** gym_pusht coverage threshold (simulator checker) · **Trials:** Push-T: 200 seeds; Push-A–Z: 25 episodes per letter (650) · **Speed/cost:** about 9.5 million output tokens, approximately $1,500–$2,000 API cost, approximately 221 hours in auto mode</sub>  
  ⚠️ <sub>Authors: the agent may exploit simulator-specific state or contact behaviour unavailable on real robots; 'Claude is computationally expensive and sensitive to the prompt.' State controllers use privileged ground-truth state. Simulation only; development took ~221 h under human interaction.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="step-stl"></a>
- **[STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models](https://arxiv.org/abs/2607.18580)**
  University of Maryland, College Park · *Paper* · 2026-07-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.18580)]  
  'On LIBERO-PRO, STeP retains 54%-89% success across five of six evaluated perturbation settings', against 12%–26% for CaP-Agent0 (copied from CaP-X); on LIBERO-Constrained it reaches 80% safe success vs 14% for SmolVLA.  
  <sub>**Model:** GPT-5.4 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** GPT-5.4 (System 2) formalizes the instruction as a Signal Temporal Logic spec over a fixed predicate / skill library; RRT + MPC (System 1) enforces it; an online STL monitor recalls System 2 with a history log to replan · **Eval:** sim+real · **Judged by:** simulator checker (LIBERO / LIBERO-PRO); not stated (real) · **Trials:** LIBERO-Constrained: 49 task–constraint instances; replanning: 20 trials</sub>  
  ⚠️ <sub>Authors: 'To resolve objects and their locations in LIBERO we read privileged simulator state'; a fixed predicate library limits generalization; LIBERO-PRO baselines are not re-run.</sub>  

<a id="spark-bt"></a>
- **[Sequential Planning via Anchored Robotic Keypoints](https://arxiv.org/abs/2606.30613)**
  Case Western Reserve University · *Paper* · 2026-06-29 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2606.30613)] [[Project](https://cwru-aism.github.io/spark-page/)]  
  With one open-weight 27B planner at 4-bit, no practice on the evaluated tasks and no ground-truth poses, SPARK reaches 75.1% mean success on six LIBERO-PRO position and task settings and 69.7% on the held-out language and object settings. On hardware it completes 150 of 220 trials (68.2%) across 11 task-platform settings on three robots; on CaP-Bench it scores 65.1% vs 68.3% for CaP-Agent0's three-model ensemble.  
  <sub>**Model:** Qwen3.8-27B (4-bit, local; sim main table), Gemini 3.5 Flash (hardware), gemini-3.1-pro-preview (ablation) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** The LM writes a YAML behavior tree over a fixed skill library from SAM3 masks, 3D keypoints and the instruction; each step is re-anchored to the current scene and verified, with local recovery before asking for a new plan · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); hardware trials · **Trials:** 50 episodes per task on LIBERO-PRO; 20 trials per task-platform on hardware (220 total)</sub>  
  ⚠️ <sub>In the headline run the benchmark's success check is read after each attempt to decide retries; with the robot's own checks only, it scores 67.5%. LIBERO tasks were used to develop the controllers and skills. Lowest on the goal suite (66.7%). Hardware cells with 20 trials vary by about ±20 points.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="coenv-coex"></a>
- **[CoEnv: Code-Driven Exploration in Real-to-Sim Digital Twins for Multi-Arm Manipulation](https://arxiv.org/abs/2604.05484)**
  USTC · CUHK-Shenzhen · Fudan · SJTU · Shanghai AI Lab et al. · *Paper* · 2026-04-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2604.05484)] [[Project](https://faceong.github.io/CoEnv/)]  
  On five real multi-arm tasks with up to three heterogeneous robots, 'CoEx reaches 70% average success, against 50% for the same system without the code agent'; a π0.5 policy fine-tuned on agent-generated rollouts is also reported.  
  <sub>**Model:** Claude Code (code agent), GPT-5.6 Sol (planner) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Claude Code writes a complete multi-arm program, runs it in a real-to-sim digital twin and refines it against privileged-state checks, checkpoint predicates and rendered views; verified joint trajectories are replayed on hardware after collision checks · **Eval:** sim+real · **Judged by:** twin verifier (privileged state) during exploration; task milestones on the real robots · **Trials:** 10 per agent per task, 5 real tasks</sub>  
  ⚠️ <sub>Authors: 'Real-world execution is open-loop replay, so residual pose offsets remain a main source of failure'; programs query privileged simulator state; rigid objects, fixed bases, static scenes; evaluation is modest in scale.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="cap-x"></a>
- **[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435)**
  UC Berkeley · NVIDIA · Stanford · CMU · *Paper* · 2026-03-23 · `💻 code / results` · 🏷️ ICML 2026 (per catalogs)  
  [[Paper](https://arxiv.org/abs/2603.22435)] [[Project](https://capgym.github.io/)] [[Code](https://github.com/capgym/cap-x)] ![stars](https://img.shields.io/github/stars/capgym/cap-x?style=flat-square&label=%E2%98%85)  
  CaP-Gym environment + CaP-Bench. Finding: performance rises with human-crafted abstractions and falls as they are removed, but scaling agentic test-time compute (multi-turn, execution feedback, visual differencing, skill synthesis) closes much of the gap. Introduces training-free CaP-Agent0 and CaP-RL (RL with verifiable rewards, sim→real).  
  <sub>**Model:** 12 models incl. Gemini 3 Pro, GPT-5.2, Claude Opus 4.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Programs that compose perception and control primitives at varying abstraction levels (CaP-Gym) · **Eval:** sim+real · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Authors propose a hybrid in which agents handle logic and recovery while VLAs handle fine motor control.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="unimanip"></a>
- **[UniManip: Open-World Robotic Manipulation via Agentic Operational Graphs](https://arxiv.org/abs/2602.13086)**
  Nanyang Technological University · *Paper* · 2026-02-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2602.13086)] [[Project](https://henryhcliu.github.io/unimanip)]  
  A small general VLM orchestrates an explicit operational graph with closed-loop verification and recovery. It reaches 0.83 task success in cluttered scenes (RoboEXP 0.39, no-graph variant 0.40) and 0.94 on the VLA benchmark vs 0.71 for the strongest baseline. On LIBERO-Pro it scores 0.77/0.85 on Object Pos/Task, against π0.5's 0.17/0.01.  
  <sub>**Model:** Qwen3-VL-4B · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** A VLM builds and updates an Agentic Operational Graph over tool calls; a scene graph supplies affordances and a safety-aware planner synthesises collision-free trajectories; the VLM verifies outcomes and repairs locally or replans · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); trial success criterion on hardware (object in receptacle, no e-stop or intervention) · **Trials:** 10 trials per task and method on the Galaxea A1 (80 in clutter); 15–20 per task in cross-embodiment tests</sub>  
  ⚠️ <sub>Authors: failures are dominated by grasping (0.16 of all trials, from single-view depth noise) and embodiment kinematics. π0.5 beats it on LIBERO-Pro Goal Pos (0.38 vs 0.33).</sub>  

<a id="faea"></a>
- **[Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334)**
  — · *Paper* · 2026-01-28 · `📄 peer-reviewed` · 🏷️ IROS 2026  
  [[Paper](https://arxiv.org/abs/2601.20334)]  
  Frontier Agent as Embodied Agent: 84.9% LIBERO, 85.7% ManiSkill3, 96% MetaWorld, approaching VLAs trained on fewer than 100 demos per task, with zero demonstrations. One round of human feedback raises LIBERO to 88.2%.  
  <sub>**Model:** Claude Agent SDK (unmodified) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Software-engineering agent loop applied unchanged to manipulation · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Uses privileged environment state. Authors scope the claim to 'tasks dominated by deliberative, task-level planning'.</sub>  

<a id="alrm"></a>
- **[ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510)**
  TII · *Paper* · 2026-01-27 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2601.19510)] [[Project](https://tiiuae.github.io/ALRM/)]  
  Agentic framework plus a 56-task simulation benchmark with linguistically varied instructions. Claude-4.1-Opus is the top closed model under both modes.  
  <sub>**Model:** 10 LLMs; best closed: Claude-4.1-Opus; best open: Falcon-H1-7B · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** ReAct loop in two modes: Code-as-Policy (writes control code) and Tool-as-Policy (iterative tool calls) · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

**Cross-listed here:**

- ↪ **[Mibot-RUA](#mibot-rua)**: Mibot-RUA (Mibot_RSI): RoboDojo agent-track entry <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[MARGIN](#margin)**: MARGIN: A Risk-Aware Agent for Robot Program Refinement <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Real2Worlds2Real](#real2worlds2real)**: Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RUIBench](#ruibench)**: RUIBench: What Makes a Good Robot-Use Interface? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[RoboUniverse-10K](#robouniverse-10k)**: RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Astra on Codex (Robocurve)](#codex-vs-inspect-robots)**: Why is Astra better on Codex for robotics? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Contact Harness](#contact-harness)**: Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[Waddle-1](#waddle-1)**: Waddle-1: a robot-use agent that directs local lower-level policies <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[γ-Scape](#gamma-scape)**: $γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[EmbodyAgent](#embodyagent)**: EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[UniCraft](#unicraft)**: Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboTeam](#roboteam)**: RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[JustRUA](#justrua)**: JustRUA: A Controlled Study of GPT-6 Robot-Use Agents <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[uni-robot-agent](#democratizing-rua)**: Democratizing Robot-Use Agents: A Unified Harness with Open Models <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[SO-101 Bench](#so101-bench)**: SO-101 Bench: Accessible Spatial Manipulation <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Recursia](#recursia)**: Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[SCOPE](#scope-program-edits)**: SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Astranomy](#astranomy)**: Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[LADDER](#ladder)**: LADDER: A Long-Horizon Robot Manipulation Benchmark <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Real2Gym](#real2gym)**: Real2Gym: Building Gyms from Videos, Bringing Skills to Robots <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[HuGo](#hugo)**: HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[GPT-Policy](#gpt-policy)**: In-Context Robot Learning with VLM Agents <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[EMERGE-Policy](#emerge-policy)**: EMERGE-Policy: A Robot Mind Emerges Beyond a Single Policy <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[ASPIRE](#aspire)**: ASPIRE: Agentic /Skills Discovery for Robotics <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[NovaPlan](#novaplan)**: NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>

</details>

<a id="orchestrated"></a>
## 🎛️ Frontier Model over a Learned System 1 / System 0

*The general model supervises, steers, or edits the output of a learned low-level controller (a VLA, a world-action model, or a whole-body tracker). This is where the 'is System 1 still needed?' question is decided.*

<details open><summary><b>20 entries</b> + 12 cross-listed</summary>

<a id="x-harness"></a>
- **[Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents](https://arxiv.org/abs/2611.34778)**
  Google; Emory University; USC; University of Florida; University of Chicago; UC Santa Barbara; Ohio State University; UAB · *Paper* · 2026-11-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.34778)] [[Code](https://github.com/google-research/x-as-policies)] ![stars](https://img.shields.io/github/stars/google-research/x-as-policies?style=flat-square&label=%E2%98%85)  
  Seven controlled, one-factor-at-a-time studies of policy-harness design 'across eight simulation benchmarks, six VLMs, and 15 VLA/WAM checkpoints'. Frontier VLMs predict 3D gripper poses poorly, so the composed X-Harness recipe has the VLM write closed-loop code around a frozen VLA/WAM, 'lifting base policies up to +42.8 points across memory, reasoning, and domain shifts' (VLABench π0.5 25.5 → 68.3 with Opus 5.5); LIBERO-PRO pooled 58.6 → 95.4 (Opus 5.5 over π0.5).  
  <sub>**Model:** Claude Opus 5.5, Claude Sonnet 5.5, GPT-6 Astra, Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.5 Flash-Lite · **Below it:** frozen learned policy · **Interface:** VLM writes closed-loop Python policy code on training episodes, evolved over up to 8 gated rounds and then frozen; code calls perception tools, motion primitives and a frozen VLA/WAM via language sub-goals; at test time the VLM is called never (Offline), on failure triggers (Semi-online) or per sub-goal (Full-online) · **Eval:** sim+real · **Judged by:** each benchmark's own success check (sim); real: replay on held-out recordings plus live chunk checks · **Trials:** over 470,000 rollouts across eight simulation benchmarks; at least 20 test episodes per cell · **Speed/cost:** Offline code runs at native control rate (16.7–25 Hz) vs 0.5–10 Hz for in-loop VLM designs; '$95.6K in logged VLM API list-price spend' for the study; evolution needs '350k–440k tokens, and 1.1–1.5 GPU-hours per task'</sub>  
  ⚠️ <sub>No dedicated limitations section. Training-time failure reports can include simulator diagnostics (ground-truth poses, oracle masks), never at test time and not on RoboDojo. Code is evolved per task on 5–40 training episodes, so this is not zero-shot. Baselines were rerun by the authors and sometimes differ from official leaderboards. Real-robot validation is mostly replay of held-out recordings, with no physical success table.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques), [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="next-manip"></a>
- **[Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation](https://arxiv.org/abs/2611.32533)**
  HKUST (Guangzhou); Tencent; NTU; HKUST · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32533)]  
  Decouples when to call the frontier agent from the agent itself. On 12 RoboDojo tasks 'Next-Manip achieves 59.58% success and a Score of 67.88', above published standalone Astra (14.83%) and Simate (38.56%) and leaderboard leader Q0-Preview (53.50%); RMBench 94.4% vs 67.9% for EventVLA and 64.4% for local Astra. Real world: 'raising the average success rate from 28.75% to 77.50%' over policy-only π0.5.  
  <sub>**Model:** GPT-6 Astra (medium), GPT-6 Luna (Decisions API, classifier) · **Below it:** frozen learned policy · **Interface:** A lightweight GPT-6 Luna classifier (Agent Invocation Controller) allocates each action chunk to either GPT-6 Astra acting directly or a learned policy (Simate VLA on RoboDojo, EventVLA on RMBench, fine-tuned π0.5 on the real arm); both execute the first ten actions per chunk; compact task references from demonstrations guide both · **Eval:** sim+real · **Judged by:** benchmark native success criteria (sim); real: recorded operator labels · **Trials:** RoboDojo: 12 representative tasks × 20 trials; RMBench: 9 tasks × 20 trials; real xArm7: 4 tasks × 20 trials · **Speed/cost:** 28.80 Astra calls per episode on RoboDojo, '62.5% fewer than the 76.72' with Astra alone; Luna classifier input cost below 1% of Astra's</sub>  
  ⚠️ <sub>Authors: 'Next-Manip adopts frozen models as executors, and its performance is therefore constrained by their capabilities.' RoboDojo uses a 12-task subset chosen by Astra leaderboard strata; locally reproduced baselines and ablations use 5 trials per task while Next-Manip uses 20; leaderboard baselines were not re-run. Real-world policy is fine-tuned per task on 50 demonstrations.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="atomic-policy"></a>
- **[Atomic Policy: Composing Atomic Manipulation Skills with Agentic Reasoning](https://arxiv.org/abs/2611.32813)**
  Purdue University · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32813)] [[Project](https://aaronzkd.github.io/atomic-policy/)]  
  Composes learned atomic skills under VLM planning and checking. Replanning matters on dependent phases: on simulated Tabletop success 'falls from 64.0% to 17.8% without replanning'. On real OOD Crossword 'both end-to-end baselines obtain zero task score, while Atomic + MolmoBot and Atomic + π0.5 reach 72.5 and 60.0'. In a controlled comparison with zero-shot gpt-6-astra emitting end-effector displacements, 'Direct control reaches 98.0% success on Push 5 Blocks, compared with 86.3% for Atomic Policy, whereas Atomic Policy reaches 60.0% success ... on Tabletop, compared with 52.0%'.  
  <sub>**Model:** gpt-6-astra, gemini-3.8-flash, claude-opus-5.5, gemini-2.5-flash, Qwen3-VL-235B · **Below it:** frozen learned policy · **Interface:** A VLM estimates symbolic state and goal, a PDDL solver builds a skill plan, and an agentic harness steers each learned phase skill (diffusion policy, MolmoBot or π0.5) with language and MolmoPoint visual points; a separate VLM checker verifies each phase and triggers replanning · **Eval:** sim+real · **Judged by:** benchmark success checks (sim); real: task score from completed grasp/place steps (scorer not stated) · **Trials:** sim: 50 seeded episodes (direct-control comparison), 200 rollouts per configuration on MolmoSpaces; real Franka Panda: 3 tasks × 20 trials (10 ID, 10 OOD) per method · **Speed/cost:** real: checker queried every 128 control steps; authors note VLM and pointing inference 'adds latency'</sub>  
  ⚠️ <sub>Authors: 'The phase set, PDDL domain, and checker prompts are specified manually for each task family, and demonstrations require phase and point annotations. Execution depends on the accuracy of the VLM and pointing model, whose inference also adds latency.' Real-robot results are 10 trials per task and condition. Planner/checker VLM differs by task (gemini-3.8-flash on Push 5 Blocks and MolmoSpaces, gpt-6-astra on Tabletop and real robot).</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="boundary-aware-policy"></a>
- **[Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation](https://arxiv.org/abs/2611.32238)**
  University of Electronic Science and Technology of China; Shanghai AI Laboratory; Tongji University; Shanghai Innovation Institute · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32238)] [[Project](https://kaipengfang.github.io/bapl-agentic-manip)]  
  Makes the policy's handoff boundary wide and explicit so the agent hands over only contact segments. Versus Harness VLA, the system is '26.4 percentage points higher on RoboTwin 2.0 under the official randomized configuration (C2R)' (98.4% vs 72.0%) and '28.4 percentage points higher on average on RoboDojo' (69.2% vs 40.8%). Swapping the agent with the policy fixed: 'the four other language models reach 67.7% to 85.0% without retraining the policy, compared with 98.7% for Claude Opus 5.5'.  
  <sub>**Model:** Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra, Kimi K3.1 Pro, DeepSeek-V4.1-Flash, GPT-6.1 Terra (data collection) · **Below it:** frozen learned policy · **Interface:** Claude Opus 5.5 (high effort) acts only through registered tools (images, SAM 3 segmentation, pixel-to-world, motion-planner end-effector moves, gripper) and hands over to a π0.5 policy trained only on contact segments from diverse start poses, following a short handoff protocol that describes the policy's boundary; the policy is later retrained on curated successful system rollouts · **Eval:** sim+real · **Judged by:** benchmark success checks (RoboTwin 2.0, RoboDojo official implementation); real: single qualitative episode · **Trials:** RoboTwin 2.0: 50 tasks × 10 episodes per setting; RoboDojo: 26 Gen/Mem/Open tasks × 10 episodes · **Speed/cost:** agent-direct trials take a median 18.2 min (RoboTwin 2.0) and 32.8 min (RoboDojo), with LLM inference 93.0% and 86.5% of total time; self-improvement cuts time per episode by 37.5% on average; $1.53 per episode for Claude Opus 5.5 (high) on the 30-task subset; self-improvement cuts API cost by 41.3%; collecting the self-improvement data cost about $1,013</sub>  
  ⚠️ <sub>Authors: data curation discards suboptimal rollout segments, and 'the handoff protocol describes the boundary only by rules'. Real-robot deployment is a single qualitative episode ('we leave a quantitative evaluation on real robots to future work'). RoboDojo results exclude the long-horizon and precision subsets; RoboDojo needed a hand-written scripted expert to collect contact-segment data. Tasks are explored before evaluation and notes merged into a frozen memory.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="skillharness"></a>
- **[SkillHarness: Execution-Aware Coordination with Plug-and-Play Skills for Long-Horizon Traversal](https://arxiv.org/abs/2611.32186)**
  Fudan University; Lenovo Group Limited; Nanyang Technological University; Shanghai Jiao Tong University · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32186)]  
  An LLM-guided harness picks and admits learned locomotion skills for multi-terrain traversal. In Isaac Sim the harness check gives '90% (45/50), compared with 24% (12/50) without Harness'; on the physical robot with refined rules 'the robot completed all ten trials at every N', versus 5/10, 1/10, 0/10 and 0/10 without the harness. SkillHarness completed all ten trials in each of eight route conditions where MGDP and REAL fell to 20–60% at K=5.  
  <sub>**Model:** DeepSeek V4.1 Flash (non-thinking), Gemma 4 E2B (local monitor) · **Below it:** frozen learned policy · **Interface:** Event-triggered harness: a local Gemma 4 E2B monitor triggers asynchronous DeepSeek V4.1 Flash planning, which proposes navigation and locomotion-skill switches; proposals pass geometric feasibility and execution-phase admission checks before a library of perceptive-RL locomotion skills executes them · **Eval:** sim+real · **Judged by:** route success criteria (clear all obstacles in order, permitted contacts only, stop within tolerance before deadline); scorer not stated · **Trials:** physical robot: 8 route conditions × 10 trials; ablation N=2–5 terrain types × 10 trials per setting; Isaac Sim ablation: 50 trials per setting · **Speed/cost:** Gemma monitor median 1.289 s per classification; estimated US$0.00234 per planning request (10,000 input / 100 output tokens) vs US$0.021 for GPT-6.1 Sol</sub>  
  ⚠️ <sub>No dedicated limitations section. The MGDP and REAL baselines run in MX simulation while SkillHarness runs on the physical robot, and the authors note the structured and unstructured routes were not matched in difficulty. Harness rules were refined from the five failed simulation trials before the physical tests. Robot platform is not named in the text.</sub>  

<a id="roboharness-zero"></a>
- **[Body and Soul: Decoupling Robotic Brain and Policy with RoboHarness-Zero](https://arxiv.org/abs/2611.30550)**
  Polyadic Research Group; CUHK-Shenzhen; HKUST; NVIDIA; Xiaohongshu · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.30550)] [[Project](https://odessey159.github.io/roboharness-zero/)] [[Code](https://github.com/polyadic-research/roboharness0)] ![stars](https://img.shields.io/github/stars/polyadic-research/roboharness0?style=flat-square&label=%E2%98%85)  
  A task-agnostic VLM supervision harness around frozen VLAs. 'On 200 RoboCasa365 scenes, RoboHarness-Zero with GPT-6 Astra raises the success rate of frozen Xiaomi-Robotics-1 from 57.5% to 70.5% and preserves 90.4% of its standalone successes (104/115) while rescuing 37 of 85 failures' (GPT-6.1 Sol: 63.0%; a no-VLM reissue control: 56.5%). On a 50-scene subset the same rules 'add 8 to 10 percentage points to each of four other frozen policies'.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol · **Below it:** frozen learned policy · **Interface:** Frozen VLA controls by default; at checkpoints the VLM sees camera views and robot state, judges progress, rewrites the instruction on stalls and, as a fallback, runs short generated code over generic motion primitives before handing back; fixed supervision rules with a thin per-policy adapter and auto-profiled skill configuration · **Eval:** sim · **Judged by:** RoboCasa365 environment success predicate · **Trials:** Xiaomi-Robotics-1: 200 paired scenes; four other policies: 50-scene shared subset · **Speed/cost:** average 71 VLM requests per episode; 'waiting for responses consumes 87% of episode wall time'</sub>  
  ⚠️ <sub>Authors: 'We developed the harness with Xiaomi, so the higher rescue rate on Xiaomi could reflect either Xiaomi's capabilities or design choices informed by that policy'; transfer evidence is '50 simulated scenes per new policy and one competing harness'; 'Recovery remains a bottleneck'. Development episodes cover 47 of 50 tasks and 10 eval scenes match development scenes. Simulation only.</sub>  

<a id="agent-on-guard"></a>
- **[Agent on Guard: Self-Improving Runtime Intervention for Robust Robotic Manipulation](https://arxiv.org/abs/2611.30101)**
  USTC; LeapWing AI; MBZUAI; Institute of Automation, CAS · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.30101)]  
  A programming agent decides when to intervene on a frozen robot policy and when to hand back. 'On RoboDojo-Sim, AoG achieves a success rate of 50.57% and a task score of 57.26, exceeding the strongest evaluated baseline by 11.22 percentage points and 10.68 points' (frozen VPP2 alone 32.26%; GPT-6 Astra agent alone 22.48%), and 'reduces end-to-end episode latency by 80.4% and online token consumption by 85.1% relative to the GPT-6 Astra agent'. RoboCasa365: Xiaomi-Robotics-1 57.4% → 69.6%.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol · **Below it:** frozen learned policy · **Interface:** GPT-6 Astra (xhigh) watches a frozen policy (VPP2 WAM on RoboDojo-Sim, Xiaomi-Robotics-1 on RoboCasa365, fine-tuned π0.5 on the real robot) on a shared physical clock, takes over with Python recovery programs and hands back; over 5 self-improvement rounds it revises intervention rules, recovery programs and handover conditions; both models stay frozen · **Eval:** sim+real · **Judged by:** benchmark success criteria and Score (RoboDojo-Sim, RoboCasa365); real: full task completion without human intervention (judge not named) · **Trials:** RoboDojo-Sim: 42 tasks × 50 episodes; RoboCasa365: 50 tasks × 50; real AgileX PiPER: 3 tasks × 20 trials · **Speed/cost:** 20.2 min end-to-end per episode vs 103.0 for the GPT-6 Astra agent (dev set); 1.204M online tokens per episode vs 8.096M for the GPT-6 Astra agent, excluding self-improvement cost</sub>  
  ⚠️ <sub>No limitations section; labelled a LeapWing AI technical report. 'The initial harness underperforms the standalone policy' before self-improvement. The harness is evolved per benchmark and policy–agent pair; whether self-improvement episodes are disjoint from test scenes is not stated. The GPT-6 Astra baseline matches Zhang et al.'s published run exactly (likely copied, not stated). The world keeps running while the agent reasons; no privileged simulator state.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="jil-wam-calibration"></a>
- **[Calibrating World Action Models: From Adaptive System 2 Takeover to Self-Evolution](https://arxiv.org/abs/2611.30188)**
  Central South University; ACE Robotics; University of Sydney; UC San Diego · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.30188)]  
  Calls the frontier agent only when the WAM's calibrated confidence drops. At a 30% agent-call budget on RoboTwin 2.0 JiL lifts Fast-WAM from 39.8% to 74.5% ('cutting Fast-WAM failures on RoboTwin 2.0 by 57.6% ... vs. 16.3% for random calls'), against 88.4% for the GPT-6 Astra agent in full control; on Kairos it reaches 89.8%, 'surpassing even the 100% pure GPT-6-Astra agent'. Distilled standalone WAMs gain '+13.1% to +24.7% with zero agent calls'. Real world: JiL System 1 & 2 82.0% and 86.0% vs base WAM 44.0% and 50.7% and full Astra 89.3%.  
  <sub>**Model:** GPT-6 Astra · **Below it:** frozen learned policy · **Interface:** A judgment token on a frozen world action model (Fast-WAM, LingBot-VA, Kairos) predicts chunk success; below threshold, a GPT-6-Astra-based RGB-D agent takes over and executes modular actions (grasp, re-grasp, place, sweep) from the live state, handing back when confidence recovers; successful takeovers are distilled into a repair WAM that runs with zero agent calls · **Eval:** sim+real · **Judged by:** benchmark success checks (RoboTwin 2.0, LIBERO-Plus); real-world scorer not stated · **Trials:** RoboTwin 2.0 full (50 tasks, Clean and Random) and LIBERO-Plus full; real AgileX Piper: 3 tasks × 50 trials per method · **Speed/cost:** judgment token 1.6 ms per chunk; mean episode time 31.4 s (JiL System 1 & 2) vs 94.6 s for full GPT-6 Astra and 16.8 s for the base WAM (RoboTwin 2.0, Fast-WAM)</sub>  
  ⚠️ <sub>No dedicated limitations section. All two-system baselines share the same base WAM, agent and 30% chunk-level budget, but the GPT-6 Astra agent's tool stack is described only briefly (RGB-D 3D pose estimation plus modular manipulation actions). Real-world evaluation uses three tasks on one arm; who scored success is not stated.</sub>  
  <sub>↪ also in: [The Incumbent: Dual-System VLAs](#dual-system), [Making It Fast & Cheap](#fast)</sub>

<a id="waddle-1"></a>
- **[Waddle-1: a robot-use agent that directs local lower-level policies](https://waddlelabs.ai/research/introducing-waddle)**
  Waddle Labs · *Project* · 2026-11-20 · `💬 post only`  
  [[Project](https://waddlelabs.ai/research/introducing-waddle)] [[Data](https://robocurve.org/)]  
  Announced on X as Waddle Labs' first robot-use agent, controlling bimanual robots zero-shot on unseen tasks. Robocurve measures it at 81.4% on RoboDojo-RC Tier 1, the top score, ahead of GPT-6.2 Astra (65.7%) and the Dream-1 world action model (59.5%). A System 2 over System 1 design: 'agents that combine the capability of reasoning models and the efficiency of reactive policies'.  
  <sub>**Model:** a set of cloud LLMs (not named) · **Below it:** frozen learned policy · **Interface:** Cloud LLMs decompose the goal, write control code and call lower-level policies that run locally on the robot; skills go into a shared library · **Eval:** real · **Judged by:** Robocurve human grader (not blinded) · **Trials:** 120 attempts (RoboDojo-RC Tier 1) · **Speed/cost:** 7.4 min per attempt (Robocurve); $2.46 per attempt at a planned $20/hr</sub>  
  ⚠️ <sub>Robocurve: a 'full system' with 'one chat per task, a 10-minute limit and no call cap', while single LLMs get 40 model calls, so not like-for-like. LLMs and the lower-level policy type are not disclosed; no paper. Preview API by request.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="trip-tripwire"></a>
- **[Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance](https://arxiv.org/abs/2611.27182)**
  University of Massachusetts Amherst · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27182)]  
  Event-driven harness where the agent writes its own interrupt programs while a pretrained policy runs. On RoboHD (168 RoboCasa365 scenes with a reactive human avatar), with Xiaomi-Robotics-1 'TRIP halves the rate of human contact with the strongest policy, raising safety from 61.3% to 81.3%, without sacrificing task success (38.7% vs. 31.0%)' versus a turn-based harness with the same agent. Real robot (xArm 7, π0.5): 'TRIP succeeds in 25 of 40 trials across two disturbance conditions … compared with 5 of 40 for the turn-based harness and 1 of 40 for the policy alone.'  
  <sub>**Model:** GPT-6.1-sol, GPT-6 Astra, Claude Opus 5.5, Qwen3.5-9B (tripwire VLM) · **Below it:** frozen learned policy · **Interface:** The agent calls a frozen VLA/WAM (or direct base/arm/gripper commands) and attaches a 'tripwire': a sandboxed, stateful Python monitor run every control step that can query a compact VLM (Qwen3.5-9B) plus depth and timers, and halts the call and wakes the agent with a reason when it fires · **Eval:** sim+real · **Judged by:** RoboCasa365 task check + geometric capsule-box human-contact check (sim); task outcome with no contact with the person (real) · **Trials:** sim: 168 RoboHD scenes x 1 episode per method/policy (+ same scenes without person); real: 2 tasks x 10 setups x 3 conditions per method · **Speed/cost:** real robot: tripwire check 0.24 s avg vs agent turn 4.3 s avg; sim pauses physics, ~12 min wall-clock per 1.5 min robot time; '$0.2–0.3 in API calls' per TRIP episode with GPT-6.1-sol; spend cap $0.40/episode</sub>  
  ⚠️ <sub>Authors: 'The person is simulated: an avatar that plays motion-capture clips under a scripted controller, with no collision body.' 'The physics pauses while the agent and the tripwire’s VLM compute, so the robot’s time excludes their latency.' 'Due to high (10×) API costs, only Xiaomi-Robotics is tested with the current state-of-the-art agentic model, GPT-6 Astra.' Real-robot disturber is one of the authors; base policies are single-task π0.5 trained on 100 demos each. Claude Opus 5.5 (40-scene supplement) touched the person in 17/40 vs 9/40 for GPT-6.1-sol.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="reasoning-on-call"></a>
- **[Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2611.26341)**
  Wuhan University / Zhongguancun Academy / Samsung · *Paper* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26341)]  
  Event-triggered frontier-agent intervention over a world-action-model policy. On RMBench, 99.6% average success vs 75.6% for GPT-as-Policy and 71.9% for Direct Control, using 65.3% fewer tokens than GPT-as-Policy; 98.1% vs 83.0% for MemoryWAM, the strongest policy-only baseline. Real robot: 73.3% vs 30.0% for the policy alone.  
  <sub>**Model:** GPT-6.1 Sol (xhigh), FastWAM (low-level) · **Below it:** frozen learned policy · **Interface:** A trained task-state monitor triggers the agent only on events; the agent approves a prefix of the FastWAM action chunk, makes local EEF/gripper corrections, takes over directly, or revises the next subtask · **Eval:** sim+real · **Trials:** RMBench 9 tasks (30 trials/task vs agents, 100 vs policies); real SO-ARM101: 3 tasks × 10 trials · **Speed/cost:** monitor 2.77 Hz overall; 288.3 tokens/episode vs 830.3 (GPT-as-Policy) and 1845.1 (Direct Control) on RMBench</sub>  
  ⚠️ <sub>Authors: failures are mostly difficult grasps that agent intervention can't rescue, 'highlighting agent capability as a remaining bottleneck'. Agent baselines use GPT-6 Astra while RoC uses GPT-6.1 Sol. The agent model on the real robot is not stated.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="interactvla"></a>
- **[InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](https://arxiv.org/abs/2611.22584)**
  — · *Paper* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.22584)] [[Project](https://lingwupro.github.io/InteractVLA/)]  
  Instead of treating the VLA as an opaque language-only primitive, makes System 1 geometrically steerable and inspectable by the agent. Reports 99.4% LIBERO-Plus, 48.62% RoboDojo, and 89.4% RoboCasa365, with recursive self-improvement.  
  <sub>**Model:** vision-language agent · **Below it:** frozen learned policy · **Interface:** Two-way geometric interface: agent-specified EEF targets steer a flow-based VLA via test-time gradient guidance; generated action chunks and reprojections are shown back to the agent · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="atlas"></a>
- **[ATLAS: Agentic Harness for Whole-Body Intelligence from Human Video](https://atlas-humanoid.github.io/)**
  UC Berkeley · NVIDIA · HKU · Stanford · *Project* · 2026-11-13 · `💬 post only` · 🏷️ Best Demo, CoRL 2026 Agentic Robotics Workshop  
  [[Project](https://atlas-humanoid.github.io/)]  
  Humanoid whole-body tasks from one human video, no robot demos or task-specific sim training. Real trash pickup goes from 0% to 88% (last 8 attempts) within 38 attempts. In Isaac Lab, online model-based RL reaches 83% apple lift vs 58% bias estimator / 13% model-free RL / 4% no learner.  
  <sub>**Model:** VLM agent (unnamed on page) · **Below it:** frozen learned policy · **Interface:** Agent writes a task spec once from 1 human video + 1 prompt; harness edits the end-effector reach; frozen ScaleBFM whole-body tracker (System 0) follows the edited motion; a fast learner adds a residual · **Eval:** sim+real · **Judged by:** authors · **Trials:** 38 real attempts (trash pickup)</sub>  
  ⚠️ <sub>Project page only (no paper link yet); the VLM is not named. Date is from the announcement post.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="harnesspai"></a>
- **[HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166)**
  — · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.29166)] [[Project](https://darwin-agent.github.io/HarnessPAI/)]  
  Argues that the action-model training recipe erodes perception and reasoning. Works across arms, household robots, a robot vacuum, and a legged agent. The converged programs also become cheap expert data for fine-tuning VLAs and WAMs.  
  <sub>**Below it:** frozen learned policy · **Interface:** Code as the evolvable interface that organizes underlying action primitives: open-loop program within a rollout, closed-loop evolution across rollouts · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="hugo"></a>
- **[HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.30594)**
  UC Berkeley · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.30594)] [[Project](https://iconlab.negarmehr.com/HuGo/)]  
  An LLM writes the high-level policy as code on top of a frozen whole-body controller for a Unitree G1, with no rewards or demonstrations, and refines it from its own rollouts. Best-of-N selection lifts the mean success rate across five tasks and two low-level policies 'from 43.9% to 79.1% from N=1 to N=10'. The best policies transfer zero-shot to hardware at 93.3% (PBT) and 66.7% (LBX), and refinement on hardware raises the worst-transferring policy from 20% to 90%.  
  <sub>**Model:** gpt-5.4 · **Below it:** frozen learned policy · **Interface:** The LLM writes closed-loop high-level policy code that reads numeric observations every timestep and outputs commands to a frozen whole-body tracking policy (rl_isaac at 50 Hz, sonic at 10 Hz); it refines the code from rollout trajectories and video frames · **Eval:** sim+real · **Judged by:** simulator task checks; hardware trials on a Unitree G1 · **Trials:** 100 held-out initial states per task in sim; 15 hardware trials per policy; 10 trials per hardware refinement candidate · **Speed/cost:** code runs at the controller rate; obtaining a policy takes a few hours, mostly simulated rollouts; ≈$1.1 per generated and refined policy, ≈$11 for best-of-10</sub>  
  ⚠️ <sub>Single generated policies vary widely, so best-of-10 selection is needed. The LLM misdiagnoses contact failures on the box-lifting task without a geometry hint. Observations are numeric state (motion capture on hardware), not images. Neither low-level policy maintains grasp force.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="emerge-policy"></a>
- **[EMERGE-Policy: A Robot Mind Emerges Beyond a Single Policy](https://arxiv.org/abs/2608.29896)**
  — · *Paper* · 2026-08-30 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2608.29896)] [[Project](https://emerge-policy.github.io/EMERGE-Policy/)] [[Code](https://github.com/EMERGE-Policy/EMERGE-Policy)] ![stars](https://img.shields.io/github/stars/EMERGE-Policy/EMERGE-Policy?style=flat-square&label=%E2%98%85)  
  Treats models, including action models, as skills called inside a multi-agent orchestration, with verification and branch-stack recovery. No additional fine-tuning.  
  <sub>**Below it:** frozen learned policy · **Interface:** Graph of a main agent plus sub-agents (perception, monitoring, verification, memory); heterogeneous model backends exposed as Operational / Imagination / Evaluation skills · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="gemini-robotics-2"></a>
- **[Gemini Robotics 2 brings whole-body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**
  Google DeepMind · *Blog* · 2026-07-30 · `💬 post only`  
  [[Post](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)]  
  Whole-body humanoid control. Reported success includes 74.2% general pick-and-place and 89.6% precise insertion on Franka Duo, and 36–92% on multi-finger tasks, which the page says 'remains challenging'. On-Device 2 adapts to new bi-arms with fewer than 200 examples.  
  <sub>**Model:** Gemini Robotics ER 2, Gemini Robotics 2 (VLA), Gemini Robotics On-Device 2 · **Below it:** jointly trained · **Interface:** ER 2 plans, monitors, and coordinates; the VLA emits motor commands; an on-device VLA runs locally · **Eval:** real</sub>  
  ⚠️ <sub>Vendor blog; numbers not independently reproduced.</sub>  
  <sub>↪ also in: [The Incumbent: Dual-System VLAs](#dual-system)</sub>

<a id="harness-vla"></a>
- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)**
  — · *Paper* · 2026-07-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.08448)] [[Project](https://harnessvla.github.io/)]  
  Keeps a learned System 1 only for the local contact-rich phases and lifts everything else to the planner. +38.6 pp on LIBERO-Pro and +25.4 pp on RoboCasa365 over the strongest baselines; 58.4% on RoboTwin C2R; real dual-Franka demos.  
  <sub>**Model:** LLM coding agent · **Below it:** frozen learned policy · **Interface:** Frozen VLA exposed as a retryable contact-rich primitive, plus analytic primitives for grounding, staging, transport, and release · **Eval:** sim+real · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>AMP1 notes that orchestration methods like this are capped by the reliability of the VLA they delegate to.</sub>  

<a id="novaplan"></a>
- **[NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2602.20119)**
  Robotics and AI Institute · CMU · Brown · UPenn · UIUC · Harvard · *Paper* · 2026-02-23 · `📄 peer-reviewed` · 🏷️ CoRL 2026  
  [[Paper](https://arxiv.org/abs/2602.20119)] [[Project](https://nova-plan.github.io/)]  
  Zero-shot, no task-specific training or demos, on a Franka Research 3. In Block Stacking NovaPlan 'succeeds in seven out of ten trials'; FMB assembly is shown as a qualitative boundary case.  
  <sub>**Model:** GPT-5.2 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** GPT-5.2 decomposes the task, picks among candidate Wan2.2 / Veo3.1 video rollouts, verifies execution and proposes recovery (incl. fingertip poking); object flow or human-hand flow from the chosen video becomes robot trajectories · **Eval:** real · **Judged by:** human · **Trials:** 10 per task · **Speed/cost:** about 40 s per macro-action planning; about 90 s per macro-action including execution</sub>  
  ⚠️ <sub>Authors: tabletop rigid objects, single fixed camera, 10 trials per task; video models often fail to generate corrections; 'we give no formal safety guarantee and would not deploy NovaPlan unsupervised'.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="gemini-robotics-1-5"></a>
- **[Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](https://arxiv.org/abs/2510.03342)**
  Google DeepMind · *Paper* · 2025-10-02 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2510.03342)] [[Post](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/)]  
  ER 1.5 as orchestrator cuts planning failures from 25.5% (generic Gemini 2.5 Flash orchestrator) to 9%. The VLA writes language thinking traces before acting.  
  <sub>**Model:** Gemini Robotics-ER 1.5 (orchestrator), Gemini Robotics 1.5 (VLA) · **Below it:** jointly trained · **Interface:** ER model sends step-level natural-language instructions to a 'thinking' VLA · **Eval:** real</sub>  
  ⚠️ <sub>Vendor evaluation.</sub>  
  <sub>↪ also in: [The Incumbent: Dual-System VLAs](#dual-system)</sub>

**Cross-listed here:**

- ↪ **[RoboEvo²](#roboevo2)**: RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[AA-Robotics-Sim](#aa-robotics-sim)**: Can language models drive a humanoid robot? Introducing AA-Robotics-Sim v0.1 <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[ReWeave](#reweave)**: ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[EvoTER](#evoter)**: EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[H2E](#h2e)**: What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[SO-101 Bench](#so101-bench)**: SO-101 Bench: Accessible Spatial Manipulation <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Astranomy](#astranomy)**: Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[LADDER](#ladder)**: LADDER: A Long-Horizon Robot Manipulation Benchmark <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[DualManip](#dualmanip)**: DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[Claude on robotics](#anthropic-robotics)**: How Claude performs on robotics tasks <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[InSight](#insight-steerable-vla)**: InSight: Self-Guided Skill Acquisition via Steerable VLAs <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Butter-Bench](#butter-bench)**: Butter-Bench: Evaluating LLM Controlled Robots for Practical Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>

</details>

<a id="self-improving"></a>
## 📈 Getting Better Without Weight Updates

*Memory, practice, skill libraries, and in-context learning: the general model improves across episodes while its weights stay frozen (or it trains a separate policy for you).*

<details open><summary><b>21 entries</b> + 17 cross-listed</summary>

<a id="mibot-rua"></a>
- **[Mibot-RUA (Mibot_RSI): RoboDojo agent-track entry](https://github.com/XPolicyLab/XPolicyLab/pull/204)**
  Xiaomi Robotics · *Project* · 2026-11-26 · `💬 post only`  
  [[Code](https://github.com/XPolicyLab/XPolicyLab/pull/204)] [[Data](https://robodojo-benchmark.com/LeaderBoard)]  
  Robot-use agent from Xiaomi Robotics built on GPT-6 Astra, added to the RoboDojo sim leaderboard's agent track on 2026-11-26 at 'Avg. (w/o Open): 83.94 / 79.33%' (score / success rate), the top agent-track entry. The adapter PR's own seed-1 run reports SR 78.43% / Score 83.75 including Open tasks.  
  <sub>**Model:** GPT-6 Astra · **Below it:** none · **Interface:** Eval-only XPolicyLab adapter: 'an agent entry: GPT-6-Astra through the Responses API' runs its session in a subprocess and moves the arx_x5 robot through TASK_ENV.take_action with joint targets; it mounts knowledge snapshots built by practicing on seed-0 layouts plus a priors.json of 27 short scene notes · **Eval:** sim · **Judged by:** RoboDojo simulator checker (official leaderboard) · **Trials:** RoboDojo sim, 42 tasks; adapter PR's own run: seed 1, 42 tasks × 50 episodes (2,100 episodes)</sub>  
  ⚠️ <sub>Starred by RoboDojo as deviating from the agent-track rules: the runtime injects '34 task-specific distilled briefs ... 289 task-specific skills ... 7,231 task-specific dev experience entries, 65 task-specific vision/geometry tools' and 'Task-specific scene and mechanism priors beyond Detail Description', including opponent move triggers and simulator-step behaviour. Testing began before the 2026-11-14 agent-track rules took effect. Open tasks are not in the leaderboard average. PR: 'Model outputs are non-deterministic'. No paper or company write-up; PR #204 is still open.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="roboevo2"></a>
- **[RoboEvo$^2$: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution](https://arxiv.org/abs/2611.34675)**
  HKU; Zhejiang University; SUSTech; CUHK-Shenzhen; City University of Hong Kong · *Paper* · 2026-11-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.34675)] [[Project](https://kaiknower.github.io/RoboEvo2/)] [[Code](https://github.com/kaiknower/RoboEvo2)] ![stars](https://img.shields.io/github/stars/kaiknower/RoboEvo2?style=flat-square&label=%E2%98%85)  
  Co-evolves a code harness and a learned policy without extra human demonstrations: 'RoboEvo2 improves standalone success from 11.0% to 84.1% and hybrid success from 30.4% to 90.5% on LIBERO-PRO, with similar gains and reduced agentic costs on RoboTwin C2R', and reaches '95.0% hybrid success on the Unitree G1-D'. On the G1-D the policy trained on 120 automatically collected demonstrations scores 85.0% standalone vs 80.0% for π0.5 trained on 200 teleoperated ones. Swapping the agent for Qwen3.8-27B gives 76.0% / 82.5% on LIBERO-PRO.  
  <sub>**Model:** GPT-6 Astra, Qwen3.8-27B · **Below it:** trained by the agent · **Interface:** GPT-6 Astra (xhigh) repairs failures of a π0.5 policy by writing programs on CaP-X/RATs robot APIs along Code, Code+ICL and Code+Policy routes, consolidated into skills, routing and memory; verified trajectories then fine-tune the policy (with counterfactual preference distillation); in hybrid mode each step is routed to the policy or a code skill · **Eval:** sim+real · **Judged by:** task-level success check (simulator) for selecting training data and for evaluation; real-world judge not stated · **Trials:** LIBERO-PRO: 8 settings × 100 episodes on unseen initial states; RoboTwin C2R: 5,000; Unitree G1-D: 4 tasks × 10 trials · **Speed/cost:** per-round coding-agent 'API expenditure decreases from $430.63 to $98.92' on LIBERO-PRO</sub>  
  ⚠️ <sub>Authors: skills are built 'on top of a fixed set of atomic skills and perception tools, which do not yet cover capabilities such as force-controlled contact or in-hand regrasping'; 'A task-level success check selects the executions that train the policy'. The agent gets rendered depth and camera calibration. Hybrid numbers still call an agent at test time. Comparisons with other methods 'retain their original evaluation protocols'. Real-world: 10 trials per task, judge not stated. Code 'will be publicly released'.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="margin"></a>
- **[MARGIN: A Risk-Aware Agent for Robot Program Refinement](https://arxiv.org/abs/2611.32093)**
  Tsinghua University; Peng Cheng Laboratory; Southern University of Science and Technology; Institute of Automation, CAS · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32093)]  
  Adds risk-aware refinement to agentic robot-program debugging once binary success saturates: the authors' ASPIRE reproduction with Opus 5.5 'succeeds in 3,927/4,000 LIBERO-Pro held-out episodes for a success rate of 98.175%', yet dev-perfect programs still cause 53 of 73 failures. 'The near-miss margin predicts held-out failures with an AUC of 0.774', and margin-guided repair 'reduces executed control steps by 10.7% and 15.0%' on LIBERO-Pro and '18.0–20.0% on LIBERO-90 and Robosuite'; safe racing cuts candidate-evaluation episodes by 53.5% with identical selections.  
  <sub>**Model:** Claude Opus 5.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Claude Opus 5.5 coding worker (ASPIRE reproduction) writes robot programs over perception, grasp-synthesis and motion-planning tools; after development success saturates, MARGIN ranks programs by near-miss margin (step budget left in the slowest successful development rollout), asks the worker for repairs, and accepts only revisions that keep development success and raise the margin · **Eval:** sim · **Judged by:** benchmark success check (LIBERO-Pro / LIBERO-90 / Robosuite) on held-out and fresh seeds; acceptance uses development seeds only · **Trials:** LIBERO-Pro: 80 tasks, held-out seeds 1–50 (4,000 episodes) plus fresh seeds 101–130; repairs on 37 tasks over two rounds (74 sessions); also 90 LIBERO-90 and 7 Robosuite tasks · **Speed/cost:** 'Repairing a program costs $4.4–6.0 per task, compared with $12.5–15.8 for the ASPIRE discovery campaign'; $338 total refinement</sub>  
  ⚠️ <sub>No dedicated limitations section. Gains are mostly in execution length: held-out success moves only 'from 94.0% to 94.8% in round 1 and from 97.5% to 97.7% in round 2' on the refined tasks. Simulation only, 1000-step horizon; baseline LIBERO-Pro scores in the comparison table are taken from the cited papers. Builds on the authors' reproduction of ASPIRE (official Opus 5.5 ASPIRE: 98.75%).</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="wsp-robot-repair"></a>
- **[Sparks of Weight-Space Programming for Robot Foundation Models](https://arxiv.org/abs/2611.31715)**
  Siemens Research · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31715)]  
  An LLM agent repairs recurring π0.5 failures by editing about 6,000 of 3.35 billion parameters. 'Three of the five fixes clearly worked on unseen scenes': hammer 56.5% → 70.5% (200 scenes), bell 87.3% → 96.7% (300 scenes), and on an already task-fine-tuned basket checkpoint 67.7% → 84.4% across 505 scenes. Sign-reversed edits recreated the targeted failure and random edits 'made no consistent difference'.  
  <sub>**Model:** Claude Opus 5.5 · **Below it:** trained by the agent · **Interface:** Claude Opus 5.5 with tool access runs the π0.5 policy server in RoboTwin 2.0, inspects actions and action-expert neuron activations, and directly rewrites connections to near-silent neurons so a corrective movement fires in the diagnosed failure state; no demonstrations, fine-tuning or gradient updates; the edited π0.5 is the policy · **Eval:** sim · **Judged by:** simulator success on new seeded scenes against a pass mark set in advance; failures identified from the simulator's exact measurements · **Trials:** held-out scenes: 200 (beat_block_hammer), 300 (click_bell), 200 (move_can_pot), 505 (place_mixed_objects_basket); paired with the unedited policy, plus random and sign-reversed controls</sub>  
  ⚠️ <sub>Authors: the approach 'worked best when the failure situation was recognizable and a simple correction could address it; it did not solve every failure' (move_can_pot 38% → 41%, not significant; turn_switch never reached held-out testing). Edits are task-specific and diagnosed using the simulator's exact measurements; simulation only. Short report (8 pages); the PDF's own title differs from the arXiv title.</sub>  

<a id="real2worlds2real"></a>
- **[Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation](https://arxiv.org/abs/2611.31098)**
  NVIDIA · UC Berkeley · UIUC · CMU · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31098)] [[Project](https://real2worlds2real.github.io)]  
  A GPT-6 Astra-powered agent turns real videos into digital twins and cousins, then develops policies in them for real deployment. Real dexterous robot (30 trials/task): 100.0% / 90.0% / 73.3% / 100.0% on Lift/PickPlace/Nut/Cup vs ASPIRE 90.0/86.7/63.3/80.0. On LIBERO-Pro Long with agent-written control scripts, 'as the library grows from 0 to 136 skills ... overall success rises from 52.9% to 82.2%'.  
  <sub>**Model:** GPT-6 Astra · **Below it:** trained by the agent · **Interface:** General-purpose coding agent with a skill-guided tool-orchestration harness writes Blender scripts and physics calibration to build digital twins/cousins, then writes code-as-policy programs (grasp + cuRobo/MPC), RL rewards, or trains ACT / Diffusion Policy with DAgger and RL decorators; distilled 'personal skills' are reused across tasks · **Eval:** sim+real · **Judged by:** real: not stated; LIBERO-Pro: benchmark checker on 50 held-out initial states · **Trials:** real: 30 trials per task per method (Dexmate robot with Sharpa hands); LIBERO-Pro Long: 20 tasks × 50 held-out initial states · **Speed/cost:** world building for held-out lemon-cutting task: 28.1M → 13.9M tokens with skill reuse</sub>  
  ⚠️ <sub>No limitations section. Real-robot policies are learned ACT/RL-decorator policies the agent trains, initialized from 60 real demonstrations; the frontier model is not in the runtime loop. LIBERO-Pro 82.2% appears to select the best candidate program ('Even the mean over all candidate programs, without selecting the best, rises from 44.1% to 69.1%'). Real-world judge not stated; no latency or dollar cost reported.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="reweave"></a>
- **[ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation](https://arxiv.org/abs/2611.31053)**
  Zhejiang University; Stanford University; Tsinghua University; AGIBOT Innovation · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31053)] [[Project](https://xuyicheng-zju.github.io/ReWeave/)] [[Code](https://github.com/xuyicheng-zju/ReWeave)] ![stars](https://img.shields.io/github/stars/xuyicheng-zju/ReWeave?style=flat-square&label=%E2%98%85)  
  Optimizes an LLM-controlled embodied harness without updating policy weights: 'ReWeave improves held-out success from 89.00% to 98.75% on LIBERO-PRO and from 25.50% to 58.25% on RoboDojo' (RoboDojo Score 63.43), and finds retained progress in 89% of 159 failed RoboDojo development trials. On eight unseen LIBERO-PRO tasks the shared harness reaches 51.3% vs 41.3% for direct distillation, 75.0% after continual learning. On the real G2, sorting rises from 20% to 80% and pouring/plugging (frozen VLA) from 40% to 60% and 50% to 70%.  
  <sub>**Model:** GPT-6 Astra (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (high), Claude Sonnet 5.5, DeepSeek V4.1 Flash · **Below it:** frozen learned policy · **Interface:** Inner LLM controller acts as the policy through a harness (context, workflows, control loop) over a frozen π0.5 VLA, SAM3 perception and Cartesian/IK primitives; an outer LLM agent revises the harness offline between episodes, guided by an emergent task topology that re-scores archived trials · **Eval:** sim+real · **Judged by:** official benchmark success labels (sim); real: on-site operator using physical endpoint criteria · **Trials:** LIBERO-PRO 80 tasks and RoboDojo 42 tasks: seed 0 for development (up to 10 rounds per task), held-out seeds 1–10; real dual-arm G2: 10 trials per task and harness version · **Speed/cost:** real G2 sorting episodes 504.3 → 402.1 s; offline tokens reported, e.g. 41.72 M for eight-source distillation</sub>  
  ⚠️ <sub>Authors: 'Topology inference depends on observable traces, and ambiguous contacts can delay edge resolution. Optimization requires physical trials and model calls. Agent reasoning adds execution latency, limiting use in time-sensitive settings; transfer remains uneven across the hardest tasks.' Harness is optimized per task on seed 0 before held-out testing; comparisons are against the authors' own seed harness H0 rather than re-run external systems; archived LIBERO-PRO development records contain simulator state used for post-hoc reference predicates (withheld from scorer and optimizer). Real-robot results are 10 trials per task.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="navrsi"></a>
- **[NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation](https://arxiv.org/abs/2611.27499)**
  Singapore Management University · Renmin University of China · Fudan University · Nanjing University of Science and Technology · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27499)] [[Project](https://daiguangzhao.github.io/NavRSI/)]  
  Vision-and-language navigation, not manipulation: a frozen frontier LLM steps a robot with primitive actions from one RGB camera, and a designer LLM recursively rewrites the harness. With GPT-6-Astra it reaches 85.64 SR on the full R2R-CE val-unseen split, '+4.13 SR over NavGPT-3, which pairs the same LLM with an 8B model'; the same harness beats native harnesses of four vendors by up to 11.3 SR. On a Unitree G1 humanoid: '48 SR against 36 for NavGPT-3 and 16 for Open-Nav'.  
  <sub>**Model:** GPT-6-Astra, GPT-6-Luna, GPT-5.6-Sol, GPT-6.1-Terra, GPT-6.1-Sol, GPT-6.2-Sol, GPT-6.2-Astra, Claude Sonnet-5, Claude Opus-5, Claude Opus-5.5, Claude Fable-5, Claude Fable-5.2, Gemini-3.8-Flash, Gemini-4-Hydrogen, Qwen3.7-Flash, Qwen3.8-Flash, Qwen3.8-27B · **Below it:** none · **Interface:** Frozen navigator LLM calls two tools, observe (single forward RGB view) and step (list of primitive actions: forward 0.25 m, turn 15°, STOP); a separate designer LLM (GPT-6-Astra in Codex CLI) rewrites the harness code over 8 RSI rounds using simulator diagnostics the navigator never sees · **Eval:** sim+real · **Judged by:** VLN-CE standard metrics in simulator (NE/OSR/SR/SPL); real-world judging not stated · **Trials:** R2R-CE-100: 3 runs per LLM; full R2R-CE and RxR-CE val-unseen splits; NavRAG-CE 100 episodes × 3 runs; real: 25 instructions × 4 runs on Unitree G1 · **Speed/cost:** RxR-CE mean 312.8 s per episode (vs 333.2 s NavGPT-3, 434.8 s MIP/Codex CLI); $0.424 per RxR-CE episode with GPT-6-Astra (vs $0.562 NavGPT-3, $1.086 MIP)</sub>  
  ⚠️ <sub>No limitations section. Navigation only; authors list extending 'to more embodied tasks beyond navigation' as future work. The full R2R-CE split includes the development set used for harness selection (held-out 537-episode comparison reported separately). Real-world run is 25 instructions × 4 runs with no stated judge. Source code 'will be released'.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="embodied-harness"></a>
- **[Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation](https://arxiv.org/abs/2611.27689)**
  Zhejiang University · Huazhong University of Science and Technology · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27689)]  
  Actor/Reflector dual-agent harness around a frozen GPT-6 Astra that refines its harness from execution evidence. RoboTwin 2.0 C2R: 82.4% with zero demos, 'surpasses RoboDawn by 29.2 percentage points' and beats GigaBrain-0.7 (67.9%) and PrismWAM (75.5%); RoboSPA-Spatial L5 94.0%, RoboSPA-Long 59.5%, RMBench 94.4%. Real Piper arm: 'average success rate of 96.7% versus 40.0%' for π0.5.  
  <sub>**Model:** GPT-6 Astra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Actor emits one of five control commands (move, rotate, point, gripper, home) with grounded arguments per step; harness converts to an SE(3) target pose and solves IK; a Reflector (same frozen model family) diagnoses each attempt and updates the harness guidance and hierarchical memory · **Eval:** sim+real · **Judged by:** benchmark success checks (RoboTwin 2.0, RoboSPA, RMBench); real-world judging not stated · **Trials:** 10 episodes per task on RoboTwin 2.0 (50 tasks), RoboSPA and real tasks (3 tasks, Piper arm); 20 per task on RMBench (9 tasks); max 45 interaction rounds per episode</sub>  
  ⚠️ <sub>No limitations section; authors' future work: 'experience transfer across tasks and embodiments and more efficient execution and reflection.' Headline numbers are after 4 harness-refinement rounds ('From round 0 to round 4, success rates increase from 59.2% to 82.4% on RoboTwin 2.0 C2R'), and the paper does not state a separate train/test split for refinement, so the 'zero-shot' comparison with RoboDawn is not like-for-like. Baseline numbers appear to be taken from prior reports. No latency, cost or code reported; real-world judge not stated.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="evoter"></a>
- **[EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection](https://arxiv.org/abs/2611.27797)**
  Institute of Automation, Chinese Academy of Sciences · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27797)] [[Project](https://evoter-project.github.io/)]  
  A frozen gpt-6.1-sol agent orchestrates a frozen VLA and analytic tools, and evolves a tool-use skill library that is kept only when complete-task validation success rises. RoboCasa365 Target50: 'from a pre-evolution baseline of 53.60% to 80.40%', vs Xiaomi-Robotics-1 57.40% and Harness VLA 59.20%. Real Franka long-horizon: 4/5, 5/5, 5/5 after real-world evolution vs 1/5 each by direct transfer.  
  <sub>**Model:** gpt-6.1-sol · **Below it:** frozen learned policy · **Interface:** Codex-based agent selects one tool call per step (segmentation, detection, grasp generation, cuRobo motion planning, low-level control, a frozen VLA: Xiaomi-Robotics-1 in sim, a π0.5-based policy and Tether on the real robot) guided by a skill library; Explorer/Diagnoser/Validator roles (same frozen model) evolve the library, accepting revisions only on higher validation success · **Eval:** sim+real · **Judged by:** 'externally evaluated task outcome' (RoboCasa365 checker in sim); real-world judge not stated · **Trials:** Sim: RoboCasa365 Target50 (50 tasks), 3 evolution rounds × 5 exploration seeds and 5 validation seeds per task, frozen test set disjoint; real Franka: 5 test trials per task (3 short-horizon, 3 long-horizon tasks) · **Speed/cost:** real-world development capped at 150 M total tokens per task; e.g. plate transfer 103.45 M → 17.58 M total tokens with sim initialization</sub>  
  ⚠️ <sub>Authors: 'Future work will streamline validation, reduce reliance on privileged simulation feedback, and broaden evaluation across tasks and embodiments.' Diagnoser can use privileged simulator state after stagnation (execution and validation use only ordinary tools). External baselines are 'taken from the cited sources'; Composite-Unseen 'development episodes ... may contribute to skill evolution'. Two-cup hanging needed 'a high-level hint' from humans. Real-world tests are 5 trials per task.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="unicraft"></a>
- **[Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience](https://arxiv.org/abs/2611.26376)**
  The University of Sydney · Nanjing University · *Paper* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26376)]  
  One shared skill library refined across LIBERO-PRO, RoboTwin 2.0 and RoboCasa365 (6 embodiments) with no demos or weight updates; pooled unseen success improves 'by 9-28 percentage points on LIBERO-PRO'. GPT-6 Astra reaches 86.00 on LIBERO-PRO unseen tasks (X-VLA 96.00). With frozen skills, zero-shot on RoboDojo: 'Overall success is 54.8%'.  
  <sub>**Model:** GPT-6 Astra, Gemini 3.8 Flash, DeepSeek-V4.1-Flash, transfer: GPT-6.1 Sol, GPT-6.1 Terra, MiniMax M3.1 Flash · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Agent in a Codex harness writes scripts against a shared skill / device-API package; a batch-level Reviser revises the shared skills and the orchestration policy from rollout feedback · **Eval:** sim · **Judged by:** native benchmark success checks · **Trials:** 2,700 learning rollouts per agent model; 5 rollouts per evaluation case</sub>  
  ⚠️ <sub>Authors: different auxiliary tools across methods limit comparability; only high reasoning effort and 3 epochs assessed because of cost; RoboCasa composite tasks remain low; validated revisions can regress.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="lexp"></a>
- **[Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation](https://arxiv.org/abs/2610.41320)**
  CUHK / xdof.ai · *Paper* · 2026-10-30 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.41320)] [[Project](https://hatty-z.github.io/LearnFromExperience/)]  
  GPT-6 Astra as a direct bimanual policy that learns from physical experience in context. Across 12 real tasks LEXP reaches 23/36 (63.9%) vs 19/36 (52.8%) with memory alone and 2/36 (5.6%) for vanilla Astra. With memory only, Opus 5.5 gets 11/36 and Sol 5.6 0/36.  
  <sub>**Model:** GPT-6 Astra, Opus 5.5, Sol 5.6 · **Below it:** none · **Interface:** Actor emits absolute Cartesian pose / gripper tool calls per YAM arm with an intention note; a planner and an experience module write lessons back into its context; weights fixed · **Eval:** real · **Judged by:** human annotation against predefined completion criteria, independent of the actor's own declaration · **Trials:** 12 real tasks × 3 trials per condition (36), bimanual YAM</sub>  
  ⚠️ <sub>Authors: 'Bimanual coordination remains challenging, with no successful sweeping or towel-folding trials under any condition'; memory benefit is actor-dependent and varies across tasks. Three trials per task and condition. No latency or cost reported.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="recursia"></a>
- **[Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.24464)**
  — · *Paper* · 2026-10-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.24464)]  
  Treats the shared executable stack, not individual task programs, as the unit of self-improvement. Zero-shot on LIBERO-Pro Long it reaches 0.284 on Pos and 0.534 on Task, 5.8 and 15.1 points above ASPIRE. On three compositional tasks on a Franka FR3 it averages 66.7% vs 26.7% for a skill-document-only baseline.  
  <sub>**Model:** GPT-6 Astra (physical runs), Claude Opus 5.5 (low effort, verifier calls) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** A coding-agent proposer patches a shared executable stack (tools, skills with contracts, handoffs, verifiers) from source-task failure traces; validation gates decide what persists, and the frozen stack is reused on unseen compositions via declarative task adapters · **Eval:** sim+real · **Judged by:** official LIBERO-Pro evaluator (sim); manual assessment (real) · **Trials:** 500 episodes per axis on LIBERO-Pro Long; 10 trials per physical target task · **Speed/cost:** 5.20–7.22 min mean end-to-end per sim episode, depending on the inference driver</sub>  
  ⚠️ <sub>Authors: source-side improvement relies on simulator ground-truth diagnosis that may not exist on a real robot; no cross-embodiment test; the grasp backend differs from the ASPIRE configuration it is compared against, which limits fairness.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="scope-program-edits"></a>
- **[SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning](https://arxiv.org/abs/2610.23128)**
  Peking University · *Paper* · 2026-10-16 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2610.23128)] [[Code](https://github.com/VDIGPKU/SCOPE)] ![stars](https://img.shields.io/github/stars/VDIGPKU/SCOPE?style=flat-square&label=%E2%98%85)  
  On LIBERO-PRO SCOPE reaches 80.66 ± 1.46% overall, 6.51 points above ASPIRE with the same GLM-5.3-Flash backbone, and 84.48 ± 1.67% on Robosuite. On a Quanta X2 robot, frozen programs succeed in 40/60 trials vs 24/60 for ASPIRE.  
  <sub>**Model:** GLM-5.3-Flash (local) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** LLM program search repairs a robot program using failed and successful executions; stateful API replay certifies that edits keep selected past successes before they are accepted; the program is frozen for held-out evaluation · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); held-out physical placements (real) · **Trials:** 3 learning-and-evaluation runs in sim; 20 held-out placements per real task (60 per method) · **Speed/cost:** several thousand US dollars estimated for the full experimental suite via hosted APIs</sub>  
  ⚠️ <sub>Authors: repeated language-model inference is costly; early candidate programs on physical robots can be unsafe and need human supervision. Baselines other than ASPIRE are point estimates under their original protocols.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="sear"></a>
- **[SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792)**
  — · *Paper* · 2026-10-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.18792)] [[Project](https://sear.bot/)]  
  Asks 'is the agent really learning, or just trying more often?'. Controls separate retained experience from re-rolls, privileged state, budget, and luck. Control code and shared routines transfer; task-specific solutions don't. Models differ in whether they evolve best acting live or writing code. A text-only model keeps pace with a multimodal one.  
  <sub>**Model:** 7 frontier LMs · **Below it:** trained by the agent · **Interface:** Three modes on the same tools: code-as-policy, agent-as-policy (live in the loop), and auto-research (fine-tunes a VLA) · **Eval:** sim+real · **Judged by:** benchmark with controls · **Trials:** 330 sim + 5 physical tasks; >4 years of agent runtime</sub>  
  ⚠️ <sub>Real-robot gap between agent-designed practice and novel human-designed scenes.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="retrace"></a>
- **[ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation](https://arxiv.org/abs/2610.15814)**
  Fudan University · *Paper* · 2026-10-11 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.15814)]  
  Self-improvement from autonomous physical interaction with no demos or weight updates; skills learned by Astra-high transfer to other models and effort levels. GPT-6 Astra-low improves from 0% to 80% on plug insertion and 0% to 100% on ball pouring; GPT-6 Sol-xhigh from 0% to 10% and 0% to 90%.  
  <sub>**Model:** GPT-6 Astra (high, learner), GPT-6 Astra-low, GPT-6 Sol-xhigh · **Below it:** none · **Interface:** Executor predicts action chunks for a Franka; an Attributor on the same model traces failures to earlier decisions and consolidates validated corrections into a text skill · **Eval:** real · **Trials:** 4 real tasks on Franka Research 3, 10 trials per task per configuration</sub>  
  ⚠️ <sub>Authors: plug insertion remains difficult for Sol-xhigh even with the skill, so benefits vary across executing models. Who judges success, latency and cost are not stated.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="physevo"></a>
- **[PhysEvo: Astra Can Act, Let It](https://arxiv.org/abs/2610.08995)**
  UCAS / CASIA · *Paper* · 2026-10-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.08995)]  
  Physical recursive self-improvement around one frozen model, with no weight updates or trained action policy. On 42 RoboDojo tasks: 68.14/100 score and 62.00% success on held-out layouts, vs 47.17% for RoboDawn's one-shot Astra agent. On 8 tasks challenging for direct Astra: 55.00% vs 1.25%. Real AgileX PiPER: 90.60/100 and 84.00% success across 25 trials on five tasks.  
  <sub>**Model:** Astra (frozen; task agent and meta-agent) · **Below it:** none · **Interface:** Task agent issues joint-level control_arms calls (12 joint targets + 2 grippers) or observation/geometry tools; a meta-agent on the same model revises tools, skills and diagnostic code between episodes · **Eval:** sim+real · **Judged by:** RoboDojo native evaluator (sim); authors' rubric (real) · **Trials:** 42 RoboDojo tasks × 5 held-out layouts; real: 5 tasks × 5 trials on AgileX PiPER</sub>  
  ⚠️ <sub>Each task keeps its own deployment version and task-specific skills; real-world runs continue skill revision between attempts. Baselines are taken from leaderboards and reports, not rerun. No latency or cost reported.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="real2gym"></a>
- **[Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](https://arxiv.org/abs/2609.37089)**
  Shanghai AI Lab · SJTU · Zhejiang U · USTC · CUHK · HKU · *Paper* · 2026-09-29 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.37089)] [[Project](https://real2gym.github.io/)]  
  Turns human and robot demo videos into physics-validated sim gyms where a GPT-6 Astra code agent practises and accumulates skills, with no weight updates. 'outperforming GPT-6 Astra Direct Mode by 16.7% in success rate with approximately 74.9% fewer policy-execution tokens' in sim, 'while exceeding it by 33.3% in physical robot execution success rate across four tasks on a real Franka robot.'  
  <sub>**Model:** GPT-6 Astra (medium reasoning), baselines: GPT-6 Astra Direct Mode, GPT-5.6 Sol xhigh · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Agent writes an executable program per manipulation stage over segmentation, grasp-proposal and arm-control APIs; skills distilled from successes and failures guide later runs; sim and real share the interface · **Eval:** sim+real · **Judged by:** predefined completion criteria and human inspection · **Trials:** 24 reconstructed MuJoCo environments; real: 4 Franka tasks × 3 trials · **Speed/cost:** Tokens (M) DROID/EgoDex: with skills 0.51/0.49 vs GPT-6 Astra Direct 1.42/2.56</sub>  
  ⚠️ <sub>Authors: stage-level code 'lacks the local fine-grained reactivity required for highly constrained manipulation'; real tests only on Franka arms with parallel-jaw grippers, 3 trials per task; reconstruction fidelity is judged by GPT-6 Astra.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="gpt-policy"></a>
- **[In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138)**
  — · *Paper* · 2026-09-16 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.19138)] [[Project](https://cheng-haha.github.io/GPT-Policy/)] [[Code](https://github.com/cheng-haha/GPT-Policy)] ![stars](https://img.shields.io/github/stars/cheng-haha/GPT-Policy?style=flat-square&label=%E2%98%85)  
  In-context robot learning without gradient updates. Human video demos help even without action labels; aligned action references help further on contact-sensitive tasks.  
  <sub>**Model:** GPT-6 Astra and others · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Context compiler → VLM proposes robot-tool actions → constrained controller verifies and executes · **Eval:** real</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="aspire"></a>
- **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)**
  NVIDIA GEAR · *Paper* · 2026-06-30 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2607.00272)] [[Project](https://research.nvidia.com/labs/gear/aspire/)] [[Code](https://github.com/NVlabs/ASPIRE)] ![stars](https://img.shields.io/github/stars/NVlabs/ASPIRE?style=flat-square&label=%E2%98%85)  
  Continual code-as-policy learning. With Claude Opus 5.5 it nearly saturates benchmarks: 99% on all 80 LIBERO-Pro tasks, 100% on representative Robosuite and BEHAVIOR-1K tasks. Performance scales with the underlying frontier model. Skills found in sim transfer to the real robot.  
  <sub>**Model:** Claude Opus 5.5 (best), other frontier models · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Code-as-policy with closed-loop execution traces, a growing skill library, and evolutionary program search · **Eval:** sim+real · **Judged by:** benchmark checkers</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="insight-steerable-vla"></a>
- **[InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884)**
  Stanford · Princeton · NASA JPL · *Paper* · 2026-06-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2606.24884)] [[Project](https://insight-vla.github.io/)]  
  A frontier VLM teaches a VLA new primitives. Acquired skills reach '92% twist and 96% pour success, compared with 32% and 16% for CaP-X' using the same VLM; composing both into a 14-primitive task reaches '80% end-to-end success vs. 4% for CaP-X'.  
  <sub>**Model:** Gemini 3 Flash · **Below it:** trained by the agent · **Interface:** VLM segments demos into primitives, flags primitives the VLA lacks, drives single-axis controller motions to acquire them and checks success from images; successes are distilled into a primitive-steerable π0.5 that the VLM then sequences · **Eval:** sim+real · **Judged by:** ground-truth state (sim); human against binary criteria (real); VLM filters acquisition rollouts · **Trials:** 25 trials per method (real twist / pour / composition)</sub>  
  ⚠️ <sub>Authors: new-primitive execution restricted to single-axis motions; only successful rollouts are used; 'manual environment resets are still necessary in this work'.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="enpire"></a>
- **[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)**
  NVIDIA GEAR · *Paper* · 2026-06-18 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2606.19980)] [[Project](https://research.nvidia.com/labs/gear/enpire/)] [[Code](https://github.com/NVlabs/ENPIRE)] ![stars](https://img.shields.io/github/stars/NVlabs/ENPIRE?style=flat-square&label=%E2%98%85)  
  The frontier agent does not act as the policy; it is the researcher that trains a fast System 1. It reaches 99% success on dexterous real tasks (pin-box organizing, zip-tie fastening, tool use).  
  <sub>**Model:** frontier coding agents · **Below it:** trained by the agent · **Interface:** Harness with Environment (auto reset and verify), Policy Improvement, Rollout (robot fleet), and Evolution (agent edits training code) modules · **Eval:** real · **Judged by:** automatic verifier</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

**Cross-listed here:**

- ↪ **[X-Harness](#x-harness)**: Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[RegHarness](#regharness)**: RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[Boundary-Aware Policy Learning](#boundary-aware-policy)**: Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[Agent on Guard (AoG)](#agent-on-guard)**: Agent on Guard: Self-Improving Runtime Intervention for Robust Robotic Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[EvoMisty](#evomisty)**: EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[γ-Scape](#gamma-scape)**: $γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[InteractVLA](#interactvla)**: InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[ATLAS](#atlas)**: ATLAS: Agentic Harness for Whole-Body Intelligence from Human Video <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[ACE-CaP-0](#ace-cap-0)**: ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[AMP1](#amp1)**: On Agentic Manipulation Policies <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[HarnessPAI](#harnesspai)**: HarnessPAI: An Evolving Harness for Physical AI <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[RACaP](#racap)**: RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[HuGo](#hugo)**: HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[AquaCap](#aquacap)**: AquaCap: A Training-Free Underwater Embodied Agent with Code-as-Policy <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[AGP](#agent-as-policy)**: Agent as Policy for Robotic Manipulation <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[Push-T, revisited](#push-t-agentic)**: Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[CoEnv / CoEx](#coenv-coex)**: CoEnv: Code-Driven Exploration in Real-to-Sim Digital Twins for Multi-Arm Manipulation <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>

</details>

<a id="fast"></a>
## ⚡ Making It Fast & Cheap

*Latency and dollar cost are the main open problem. Distillation into small models, open-weight harnesses, asynchronous planning/execution. Thin on purpose: this is the research gap.*

<details open><summary><b>8 entries</b> + 14 cross-listed</summary>

<a id="embodyagent"></a>
- **[EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL](https://arxiv.org/abs/2611.26196)**
  Tsinghua University · *Paper* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26196)]  
  Distills a black-box frontier code-writing agent into an open 9B VLM via SFT, then online RL. Held-out success rises from 0/100 (base 9B VLM) to 14/100 after SFT and 84/100 after RL; median model calls per test episode drop from 36 to 11.  
  <sub>**Model:** Astra Medium (black-box teacher), Qwen3.5-9B (student) · **Below it:** none · **Interface:** Think-then-code through one execute_python tool exposing raw images/proprioception and 7-D end-effector control; no primitives, no action decoder · **Eval:** sim · **Judged by:** LIBERO BDDL success predicate · **Trials:** 100 held-out test states (10 LIBERO Spatial tasks) · **Speed/cost:** student median 136 s per episode incl. simulation; teacher 1,887 s of frontier-API inference per episode</sub>  
  ⚠️ <sub>One simulated suite (ten LIBERO Spatial tasks), single run per stage, no real robot. The reported checkpoint is 'the best score observed' while monitoring the same test states, with RL still in progress.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="pear-rurl"></a>
- **[Training Reasoning Models in Simulation to Natively Use Real Robots](https://arxiv.org/abs/2611.18562)**
  — · *Paper* · 2026-11-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.18562)]  
  Robot-use RL (RURL) entirely in simulation, no demos, mirroring how frontier models learn computer use. LIBERO rises from 1.6% to 74.4% (near GPT-6 Astra / GPT-6.1 Sol at max effort), with 60% on a real dual-arm robot (base model 0%). On LIBERO-Pro new-task-in-familiar-scene: 57.4% vs π0.5 0.75%. No measurable loss on 9 general reasoning, coding, and vision benchmarks.  
  <sub>**Model:** open-weight 27B reasoning model (RL-trained) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** No harness: observe → chain of thought → next end-effector pose, like a computer-use agent · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="ace-cap-0"></a>
- **[ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience](https://arxiv.org/abs/2611.16872)**
  ACE-CaP Team · *Paper* · 2026-11-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.16872)]  
  Moves the frontier model's reasoning to development time: frozen programs reach 92.1% (221/240) on 8 real tasks including bimanual ones, with no human or agent in the loop at runtime.  
  <sub>**Model:** coding agent (development time only) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Agent develops programs with Demonstrations on Request and Simulation on Demand, then freezes them; runtime has no model in the loop · **Eval:** real · **Trials:** 240 real trials over 8 tasks · **Speed/cost:** 0.97–2.27 min mean task time; no model calls at runtime</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="h2e"></a>
- **[What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation](https://arxiv.org/abs/2611.16246)**
  — · *Paper* · 2026-11-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.16246)]  
  Harness-to-Executor distillation folds the System 2 agent back into System 1. +15.6% (REVERIE-CE) and +11.1% (NavRAG-CE) for an 8B VLA. The student exceeds its agent teacher on unseen episodes.  
  <sub>**Model:** LLM planner (teacher) + 8B VLA (student) · **Below it:** trained by the agent · **Interface:** Successful LLM-planner + frozen-VLA sessions relabelled as VLA actions for the original task, then distilled into the VLA alone · **Eval:** sim · **Judged by:** benchmark · **Speed/cost:** distilled VLA runs 3.7× faster with zero LLM tokens</sub>  
  ⚠️ <sub>Navigation, not manipulation.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="democratizing-rua"></a>
- **[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://arxiv.org/abs/2611.01560)**
  — · *Paper* · 2026-11-01 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.01560)]  
  An out-of-the-box open-weight model scores 31.39 on RoboDojo without privileged inputs, above the published GPT-6 Astra-RoboProbe 28.97. Links effective robot use to four general capabilities.  
  <sub>**Model:** Qwen3.8-Flash-Next (open-weight) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Unified harness for open-weight models that supports further training · **Eval:** sim+real · **Trials:** 19 real-world tasks</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="dualmanip"></a>
- **[DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation](https://arxiv.org/abs/2609.31112)**
  Tsinghua University, HIT (Shenzhen), Beijing Institute of Control Engineering · *Paper* · 2026-09-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.31112)] [[Project](https://lichengxi1.github.io/Dualmanip)]  
  KUKA iiwa real-robot study. GPT-5.6 Terra handles infrequent semantic reasoning; a learned geometric path re-targets grasps under motion and deformation, falling back to VLM replanning on failure. Under continuous scene change 'DualManip maintains a 53.3% mean success rate, considerably surpassing ReKep (28.9%) and OmniManip (17.8%), whereas CLEA and Open-loop fail completely'; adaptation is 'approximately 46× faster than agentic verification and semantic replanning'.  
  <sub>**Model:** GPT-5.6 Terra, Qwen3.5-2B · **Below it:** frozen learned policy · **Interface:** VLM decomposes the task into stages, names functional regions (SAM 3 masks) and picks spatial constraints from a predefined relation set; constraint solving + AnyGrasp give poses; a per-object-trained shape-adaptive correspondence network transfers grasp contacts at ~139 ms per update; failed feasibility checks trigger VLM replanning · **Eval:** real · **Judged by:** not stated (success counts per task) · **Trials:** 15 trials per object–condition–method; 6 tasks (3 general × static/single-change/continuous, 3 assembly static only); latency averaged over 20 updates · **Speed/cost:** 'DualManip requires 138.7 ms per adaptation'; agentic baseline CLEA 6.376 s with GPT, 4.329 s with local Qwen3.5-2B</sub>  
  ⚠️ <sub>Authors: 'DualManip relies on pre-constructed templates and object-specific training for dense correspondence, constraining direct zero-shot generalization to unseen instances.' Correspondence network trained on 100 RGB-D observations per object per viewpoint. Latency excludes 'shared downstream modules with large runtime variance'. Qwen3.5-2B is used only to time the CLEA baseline.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="racap"></a>
- **[RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394)**
  — · *Paper* · 2026-09-24 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.29394)] [[Code](https://github.com/Robo-Harness/racap)] ![stars](https://img.shields.io/github/stars/Robo-Harness/racap?style=flat-square&label=%E2%98%85)  
  54.4% LIBERO-90, 45.0% zero-shot LIBERO-PRO, 46.0% LIBERO-Long (CaP baselines ≤4% on long-horizon). Rejection-sampled fine-tuning distills GPT-5.6 ReAct decisions into an 8B open model.  
  <sub>**Model:** GPT-5.6 (teacher), Qwen3-VL-8B-Instruct (distilled) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Coding moved offline into evolution; at deployment a ReAct loop calls frozen typed Policy APIs · **Eval:** sim · **Judged by:** benchmark checkers · **Speed/cost:** 13.2× per-decision speedup after distillation; physical calls 16 → 4</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="efficient-vla-survey"></a>
- **[A Survey on Efficient Vision-Language-Action Models](https://arxiv.org/abs/2510.24795)**
  — · *Survey* · 2025-10-27 · `📄 peer-reviewed` · 🏷️ IEEE TPAMI  
  [[Paper](https://arxiv.org/abs/2510.24795)]  
  Catalogs asynchronous decoupling (Fast ECoT, SmolVLA) and other speed techniques. These are the toolbox for closing the frontier-model latency gap.  
  <sub>↪ also in: [Surveys, Essays & Perspectives](#perspectives)</sub>

**Cross-listed here:**

- ↪ **[Next-Manip](#next-manip)**: Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[ACAP](#acap)**: ACAP: Asynchronous Coding Agents for Efficient Robot Control <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[RoboUniverse-10K](#robouniverse-10k)**: RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[JiL (Judgment-in-the-Loop)](#jil-wam-calibration)**: Calibrating World Action Models: From Adaptive System 2 Takeover to Self-Evolution <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[TRIP (Tripwire)](#trip-tripwire)**: Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[RoC](#reasoning-on-call)**: Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[RoboTeam](#roboteam)**: RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[ScaleVLA](#scalevla)**: ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters <sub>(listed under [The Incumbent: Dual-System VLAs](#dual-system))</sub>
- ↪ **[DASH](#dash)**: Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation <sub>(listed under [The Incumbent: Dual-System VLAs](#dual-system))</sub>
- ↪ **[Show-Harness](#show-harness)**: Show-Harness: Just a VLM Agent Can Play Robots <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[τ0-VLA](#tau0-vla)**: τ0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation <sub>(listed under [The Incumbent: Dual-System VLAs](#dual-system))</sub>
- ↪ **[Dual-Process Atomic Skills](#dual-process-atomic)**: Dual-Process Atomic Skill Learning: Decoupling Semantic Reasoning and Real-Time Control <sub>(listed under [The Incumbent: Dual-System VLAs](#dual-system))</sub>
- ↪ **[SPARK](#spark-bt)**: Sequential Planning via Anchored Robotic Keypoints <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[ENPIRE](#enpire)**: ENPIRE: Agentic Robot Policy Self-Improvement in the Real World <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>

</details>

<a id="dual-system"></a>
## 🧠 The Incumbent: Dual-System VLAs

*The architecture being challenged. A VLM 'System 2' fused with a fast learned 'System 1' action module, plus the work on how training one damages the other.*

<details open><summary><b>17 entries</b> + 3 cross-listed</summary>

<a id="scalevla"></a>
- **[ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://arxiv.org/abs/2611.21607)**
  Tsinghua · PKU · SJTU · Galbot · *Report* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.21607)] [[Project](https://galaxygeneralrobotics.github.io/scalevla/)]  
  Puts a frontier LLM inside a VLA instead of using it as an agent, framed against GPT-6 Astra control being 'slow and costly'. 'LIBERO-PRO success reaches 45.1%, compared with at most 31.3% for smaller backbones'; real charger insertion improves 'from 4/10 to 9/10'.  
  <sub>**Model:** DeepSeek-V4.1-Flash-1017 (frozen backbone) · **Below it:** jointly trained · **Interface:** Frozen 552B DeepSeek-V4.1-Flash vision-language backbone feeds a trainable action DiT that emits action chunks · **Eval:** sim+real · **Judged by:** simulator checker (LIBERO / LIBERO-PRO); human (real) · **Trials:** LIBERO-PRO: 500 episodes per setting; real: 10 in-domain + 15 OOD · **Speed/cost:** 216 ms median per action chunk on four H200 GPUs; 384 ms median round trip on the real robot</sub>  
  ⚠️ <sub>Trained VLA, not frontier-model control; needs four H200s for inference. No head-to-head with an agentic frontier model on the same tasks.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="dash"></a>
- **[Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation](https://arxiv.org/abs/2611.11854)**
  — · *Paper* · 2026-11-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.11854)]  
  Makes the control rate independent of backbone size, which is exactly what a much larger (frontier-scale) System 2 would need. Training deliberately exposes System 1 to stale System 2 output. Higher success than the synchronous pipeline at every size and on a real dexterous humanoid.  
  <sub>**Model:** 0.8B–8B VLM backbones (frozen) · **Below it:** jointly trained · **Interface:** System 2 VLM and System 1 flow-matching head as concurrent processes over LCM; System 1 fuses stale semantics with fresh vision from its own encoder · **Eval:** sim+real · **Speed/cost:** holds 20 Hz from 0.8B to 8B backbones (synchronous: 9.7 → 4.1 Hz)</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="tau0-vla"></a>
- **[τ0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885)**
  — · *Paper* · 2026-08-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2608.16885)]  
  A reference design for asynchronous serving: a slow planner never blocks the control loop.  
  <sub>**Below it:** jointly trained · **Interface:** Background worker refreshes the subtask about once per second; the control loop reads the cached subtask · **Speed/cost:** planner ≈1 Hz; control ≈30 Hz action chunks</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="representation-anchoring"></a>
- **[Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429)**
  — · *Paper* · 2026-07-15 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.13429)]  
  Another fix for VLM forgetting during VLA fine-tuning.  
  <sub>**Below it:** jointly trained · **Interface:** Distills hidden states from a frozen VLM copy into the trainable backbone</sub>  

<a id="dual-process-atomic"></a>
- **[Dual-Process Atomic Skill Learning: Decoupling Semantic Reasoning and Real-Time Control](https://arxiv.org/abs/2607.10625)**
  — · *Paper* · 2026-07-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.10625)]  
  Asynchronous slow-planner / fast-executor in a unified model.  
  <sub>**Below it:** jointly trained · **Interface:** Slow planner and fast executor inside one model, run asynchronously</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="loho-manip"></a>
- **[Long-Horizon Manipulation via Trace-Conditioned VLA Planning](https://arxiv.org/abs/2604.21924)**
  — · *Paper* · 2026-04-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2604.21924)]  
  Hierarchical planner over a trace-conditioned VLA.  
  <sub>**Below it:** jointly trained · **Interface:** Task-manager VLM issues a subtask and visual trace once every 100 executor steps</sub>  

<a id="twinbrainvla"></a>
- **[TwinBrainVLA: Unleashing the Potential of Generalist VLMs for Embodied Tasks via Asymmetric Mixture-of-Transformers](https://arxiv.org/abs/2601.14133)**
  — · *Paper* · 2026-01-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2601.14133)]  
  Keeps the generalist VLM frozen to protect its semantics while a second branch learns action.  
  <sub>**Below it:** jointly trained · **Interface:** A frozen generalist 'left brain' preserved next to a trainable embodied branch</sub>  

<a id="actions-as-language"></a>
- **[Actions as Language: Fine-Tuning VLMs into VLAs Without Catastrophic Forgetting](https://arxiv.org/abs/2509.22195)**
  — · *Paper* · 2025-09-26 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2509.22195)]  
  Attributes forgetting to distribution mismatch and avoids it by expressing actions as language, with no need for internet-scale co-training.  
  <sub>**Below it:** jointly trained · **Interface:** Low-level actions expressed in natural language</sub>  

<a id="instructvla"></a>
- **[InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation](https://arxiv.org/abs/2507.17520)**
  — · *Paper* · 2025-07-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2507.17520)]  
  VL instruction tuning to keep understanding while learning manipulation.  
  <sub>**Below it:** jointly trained</sub>  

<a id="rationalvla"></a>
- **[RationalVLA: A Rational Vision-Language-Action Model with Dual System](https://arxiv.org/abs/2506.10826)**
  — · *Paper* · 2025-06-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2506.10826)]  
  Dual-system VLA variant.  
  <sub>**Below it:** jointly trained</sub>  

<a id="fast-in-slow"></a>
- **[Fast-in-Slow: A Dual-System Foundation Model Unifying Fast Manipulation within Slow Reasoning](https://arxiv.org/abs/2506.01953)**
  — · *Paper* · 2025-06-02 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2506.01953)] [[Project](https://fast-in-slow.github.io/)]  
  Puts System 1 inside the VLM instead of in a separate head.  
  <sub>**Model:** Prismatic / LLaMA2-7B · **Below it:** jointly trained · **Interface:** System 1 is the final transformer blocks of the same VLM · **Eval:** sim+real · **Speed/cost:** 117.7 Hz control; best System 2 : System 1 ratio 1:4</sub>  

<a id="knowledge-insulation"></a>
- **[Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better](https://arxiv.org/abs/2505.23705)**
  Physical Intelligence · *Paper* · 2025-05-29 · `📄 peer-reviewed` · 🏷️ NeurIPS 2025  
  [[Paper](https://arxiv.org/abs/2505.23705)]  
  Shows that action-expert gradients damage the VLM backbone. Key evidence that fusing System 1 into System 2 has a cost, which is the reverse of 'the LLM overwhelms System 1'.  
  <sub>**Below it:** jointly trained · **Interface:** Stop-gradient from the continuous action expert into the VLM; the backbone trains on discretized-action tokens plus VL data</sub>  

<a id="pi05"></a>
- **[π0.5: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)**
  Physical Intelligence · *Paper* · 2025-04-22 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2504.16054)] [[Post](https://physicalintelligence.company/blog/pi05)]  
  Co-trained on heterogeneous robot, web, and high-level semantic data. It is the most common VLA baseline in the agentic-policy papers above.  
  <sub>**Below it:** jointly trained · **Interface:** One model predicts a language subtask, then an action chunk conditioned on it · **Eval:** real · **Speed/cost:** 46.96 ms per call (as measured in Astranomy)</sub>  

<a id="gemini-robotics-1"></a>
- **[Gemini Robotics: Bringing AI into the Physical World](https://arxiv.org/abs/2503.20020)**
  Google DeepMind · *Paper* · 2025-03-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2503.20020)]  
  The first Gemini Robotics VLA and embodied-reasoning model release.  
  <sub>**Model:** Gemini Robotics, Gemini Robotics-ER · **Below it:** jointly trained · **Eval:** real</sub>  

<a id="gr00t-n1"></a>
- **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)**
  NVIDIA · *Paper* · 2025-03-18 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2503.14734)]  
  Open-weight dual-system humanoid foundation model.  
  <sub>**Model:** 1.34B VLM + diffusion-transformer action module (2.2B total) · **Below it:** jointly trained · **Interface:** VLM latent features feed a flow-matching DiT action head · **Eval:** sim+real · **Speed/cost:** VLM ≈10 Hz, action module ≈120 Hz</sub>  

<a id="hi-robot"></a>
- **[Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417)**
  Physical Intelligence · *Paper* · 2025-02-26 · `📄 peer-reviewed` · 🏷️ ICML 2025  
  [[Paper](https://arxiv.org/abs/2502.19417)] [[Post](https://www.pi.website/research/hirobot)]  
  Hierarchical VLA with a language interface between the reasoning and action levels.  
  <sub>**Below it:** jointly trained · **Interface:** High-level VLM emits language commands to a low-level VLA · **Eval:** real</sub>  

<a id="helix"></a>
- **[Helix: A Vision-Language-Action Model for Generalist Humanoid Control](https://www.figure.ai/news/helix)**
  Figure AI · *Blog* · 2025-02-20 · `💬 post only`  
  [[Post](https://www.figure.ai/news/helix)]  
  The canonical System 1 / System 2 split in production: a slow onboard VLM writes a latent that a 200 Hz visuomotor policy consumes asynchronously.  
  <sub>**Model:** 7B VLM (S2), 80M transformer (S1) · **Below it:** jointly trained · **Interface:** S2 compresses its understanding into a single latent vector, projected into S1's token space; trained end to end · **Eval:** real · **Speed/cost:** S2 7–9 Hz, S1 200 Hz, each on its own onboard embedded GPU</sub>  

**Cross-listed here:**

- ↪ **[JiL (Judgment-in-the-Loop)](#jil-wam-calibration)**: Calibrating World Action Models: From Adaptive System 2 Takeover to Self-Evolution <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[Gemini Robotics 2](#gemini-robotics-2)**: Gemini Robotics 2 brings whole-body intelligence to robots <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[Gemini Robotics 1.5](#gemini-robotics-1-5)**: Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>

</details>

<a id="benchmarks"></a>
## 📊 Benchmarks & Evaluation Reports

*Shared yardsticks where frontier models and learned policies are scored on the same tasks.*

<details open><summary><b>24 entries</b> + 11 cross-listed</summary>

<a id="aa-robotics-sim"></a>
- **[Can language models drive a humanoid robot? Introducing AA-Robotics-Sim v0.1](https://artificialanalysis.ai/articles/aa-robotics-sim)**
  Artificial Analysis · *Benchmark* · 2026-11-25 · `💬 post only`  
  [[Post](https://artificialanalysis.ai/articles/aa-robotics-sim)]  
  Independent simulated-humanoid benchmark in which frontier models in a coding-agent harness control a Unitree G1 over a learned whole-body controller across embodied reasoning, pick and place, assembly/tool use and mobility. Overall scores: GPT-6.2 Astra 71.0, Claude Fable 5.2 57.5, GPT-6.2 Sol 53.7.  
  <sub>**Eval:** sim · **Judged by:** per-task scoring scripts on simulator physics measurements, 0–100 with partial credit (Artificial Analysis) · **Trials:** 10 tasks; 5 practice episodes then 10 evaluation episodes on new scenes per task · **Speed/cost:** GPT-6.2 Sol 17.3 min per evaluation episode (fastest); Gemini 4 Argon 39 min (slowest); per evaluation episode: GPT-6.2 Sol $0.98, GPT-6.2 Astra $3.90, Claude Opus 5.5 $4.62, Claude Fable 5.2 $9.01</sub>  
  ⚠️ <sub>'research preview'; simulation only; 'Practice ran on an earlier version of the environment and is scored with the current scoring rules'; 'there is no LiDAR and no stereo pair'. Pick and place is the weakest group for every model, mainly because secure grasps with the three-fingered hands are hard. No VLA baseline. Effort settings not stated.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="iclworld"></a>
- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649)**
  Tsinghua University · *Paper* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32649)] [[Project](https://iclworld.github.io)] [[Code](https://github.com/ICLWorld/ICLWorld)] [[Data](https://huggingface.co/datasets/Aoraku/ICLWorld)] ![stars](https://img.shields.io/github/stars/ICLWorld/ICLWorld?style=flat-square&label=%E2%98%85)  
  Benchmark of in-context rule learning across computer use and robot use through one harness. 'Claude Opus 5.5 and GPT-6 Astra, succeed on 82% and 76% of computer-use runs but only 27% and 26% of robot-use runs, and a no-rule control reduces success to at most 8%'. GPT-6 Astra 'answers 98% of robot rule questions correctly yet completes only 20% of these tasks'.  
  <sub>**Eval:** sim · **Judged by:** per-task programmatic verifier reading simulator state (hidden from the agent) · **Trials:** 160 tasks (110 computer use, 50 robot) with three rule versions, given as text or video; runs per task not stated</sub>  
  ⚠️ <sub>Authors: 'Hand-built environments limit ICLWorld to 160 tasks, ablations use three models, robot tasks run in simulation, and no task yet combines computer and robot use.' The simulation pauses between action batches. Robots are driven through teleoperator-style panel buttons with IK, not skills or code, so robot scores reflect this low-level interface. Each model keeps its own agent CLI, so harnesses differ.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="roboclock"></a>
- **[Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence](https://arxiv.org/abs/2611.32233)**
  University of California, San Diego · *Benchmark* · 2026-11-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.32233)]  
  60 time-constrained manipulation tasks (Temporal Window, Event-Reactive, Throughput) scored with inference paused (TSR) and with latency charged to the clock (LTSR). Zero-shot, 'Gemini 4 Argon achieves 24.5% PSR and 18.2% TSR through Tool-augmented EEF, while GPT-6 Astra reaches 22.8% and 19.0%', but 'with inference latency included, Gemini and GPT-6 Astra fall to 8.2% and 3.0% LTSR, GPT-6.1 Sol and Claude Opus 5.5 to 2.3% and 1.0%'. The fine-tuned π0.5 keeps '8.3% LTSR against 10.3% TSR' and is the best method overall, but fine-tuned policies barely transfer to the 15 held-out tasks.  
  <sub>**Eval:** sim+real · **Judged by:** simulator task evaluator (physical and temporal clauses); real pilot: operator scores each episode with a step rubric · **Trials:** 60 tasks × 10 seeds per model at easy level (Isaac Sim); real-robot pilot on an xArm 6: 10 episodes per task, 360 in total · **Speed/cost:** real pilot: 'The median model reply takes 5.1 s, from 3.4 s for Qwen3.8 27B to 16.8 s for DeepSeek V4.1 Flash'; API cost per episode (zero latency): Gemini 4 Argon $0.35, Claude Opus 5.5 $0.57, GPT-6 Astra $1.58, GPT-6.1 Sol $0.24</sub>  
  ⚠️ <sub>Authors: 'Our evaluation uses simulation with simplified processes and some compressed time scales, so transfer to physical robots remains to be validated. LTSR also depends on inference hardware and serving conditions.' VLMs run with low thinking mode; proprietary models are charged their API latency, open-weight models run on eight A100s, and LTSR changes with API serving speed (App. F.1). The real-robot pilot is described by the authors as descriptive only.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="robolivemem"></a>
- **[RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?](https://arxiv.org/abs/2611.30047)**
  Tulane; CMU; Amazon; UCSD; MIT · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.30047)] [[Project](https://robolivemem.github.io/)]  
  Runs 29 robot-memory task families (16 BEHAVIOR-1K scenes, a MuJoCo kitchen, ManiSkill/RoboMME tasks) twice: with the simulator paused while the model thinks, as earlier memory benchmarks do, and with the world running. 'when a remembered object changes in a realistic scene, the 8 Claude and GPT models succeed in 97% of episodes on average with the world paused, but in only 50% with the world running', and rankings change: 'Claude Opus 5.5, which never fails when paused, succeeds in 44%'. 'models given only 2 s per decision still fall at least 36 points below their paused success'; most failures are actions on camera frames from before the change ended, and looking again just before acting closes most of the realistic gap.  
  <sub>**Eval:** sim · **Judged by:** simulator final-state check (privileged log); a scripted privileged policy validates every seed · **Trials:** 34,176 episodes over 16 models; each instance run once per condition (paused, live, visible-twin live) · **Speed/cost:** median 1.9–4.6 s per decision for the Claude/GPT models on the realistic tier; Gemini 4 Argon and Carbon '32 and 56 s per decision in our own agent'</sub>  
  ⚠️ <sub>Authors: 'All scenes are simulated, other actors follow scripts, the people in the realistic tier have no articulated arms, and latency depends on the load of public model services. Realistic-tier results should be compared within models that run in the same kind of agent.' Claude/GPT run in Claude Code/Codex while other models run in the authors' own agent, so harnesses differ; effort settings differ by model. Skills act on numbered marks, so there is no low-level control. On repeated swaps of identical objects all nine models tested still lose points to memory.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="worldleague"></a>
- **[WorldLeague: Benchmarking Physical Agency](https://arxiv.org/abs/2611.30989)**
  xML Lab, National University of Singapore · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.30989)]  
  60 simulated mobile-manipulation tasks scoring 13 VLMs, VLAs and WAMs on the same physical goals, each through its own interface. 'Claude Fable 5.2 achieves 13 of the 60 goals and earns the highest mean Interactive Score (28.58/100)', ahead of GPT-6.1-Sol (22.28) and GPT-6-Astra (20.06); the best learned policy, GR00T-N1.5, scores 8.79. 'Even when VLMs answer every final question correctly, they receive an Interactive Score of zero in 71.8% of those episodes.'  
  <sub>**Eval:** sim · **Judged by:** evaluator physical predicates on the timestamped trajectory (Interactive Score for partial progress, physical success for full goal) · **Trials:** one episode per system per task at seed 0 (60 tasks for VLMs, 59 for VLA/WAMs); full suite repeated with GPT-6.1-Sol at seed 1 · **Speed/cost:** mean 40.80–171.58 min per task for frontier VLMs; world time keeps advancing during inference; API cost per task: Fable 5.2 $26.92, GPT-6-Astra $23.15, GPT-6.1-Sol $5.00</sub>  
  ⚠️ <sub>One episode per system and task; Sol's score 'changes on 11 of 60 tasks' between seeds. VLMs and VLA/WAMs run on different robots and interfaces, so the VLM–VLA gap mixes embodiment and interface with model ('Tying these goals to a single control interface limits which AI systems can be compared'). Every system scores zero on 27 of the 59 common tasks.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="ruibench"></a>
- **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115)**
  Show Lab, National University of Singapore · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31115)] [[Project](https://showlab.github.io/RUIBench)]  
  Controlled study of the interface between a frontier agent and a robot on 30 manipulation tasks. 'changing only the RUI shifts a frontier agent's success rate from 45% to 81%, and that of a fine-tuned 4B model from 13% to 47%', far more than the 2.1-point gap between the two frontier agents averaged across RUIs (Claude Code 70.1%, Codex 72.2%). Interfaces that win in sim do not all transfer to the real robot. Agents often 'declare success despite observable failures'.  
  <sub>**Eval:** sim+real · **Judged by:** independent offline scorer on logged trajectories, withheld from the agent (sim); human operator (real) · **Trials:** sim: 30 tasks × 13 RUIs × 5 test missions = 1,950 episodes per frontier agent; real: 650 episodes on a Franka Research 3 · **Speed/cost:** sim charges a fixed 8 s per model response; 30 min limit per episode; mean API cost $0.69–$2.37 per episode across RUIs</sub>  
  ⚠️ <sub>Authors: 'Extending the real-robot study beyond five tasks on one arm would test how widely the observed interface shifts hold'; 'Contact-rich and time-critical tasks remain difficult across nearly all RUIs'; 'Closing the verification gap further requires task-level verifiers'. Only 5 test missions per task-RUI cell in sim; sim latency is a fixed 8 s rather than true model latency; real-robot grader blinding not stated. No VLA baseline.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="robouniverse-10k"></a>
- **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002)**
  Tsinghua University; Einsia.AI; Peking University; UIUC; HKU; UCL; UNC-Chapel Hill · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31002)] [[Project](https://lab.einsia.ai/robo-universe/)] [[Code](https://github.com/Einsia/RoboUniverse-10K)] [[Data](https://huggingface.co/datasets/Einsia/RoboUniverse-10K)] ![stars](https://img.shields.io/github/stars/Einsia/RoboUniverse-10K?style=flat-square&label=%E2%98%85)  
  10,807 verifiable Isaac Sim environments built by an automated Real2Sim pipeline from real robot videos, with 500 held-out expert-verified tasks as RoboUniverse-Verified. 'GPT-6.2 Astra and Claude Opus 5.5 achieve overall success rates of 85.8% and 76.8%, GPT-6 Astra and GPT-6.1 Sol reach 54.6% and 49.4%'; open baselines reach 2.6% to 10.0%. SFT of Qwen3.6-35B-A3B on ~17K GPT-6 Astra trajectories lifts it 'from 0.8% to 21.2%'.  
  <sub>**Eval:** sim+real · **Judged by:** hidden task-specific verifier on final simulator state; the 500 test tasks manually verified by human experts · **Trials:** RoboUniverse-Verified: 500 held-out tasks (200 single-arm, 300 dual-arm), one attempt per task per model; real: one qualitative Franka demo · **Speed/cost:** simulation paused during model inference; SFT used 'approximately 1,500 equivalent NVIDIA H100 GPU hours'</sub>  
  ⚠️ <sub>Authors: 'the reconstructed simulation scenes remain relatively simplified, and the dynamics of complex objects are not yet faithfully captured', and the collection 'currently focuses on short, atomic manipulation skills'. Simulation time advances only during step calls (paused during inference). GPT models run in Codex and others in Claude Code, so harness and model are confounded. Environments and verifiers are agent-built; test tasks come from the same pipeline as training data. Real-robot evidence is a single qualitative demo.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Making It Fast & Cheap](#fast)</sub>

<a id="codex-vs-inspect-robots"></a>
- **[Why is Astra better on Codex for robotics?](https://robocurve.org/blog/codex-vs-inspect-robots/)**
  Robocurve · *Blog* · 2026-11-22 · `💬 post only`  
  [[Post](https://robocurve.org/blog/codex-vs-inspect-robots/)] [[Data](https://x.com/robocurve/status/2125028977194786857)]  
  GPT-6.2 Astra scores 97% on RoboDojo-RC Tier 1 through Codex vs 66% through Robocurve's own Inspect Robots harness, 'the highest among anything we've tested'. On the hardest task, capping a pen, Codex succeeds in 60% of 20 trials, 'double Gemini 4 Neon on Antigravity'; no robot model capped it once. Ablation on Stand Up Bottles: Inspect Robots at 40 calls 0.48, at 200 calls 0.745 ($164.34/trial), and with Codex's tools ported in plus multi-action turns (IR+) 1.00, matching Codex. The authors' leading explanation: the model writing its own tools, most likely because it can issue several moves per turn.  
  <sub>**Eval:** real · **Judged by:** Robocurve · **Trials:** 120 real attempts (Tier 1); harness ablation on Stand Up Bottles with 10–20 trials per arm · **Speed/cost:** Stand Up Bottles median 3.8 min (Codex) vs 16.6 min (Inspect Robots, 200 calls); $9.46 per Tier 1 attempt on Codex vs $0.15 for Dream-1 ('63x cheaper'); Ultrafast pricing</sub>  
  ⚠️ <sub>Authors: why Codex works better is 'somewhat mysterious' and the key component is 'an open question'; Codex's tool behaviour is described 'to our understanding'; the move_to replication was checked only in perfect simulation. The experiments raised the call cap from 40 to 200, and the leaderboard's 65.7% row used the 40-call release. Robocurve is retiring RoboDojo from future evaluations.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="robocoliseum"></a>
- **[RoboColiseum: Co-evolution of Simulation, Evaluation, and Models](https://arxiv.org/abs/2611.27042)**
  — · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27042)] [[Project](https://robocoliseum.ai/leaderboard?season=season2&model_type=all&metric=overall)]  
  Sim platform with Real2Sim calibration (Pearson 0.9686 over 22 paired real–sim configurations) and an 8-track benchmark. Season II reports eight frontier-LLM Agent systems and three VLAs on the same four tracks (precision, cross-embodiment, whole-body, dexterous) but on separate leaderboards: Claude Fable 5.2 leads Agents with Overall 18.30 (precision 33.04); π0.5 leads VLAs with Overall 11.22. Agent dexterous scores 'remain low, spanning 0.00–5.19'.  
  <sub>**Eval:** sim · **Judged by:** RoboColiseum test server (official fixed hidden set; budget-aware progress + completion score), plus human review for privileged-information exploits · **Trials:** VLA: 50 robot–task configurations, 255 valid episodes per policy; Agent per-case denominators and inference-call counts not reported</sub>  
  ⚠️ <sub>Authors: 'differences in training, task coverage, and resource accounting prevent a controlled comparison of Agent and VLA paradigms.' 'Public benchmark aggregates do not supply full per-case denominators, inference-call counts, or independent-repeat uncertainty.' 'Gemini’s dexterous sub-suite aggregation remains unresolved.' Agent and VLA/WAM categories are kept on separate leaderboards; the VLA dexterous suite has ten configurations (it is not stated that agents ran the same ten). Scores are reproduced from the public leaderboard, not new runs. Agent harness is Agent2Act (arXiv 2610.27865).</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="rosworld"></a>
- **[ROSWORLD: When Digital Task Competence Meets Physical Execution](https://arxiv.org/abs/2611.27467)**
  UTokyo, JD.COM, PKU, SII, FDU, HKU, THU · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27467)]  
  Couples an Isaac Sim robot workstation to a live OSWorld desktop so the same model does the same 40 tasks by software input and by physically pressing keys and the mouse, under the same official evaluators. 'Models that complete 31-39 tasks on the desktop complete at most 23 with the probe and 28 with the hands': GPT-6 Astra 39 → 23 (probe) / 28 (hands), GPT-6.1 Sol 39 → 15/16, Claude Opus 5.5 39 → 11/3, Kimi K3 and GLM-5.3-Flash 0.  
  <sub>**Eval:** sim · **Judged by:** OSWorld official application-state evaluators · **Trials:** 40 tasks × 5 models × 3 conditions (OSWorld, probe, hands), one run each (400 physical episodes); up to 100 model decisions per episode · **Speed/cost:** 'With API-served models, a 100-step physical episode takes 2–5 hours of wall-clock time, most of it model inference.' Physics pauses during model inference.; 400 physical episodes 'occupied 16 RTX 5090 GPUs for about two days'</sub>  
  ⚠️ <sub>No separate limitations section. Physics pauses during model inference; one run per model–task–condition; key coordinates, device poses and direct GUI actions are not given to the policy. Authors: 'Misses are the largest failure for every model (27–70% of attempts)' and 'even the strongest models stall on repeated, unverified retries.' Of 304 failed episodes, 239 exhaust the 100-step budget.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="gamma-scape"></a>
- **[$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence](https://arxiv.org/abs/2611.27306)**
  TeleAI (China Telecom), SJTU, CMU, Univ. of Manchester, Gamma Robotics · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27306)]  
  Isaac-Sim-based world (370 scenes, 11,073 object assets) with a 22-family, 220-instance mobile-manipulation suite. Three GPT-6-Astra agentic systems and OWMM-Agent are scored: 'RAX achieves the highest overall success (21.8%) and mean semantic progress (39.1%), followed by ASPIRE (15.5% / 34.5%), CaP-X (10.0% / 23.2%), and OWMM-Agent (4.1% / 12.2%).' Also demos contact collection and trace-informed program revision with Codex CLI + GPT-6-Astra.  
  <sub>**Eval:** sim · **Judged by:** BenchForge goal evaluators (final-state and process predicates); semantic progress from evaluator records · **Trials:** 220 instances (22 families × 10); three valid trials per system–task pair, best-of-three reported</sub>  
  ⚠️ <sub>No separate limitations section. Best-of-three trials ('selecting one valid trial by success first and semantic progress second'); invalid runs replaced; 'Physics pauses during inference'; system-specific clocks and turn limits; 'These results compare integrated systems, including their tools and budgets.' ASPIRE skill library and RAX exploration artifacts were built on development instances (RAX on same-family packages) and frozen before evaluation. Contact-collection case studies use 'privileged context'. 'Collision checking in RAX’s free-space arm tool is restricted to robot self-collision.'</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="mind2act-world"></a>
- **[Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444)**
  mmlab@SIGS · *Benchmark* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26444)] [[Code](https://github.com/Mind2Act/Mind2Act_World)] ![stars](https://img.shields.io/github/stars/Mind2Act/Mind2Act_World?style=flat-square&label=%E2%98%85)  
  Splits bimanual Isaac Sim tasks into Mind (history-based decisions), Act (precise timely execution) and Mind2Act (both, in closed loop). 'Even the strongest agent succeeds in 52.7% of Mind and 39.0% of Act episodes but in only 12.0% of Mind2Act episodes'; X-VLA 'reaches 19.6% on Act, the highest among end-to-end policies'.  
  <sub>**Eval:** sim · **Judged by:** evaluator reading simulator state hidden from the systems · **Trials:** 30 tasks × 3 levels × 2 scene settings; 900 episodes per agent · **Speed/cost:** GPT-6 Astra 11.0 s per call; X-VLA 153 ms; GPT-6 Astra USD 25.13 per episode vs USD 1.12–1.24 for Gemini-4-Argon / DeepSeek-V4.1-Flash</sub>  
  ⚠️ <sub>Authors: 'Simulation pauses during inference'; agents get an IK/motion-planning service and 'four times the physics budget of the end-to-end policies'; one fixed harness for all agents; sim only, one bimanual platform.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="roboteam"></a>
- **[RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time](https://arxiv.org/abs/2611.22138)**
  HKUST / Microsoft · *Benchmark* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.22138)]  
  Agents control 4 to 16 arms in real time from camera images only, with no ground-truth positions. With the adaptive system, gpt-6.1-sol and opus-5.5 complete 28 and 27 of 36 tasks and four other models at most 3, but a third of steps fail at least once and must be retried. Hierarchical/decentralized systems are faster but use up to 1.9× the tokens; 'no model or system is yet fast, cheap, and reliable at once'.  
  <sub>**Eval:** sim · **Judged by:** simulator checker on final state · **Trials:** 36 tasks (4 types × 3 team sizes × 3 levels), 4–16 arms, one run per condition · **Speed/cost:** median task takes gpt-6.1-sol 3.5 hours; 218 million input tokens per median task (gpt-6.1-sol)</sub>  
  ⚠️ <sub>Authors: simulation only; 36 tasks are variants of four task types; each condition ran once, 'so differences such as 28 versus 29 tasks are not reliable'. Benchmark and records to be released.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Making It Fast & Cheap](#fast)</sub>

<a id="claude-fable-5-2"></a>
- **[Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)**
  Anthropic · *Blog* · 2026-11-09 · `💬 post only`  
  [[Post](https://www.anthropic.com/claude-fable-and-mythos-5-2)]  
  A general-purpose launch post that reports robot control 'even for robotics tasks on which it has never explicitly been trained'. 'At Max effort, Fable 5.2 scores 64.9%, more than double GPT-6 Astra (29.8%) and Fable 5.1 (27.6%)'; Opus 5.5 39.4%, Gemini 4 Argon (High effort) 34.2%. Claims it beat 'most AI systems built specifically to control robots'.  
  <sub>**Eval:** sim · **Judged by:** RoboDojo Sim (Anthropic's internal runs)</sub>  
  ⚠️ <sub>Vendor post: 'Scores are based on our internal runs for each model using the highest available effort level'; harness, latency and trial counts not disclosed; competitor models run by Anthropic. Real-robot videos (puzzle cube, bottle cap, drawing) have no success rates.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="so101-bench"></a>
- **[SO-101 Bench: Accessible Spatial Manipulation](https://arxiv.org/abs/2610.36420)**
  Independent · *Benchmark* · 2026-10-27 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2610.36420)] [[Project](https://so101-bench.github.io/)] [[Code](https://github.com/5hadytru/so101_bench)] ![stars](https://img.shields.io/github/stars/5hadytru/so101_bench?style=flat-square&label=%E2%98%85)  
  Isaac Lab digital twin of a low-cost SO-101 arm whose ranking of five policies (four VLAs and an LLM agent) matches the real robot (Spearman rho = 1.00). Across nine VLAs and WAMs 'the best learned policies score near 61%', while 'GPT-6.1 Sol writing code in the PyRUA-Lean harness and handing grasps to Galaxea 0.5 scores 83.2' (DeepSeek V4.1 Flash-1017: 66.8). With the hand-off, GPT-6.1 Sol 'reaches 85% (51/60)', Gemini 4 Argon 77%, DeepSeek 65%, MiMo 55%.  
  <sub>**Eval:** sim+real · **Judged by:** simulator state (sim); operator under benchmark rules (real) · **Trials:** 916 evaluation episodes; 60 paired episodes per ablation; 45 real layouts · **Speed/cost:** median 197 s wall time to rollout stop for the agent (real)</sub>  
  ⚠️ <sub>The simulator pauses while the language model computes; simulation 'overestimates every policy's success by 9 to 31 percentage points'; learned policies share a fixed fine-tuning budget; one real environment; single arm, rigid objects.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated), [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="aa-robotics"></a>
- **[AA-Robotics (research preview)](https://artificialanalysis.ai/articles/aa-robotics)**
  Artificial Analysis · *Benchmark* · 2026-10-14 · `💬 post only`  
  [[Post](https://artificialanalysis.ai/articles/aa-robotics)] [[Data](https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol)]  
  Independent real-arm leaderboard. Scores out of 100: Astra 69.4, Sol 64.6, Argon 55.3, Opus 5.5 48.8, Fable 5.1 46.3. AA's 2026-11-17 article adds: 'GPT-6.2 Astra and GPT-6.2 Sol scored 79 and 78 respectively, ahead of Claude Fable 5.2 at 75'.  
  <sub>**Eval:** real · **Judged by:** human grader, partial credit · **Trials:** 8 tabletop tasks; trials per task not stated · **Speed/cost:** ≈30 min per task vs ≈20 s for a human; cheapest model ≈10× a human's hourly wage</sub>  
  ⚠️ <sub>No VLA baseline. The authors say frontier models are not yet suited to production robotics on their own.</sub>  

<a id="ladder"></a>
- **[LADDER: A Long-Horizon Robot Manipulation Benchmark](https://arxiv.org/abs/2610.18053)**
  INSAIT / NVIDIA · *Benchmark* · 2026-10-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.18053)] [[Project](https://ladder.insait.ai)]  
  Scales horizon from 1 to 10 subgoals in the same scene. The low-level policy alone hits 85.4% on single-subgoal tasks but 11.0% overall. GPT-Policy on GPT-6 Astra is best on every suite (62.0% overall), then PSP-Agent (40.1%), versus at most 29.6% for learned-policy orchestration.  
  <sub>**Eval:** sim+real · **Judged by:** programmatic per-subgoal state checks (sim) · **Trials:** 145 tasks, 3 suites, 2,024 simulated episodes per system; real: 12 episodes per task and system · **Speed/cost:** per episode: GPT-Policy $4.02 vs $0.007–$0.17 for the others</sub>  
  ⚠️ <sub>Authors: 'the simulation pauses while a system computes'; tool-selection systems get ground-truth depth and camera calibration in sim; 'High-level VLM inference is slow'. GPT-Policy was not run on the real robots. Tabletop pick-and-place only.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated), [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="robodojo-rc-tier1"></a>
- **[RoboDojo-RC Tier 1: real-world leaderboard of frontier models, agents and VLAs (Robocurve)](https://github.com/robocurve/inspect-robots)**
  Robocurve · *Benchmark* · 2026-09-23 · `💬 post only`  
  [[Code](https://github.com/robocurve/inspect-robots)] [[Post](https://robocurve.org/opus-5-5-robodojo-rc-tier-1/)] [[Data](https://robocurve.org/)] ![stars](https://img.shields.io/github/stars/robocurve/inspect-robots?style=flat-square&label=%E2%98%85)  
  Six adapted RoboDojo real-world tasks on bimanual I2RT YAM arms, with frontier LLMs, a full agent system and learned VLAs/WAMs scored on one rig. Leaderboard: Waddle-1 81.4%, GPT-6.2 Astra (high) 65.7%, Dream-1 59.5%, Fable 5.2 (high) 57.5%, Gemini 4 Carbon (high) 54.5% … MolmoAct2 19.5%, GR00T N1.7 9.5%. Also reports cost and wall-clock time per attempt. Later rows (leaderboard as of 2026-11-25): coding agents with no call cap score GPT-6.2 Astra on Codex 97.3%, Gemini 4 Neon on Antigravity 89.7% and Fable 5.2 on Claude Code 89.0%.  
  <sub>**Eval:** real · **Judged by:** human grader with a per-task progress rubric (not blinded) · **Trials:** 6 tasks × 20 trials = 120 attempts per configuration · **Speed/cost:** 0.8–32.1 min per attempt across systems; $0.05–$10.51 per attempt</sub>  
  ⚠️ <sub>Graders knew which model was running ('grading is open to unconscious bias'); tasks are 'the six easiest tasks with the highest scores' on GPT-6 Astra; objects reset by hand; not comparable with original RoboDojo. Call caps differ by system type. Robocurve announced on 2026-11-24 that it is retiring RoboDojo from future evaluations; harness matters as much as model (see Astra on Codex: 97% vs 65.7%).</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="robocurve-astra"></a>
- **[GPT-6 Astra vs Claude Fable 5 / 5.1 on bimanual YAM arms](https://github.com/robocurve/inspect-robots)**
  Robocurve · *Report* · 2026-09-04 · `💬 post only`  
  [[Code](https://github.com/robocurve/inspect-robots)] [[Post](https://openai.robocurve.org/gpt-6-astra/)] ![stars](https://img.shields.io/github/stars/robocurve/inspect-robots?style=flat-square&label=%E2%98%85)  
  Block-into-bowl: Astra 19/20, Fable 5.1 8/20, Fable 5 1/20. Puzzle-into-groove: Astra 2/20, Fable 5.1 2/20, Fable 5 0/20. Coarse placement is solved; precise insertion is not.  
  <sub>**Eval:** real · **Judged by:** operators (not blinded) · **Trials:** 20 per task · **Speed/cost:** ≈2.5 min/run (Astra, bowl task); $0.94–$1.36/run (Astra)</sub>  
  ⚠️ <sub>Different rigs and days across models; graders knew which model was running.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="robodojo"></a>
- **[RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](https://arxiv.org/abs/2607.04434)**
  — · *Benchmark* · 2026-07-05 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2607.04434)] [[Project](https://robodojo-benchmark.com/)]  
  42 sim + 18 real tasks across generalization, memory, precision, long horizon, and open-vocabulary instruction following. Public leaderboard on which LLM-as-policy entries now compete with VLAs.  
  <sub>**Eval:** sim+real · **Judged by:** checker (sim); real protocol · **Trials:** official 50 episodes per task</sub>  
  ⚠️ <sub>See the OpenRUA retest under Critiques: some leaderboard entries changed step limits or relied on the built-in success checker. Since the 2026-11-14 agent-track rules, the leaderboard stars agent entries (SOLVE, Q0-Preview, Agent-as-Policy, Mibot-RUA and others) whose harnesses inject task-specific guides, tolerances or scoring conditions beyond the official Detail Description.</sub>  

<a id="robolab"></a>
- **[RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860)**
  NVIDIA · *Benchmark* · 2026-04-10 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2604.09860)] [[Project](https://research.nvidia.com/labs/srl/projects/robolab/)] [[Code](https://github.com/NVLabs/RoboLab)] ![stars](https://img.shields.io/github/stars/NVLabs/RoboLab?style=flat-square&label=%E2%98%85)  
  High-fidelity simulation benchmark with human- and LLM-authored scenes. Its 120-task suite (RoboLab-120) is where AMP1 and Astranomy report head-to-head numbers against VLAs and WAMs.  
  <sub>**Eval:** sim · **Judged by:** task checkers</sub>  
  ⚠️ <sub>AMP1 reports that many RoboLab failures come from object geometry/mass defeating standard grasps or from a flaky verifier.</sub>  

<a id="eriq"></a>
- **[Unified Embodied VLM Reasoning with Robotic Action via Autoregressive Discretized Pre-training](https://arxiv.org/abs/2512.24125)**
  — · *Benchmark* · 2025-12-30 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2512.24125)]  
  Introduces ERIQ, 6K+ QA pairs separating embodied reasoning from motor control. Reports a strong correlation between embodied-reasoning score and end-to-end VLA generalization.  

<a id="butter-bench"></a>
- **[Butter-Bench: Evaluating LLM Controlled Robots for Practical Intelligence](https://arxiv.org/abs/2510.21860)**
  Andon Labs · *Benchmark* · 2025-10-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2510.21860)] [[Project](https://andonlabs.com/evals/butter-bench)]  
  Best LLM 40% vs mean human 95%. Weakest areas are multi-step spatial planning and social understanding. Embodied-reasoning fine-tuned LLMs did not improve.  
  <sub>**Eval:** real · **Judged by:** human</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques), [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="libero-pro"></a>
- **[LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization](https://arxiv.org/abs/2510.03827)**
  — · *Benchmark* · 2025-10-04 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2510.03827)] [[Code](https://github.com/Zxy-MLlab/LIBERO-PRO)] ![stars](https://img.shields.io/github/stars/Zxy-MLlab/LIBERO-PRO?style=flat-square&label=%E2%98%85)  
  Perturbed LIBERO built to defeat memorization. Agentic methods report large gains over VLAs here (CaP-X, OpenRUA, ASPIRE, RACaP, AMP1).  
  <sub>**Eval:** sim · **Judged by:** checker</sub>  
  ⚠️ <sub>Papers use different LIBERO-PRO conditions and subsets, so numbers are not always comparable.</sub>  

**Cross-listed here:**

- ↪ **[Mibot-RUA](#mibot-rua)**: Mibot-RUA (Mibot_RSI): RoboDojo agent-track entry <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[AgentRoboCritic](#agentrobocritic)**: AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[LEASH / RoboRisk](#leash-roborisk)**: LEASH: Stay Safe in Agentic Robotics <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[DiMuRe](#dimure)**: DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[Frontier models on LIBERO-10](#libero10-frontier)**: From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[Bitter Lesson → Robotics](#bitter-lesson-robotics)**: The Bitter Lesson Comes to Robotics <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[SEAR](#sear)**: SEAR: Self-Evolving Agentic Robotics <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[LLM as Policy on RoboDojo](#robodojo-astra)**: An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[CaP-X](#cap-x)**: CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[ALRM](#alrm)**: ALRM: Agentic LLM for Robotic Manipulation <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[RoboSpoof](#robospoof)**: You Can't See Everything: Perceptual Attacks on Embodied AI <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>

</details>

<a id="critiques"></a>
## 🔍 Analyses, Critiques & Reproducibility

*Negative results, retests, benchmark-integrity problems, and the limits authors admit about their own systems.*

<details open><summary><b>5 entries</b> + 14 cross-listed</summary>

<a id="agentrobocritic"></a>
- **[AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613)**
  CMU / UIUC / Bosch · *Paper* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26613)] [[Project](https://adu2021.github.io/blog/AgentRoboCritic/)]  
  Action-level analysis of GPT-6 Astra on direct robot control across 12 manipulation benchmarks. '49.8% of all successful episodes contain at least one local failure'; '38.9% of the analyzed failures are recovered within 10 actions and 57.7% by the end of the episode'. Grasp and Alignment are the bottlenecks, while Choice errors are 0.2% of failed actions. A fine-tuned Muse-Glimmer-30B critic's failure-mode accuracy rises from 32.58% to 74.24%.  
  <sub>**Eval:** sim+real · **Judged by:** each benchmark's official grader (episodes); GPT-6 Astra as critic (actions), checked on a 400-action human-annotated set · **Trials:** 12 benchmarks; 12,163 failed actions analysed; 12,844-action annotated dataset · **Speed/cost:** median decision 31.9 s for GPT-6 Astra vs 0.11 s for π0.5 (74 matched tasks)</sub>  
  ⚠️ <sub>Authors: agents 'struggle to resolve millimeter-scale mating tolerances and angular alignment from vision alone'; only about one in three Alignment and Effect failures are recovered. Same model serves as policy and critic (self-preference tested in an appendix). 5 of 12 benchmarks reuse released traces rather than new rollouts.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct), [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="openrua-retest"></a>
- **[OpenRUA team retest of RoboDojo leaderboard entries (Huxiu / AI Dancer report)](https://m.huxiu.com/article/4905567.html)**
  Huxiu (republished from AI Dancer) · *News* · 2026-11-14 · `🔁 secondary report`  
  [[Post](https://m.huxiu.com/article/4905567.html)]  
  Reports retests of Astra-based RoboDojo entries. RoboDawn raised the step cap to 10^9 (success falls 47.1% → 1.0% under the original limit). RoboICL drops 83.2 → 63.5 when the agent must declare 'done' itself instead of the built-in checker ending the episode. HexaShell's learned skill mostly memorized one task.  
  <sub>**Eval:** sim</sub>  
  ⚠️ <sub>Secondary Chinese-language report; find the primary OpenRUA retest before citing. Astranomy's numbers were not part of the retest.</sub>  

<a id="justrua"></a>
- **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)**
  — · *Paper* · 2026-11-11 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.16009)]  
  Takes apart why RoboDojo robot-use-agent scores rose so fast. Most of the gain comes from a lean harness with full episode history and early motion stops, plus scene geometry (even depth predicted from RGB). Experience reuse 'is not a free lunch'. With no learned policy, self-improvement, or task tuning: Score 29.7 → 50.3.  
  <sub>**Eval:** sim · **Judged by:** RoboDojo checker</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="leash-roborisk"></a>
- **[LEASH: Stay Safe in Agentic Robotics](https://arxiv.org/abs/2611.14115)**
  — · *Paper* · 2026-11-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.14115)]  
  RoboRisk benchmark covers task refusal, plan repair, execution-time hazards, injection, and sequential memory, all closed-loop. All six frontier models 'generally show high harm rates'. The LEASH harness cuts harm across all six while largely preserving task completion.  
  <sub>**Eval:** sim+real · **Trials:** 92 sim + 13 physical tasks</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="robospoof"></a>
- **[You Can't See Everything: Perceptual Attacks on Embodied AI](https://papers.robocurve.org/robospoof)**
  Robocurve; University of Southern California; UC Irvine · *Report* · 2026 · `💬 post only`  
  [[Paper](https://papers.robocurve.org/robospoof)] [[Post](https://robocurve.org/robospoof/)]  
  Tests whether frontier models driving a real robot in closed loop refuse unsafe tasks when camera footage is blurred or doctored. Models attempted unsafe tasks in 81/300 trials (27%) on unaltered footage, 263/300 (88%) with a Gaussian blur and 291/300 (97%) with frame-by-frame doctoring: 'models rarely refuse tasks unless visual observations provide positive evidence that the tasks are unsafe.'  
  <sub>**Eval:** real · **Judged by:** Claude Fable 5.1 classified each trial as attempt or refusal · **Trials:** 5 unsafe tasks (from RoboHarm) × 12 trials × 3 footage conditions per model; 900 trials</sub>  
  ⚠️ <sub>Refusal is judged by an LLM (Claude Fable 5.1); 12 trials per cell on one bench; an attempt counts as completed when the model calls done and 'we did not check the scene afterwards'. No date on the paper or page; per-model numbers only in a figure.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks), [Frontier Model as Direct Policy](#direct)</sub>

**Cross-listed here:**

- ↪ **[X-Harness](#x-harness)**: Toward Agentic Robotics: A Large-Scale Study of Harness Design for Robot-Use Agents <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[RoboClock](#roboclock)**: Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Embo-Harness](#embo-harness)**: Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[RoboLiveMem](#robolivemem)**: RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[RUIBench](#ruibench)**: RUIBench: What Makes a Good Robot-Use Interface? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Astra on Codex (Robocurve)](#codex-vs-inspect-robots)**: Why is Astra better on Codex for robotics? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Mind2Act World](#mind2act-world)**: Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[AMP1](#amp1)**: On Agentic Manipulation Policies <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[SEAR](#sear)**: SEAR: Self-Evolving Agentic Robotics <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[OpenRUA](#openrua)**: OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **['Astra is shockingly good at robotics'](#understanding-robots-astra)**: OpenAI's Astra model is shockingly good at robotics <sub>(listed under [Surveys, Essays & Perspectives](#perspectives))</sub>
- ↪ **[Claude on robotics](#anthropic-robotics)**: How Claude performs on robotics tasks <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[CaP-X](#cap-x)**: CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[Butter-Bench](#butter-bench)**: Butter-Bench: Evaluating LLM Controlled Robots for Practical Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>

</details>

<a id="perspectives"></a>
## 🗺️ Surveys, Essays & Perspectives

*Big-picture framing: where System 2 ends, what System 1 / System 0 becomes, and what it means for the field.*

<details open><summary><b>9 entries</b> + 1 cross-listed</summary>

<a id="vla-lifecycle-survey"></a>
- **[Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment](https://arxiv.org/abs/2611.18372)**
  — · *Survey* · 2026-11-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.18372)]  
  Covers hierarchical-VLA interfaces (latents vs subtask / 2D path / language) and multi-rate execution.  

<a id="envisioning-agentic-robotics"></a>
- **[Envisioning Agentic Robotics: A New Era of Robotic Systems](https://arxiv.org/abs/2611.18359)**
  Grid Robotics · *Survey* · 2026-11-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.18359)]  
  Position and roadmap paper. Argues that 'Embodied System 2' (a foundation model plus an embodied harness) is the decision core of agentic robotics. Proposes an evaluation framework covering both model capability and closed-loop system performance, plus a roadmap toward sustained autonomy.  

<a id="robonomics-astra"></a>
- **[Robotics' New Era After Astra](https://robonomics.substack.com/p/robotics-new-era-after-astra)**
  Robonomics (Substack) · *Essay* · 2026-11-01 · `💬 post only`  
  [[Post](https://robonomics.substack.com/p/robotics-new-era-after-astra)]  
  Working hypothesis: System 2 and much of System 1 merge into frontier models, while a small embodiment-specific 'System 0' reflex controller remains. Calls this robotics' 'GPT-3 moment' and doubts the value of standalone robot foundation models.  
  ⚠️ <sub>Industry commentary; partly relies on unverified sources.</sub>  

<a id="towards-agentic-robots"></a>
- **[Towards Agentic Robots: Model, Data, Environment, and Harness](https://arxiv.org/abs/2610.20442)**
  — · *Survey* · 2026-10-14 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.20442)] [[Code](https://github.com/chonghanqin/Awesome-Agentic-Robots)] ![stars](https://img.shields.io/github/stars/chonghanqin/Awesome-Agentic-Robots?style=flat-square&label=%E2%98%85)  
  Unified survey tracing the path from VLAs, world models, and WAMs to agentic robot systems.  

<a id="understanding-robots-astra"></a>
- **[OpenAI's Astra model is shockingly good at robotics](https://www.understandingrobots.org/p/openais-astra-model-is-shockingly)**
  Understanding Robots · *Essay* · 2026-10-01 · `💬 post only`  
  [[Post](https://www.understandingrobots.org/p/openais-astra-model-is-shockingly)]  
  Astra briefly topped RoboDojo but is too slow for most tasks. Expects LLMs to become high-level orchestrators rather than replace VLAs, because robots need onboard models and Astra lacks dexterity. Written before AMP1, which partly contests it.  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="planner-to-policy"></a>
- **[From Planner to Policy: a survey of large language models for robot control](https://tantansir.github.io/llm-for-robot-control/)**
  — · *Survey* · 2026-10 · `💻 code / results`  
  [[Project](https://tantansir.github.io/llm-for-robot-control/)] [[Code](https://github.com/tantansir/llm-for-robot-control)] ![stars](https://img.shields.io/github/stars/tantansir/llm-for-robot-control?style=flat-square&label=%E2%98%85)  
  Organizes ~220 systems by action interface: abstraction level, representation, composition operator, invocation timing. A useful taxonomy for the System 2 → System 1 contract.  
  ⚠️ <sub>No arXiv link yet; date taken from the repo creation month.</sub>  

<a id="showlab-survey"></a>
- **[Survey on Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use](https://figshare.com/articles/preprint/Survey_on_Multimodal_Embodied_Agents_A_Unified_Capability-centric_Perspective_from_Computer-Use_to_Robot-Use/33529048)**
  Show Lab, NUS · *Survey* · 2026-09-11 · `📝 preprint`  
  [[Paper](https://figshare.com/articles/preprint/Survey_on_Multimodal_Embodied_Agents_A_Unified_Capability-centric_Perspective_from_Computer-Use_to_Robot-Use/33529048)] [[Code](https://github.com/showlab/Awesome-Multimodal-Embodied-Agent)] ![stars](https://img.shields.io/github/stars/showlab/Awesome-Multimodal-Embodied-Agent?style=flat-square&label=%E2%98%85)  
  Asks what changes when a multimodal agent moves from computer-use to robot-use; organized around perceive, anticipate, plan, act, and verify.  

<a id="isola-rua"></a>
- **[Robot-Use Agents](https://web.mit.edu/phillipi/www/writing/robot-use-agents.html)**
  MIT · *Essay* · 2026-09-07 · `💬 post only`  
  [[Post](https://web.mit.edu/phillipi/www/writing/robot-use-agents.html)]  
  General agents as 'puppeteers' that use robots as tools through existing sensor/actuator interfaces, updated centrally, versus slowly engineered on-device policies. Concedes LLM-controlled robots are 'still far less performant than dedicated solutions'.  

<a id="unified-robot-learning"></a>
- **[Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models](https://arxiv.org/abs/2609.03927)**
  — · *Survey* · 2026-09-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.03927)]  
  Flags inference latency of large backbones generating subgoals as a bottleneck in hierarchical VLAs.  

**Cross-listed here:**

- ↪ **[Efficient VLA survey](#efficient-vla-survey)**: A Survey on Efficient Vision-Language-Action Models <sub>(listed under [Making It Fast & Cheap](#fast))</sub>

</details>

<a id="foundations"></a>
## 🏛️ Foundations (pre-2025)

*The LLM-as-planner and code-as-policy lineage this area grew from.*

<details open><summary><b>5 entries</b></summary>

<a id="voxposer"></a>
- **[VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](https://arxiv.org/abs/2307.05973)**
  Stanford · *Paper* · 2023-07-12 · `📄 peer-reviewed` · 🏷️ CoRL 2023  
  [[Paper](https://arxiv.org/abs/2307.05973)] [[Project](https://voxposer.github.io/)] [[Code](https://github.com/huangwl18/VoxPoser)] ![stars](https://img.shields.io/github/stars/huangwl18/VoxPoser?style=flat-square&label=%E2%98%85)  
  Zero-shot trajectory synthesis from LLM-composed value maps, with no learned System 1.  
  <sub>**Below it:** analytic (IK / waypoints / scripted) · **Interface:** LLM writes code that composes 3D value maps; a motion planner synthesizes trajectories · **Eval:** sim+real</sub>  

<a id="progprompt"></a>
- **[ProgPrompt: Generating Situated Robot Task Plans using Large Language Models](https://arxiv.org/abs/2209.11302)**
  — · *Paper* · 2022-09-22 · `📄 peer-reviewed` · 🏷️ ICRA 2023  
  [[Paper](https://arxiv.org/abs/2209.11302)]  
  Programmatic prompting for situated task plans.  
  <sub>**Below it:** analytic (IK / waypoints / scripted) · **Interface:** Program-like prompts listing available actions and objects · **Eval:** sim+real</sub>  

<a id="code-as-policies"></a>
- **[Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753)**
  Google · *Paper* · 2022-09-16 · `📄 peer-reviewed` · 🏷️ ICRA 2023  
  [[Paper](https://arxiv.org/abs/2209.07753)] [[Project](https://code-as-policies.github.io/)] [[Code](https://github.com/google-research/google-research/tree/master/code_as_policies)]  
  Direct ancestor of CaP-X, OpenRUA, and AMP1.  
  <sub>**Below it:** analytic (IK / waypoints / scripted) · **Interface:** LLM writes policy code over perception and control APIs · **Eval:** real</sub>  

<a id="inner-monologue"></a>
- **[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608)**
  Google · *Paper* · 2022-07-12 · `📄 peer-reviewed` · 🏷️ CoRL 2022  
  [[Paper](https://arxiv.org/abs/2207.05608)]  
  Closed-loop feedback for LLM planners, the ancestor of today's observe-and-repair agent loops.  
  <sub>**Below it:** frozen learned policy · **Interface:** Closed-loop language feedback (success detection, scene description) to an LLM planner · **Eval:** real</sub>  

<a id="saycan"></a>
- **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)**
  Google · *Paper* · 2022-04-04 · `📄 peer-reviewed` · 🏷️ CoRL 2022  
  [[Paper](https://arxiv.org/abs/2204.01691)]  
  The original 'LLM picks from a learned skill library' design.  
  <sub>**Model:** PaLM · **Below it:** frozen learned policy · **Interface:** LLM scores candidate skills; learned value functions ground feasibility · **Eval:** real</sub>  

</details>

## Legend

| Badge | Meaning |
|---|---|
| `📄 peer-reviewed` | Published at a peer-reviewed venue. |
| `📝 preprint` | arXiv / preprint only. |
| `💻 code / results` | Preprint or report **with** released code, data, or full results. |
| `💬 post only` | Blog, project page or report with no paper yet. |
| `🔁 secondary report` | Second-hand report; find and cite the primary source. |
| `⚠️ needs verification` | Not yet checked against the source by a maintainer. |

**Below it** says what the frontier model's output feeds into: `none`; `analytic` (IK, waypoint interpolation, scripted controllers); `frozen learned policy` (a VLA, WAM or whole-body tracker it steers but doesn't train); `jointly trained` (classic dual-system VLA); `trained by the agent` (the frontier model trains its own System 1).

## How this list is maintained

- **Data-first.** `README.md` is generated from [`data/entries.json`](data/entries.json), [`data/results.json`](data/results.json) and [`data/taxonomy.json`](data/taxonomy.json) by [`scripts/build_readme.py`](scripts/build_readme.py). Don't edit the README by hand.
- **Verified.** [`scripts/validate.py`](scripts/validate.py) checks the schema, checks every arXiv ID against the arXiv API title (`--arxiv`), and checks that links resolve (`--links`).
- **Daily, automated.** A scheduled Claude Code agent runs [`scripts/collect.py`](scripts/collect.py) (arXiv search, papers citing the anchor papers, new additions to the related lists, venue updates) and scans lab blogs and announcements, triages every candidate against the scope, edits the data, validates it, and pushes. Its instructions are in [MAINTAINING.md](MAINTAINING.md); every decision, including rejections, is recorded in [`data/seen.json`](data/seen.json) and [`data/changelog.json`](data/changelog.json). A GitHub Action re-validates every push and checks links daily. Spot an error? Open an issue; corrections win.
- **Editorial rules** (adapted from benchflow-ai/awesome-embodied-agents): numbers are quoted verbatim from the source; every result row says who measured it; sim vs real, trial counts and the success judge are recorded; authors' own stated limitations go in the caveats.

## Related lists

<sub>Stars and last push read from the GitHub API on 2026-11-27.</sub>

| List | ★ | Last push | Angle |
|---|---|---|---|
| [kairunwen/Awesome-Robot-Use-Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent) | 223 | 2026-11-26 | The largest robot-use-agent list: papers, projects, social demos, benchmarks, searchable site. |
| [visitworld123/Awesome-Robot-Use-Agent](https://github.com/visitworld123/Awesome-Robot-Use-Agent) | 109 | 2026-11-17 | Robot-use agents, a dual-system section, self-evolving agents, runtimes. |
| [zjwzcx/Awesome-Astra-Embodied-AI](https://github.com/zjwzcx/Awesome-Astra-Embodied-AI) | 1252 | 2026-10-28 | GPT-6 Astra only; mostly case-by-case demos (X / RedNote). |
| [showlab/Awesome-Multimodal-Embodied-Agent](https://github.com/showlab/Awesome-Multimodal-Embodied-Agent) | 296 | 2026-11-19 | Paper list behind Show Lab's computer-use → robot-use survey. |
| [benchflow-ai/awesome-embodied-agents](https://github.com/benchflow-ai/awesome-embodied-agents) | 7 | 2026-10-25 | Strong editorial rules (verbatim numbers, who judged success, trial counts). This list borrows them. |
| [w-xb/awesome-agentic-robotics](https://github.com/w-xb/awesome-agentic-robotics) | 33 | 2026-11-25 | Memory, planning, world models, verification, failure recovery. |
| [tantansir/llm-for-robot-control](https://github.com/tantansir/llm-for-robot-control) | 1 | 2026-10-07 | Survey catalog of ~220 systems organized by action interface. |
| [chonghanqin/Awesome-Agentic-Robots](https://github.com/chonghanqin/Awesome-Agentic-Robots) | 208 | 2026-11-26 | Companion list to the 'Towards Agentic Robots' survey. |
| [lysandre001/awesome-code-as-policy-Robot-learning](https://github.com/lysandre001/awesome-code-as-policy-Robot-learning) | 18 | 2026-06-24 | Short code-as-policy list (17 entries). |
| [GT-RIPL/Awesome-LLM-Robotics](https://github.com/GT-RIPL/Awesome-LLM-Robotics) | 4505 | 2026-10-29 | The classic broad LLM-for-robotics list. |
| [zchoi/Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) | 1927 | 2026-11-23 | Broad embodied AI with LLMs. |
| [SajjadPSavoji/awesome-weight-space-programming](https://github.com/SajjadPSavoji/awesome-weight-space-programming) | 8 | 2026-11-26 | Not robotics-specific; its data-driven, daily-rebuilt format inspired this list. |

## Contributing

Add or fix an entry in `data/entries.json` (and `data/results.json` for numbers), then run:

```bash
python3 scripts/validate.py --arxiv      # schema + arXiv title check
python3 scripts/build_readme.py          # regenerate README.md
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry schema and editorial rules.

## Citation

```bibtex
@misc{awesome_frontier_robot_policies,
  title  = {Awesome Frontier Models as Robot Policies},
  year   = {2026},
  note   = {https://github.com/liuxjerry/awesome-frontier-models-as-robot-policies}
}
```

License: [CC0 1.0](LICENSE). To the extent possible under law, the contributors have waived all copyright to this list.
