# 个人AI编程经验分享

## 1. 为什么需要 AI 编程？

## 2. 目前热门 ai 编程工具对比
### 两大平台
- openai（我常用的）
    特点：做AI基础设施、额度高、对国内使用限制低
    应用生态：codex; chatgpt; gpt-imageGen-2; sora
- anthropic
    特点：做专家型AI工具、额度低、对国内使用限制高
    应用生态：claude; claude code
（cursor：提供claude模型，额度不够用转codex）

### 编程工具 claude code 和 codex 的区别
claude code：
    适合制定计划、编写规则、代码审查。可以参与设计到代码落地的全流程决策。
    角色：决策者[head]
    使用体验：
        在编写代码时有更多自我决策，在用户提供需求不清晰的情况下，会主动询问用户并完成任务。在代码的收敛性上更好，通常写出的代码可以直接运行。
codex：
    适合执行具体任务、编写代码
    角色：执行者[hands]
    使用体验：
        codex的角色定位是快速完成用户需求，因此很多情况下需求还没分析清楚就开跑（gpt-5.4存在这个情况，gpt-5.5优化了这个问题）。
    解决办法：写 .codex/AGENT.md 文档，要求 AGENT 在需求对话中主动询问用户，拿到边界约束、确认需求后才开始行动。

### 我的主要编程流程-codex
1. 订阅：codex禁止国内使用，需要使用 paypal 绑定国内信用卡(招商银行信用卡)，再进行订阅。
2. 使用：
    codex windows客户端
    codex vscode插件
    codex cli
3. 流程：
    codex 适合写具体的小任务。复杂任务需要手动拆分，一步一步喂给agent。先写TODO.md理清需求。
    0. 确认git tree提交干净
    1. /plan 模式，与 agent 讨论需求，制定计划
    2. 审查计划，提出修改意见，确认完毕后开始实现
    3. 审查代码，有问题的再次提出修改，方向偏离太大则redo，直到审查通过后提交git。
    4. 循环0-3, 直到需求完成。

### open-ai生态使用
1. chatgpt: 平时的问题，需要了解的信息直接询问gpt，比搜索引擎更快、更准确。
2. gpt-imageGen-2: 图片生成神器，有图有真相时代的终结者，可以生成以假乱真的图片。在chatgpt内直接使用：
    示例：https://chatgpt.com/share/69f054ca-55cc-839e-aa57-55161aa0aa82

### anthropic生态使用
1. claude：免费的额度受限，主要用来写/优化agent skill和agent文档。
2. claude design: claude的UI设计规范，让agent严格要求设计规范生成UI可视化代码。web-design-engineer/

## 案例：个人知识库搭建——以codex cloud为基础
1. 需求场景：
    1. 看到一篇技术文章，需要总结出来并持久保存。
    2. 教程：软件安装/环境配置，之前按照教程做了一遍，后面忘了又要重新搜索。
    3. 与chatgpt的对话，有价值的需要总结保存。
2. 工具：codex cloud, github actions, obsidian
3. 流程：
    用户输入：总结文章 <url> -> agent总结文章并写入 -> 提交pr -> github actions自动合并 -> obsidian查看
4. 详情： Codex云端个人知识库搭建指南.md