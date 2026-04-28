---
title: "LLM Wiki"
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md"
author: "Andrej Karpathy"
published: "2026-04-04"
ingested: "2026-04-28"
tags:
  - llm-wiki
  - knowledge-base
  - obsidian
  - rag
  - ai-workflow
content_type: article
status: evergreen
confidence: high
---

# TL;DR

Karpathy 提出的 LLM Wiki 不是在问答时临时检索文档，而是让 LLM 持续维护一个“可累积”的中间层知识库（markdown wiki）。
它把分散来源转成结构化页面、交叉链接和持续修订的结论，让知识沉淀从“每次重算”变成“持续编译”。
核心分工是：人类负责选源与提问，LLM 负责总结、归档、关联、更新与一致性维护。
对长期项目而言，这比一次性回答更有复利价值。

---

# Core Insight

- 真正的创新点不是“让 LLM 读文档”，而是把知识管理从 query-time retrieval（RAG）改为 ingest-time compilation（持续编译）。
- 这个模式的产物不是一次回答，而是一个会持续演化的知识资产：同一问题的回答质量会随时间自然提升，因为底层 wiki 已经被持续维护。
- 它把“知识系统失败的核心原因”定位为维护成本，而不是输入不足；LLM 的价值在于把跨页面维护成本压到接近零。

---

# How It Works

- 三层结构：
  - Raw sources：原始资料层，只读且不可变，是事实源。
  - Wiki：LLM 维护的 markdown 页面层，承载摘要、实体、主题、对比、综合判断。
  - Schema：给代理的规则文档（如 AGENTS.md/CLAUDE.md），约束目录结构、命名、摄取流程与问答产出。
- 三类操作：
  - Ingest：新资料进入后，LLM 读取并更新多页（摘要页、实体页、概念页、索引、日志）。
  - Query：先查 index 再钻取相关页面，生成回答；高价值回答可回写成新页面。
  - Lint：周期性做健康检查，找矛盾、过期结论、孤立页面、缺失交叉引用与数据空洞。
- 两个关键文件：
  - index.md：内容视角导航（按类别列出页面与一句话摘要）。
  - log.md：时间视角流水（记录 ingest/query/lint 事件），便于回溯和自动化处理。

---

# Why It Matters

- 对个人开发者最关键的价值是“跨项目复用”：知识不再散落在聊天记录与临时笔记里，而是变成可检索、可演化、可版本化的工程资产。
- 它能降低上下文切换成本：当我在架构、实现、复盘之间切换时，wiki 提供稳定的共享上下文，减少重复解释。
- 相比追求更复杂的基础设施，这个方案先用 markdown + git 起步，门槛低、可渐进增强，符合小团队/单人长期维护的现实约束。

---

# Failure Modes / Criticism

- 如果 schema 设计模糊，LLM 会稳定地产生“结构化噪声”，让 wiki 变得看似完整但检索价值下降。
- 当来源质量参差或缺少溯源要求时，错误结论会被“高可读性”包装并长期滞留。
- 规模上来后，仅靠手工 index 可能出现导航失真，需要补充搜索与质量审计机制。
- 该方法默认“持续维护值得投入”；若主题短平快、生命周期极短，维护投入可能大于收益。

---

# My Take

我非常认同这套方法把重点放在“知识编译”而不是“即时回答”。这和我做项目时的痛点完全一致：真正拖慢交付的，往往不是不知道答案，而是过去的决策无法被复用。

我觉得被低估的一点是 schema 的战略价值。很多人会把它当提示词模板，但对我来说它更像工程规范：它定义了什么信息值得沉淀、怎么命名、什么时候更新、冲突怎么处理。这个层面如果做好，后续每个项目都能复用。

我会优先测试三件事：
- 把“总结文章 <url>”流程固化为单命令摄取；
- 强制每次 ingest 更新 index 与 log，避免知识孤岛；
- 给关键结论加来源定位规则，减少后期追溯成本。

从策略上看，这不是“再加一个 AI 工具”，而是把个人开发流程从“会话驱动”切到“资产驱动”。如果持续半年，我预期最大的收益不是回答更快，而是技术决策质量更稳定。

---

# Connections

- [[Personal Knowledge Base]]
- [[AI Workflow]]
- [[Obsidian]]
- [[RAG]]
- [[Engineering Playbook]]

---

# References

https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md

---
