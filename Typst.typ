
#figure(
  table(
    align: center + horizon,
    columns: (auto, 1fr, 1fr, 1fr),
    inset: (x: 12pt, y: 6pt),
    stroke: none,
    table.hline(stroke: 1.25pt),
    table.header(
      [*参数*], [*数值*], [*单位*], [*备注*]
    ),
    table.hline(stroke: 0.75pt),
    [t], [0.3s], [s], [-],
    [y], [0.4s], [s], [-],
    [z], [0.8s], [s], [-],
    table.hline(stroke: 1.25pt),
  ),
  caption: [三线表示例],
)



#import "@preview/mmdr:0.2.2": mermaid

#figure(
mermaid("
sequenceDiagram
    autonumber
    participant FE as Frontend
    participant EF as Edge Function<br/>breakdown_task
    participant LLM as OpenAI-Compatible API

    FE->>EF: POST /breakdown_task\n{todosTree, selectedNodeId, query}
    EF->>EF: 校验请求体 + 构造上下文
    EF->>LLM: chat.completions.create(stream=true)

    loop 每个流分片 chunk
        LLM-->>EF: delta.content
        EF->>EF: 追加 fullContent
        EF->>EF: 增量解析完整任务对象
        alt 解析到新任务
            EF-->>FE: SSE data: {type:\"task\", data, index}
        end
    end

    EF-->>FE: SSE data: {type:\"done\", totalCount}
	"
  ),
  caption: [任务分解流程时序图]
)



#import "@preview/mmdr:0.2.2": mermaid

#figure(
mermaid("
stateDiagram-v2
    state \"我的状态\" as S1
    state \"选择状态\" as point <<choice>>

    S1 --> point: 自旋
    point --> S1
	"
  ),
  caption: [状态机示例]
)

#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge

#figure(
align(center)[
#diagram(
  node-stroke: 0.5pt,
  node-fill: rgb("#E8F5E9"),
  spacing: 2em,
  
  node((0,0), [数据库], fill: rgb("#FFF9E1")),
  
  edge((0,0), (-1,0), "-"),
  node((-1,0), [关系型数据库]),
  
  edge((-1,0), (-2,0), "-"), // 模拟大括号分支
  node((-2, -1), [MySQL], fill: rgb("#E1F5FE")),
  node((-2, 0), [Oracle], fill: rgb("#E1F5FE")),
  node((-2, 1), [MariaDB], fill: rgb("#E1F5FE")),
)]
,
caption: [数据库分类示例],
)


#import "@preview/finite:0.5.0": automaton

#automaton((
  // 转移定义
  q0: (q1: "0", q0: "1"),
  q1: (q2: "0", q1: "1"),
  q2: none,  // 终止状态
))

