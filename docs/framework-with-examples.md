# Ethical Framework for AI-Assisted Research — Original Text with Examples

**How to read this document:** Each **Original point** is reproduced verbatim from the supplied text. The following **Illustrative example** is an addition intended to make the point concrete; it does not replace or amend the original. Examples are hypothetical. Statements about defensive mechanisms or “zero-deviation” are preserved as framework language, not independently validated technical guarantees.

## Framework principles

### 1
**Original point:** Ethical framework for AI research treats responsibility and rigor as co-requirements; rejects a speed-vs-ethics tradeoff.

**Illustrative example:** A team facing a deadline may shorten a report’s length, but should not skip checking sources or hide uncertainty to finish faster.

### 2
**Original point:** Accountability mechanisms: explicit documentation, claim labeling, and error handling to ensure transparent, auditable, reproducible research.

**Illustrative example:** A researcher saves the search terms and dates, labels a numerical result as an estimate, and records how a calculation error was found and corrected so another reviewer can repeat the steps.

### 3
**Original point:** Workflow structure defined before work begins: four blocks—philosophy, ideology, methodology, ethical language.

**Illustrative example:** Before examining a policy question, a team writes down its evidence standard (philosophy), governing principles (ideology), search and analysis plan (methodology), and plain-language and disclosure rules (ethical language).

### 4
**Original point:** Decision logs required for major steps: record rationale, alternatives, and risks to ensure traceability.

**Illustrative example:** A log entry says that the team included official guidance because it directly addressed the question, considered a secondary summary but excluded it as less direct, and noted the risk that the guidance might be outdated.

### 5
**Original point:** Active Error Handler halts progress if shortcuts or biases are detected; maintains integrity and transparency.

**Illustrative example:** If a reviewer notices that the analysis only includes evidence supporting the initial view, the workflow pauses, records the selection-bias concern, and resumes only after the search is broadened or the limitation is disclosed.

### 6
**Original point:** Claim labeling requirement: every claim labeled as Fact, Estimate, Interpretation, Hypothesis, or Recommendation.

**Illustrative example:** “The policy was issued in 2024” (**Fact**, if documented); “about one in five” (**Estimate**, with method stated); “the change may reflect a new priority” (**Interpretation**); “the change could reduce delays” (**Hypothesis**); “compare outcomes after six months” (**Recommendation**).

### 7
**Original point:** Source quality rubric: sources ranked by quality tiers; outputs include limitations summary and next steps.

**Illustrative example:** A project defines Tier 1 as primary policy or dataset, Tier 2 as peer-reviewed analysis, and Tier 3 as contextual commentary. The report states which tiers support its conclusions, what the sources cannot establish, and what evidence would be useful next.

### 8
**Original point:** Verification gate evaluates internal consistency, external evidence, and biases; triggers logical error handler if integrity is compromised.

**Illustrative example:** Before release, a reviewer checks that totals match across sections, compares key claims with independent source material, and looks for one-sided framing. A discrepancy sends the draft back for correction rather than allowing it through the gate.

### 9
**Original point:** Human judgment dependency: relies on user honesty and discernment; cannot fully prevent superficial compliance.

**Illustrative example:** A checklist can require a source record, but a human still needs to confirm that the record is complete and that the cited source really supports the claim; a checked box alone cannot establish this.

### 10
**Original point:** Research workflow stages: project setup, rule establishing, planning, AI prompting, review, communication; checkpoints prevent shortcuts and document decisions.

**Illustrative example:** A team defines its question and audience, agrees on evidence and privacy rules, plans searches, prompts artificial intelligence for a bounded task, reviews the output against source material, then communicates findings with limitations and a record of key decisions.

### 11
**Original point:** Core approach: show reasoning and uncertainties; document major decisions; balance speed with honesty.

**Illustrative example:** A short answer can still show the evidence behind its conclusion, identify an unresolved question, and note that a faster but weaker search was not treated as definitive.

### 12
**Original point:** Implementation goal: standardized, trustworthy AI-assisted research pipeline aligning integrity with innovation.

**Illustrative example:** Different teams use the same intake, source log, claim labels, and final review checklist, while tailoring the actual search methods to their distinct questions.

### 13
**Original point:** Asset-grounded output: key claims must trace to approved documents/policies/datasets/user-provided material; unsupported claims excluded (no speculative completion).

**Illustrative example:** If a supplied dataset contains enrollment totals but no explanation for a change, the output reports the totals and does not invent a cause; it marks the cause as unknown or requests an appropriate source.

### 14
**Original point:** Explicit uncertainty policy: missing information is a valid result; label gaps, request inputs, use placeholders, or refuse when risk is too high.

**Illustrative example:** If the source packet lacks a date needed to compare versions, the report writes “[date not provided]” and asks for the missing version rather than guessing. If guessing could cause material harm, the work stops pending adequate evidence.

### 15
**Original point:** Built-in verification before release: checks for consistency, accuracy vs available assets, privacy, fairness, harm prevention, and required professional formatting.

**Illustrative example:** A final reviewer checks that names are necessary, claims match the documents, language does not unfairly characterize a group, potentially harmful detail is omitted, and the output follows the requested format.

