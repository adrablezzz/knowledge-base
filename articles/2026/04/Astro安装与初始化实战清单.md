---
title: "安装 Astro | Docs"
source: "https://docs.astro.build/zh-cn/install-and-setup/"
author: "Astro Docs"
published: "unknown"
ingested: "2026-04-25"
tags:
  - ai
  - agents
  - infrastructure
content_type: article
status: evergreen
confidence: high
---

# Summary
这篇文档系统讲清了 Astro 项目从 0 到可运行的两条路径：`create astro` 向导式安装与手动安装。它不仅给出命令，还强调了关键边界条件，例如 Node.js 版本要求、本地安装约束、以及 TypeScript 与编辑器体验的关系。文档的核心价值在于把“能跑起来”和“后续可维护”一起交付：从脚本、目录结构到配置文件都给了最小可行基线。对于团队来说，这是一份可直接落地为内部脚手架规范的官方标准说明。

# Why It Matters
前端团队常见问题不是“不会启动项目”，而是不同成员初始化方式不一致，导致脚本、目录、配置分叉。该指南通过标准化安装路径与配置基线，显著降低新项目启动成本和后续协作摩擦，也为 CI/CD、类型检查和集成扩展打下统一起点。

# Key Ideas
- **双路径安装策略**：优先用 `create astro` 快速初始化；若需完全可控流程，则走手动安装步骤。
- **环境前置约束明确**：Node.js 需 `v22.12.0+`（不支持奇数版本如 v23），并建议配合 VS Code + 官方扩展。
- **CLI 参数即“初始化策略”**：`--add` 可在建项目时直接加集成；`--template` 可从官方样板或 GitHub 仓库启动。
- **本地安装原则**：Astro 只能本地依赖安装，禁止全局安装，避免版本漂移与环境污染。
- **可维护最小结构**：`src/pages/index.astro`、`public/robots.txt`、`astro.config.mjs`、`tsconfig.json` 组成了可运行且可扩展的项目骨架。

# Notable Quotes / Examples
- 文档给出的“最快起手”是：`npm create astro@latest`（或 pnpm/yarn 对应命令）。
- 创建项目时可直接组合能力：`--add react --add partytown`，减少后续手工接线。
- 模板来源不局限于官方示例，也可直接指向任意 GitHub 仓库 `main` 分支（并支持 `#branch`）。
- 手动安装流程中，官方明确提示不要执行 `npm install -g astro` / `pnpm add -g astro` / `yarn add global astro`。

# Contrarian View
这份指南偏重“通用正确路径”，对企业级场景（如 monorepo、私有 registry、离线镜像、统一锁版本策略）覆盖较少；如果团队直接照搬，可能仍需补充工程化规范。此外，Node.js 版本门槛较新，部分旧环境或公司受控开发机升级成本不低，迁移节奏要与组织基础设施能力匹配。

# Connections
- [[RAG]]
- [[Agent Infrastructure]]
- [[Startups]]

# My Take
- 这篇文档可被视为“Astro 项目初始化协议”，建议沉淀成公司内部 `create-frontend` 模板的一部分，而不是每次人工照文档执行。
- `--add` 与 `--template` 实际上是“架构决策前置”：在项目 Day 0 就决定技术栈和样板来源，能减少后续重构成本。
- 如果要做投资或技术评估，Astro 的文档成熟度本身就是信号：开发者上手摩擦低，社区扩散与团队采用速度通常更快。

# Action Items
- 把 Astro 官方初始化命令封装为团队脚手架（含 Node 版本检测与包管理器策略）。
- 设计一份“手动安装最小基线”检查表，用于 CI 校验目录与关键配置文件完整性。
- 在现有前端模板中做一次 Astro PoC，对比 Next/Vite 方案在内容型站点的交付效率。

# Source
https://docs.astro.build/zh-cn/install-and-setup/
