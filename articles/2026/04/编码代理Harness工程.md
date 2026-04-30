---
title: "Harness engineering for coding agent users"
source: "https://martinfowler.com/articles/harness-engineering.html"
author: "Birgitta Böckeler"
published: "2026-04-02"
ingested: "2026-04-28"
tags:
  - coding-agents
  - harness-engineering
  - feedback-loops
  - software-quality
  - architecture-fitness
content_type: article
status: evergreen
confidence: high
---

# TL;DR

这篇文章把“如何信任编码代理”拆成一个工程问题：不是盲目相信模型能力，而是主动设计一套外部控制系统（harness），让代理在生成前被引导、生成后被校正。核心机制是把控制分为前馈（guides）和反馈（sensors），再按计算型与推理型两类能力组合，持续迭代成可复用的质量治理回路。结论很实用：想降低人工盯防，就要把“人的经验”尽量外显成规则、检查器和自纠流程，而不是只升级模型。

---

# Core Insight

- 对编码代理来说，真正可规模化的信任来源不是“模型更聪明”，而是“系统化的外部约束”：前馈提高首轮命中率，反馈提高自我修复率，二者必须同时存在。
- harness 需要区分三类治理目标：可维护性（最容易落地）、架构适配度（可用 fitness functions 约束）、功能行为正确性（目前最难，仍高度依赖人工测试与审查）。
- 人类角色不会被直接替代，而是从“逐行兜底”转向“设计和迭代 harness”：把重复犯错转成可执行规则，逐步把监督成本压到关键决策点。

---

# How It Works

- 控制框架：Feedforward + Feedback
  - Guides（前馈）：在代理行动前提供结构化约束，例如 AGENTS.md、技能说明、架构规范、脚本/代码改造工具。
  - Sensors（反馈）：在代理行动后提供可消费信号，例如 lint、测试、结构规则、AI review，让代理先自纠再提交给人。

- 能力类型：Computational + Inferential
  - 计算型控制：确定性、便宜、可高频运行（类型检查、lint、结构测试、覆盖率规则）。
  - 推理型控制：语义判断更强但成本高且非确定（AI review、LLM-as-judge）。
  - 实际策略是“计算型保底 + 推理型补盲”，而不是二选一。

- 运行节奏：Keep quality left
  - 把快而确定的检查尽量前移到提交前与集成前。
  - 把昂贵检查放在流水线或周期性巡检中。
  - 除了变更链路，还要有持续漂移传感器（如死代码、依赖风险、SLO 退化）。

- 治理分层：Regulation categories
  - Maintainability harness：当前最成熟，能稳定抓住结构与风格类问题。
  - Architecture fitness harness：围绕性能、可观测性、边界约束建立架构级反馈。
  - Behaviour harness：目前短板，AI 生成测试的可信度仍不足，人工验证仍关键。

- 规模化路径：Harness templates
  - 对常见服务拓扑（如 CRUD 服务、事件处理、数据看板）预制 guides + sensors 套件。
  - 通过限制可变空间（类似 Ashby 定律的“降复杂度”）提高治理可行性。

---

# Why It Matters

- 对 AI 工程：它把“如何用代理”从提示词技巧升级成“控制系统设计”，讨论层级从功能清单提升到可治理性。
- 对团队交付：这是一条现实路径——不是追求完全无人化，而是把人工精力集中在高价值判断，减少低价值重复审查。
- 对个人/小团队：harness 一旦沉淀成模板，下一项目可直接复用，长期收益来自规范复利，而非一次性效率红利。

---

# Failure Modes / Criticism

- 行为正确性问题仍未被充分解决：即使测试全绿，也可能只是“把错误需求实现得很完整”。
- 推理型传感器存在成本与不稳定性，若设计不当会引入“看似有反馈、实际噪声高”的伪安全感。
- harness 本身会变复杂：规则冲突、版本漂移、模板分叉、覆盖率难评估，都会侵蚀治理效果。
- 对遗留系统不友好：最需要 harness 的地方，往往也是类型系统薄弱、架构边界模糊、历史债务最重的地方。

---

# My Take

我非常认同这篇文章把问题重心放在“可治理性”而不是“模型智力”。对我这种一人负责全栈交付的人来说，真正能复用的资产从来不是某个新模型，而是能反复应用的工程约束：什么先做、什么必须检查、什么失败要阻断。

我最看重的是它的“steering loop”视角：同类错误重复出现时，不是继续人工提醒，而是把它固化进 harness。这个思路和我做个人项目的目标高度一致——把经验写成规范，让下一次启动更快、更稳。

我准备优先落地三件事：
- 用前馈文档固定默认做法（目录结构、测试策略、提交前检查清单）；
- 用计算型传感器建立低成本硬门禁（lint、类型检查、关键结构规则）；
- 把高成本 AI review 放在高风险变更上，而不是全量执行。

策略上，这篇文章提醒我：代理时代的核心竞争力是“你是否能设计一套长期可维护的控制系统”。六个月后让我感谢今天决策的，应该是这套系统，而不是一次跑得很快的生成结果。

---

# Connections

- [[Agent Infrastructure]]
- [[AI Workflow]]
- [[Engineering Playbook]]
- [[Continuous Delivery]]
- [[Architecture Fitness Functions]]

---

# References

https://martinfowler.com/articles/harness-engineering.html
