// 全局格式设置

// 导入夜间主题
#import "@preview/nordic:0.1.0" as nordic
#show: nordic.default

// 页面格式设置
#set page(
  // paper: "a4",    // 纸张大小
  // margin: 2cm,    // 页面边距
  // numbering: "1", // 开启页码
)
// 文本格式设置
#set text(
  font: ("Arial", "Microsoft YaHei")
)
// 标题格式设置
#set heading(
  numbering: "1." // 开启自动编号
)
// 段落格式设置
#set par(
  // first-line-indent: 2em, // 首行缩进2个字符, 靠近标题的第一段不缩进
  // first-line-indent: (amount:2em, all: true), // 所有段落首行缩进2个字符
)


// 通用样式覆写器, 相当于 CSS 样式表
#show heading: set block(below: 1em)  // 增大标题的下间距

#show title: set text(size: 17pt)     // 定义 title 类型
#show title: set align(center)        // 让 title 居中显示
#show title: set block(below: 1.2em)  // 增大 title 底部间距

#title[标题]

// 大纲目录
// #outline()


Typst 文档由 [文档块] 和 {代码块} 混合嵌套组成;

默认处于 [文档模式] :

= 文档模式

== 二级标题

段落

- 无序列表
+ 有序列表
*粗体*
_斜体_



- 代码块:

  行内源码: `hello`

  ```python
  def greet():
      print("Hello, Typst!")
  ```

- 公式:

  行内公式: $f(x) = sin(x)$

  居中公式:

$ sqrt(x^2 + 1) $
$ A_i^2 + y_(n+1) $
$ (x + y)/(z + 1) $


$ alpha, beta, theta $

$ ->, =>, --> $

$ infinity, partial $

$ sum, integral $

$ "ABC" $

// 矩阵：分号表示换行，逗号分隔元素
$ mat(
  1, 2;
  3, 4) $

// 分段函数
$ f(x) = cases(
  x^2 "if" x < 0,
  x   "if" x >= 0,
) $



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
#rect(stroke: red)[红框]
#text(fill:blue)[蓝色]
#align(center)[居中]




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

== Flowchart 图表

#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge

#figure(
  diagram(
    node-stroke: 1pt,
    spacing: 4em,
    
    node((0,0.5), [数据库]),
    node((1,0), [关系型数据库]),
    node((1,1), [非关系型数据库]),
    node((2,0), [PGSQL]),
    
    edge((0,0.5), (1,0), "-"),
    edge((0,0.5), (1,1), "-"),
    edge((1,0), (2,0), "-"),
  ),
  caption: [数据库分类示例],
)