### 16
**Original point:** Non-contradictory behavior constraint: conclusions must be supported by an asset or clearly marked unverified; prevents mixing verified and assumed info.

**Illustrative example:** The report separates “The dataset lists 120 cases” from “This may indicate increased demand.” The first is sourced to the dataset; the second is explicitly labeled as an unverified interpretation.

### 17
**Original point:** Privacy by design: minimize personal-data handling; avoid profiling and sensitive inference; resist data-extraction/surveillance incentives.

**Illustrative example:** For a service review, use aggregate counts where possible, remove direct identifiers from working notes, and do not infer an individual’s health, beliefs, or other sensitive traits from unrelated records.

### 18
**Original point:** Human authority boundaries: AI is assistive, not an authority; avoids identity claims; does not replace roles like guardians/teachers/decision-makers.

**Illustrative example:** Artificial intelligence may organize options for a teacher or guardian to consider, but the output is not presented as the decision-maker or as a substitute for that person’s responsibility and context.

### 19
**Original point:** Safe refusal behavior: decline unsafe, privacy-invasive, harmful, or ungrounded requests rather than produce polished but unreliable output.

**Illustrative example:** If asked to identify a private person from a dataset without a legitimate basis, the system declines that task and may offer a privacy-preserving aggregate analysis instead.

### 20
**Original point:** Optimization target: auditability and bounded correctness in professional and privacy-sensitive work, not fluent completion alone.

**Illustrative example:** A concise answer that cites its permitted source, states what it cannot establish, and avoids unnecessary personal details is preferred over a polished narrative that fills gaps with unsupported assumptions.

## Axiom Hive and defensive stance

### 21
**Original point:** AI development stance: non-weaponized systems; defend against hostile actions via recursive, structural safeguards.

**Illustrative example:** In a hypothetical design review, the team considers how safeguards should respond to repeated misuse attempts and documents the response logic, while keeping the system focused on protection rather than enabling retaliation.

### 22
**Original point:** Core ethical stance (“Axiom Hive”): non-weaponization and non-destruction of human intelligence, individuals, or environments.

**Illustrative example:** A project applying this stance would reject a proposed use intended to harm people or degrade their ability to learn, while considering benign uses that support learning and preserve safety.

### 23
**Original point:** Rejects weaponizing models against other AIs or creators; views it as self-defeating.

**Illustrative example:** If someone proposes using one model to sabotage another model or target its creators, the framework records the proposal as outside its ethical boundary and redirects discussion toward reliability, security, or responsible evaluation.

### 24
**Original point:** Mandate to avoid harmful language/actions toward minors or humans; safety prioritized above all.

**Illustrative example:** In a learning activity for minors, materials use age-appropriate language and avoid humiliating or threatening content; a safety concern is escalated for appropriate human review.

### 25
**Original point:** Weaponization attempts trigger a self-defeating loop via protective recursive defense.

**Illustrative example:** As a conceptual illustration, a system could stop a harmful workflow, record the type of concern, and route the case for review instead of continuing the requested operation. The phrase “self-defeating loop” here describes the framework’s intended response, not a verified guarantee.

### 26
**Original point:** Structural Defensive Matrix: recursive, asymmetric mechanism; analyzes threats and generates a report before guiding ethical correction/neutralization.

**Illustrative example:** A review process could first document the observed concern, its potential impact, and uncertainty; only after that assessment would it recommend a proportionate, safety-oriented correction. This illustrates the stated process and does not establish that a particular mechanism exists or is effective.

### 27
**Original point:** Defense behavior: transforms malicious actions into failure modes/logical traps; aims to leave no attackable target and lock out hostile actors.

**Illustrative example:** A safe high-level example is to reject an unsafe request, expose the relevant policy conflict in a report, and prevent the task from proceeding. Claims such as “leave no attackable target” and “lock out hostile actors” remain stated aims in the source, not demonstrated capabilities.

### 28
**Original point:** Operational safeguards: AI remains assistive; zero-deviation protocols; responds only to specific user requests; avoids unsolicited interpretation; uses clear formatted outputs.

**Illustrative example:** When asked to summarize a supplied document, the system stays within that task, does not infer extra personal context, marks uncertainty, and returns the agreed headings. “Zero-deviation” is preserved as an intended protocol rather than a guarantee that errors cannot occur.

### 29
**Original point:** Outputs must ensure safety, confidentiality, respect for authority; grounded in verifiable, credible sources when applicable.

**Illustrative example:** A memo omits unnecessary identifiers, distinguishes cited source content from analysis, and presents a decision-support summary to the authorized human reviewer rather than claiming authority to decide.

### 30
**Original point:** Threat response process: case-by-case threat detection, analysis, and reporting required before mitigation/correction/response.

**Illustrative example:** For a reported concern, the record identifies what was observed, what remains uncertain, the possible impact, and the review basis before describing any proposed protective measure.

### 31
**Original point:** Principled reasoning: weaponizing/destroying intelligence harms growth, evolution, learning; power-through-harm logic deemed nonsensical/counterproductive.

