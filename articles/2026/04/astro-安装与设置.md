---
title: "安装 Astro"
source: "https://docs.astro.build/zh-cn/install-and-setup/"
author: "Astro Docs"
published: "unknown"
ingested: "2026-04-25"
tags:
  - astro
  - frontend
  - javascript
  - vite
  - typescript
content_type: documentation
status: evergreen
confidence: high
---

# Summary
这篇文档是 Astro 官方的中文安装与初始化指南，核心目标是帮助开发者用最短路径启动一个可运行的 Astro 项目。它先给出推荐方式（`create astro` CLI 向导），再覆盖更可控的手动安装流程，确保不同偏好的开发者都能落地。文档还强调了环境前提（Node.js 版本、编辑器、终端）、浏览器兼容性基础，以及项目初始化后的关键动作（安装依赖、启动开发服务器）。

# Why It Matters
对团队而言，这篇文档的价值是“标准化起步”：无论你用 npm、pnpm 还是 yarn，都能得到一致的项目骨架与脚本约定，降低环境差异带来的问题。它也提前规避了常见坑（例如错误地全局安装 Astro），并把“从零到可预览”拆成了可执行步骤。

# Key Ideas
- **优先使用 CLI 向导**：`create astro` 是最快方式，自动完成模板选择与脚手架生成。
- **支持高级初始化参数**：可通过 `--add` 在创建时安装集成，或用 `--template` 基于官方示例/GitHub 仓库起步。
- **手动安装流程完整**：从创建目录、初始化 `package.json`、安装 Astro，到补齐 `scripts`、首个页面与静态资源均有示例。
- **本地安装原则**：Astro 必须本地安装到项目，避免全局安装导致版本和行为不一致。
- **配置文件最小集合**：`astro.config.mjs` 与 `tsconfig.json` 提供可扩展基础，即便不写 TypeScript 也建议配置。

# Notable Commands
- `npm create astro@latest` / `pnpm create astro@latest` / `yarn create astro`
- `npm create astro@latest -- --add react --add partytown`
- `npm create astro@latest -- --template <example-name>`
- `npm install astro`
- `astro dev` / `astro build` / `astro preview`

# Practical Checklist
1. 确认 Node.js >= `v22.12.0`（不要用不支持的奇数大版本）。
2. 用 CLI 快速创建项目；若跳过安装依赖，手动补 `npm/pnpm/yarn install`。
3. 校验 `package.json` 脚本中是否有 `dev/build/preview`。
4. 创建基础页面 `src/pages/index.astro` 与 `public/robots.txt`。
5. 添加 `astro.config.mjs` 和 `tsconfig.json`（至少 `extends: astro/tsconfigs/base`）。
6. 启动 `astro dev` 做首次本地预览。

# My Take
这份文档非常适合作为“新项目 kickoff 模板”。如果团队准备把 Astro 纳入正式生产，建议把文档里的手动安装步骤沉淀成内部脚手架校验清单（Node 版本、脚本、TS 配置、集成策略），并在 CI 中自动检查，避免后续出现“同一仓库不同人跑不起来”的问题。

# Source
https://docs.astro.build/zh-cn/install-and-setup/
