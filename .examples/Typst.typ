// 全局格式设置


// 导入夜间主题
// #import "@preview/nordic:0.1.0" as nordic
// #show: nordic.default

#import "@preview/catppuccin:1.1.0": catppuccin, flavors
#show: catppuccin.with(flavors.mocha)

// 页面格式设置
#set page(
  paper: "a4",    // 纸张大小
  margin: 2cm,    // 页面边距
  //numbering: "1", // 开启页码, 格式为 1、2、3、4 等
)
// 文本格式设置
#set text(
  font: ("Arial", "Microsoft YaHei")
)
// 标题格式设置
#set heading(
  numbering: "1." // 开启自动编号，格式为 1.、1.1.、1.1.1. 等
)
// 段落格式设置
#set par(
  // first-line-indent: 2em, // 首行缩进2个字符, 靠近标题的第一段不缩进
  first-line-indent: (amount:2em, all: true), // 所有段落首行缩进2个字符
)
// 通用样式覆写器, 相当于 CSS 样式表
#show heading: set block(below: 1em)  // 增大标题的下间距
#show title: set text(size: 17pt)     // 定义 title 类型, 并设置样式
#show title: set align(center)        // 让 title 居中显示
#show title: set block(below: 1.2em)  // 增大 title 的底部间距

// #outline()  // 显示大纲目录



#title[Typst 文档说明]

= 文档说明

Typst 文档由 [文档块] 和 {代码块} 混合嵌套组成;

Typst 文档默认处于文档模式;

document mode 适合进行内容创作和排版, 支持 Markdown 风格的文本格式化、公式、图表等;

= 文档模式


=== 用 `=` 号设置标题级别

==== 标题

段落

- 无序列表
+ 有序列表

*粗体*

_斜体_

公式: $f(x) = sin(x)$

$"公式内部纯文本: ABC"$

行内代码: `hello` // 行内代码

代码块:
```python
def greet():
    print("Hello, Typst!")
```


= 代码模式


用 `#` 号进入代码模式, 代码开头要紧贴 `#` 号，不能有空格

#let name = "Typst"
欢迎使用 #name 编译器。
代码作用范围比较智能
代码作用结束后会自动回到文档模式 
可以用分号 `";"` 强制结束表达式

在代码区域内用 `[]` 嵌入文档


内容排版语法:

#v(1cm) // 插入 1 厘米的垂直间距
#text(fill:blue)[晴朗] // 这段文字会变成蓝色
#align(center)[我想居中]
#rect(stroke: red)[给这段文字加个红框]

#align(center)[
  这段文字将会居中显示
] // 方括号内切回 Markup 模式，可以写任意图文

样式设置命令（Set 与 Show）


// 让接下来所有的粗体文本都变成红色
#show strong: set text(fill: red)

*这段话会变成红色的粗体*

= 文档模式


// 2. 绘制表格
#figure(
  table(
    columns: (1fr, 2fr), // 两列，宽度比例 1:2
    [学号], [姓名],       // 表头
    [001],  [张三],
    [002],  [李四],
  ),
  caption: [学生信息表],
)

// 3. 原生代码块（支持行号和主题）
```js
function greet() {
    console.log("Hello, Typst!");
}
```

$ x_i^2 + y_(n+1) $   // 上下标
$ (x + y) / (z + 1) $ // 分式（自动识别括号为分子分母）
$ sqrt(x^2 + 1) $     // 根式

Typst 公式语法比 LaTeX 简洁:

$ "公式中的纯文本:ABC" $

$alpha, beta, theta$

$->, =>, -->$

$infinity, partial$

$sum, integral$


// 矩阵：分号表示换行，逗号分隔元素
$ mat(1, 2; 3, 4) $

// 分段函数
$ f(x) = cases(
  x^2 "if" x < 0,
  x   "if" x >= 0,
) $






== 将Jupyter notebook嵌入到Typst文件中

#import "@preview/callisto:0.2.5"

#callisto.render(
  nb: json(".example/Notebook.ipynb")  // 加载你的ipynb文件
)






== 表格

#figure(
  table(
    // 对齐方式：水平居中 + 垂直居中
    align: center + horizon,
    // 列宽：第一列自适应，后面三列平均分配剩余空间
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

== 插图

#figure(
  rect(stroke: 0.5pt + gray,  inset: 0%)[
    //#image("", width: 90%)
  ],
  caption: [带边框和标题的插图],
)

== Mermaid 图表

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



== Flowchart 图表

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



== 状态机图

#import "@preview/finite:0.5.0"

#finite.automaton(
  // 2. 状态转移字典（标准状态名称作为键值）
  (
    S0: (S0: "1", S1: "0"), // 初始状态
    S1: (S1: "0", S2: "1"), // 收到 0
    S2: (S0: "1", S3: "0"), // 收到 01
    S3: (S1: "0", S4: "1"), // 收到 010
    S4: (S0: "1", S3: "0"), // 收到 0101（检测成功，若来 0 回到 S3 重叠复用，若来 1 彻底失效回 S0）
  ),
  
  // 3. 配置初始状态与接受（最终）状态
  initial: "S0",          // 自动添加 Start 复位箭头
  final: ("S4"),          // 检测成功状态，自动渲染为双圈
  layout:finite.layout.circular.with(
    offset:45deg,
    spacing:3, // 增大状态间距避免重叠
  ),
)





== 作业模板


#import "@preview/problemst:0.1.2": pset

#show: pset.with(
  class: "6.100",
  student: "Alyssa P. Hacker",
  title: "PSET 0",
  date: datetime.today(),
  collaborators: ("Ben Bitdiddle", "Louis Reasoner"),
)

#let deriv(num, dnm) = [$ (d num) / (d dnm) $]

= Definition of the derivative
Something something infinitesimals something something. We can then define the derivative as the limit of the difference quotient as $Delta x arrow 0$:
$ deriv(f(x), x)&= lim_(Delta x arrow 0) (f(x + Delta x) - f(x)) / (Delta x). $

== Code!
```go
import "fmt"

func main() {
  fmt.Println("python sux!!1!")
}
```

=== Subproblem
We can nest subproblems!

==== Subsubproblem
As far as we want!

#pagebreak()

We also have a nice little header for the ensuing pages!