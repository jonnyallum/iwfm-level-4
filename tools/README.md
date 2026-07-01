# Tools

Utility scripts for maintaining the IWFM Level 4 FM Academy repo.

## check_repo.py

Automated quality checks over the Markdown content. Run it before committing, in a CI job, or from a SessionStart hook.

```bash
python3 tools/check_repo.py          # run all checks, verbose
python3 tools/check_repo.py --quiet  # only failures and the summary
```

It runs three checks and exits non-zero if any fail:

| Check | What it verifies |
|---|---|
| **links** | Every relative Markdown/JSON link resolves to a file on disk. |
| **metadata** | Every content Markdown file carries an `ai_metadata` block (pure trackers such as `CHANGELOG.md` and `TODO.md` are exempt). |
| **structure** | Every course module file (`NN-*/module-*.md`, excluding workbook files) contains the required section headings. |

### Requirements

Python 3.8+ only. No third-party packages.

### Extending

- Add exempt files to `METADATA_EXEMPT`.
- Adjust the required module headings in `REQUIRED_MODULE_SECTIONS`.
- The module file pattern is `MODULE_GLOB`; workbook files (`*-workbook.md`) are excluded from the structure check.

## Related

- [Contributing](../CONTRIBUTING.md)
- [Commit guide](../COMMIT_GUIDE.md)
- [Master index](../MASTER_INDEX.md)
