# Ethical AI-Assisted Research Framework

A practical, evidence-grounded toolkit for planning, conducting, reviewing, and communicating research supported by artificial intelligence. The supplied framework is preserved verbatim in [`docs/source-framework.txt`](docs/source-framework.txt); [`docs/framework-with-examples.md`](docs/framework-with-examples.md) pairs every original point with a clearly labeled illustrative example.

This repository is primarily a documentation and template toolkit. It does not require a package installation or third-party Python dependencies.

## Principles at a glance

- Treat responsibility and rigor as co-requirements; do not trade integrity for speed.
- Define the research question, audience, scope, non-goals, risks, and success criteria before work begins.
- Keep claims traceable to approved source material; label facts, estimates, interpretations, hypotheses, and recommendations.
- Record major decisions, alternatives, risks, source provenance, limitations, and unresolved questions.
- Verify consistency, evidence, and bias before release; state what is known, unknown, and needed.
- Minimize personal-data handling, respect human authority, and decline unsafe, privacy-invasive, harmful, or unsupported work.
- Treat defensive concepts and strong protocol language in the source as stated aims unless independently demonstrated.

## Repository contents

| Path | Purpose |
| --- | --- |
| `docs/source-framework.txt` | Source text as supplied. |
| `docs/framework-with-examples.md` | All 44 source points reproduced verbatim, each with a clearly labeled practical example. |
| `docs/implementation-guide.md` | Suggested lifecycle for applying the framework. |
| `templates/research-charter.md` | Project intake, scope, principles, methodology, and human-review template. |
| `templates/source-register.csv` | Source provenance, relevance, limitations, and quality-tier record. |
| `templates/claim-ledger.csv` | Claim label, supporting evidence, uncertainty, and review record. |
| `templates/decision-log.csv` | Major decisions, rationale, alternatives, and risks. |
| `templates/verification-checklist.md` | Pre-release evidence, ethics, safety, and communication review. |
| `scripts/validate_framework.py` | Checks verbatim source-point coverage and example count. |

## Setup

### Prerequisites

- Git, for cloning and tracking changes.
- Python 3.8 or later. The preservation validator and unit tests use the Python standard library; `coverage` is needed only for local coverage reporting.

The documents and CSV templates can also be used without Python.

### Get a local copy

```bash
git clone https://github.com/CadenMcCullenSoftware/ethical-ai-research-framework.git
cd ethical-ai-research-framework
```

### Verify the framework document

Run the built-in check from the repository root:

```bash
python3 scripts/validate_framework.py
```

A successful run reports that all 44 source points are preserved verbatim and each has an example. The script returns a non-zero exit status if it detects missing, changed, or unpaired points. Run it after editing either the source text or the expanded framework.

### Run unit tests and coverage

Install the coverage reporter and run the tests from the repository root:

```bash
python3 -m pip install coverage
python3 -m unittest discover -s tests -v
python3 -m coverage run --branch --source=scripts -m unittest discover -s tests -v
python3 -m coverage report --include="scripts/validate_framework.py" --fail-under=90
python3 -m coverage html
```

Open `htmlcov/index.html` for a detailed local report. The GitHub Actions workflow runs the unit tests, enforces a 90% minimum coverage threshold, writes a coverage summary to the Actions job summary, and uploads HTML/XML reports as a 14-day artifact on pushes and pull requests.

### Start a research project with the toolkit

1. Copy `templates/research-charter.md` into the project’s working area and complete it before substantive research. Record the question, audience, scope, non-goals, stakeholders, risks, success criteria, and human reviewer.
2. Define the project’s philosophy, principles, methodology, and communication standards in the charter. Set source-tier definitions appropriate to the project before assessing sources.
3. Copy `templates/source-register.csv`, `templates/claim-ledger.csv`, and `templates/decision-log.csv` into the project’s working area. Add rows as evidence is collected, claims are assessed, and material decisions are made.
4. Follow [`docs/implementation-guide.md`](docs/implementation-guide.md) for evidence collection, uncertainty handling, analysis, verification, and communication.
5. Complete `templates/verification-checklist.md` before release. Keep records proportionate to the project and protect personal or confidential data.

For example, copy the Markdown template with `cp templates/research-charter.md ./research-charter.md`. CSV files can be edited in a text editor or spreadsheet application. Avoid committing project records containing private data, credentials, or confidential material to this public repository.

## Claim labels

Use one visible label for each material claim:

- **Fact** — directly supported by a cited source or approved asset.
- **Estimate** — a quantified or approximate result with method and uncertainty stated.
- **Interpretation** — an explanation or meaning inferred from evidence.
- **Hypothesis** — a proposition that remains to be tested.
- **Recommendation** — a proposed action, with rationale and relevant trade-offs.

These labels organize the work; they do not make a claim reliable by themselves. Record the supporting evidence, assumptions, and limitations.

## Source-quality tiers

Set tier definitions appropriate to the project before collection. Prefer primary material and peer-reviewed work when relevant. For every source, capture provenance, date, relevance, limitations, and the basis for its tier. A tier is a project assessment, not a universal guarantee of truth. Keep artificial-intelligence-generated search leads distinct from verified evidence until the underlying source has been reviewed.

## Contributing

Contributions that clarify the toolkit, improve examples, strengthen usability, or fix errors are welcome. Keep source-derived requirements distinct from added interpretation, editorial guidance, and examples.

### Suggested contribution workflow

1. **Discuss substantial changes first.** Open an issue describing the problem, affected files, proposed change, and any trade-offs. Small typo fixes can go directly to a pull request.
2. **Create a focused branch.** Use a descriptive name such as `docs/clarify-source-records` or `fix/validator-message`.
3. **Make a scoped change.** Prefer small, reviewable commits. Preserve the supplied source text unless the change explicitly concerns that source. When proposing a change to source-derived requirements, explain why and retain a clear record of what changed.
4. **Keep examples honest.** Label new examples as illustrative. Do not present examples, assumptions, or artificial-intelligence-generated leads as independently verified evidence. Do not present conceptual defenses or protocol aspirations as proven guarantees.
5. **Protect privacy and safety.** Do not commit personal, confidential, or sensitive project data, credentials, access tokens, or private research records. Do not include operational instructions that would facilitate harm.
6. **Run the checks.** From the repository root, run `python3 scripts/validate_framework.py`. Review Markdown for readability, links, and consistency with the framework.
7. **Open a pull request.** Describe the purpose, summarize the changes, identify any source text affected, list the checks run, and note relevant limitations or open questions. Link a related issue when one exists.

### Review expectations

Pull requests should be focused, understandable, and consistent with the framework’s emphasis on traceability, uncertainty, privacy, fairness, and human authority. Reviewers should check factual support for new claims, distinguish source content from commentary, confirm that examples are clearly marked, and run the validator when framework text or examples change. A review checklist records work performed; it is not a guarantee that an output is error-free.

### Reporting a sensitive concern

Do not disclose credentials, private personal information, or confidential research material in a public issue or pull request. Use a private reporting route if one is available for the repository. If no private route is available, provide only a high-level description in public and do not post the sensitive details.

## Scope and limitations

This repository operationalizes the supplied framework as documentation and reusable templates. It does not certify compliance, guarantee that errors or harmful outcomes can be prevented, or independently validate technical mechanisms described in the source. Human review and sound source material remain necessary. Examples are illustrative, not external evidence.

No software license is included because none was specified. Add a license only after choosing the intended reuse terms; the presence of contribution guidance does not itself grant a license.
