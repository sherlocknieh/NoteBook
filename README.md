# NoteBook

文字,公式,代码,插图混合写作方案

# 方案一：Markdown

LaTeX + Mermaid + TikZ

#### 依赖

- VSCode
- Markdown Preview Enhanced (VSCode 插件)
  - 支持 LaTeX + Mermaid + TikZ 的显示
  - 支持导出 PDF (利用 Chrome 或 Edge 浏览器)

示例文件: [example.md](./example.md)


# 方案二：Typst

- 适合学术论文写作

#### 依赖

- VSCode
- Tinymist Typst (VSCode 插件)
- Typst 引擎: `winget install Typst`

示例文件: [example.typ](./example.typ)


# 方案三：Jupyter Notebook

- 适合算法习题或者笔记;

示例文件: [example.ipynb](./example.ipynb)

markdown 的预览效果依赖于 vscode 内置的支持

vscode 官方已经内建支持 LaTeX 公式和 Mermaid 预览
但是不支持导出 PDF
