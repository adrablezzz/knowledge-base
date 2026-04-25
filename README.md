# Knowledge Base
This is a personal knowledge base for myself and my team.

## How to use
1. use skill $article_ingest https://xxx.com to ingest a new md file.
2. choose a folder to store your notes or create a new one.

Create a new branch.

Commit the changes.

Open a pull request to `master` with:
title: add knowledge note: <title>
body:
- source URL
- generated markdown path
- summary of changes
label:
- codex-auto-merge

## Codex Cloud auto-merge

Codex Cloud PRs are auto-merged only when all of these are true:

- the PR targets `master`
- the PR is not a draft
- the PR has the `codex-auto-merge` label
- the `Markdown basic / validate` check passes

Repository settings that must be enabled in GitHub:

- Settings > General > Pull Requests > Allow auto-merge
- Settings > General > Pull Requests > Allow squash merging
- Settings > Actions > General > Workflow permissions > Read and write permissions
- Protect `master` with a branch rule or ruleset that requires `Markdown basic / validate`
- Create the label `codex-auto-merge`
