# Implementation Guide

This guide turns the supplied framework into a repeatable project workflow. It is operational guidance, not a claim that following a checklist alone guarantees correctness or safety.

## 1. Project setup

Use `../templates/research-charter.md` to document:

- The research question, audience, and decision the work may inform.
- Scope, constraints, non-goals, stakeholders, potential harms, and acceptable risk.
- Required records, success criteria, and human review responsibilities.

Do not begin substantive analysis until the scope and authority boundaries are clear. Missing information should be recorded as a gap, not silently filled in.

## 2. Establish the four-block framework

Before collection, define:

1. **Philosophy:** what counts as evidence, how uncertainty is represented, and what “known” means for this project.
2. **Ideology/principles:** fairness, transparency, privacy, non-weaponization, and respect for human authority that govern the work.
3. **Methodology:** sources, search plan, inclusion/exclusion criteria, analysis steps, and verification approach.
4. **Ethical language:** audience, accessibility, disclosure, claim labeling, and wording standards.

Record changes to these choices in the decision log.

## 3. Collect and assess evidence

- Prioritize credible, relevant primary sources and peer-reviewed research where appropriate.
- Capture provenance, publication/update date, relevance, limitations, and a project-defined reliability tier in `../templates/source-register.csv`.
- Seek disconfirming evidence and record important alternatives.
- Keep artificial-intelligence-generated leads distinct from verified source evidence. A suggested lead becomes evidence only after a human checks the underlying source.
- Minimize personal data. Use aggregate or de-identified material where feasible, and do not infer sensitive characteristics without a justified and authorized basis.

## 4. Maintain traceability

Use `../templates/decision-log.csv` for decisions that affect scope, inclusion, assumptions, analysis, or evidence quality. Record the rationale, alternatives considered, risks, and consequences. Use `../templates/claim-ledger.csv` to connect material claims to evidence and uncertainty.

## 5. Analyze with uncertainty visible

Separate observations from inferences and actions. Assign a claim label (Fact, Estimate, Interpretation, Hypothesis, or Recommendation) to each material claim. State assumptions, impacts, limitations, and missing evidence. If a claim cannot be grounded in an approved asset, label it unverified, use a placeholder, ask for the missing input, or omit it.

## 6. Verify

Use the release checklist in `../templates/verification-checklist.md` to assess:

- Internal consistency and calculations.
- Accuracy against available source material.
- Independent corroboration for important claims where possible.
- Selection, confirmation, and framing bias, including counterarguments.
- Privacy, fairness, harm, human authority, and confidentiality.
- Whether any speed-related reduction in rigor is recorded and repaired, or transparently disclosed with a narrower claim.

When integrity is in doubt, pause the affected work, document the issue, and re-verify or revise transparently before proceeding.

## 7. Communicate and retain records

Present findings in an audience-appropriate format. Make claim labels and uncertainty visible; include what is known, unknown, and needed next. Summarize the methodology, source record, material decisions, and limitations. Conduct a final review for accuracy, fairness, clarity, accessibility, privacy, and non-misleading language.

## 8. Handling concerns and refusal

Assess concerns case by case. Record what was observed, what is uncertain, plausible impacts, and the basis for any protective recommendation before proposing correction or mitigation. Do not convert conceptual language such as “self-defeating loop,” “zero-deviation,” or “lock out hostile actors” into an unsupported technical guarantee. Decline work that is unsafe, privacy-invasive, harmful, or materially ungrounded, and offer a safer alternative when appropriate.

## Record retention

Keep only records needed for reproducibility, accountability, and applicable policy. Store them with appropriate access controls and retention periods. Do not place sensitive personal information in public issue trackers or repository history.
