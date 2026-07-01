# NoteBook

VSCode 中文+公式+代码+插图混合写作方案实践

## 方案一：[Markdown.md](.examples/Markdown.md)

依赖:

- VSCode 插件:
  - Markdown Preview Enhanced
    - 支持 LaTeX + Mermaid + TikZ 的显示
    - 支持导出 PDF (利用浏览器的打印功能)




## 方案二：[Jupyter Notebook.ipynb](.examples/Notebook.ipynb)


依赖:

- 系统依赖:
  - Python: `winget install Python`


- VSCode 插件:
  - Jupyter


- Python库:
  - ipykernel: `uv add ipykernel`
  - notebook: `uv add notebook`
    - 可选, 导出文档时需要

补充:

- 可以边写边文档边运行代码, 适合写算法笔记/教程/文档;

- 预览效果依赖于 vscode 内置的支持 (vscode 已经内建支持 LaTeX 公式和 Mermaid 预览)

- 如果用来写算法作业, 需要导出 PDF 提交的话, 体验不如直接用 markdown 文档:
  - 在 .ipynb 中运行代码有几率卡死, 调试也不方便;
  - 从 .ipynb 导出 PDF 不如 .md 方便;

- 支持导出 HTML, 然后用 Chrome 或 Edge 打印成 PDF;

- 也支持直接导出 PDF, 但依赖于 LaTeX 环境, 还要解决中文显示问题, 较为麻烦;


## 方案三：[Typst.typ](.examples/Typst.typ)

依赖:

- Tinymist Typst (VSCode 插件)
- Typst: `winget install Typst`

补充:

- 默认模式下和 Markdown 一样方便;
- 公式的语法比 LaTeX 简洁;
- 可以用代码微调格式, 美化布局;
- 有丰富的第三方模板和库, 能在线导入使用;
- AI 不太熟悉 Typst 最新语法, 生成的代码总是有BUG;

总结:

- 既能快速写作, 也能精细排版;
- 适合写论文, 报告, 或者简历;