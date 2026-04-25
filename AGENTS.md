# AGENTS.md

## Daily Article Command

When the user says `总结文章 <url>`, `总结文字 <url>`, or `总结 <url>`, treat it as an article-ingest request.

Do not require a registered Codex skill named `article_ingest`. Instead, read `.agents/skills/article_ingest.md` from this repository and follow it as the authoritative workflow.

For article-ingest requests:

- Read the URL or provided article content.
- Create or update the note exactly in the format required by `.agents/skills/article_ingest.md`.
- Keep section names exactly aligned with that file so `Markdown basic / validate` passes.
- Save new notes under `articles/YYYY/MM/<中文主题短标题>.md`.
- Commit with message `add knowledge note: <article title>`.
- Open a pull request targeting `master`.
- Use PR title `add knowledge note: <article title>`.
- Include source URL, generated markdown path, and summary of changes in the PR body.
- Include this exact line in the PR body: `Please add label: codex-auto-merge`

The `codex-auto-merge` label is added by GitHub Actions when the PR matches the article-ingest PR rules.
