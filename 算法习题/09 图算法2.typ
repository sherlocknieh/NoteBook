// 全局格式设置


// 导入夜间主题
#import "@preview/nordic:0.1.0" as nordic
#show: nordic.default

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
  // numbering: "1." // 开启自动编号，格式为 1.、1.1.、1.1.1. 等
)
// 段落格式设置
#set par(
  // first-line-indent: 2em, // 首行缩进2个字符, 靠近标题的第一段不缩进
  // first-line-indent: (amount:2em, all: true), // 所有段落首行缩进2个字符
)
// 通用样式覆写器, 相当于 CSS 样式表
#show heading: set block(below: 1em)  // 增大标题的下间距
#show title: set text(size: 17pt)     // 定义 title 类型, 并设置样式
#show title: set align(center)        // 让 title 居中显示
#show title: set block(below: 1.2em)  // 增大 title 的底部间距


#title[第9章 图算法+]

= 最大流问题


初始管道容量:
```mermaid
graph LR
    S(("S"))
    A(("A"))
    B(("B"))
    T(("T"))

    S ==1==> A
    A ==1==> T
    A ==1==> B
    S ==1==> B
    B ==1==> T
```

== Flowchart 图表

#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge

#figure(align(center)[
    #diagram(
    node-stroke: 1pt,
    spacing: 4em,
    
    node((-2,0), [S]),
    node((0,-1), [A]),
    node((0,1), [B]),
    node((2,0), [T]),
    
    edge((0,0), (-1,0), "-"),


    )]
)
