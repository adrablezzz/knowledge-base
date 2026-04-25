---
title: "安装 Astro | Docs"
source: "https://docs.astro.build/zh-cn/install-and-setup/"
author: "Astro Docs"
published: ""
ingested: "2026-04-25"
tags:
  - astro
  - 前端工程
  - 开发环境
content_type: article
status: evergreen
confidence: high
---

# Summary
这篇文档系统说明了如何从零安装并初始化 Astro 项目，优先推荐 `create astro` CLI 向导。核心信息是：先满足 Node.js 版本要求（`v22.12.0+`，不支持奇数大版本），再通过 npm/pnpm/yarn 一键建项目并启动开发服务器。文档也提供了完整手动安装路径，包括 `package.json` 脚本、`src/pages/index.astro`、`public/robots.txt`、`astro.config.mjs` 与 `tsconfig.json` 的最小配置。一个关键约束是 Astro 需要本地安装，不能全局安装。整体上它把“快速上手”和“可控手工搭建”两条路径都给到了。

# Why It Matters
对工程团队来说，这类“官方最小可运行路径”直接决定了 onboarding 速度、脚手架一致性和后续集成（React/MDX/Partytown 等）的可扩展性。把安装流程标准化还能显著减少环境问题与“新同学第一天卡住”的摩擦成本。

# Key Ideas
- `create astro` 是最快启动方式，支持交互向导与模板化创建。
- 前提环境必须满足 Node.js `v22.12.0` 或更高，且不支持奇数版本（如 `v23`）。
- 可在初始化时通过 `--add` 直接安装集成，通过 `--template` 基于官方示例或 GitHub 仓库创建项目。
- 手动安装路径强调“本地安装 Astro + 最小配置文件齐全”，保证可运行与可扩展。
- `tsconfig.json` 即便在非 TypeScript 项目里也有工具链价值（编辑器能力与导入体验更完整）。

# Notable Quotes / Examples
- 示例命令：`npm create astro@latest` / `pnpm create astro@latest` / `yarn create astro`。
- 集成安装示例：`npm create astro@latest -- --add react --add partytown`。
- 模板安装示例：`--template <example-name>` 或 `--template <github-username>/<github-repo>`。
- 关键约束：Astro 必须本地安装，不建议 `npm install -g astro` 这类全局安装方式。

# Contrarian View
这份指南对“现代 Node 与 CLI 工具链”前提假设较强，对受限企业环境（内网镜像、锁版本、代理复杂）缺少更细的故障排查路径。另一个不足是它给了最小骨架，但对“生产级默认实践”（测试、lint、CI、目录规范）覆盖较少，团队仍需二次封装自己的工程模板。

# Connections
Link related notes in my knowledge base using wiki links:

- [[RAG]]
- [[Agent Infrastructure]]
- [[Startups]]

# My Take
如果把 Astro 当作“内容型站点基础设施”，最有价值的不是框架本身，而是它把项目创建、集成安装与模板复用收敛成了统一 CLI 入口，这对多项目复制非常关键。Node 版本与本地安装约束看似琐碎，但恰好是降低环境漂移的底线规则，值得写入团队脚手架检查。对创业团队而言，先用官方模板跑通并尽早引入 `--add` 集成，比从空仓手写配置更能节约首周工程时间。

# Action Items
- 在团队模板仓库固化 Astro 初始化脚本与 Node 版本约束（含奇数版本拦截）。
- 评估 `--template` + 私有 starter 的组合，沉淀可复用的内容站点基线。
- 对比 `base/strict/strictest` 三种 tsconfig 策略，确定默认工程标准。

# Source
https://docs.astro.build/zh-cn/install-and-setup/
