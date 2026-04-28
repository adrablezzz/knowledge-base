---
title: "Superpowers"
source: "https://github.com/obra/superpowers/blob/main/README.md"
author: "Jesse (obra)"
published: ""
ingested: "2026-04-28"
tags:
  - coding-agents
  - software-methodology
  - tdd
  - workflow-design
  - ai-engineering
content_type: article
status: evergreen
confidence: medium
---

# TL;DR

这篇 README 的核心不是“一个插件集合”，而是把 AI 编程从“即时生成代码”改造成“先设计、再计划、再执行、全程验证”的工程流程。它强调在动手前先澄清需求、拆分可验证任务，并通过 TDD 与代码审查把质量门禁前置。对个人开发者而言，最有价值的是：把可复用的方法固化到技能触发链里，减少每个项目从零定义流程的决策成本。

---

# Core Insight

- Superpowers 的真正产品不是单个能力，而是“按顺序自动触发的一组强约束工程习惯”：需求澄清 → 设计确认 → 实施计划 → 分工执行 → 测试与评审 → 收尾决策。
- 它把“经验型工程师的隐性判断”尽量外显成技能与检查点，让代理在缺少上下文和判断力时，仍能沿着可控路径前进。
- 相比追求更强模型，它更重视“流程防错”：通过 TDD、分阶段 review、工作区隔离等机制降低返工和偏航概率。

---

# How It Works

- 入口阶段（brainstorming）
  - 先追问目标与约束，不直接写代码。
  - 把设计按可读片段呈现给人确认，避免“默认假设直接落地”。

- 设计后阶段（using-git-worktrees + writing-plans）
  - 设计确认后创建隔离分支/工作区，先验证基线可运行。
  - 把工作拆成 2-5 分钟粒度的任务，每个任务包含明确文件路径、实现内容和验证步骤。

- 实施阶段（subagent-driven-development / executing-plans）
  - 每个任务由独立子代理执行，并进行两阶段审查（规格符合度、代码质量）。
  - 允许批处理执行，但保留人工检查点，避免长时间无人监督漂移。

- 质量阶段（test-driven-development + requesting-code-review）
  - 强制 RED-GREEN-REFACTOR，反对先写代码后补测试。
  - 在任务间持续代码审查，关键问题会阻断后续推进。

- 收尾阶段（finishing-a-development-branch）
  - 完成后统一校验测试，给出 merge / PR / 保留分支 / 丢弃分支的明确出口策略。

---

# Why It Matters

- 对 AI 工程实践：它把“提示词技巧”升级为“可执行开发制度”，能跨模型迁移并长期复用。
- 对独立开发：单人最缺的是稳定流程而非新工具，这套方法可以降低上下文切换与决策疲劳。
- 对交付质量：把质量控制放在开发过程内部，而不是上线前一次性补救，能显著减少后期排错成本。

---

# Failure Modes / Criticism

- README 主要是方法论与技能目录，缺少量化证据（如缺陷率、交付周期对比），因此“效果稳定性”仍需项目内验证。
- 工作流偏“流程重”，在超小任务或一次性脚本场景可能带来过度治理成本。
- 对工具链能力有隐含前提（子代理、插件市场、review 机制），跨环境复制时可能出现能力不对齐。
- 该体系默认测试可有效表达需求；若需求本身模糊，TDD 也可能把错误目标高质量实现出来。

---

# My Take

我认同它最有价值的点：把“会做项目”拆成一套可触发、可检查、可交接的流程资产，而不是依赖临场发挥。对我这种一人全栈来说，真正稀缺的不是再多一个框架，而是减少“每次开新项目都要重新定义开发纪律”的脑力消耗。

我觉得被低估的是它的“顺序约束”。很多 AI 编程失败并不是模型不会写，而是过早实现、跳过设计确认、没有中间验收。Superpowers 把这些关键闸门固定下来，本质是在降低不可逆错误。

我会优先落地三件事：
- 把“先出可读设计再编码”固化为默认启动流程；
- 把任务强制拆到可在短时间内验证完成的粒度；
- 把“未通过测试和评审不能推进”设为硬门禁。

策略上，这类方法比追逐新工具更可复用。六个月后回看，我更可能感谢“当时把流程写进系统”，而不是“当时试了一个更炫的插件”。

---

# Connections

- [[AI Workflow]]
- [[Test-Driven Development]]
- [[Engineering Playbook]]
- [[Agent Infrastructure]]

---

# References

https://github.com/obra/superpowers/blob/main/README.md