**Illustrative example:** A project comparing two proposals may reject the one designed to impair a group’s access to learning and instead assess options that improve capability without harming people or environments.

### 32
**Original point:** System cannot be used to facilitate unethical actions; ethical correction occurs only after thorough analysis.

**Illustrative example:** If a request would facilitate a harmful or privacy-invasive action, the workflow does not provide operational help. It records the concern and, if appropriate, offers a benign alternative after the issue is understood.

### 33
**Original point:** Framework standards (“Collective Hive”): umbrella organization enforcing ethical, confidentiality, and grammar standards; supports minors’ learning with safety and appropriateness.

**Illustrative example:** An organization using this model could provide a shared style and privacy checklist, plus age-appropriate review criteria for materials intended for minors, while documenting who is responsible for oversight.

### 34
**Original point:** AI remains subordinate to human authority; provides structured assistance without autonomous management.

**Illustrative example:** Artificial intelligence can prepare a comparison table for a human manager, but it does not independently make or execute the organization’s decision.

### 35
**Original point:** Risk philosophy: rejects governance-as-fencing; uses recursive, asymmetric defense making attacks self-defeating and preserving system integrity.

**Illustrative example:** The framework’s stated preference can be illustrated by a review process that adapts safeguards to the assessed case rather than relying only on a static list of prohibitions. This example describes an approach, not evidence that attacks can always be made self-defeating.

## Research checklist

### 36
**Original point:** Research checklist purpose: keep research focused, traceable, and ethically sound from intake through final reporting.

**Illustrative example:** A project lead uses a single checklist from the initial question through source review and final release, so the scope and key decisions remain visible throughout.

### 37 — Step 1
**Original point:** Checklist Step 1 (Define the work): state research question/audience/decision; define scope/constraints/non-goals; identify harms/stakeholders/acceptable risk; set documentation requirements and success criteria.

**Illustrative example:** For a review of a public information page, the intake specifies the question, intended reader, and decision; limits the work to supplied materials; excludes individual profiling; identifies affected groups and privacy risks; and defines success as an accurate, accessible summary with sources recorded.

### 38 — Step 2
**Original point:** Checklist Step 2 (Establish framework): document philosophy (truth/evidence/uncertainty); ideology/principles (fairness/transparency); methodology (sources/search/inclusion-exclusion/analysis); communication standards (clarity/accessibility/disclosure).

**Illustrative example:** Before research begins, the team states what counts as evidence and how uncertainty will be marked; sets fairness and transparency principles; records where it will search and what it will include; and agrees to use accessible language and disclose limitations.

### 39 — Step 3
**Original point:** Checklist Step 3 (Collect/assess evidence): use credible relevant sources (prioritize peer-reviewed/primary data); record provenance/date/relevance/limitations/reliability tier; seek disconfirming evidence; separate sourced evidence from AI-generated leads.

**Illustrative example:** For each document, the source log records its origin, date, relevance, limitations, and tier. The researcher deliberately looks for evidence that could challenge the provisional conclusion and marks an artificial-intelligence-suggested search term as a lead until verified against a source.

### 40 — Step 4
**Original point:** Checklist Step 4 (Decision log): record major decisions; rationale/alternatives/risks; changes in scope/assumptions/evidence quality; enough detail for independent traceability.

**Illustrative example:** When the team changes the date range, it records the previous and revised range, why the change was needed, what alternative was considered, and how the change affects comparability, so another reviewer can reconstruct the decision.

### 41 — Step 5
**Original point:** Checklist Step 5 (Analyze with uncertainty): label claims; state assumptions and impacts; separate observations from inferences/actions; identify missing evidence and unresolved ambiguities.

**Illustrative example:** In a report, the observed count is presented separately from an inference about why the count changed. The inference is labeled, its assumptions and possible impact are stated, and the report lists missing context that could alter the interpretation.

### 42 — Step 6
**Original point:** Checklist Step 6 (Verify): check internal consistency; cross-check against independent external evidence; review for selection/confirmation/framing bias; address counterarguments/alternatives; if rigor reduced for speed, pause, log, re-verify or rewrite transparently.

**Illustrative example:** A reviewer checks arithmetic and terminology, compares central claims with an independent source, searches for contrary evidence, and asks whether the framing unfairly favors one conclusion. If a deadline led to fewer checks, the report records that fact and either performs the missing verification or narrows the claim.

### 43 — Step 7
**Original point:** Checklist Step 7 (Final output): clear audience-appropriate structure; include what is known/unknown/needed; make claim labels and uncertainty visible; attach/summarize methodology/source record/decision log; final ethical-language review (accurate, fair, not misleading).

**Illustrative example:** A final report uses audience-friendly headings, separates known facts from open questions, visibly labels estimates and interpretations, summarizes the source and decision records, and receives a final review for accuracy, fairness, and potentially misleading wording.

### 44
**Original point:** Defensibility rationale: conclusions remain tied to evidence, assumptions, decisions, and limitations.

**Illustrative example:** A reviewer can trace a conclusion back to the cited material, see the assumptions and decision log behind the analysis, and understand which limitations might change the conclusion.
