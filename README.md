# Ethical AI-Assisted Research Framework

A practical, evidence-grounded toolkit for planning, conducting, reviewing, and communicating research supported by artificial intelligence. The supplied framework is preserved verbatim in `docs/source-framework.txt`; `docs/framework-with-examples.md` pairs every original point with a clearly labeled illustrative example.

## Principles at a glance

- Treat responsibility and rigor as co-requirements; do not trade integrity for speed.
- Define the research question, audience, scope, non-goals, risks, and success criteria before work begins.
- Keep claims traceable to approved source material; label facts, estimates, interpretations, hypotheses, and recommendations.
- Record major decisions, alternatives, risks, source provenance, limitations, and unresolved questions.
- Verify consistency, evidence, and bias before release; state what is known, unknown, and needed.
- Minimize personal-data handling, respect human authority, and decline unsafe, privacy-invasive, harmful, or unsupported work.
- Treat defensive concepts and strong protocol language in the source as stated aims unless independently demonstrated.

## Repository map

- `docs/source-framework.txt` — source text as supplied.
- `docs/framework-with-examples.md` — all 44 source points reproduced verbatim with one practical example each.
- `docs/implementation-guide.md` — suggested lifecycle for adopting the framework.
- `templates/research-charter.md` — intake and scope template.
- `templates/source-register.csv` — evidence provenance and quality record.
- `templates/claim-ledger.csv` — claim type, support, uncertainty, and review record.
- `templates/decision-log.csv` — traceable decisions and alternatives.
- `templates/verification-checklist.md` — pre-release review.
- `scripts/validate_framework.py` — checks that all source statements appear verbatim in the expanded document and that each has an example.

## Quick start

1. Copy `templates/research-charter.md` and complete it before beginning research.
2. Keep a source register, claim ledger, and decision log as the work proceeds.
3. Follow the stages and checkpoints in `docs/implementation-guide.md`.
4. Complete `templates/verification-checklist.md` before communicating results.
5. Run the preservation check:

   ```bash
   python3 scripts/validate_framework.py
   ```

## Claim labels

Use one visible label for each material claim:

- **Fact** — directly supported by a cited source or approved asset.
- **Estimate** — a quantified or approximate result with method and uncertainty stated.
- **Interpretation** — an explanation or meaning inferred from evidence.
- **Hypothesis** — a proposition that remains to be tested.
- **Recommendation** — a proposed action, with rationale and relevant trade-offs.

These labels organize the work; they do not make a claim reliable by themselves. Record the evidence and limitations.

## Source-quality tiers

Set tier definitions appropriate to the project before collection. Prefer primary material and peer-reviewed work when relevant. For every source, capture provenance, date, relevance, limitations, and the basis for its tier. A tier is a project assessment, not a universal guarantee of truth.

## Scope and limitations

This repository operationalizes the supplied framework as documentation and reusable templates. It does not certify compliance, guarantee that errors or harmful outcomes can be prevented, or independently validate technical mechanisms described in the source. Human review and sound source material remain necessary. Examples are illustrative, not external evidence.

No software license is included because none was specified. Add a license only after choosing the intended reuse terms.

## Contributing

Propose changes through an issue or pull request. Keep source-derived requirements distinct from editorial guidance and examples. For changes to framework text, document the rationale and update the preservation check as appropriate.
