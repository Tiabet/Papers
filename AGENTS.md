# Repository Guidelines

## Project Structure & Module Organization
- `organize_papers.py` houses the classification rules and file mover; run it from the repo root with access to the paper folders.
- Topic folders (`RAG`, `자연어처리`, `딥러닝전반`, `연구`, `종설1논문관련`, `종설2논문관련`) contain numbered subdirectories such as `00_Surveys_Overviews` or `03_Prompting_Agentic`. Place new PDFs in the appropriate top-level folder; the script routes them to a numbered bucket or `99_Misc`.
- Keep supplemental docs (like this guide and `README.md`) in the root for quick discovery.

## Build, Test, and Development Commands
- `python organize_papers.py`: Reclassifies PDFs based on the regex rules. Run after adding or renaming papers; rerun if you update the patterns.
- `find . -path '*99_Misc/*.pdf'`: Quick sanity check for leftovers that still need better naming or new rules.

## Coding Style & Naming Conventions
- Python files follow standard PEP 8 indentation (4 spaces) and snake_case function names. Favor concise helpers rather than inline complex logic.
- Regex patterns in `RULES` should stay lowercase and focus on distinctive substrings (e.g., `r"(survey|overview)"`). Add comments sparingly to explain non-obvious matches.
- PDF filenames should be descriptive, CamelCase or kebab-case, and omit spaces when possible (`GraphRAGSurvey.pdf`, `Hybrid-RAG.pdf`). This improves regex matching and portability.

## Testing Guidelines
- There is no automated test suite; rely on manual validation. After modifying rules, run the organizer and inspect moved files or git status before committing.
- When adding new categories, stage a dry run by copying sample filenames into a scratch folder and observing the printed move plan.

## Commit & Pull Request Guidelines
- Use imperative, scope-aware commit messages (`Add multi-hop keywords for RAG routing`). Group related regex updates together so reviewers can reason about coverage.
- Pull requests should summarize the new categorization logic, list representative filenames that motivated the change, and note any manual verification performed (e.g., remaining `99_Misc` entries).

## Security & Configuration Tips
- The script assumes the repository root is `c:/Development/Paper`. Update `ROOT` if you clone elsewhere to avoid moving files into an unintended location.
- Avoid running the organizer on network-mounted folders without backups; moves are destructive. Use version control or temporary copies when experimenting with new rules.
