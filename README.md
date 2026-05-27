# NoteBook

VSCode 中文+公式+代码+插图混合写作方案实践笔记

# 方案一：Markdown


- 适合写草稿, 堆内容; 

依赖:

- Markdown Preview Enhanced (VSCode 插件)
  - 支持 LaTeX + Mermaid + TikZ 的显示
  - 支持导出 PDF (利用 Chrome 或 Edge 浏览器)

补充:

- 需要微调格式, 美化布局时能感受到局限性;
- 导出的 Mermaid 和 TikZ 图不能居中显示;

示例文件:

- [example.md](./example.md)




# 方案二：Jupyter Notebook

- 适合写算法习题, 可以边写边运行代码

依赖:

- Jupyter (VSCode 插件)
- ipykernel (Python 包)
  - `uv pip install ipykernel`


补充:

 - markdown 的预览效果依赖于 vscode 内置的支持 (vscode 已经内建支持 LaTeX 公式和 Mermaid 预览)

- 支持导出 HTML, 然后用 Chrome 或 Edge 打印成 PDF;

- 也支持直接导出 PDF, 但依赖于 LaTeX 环境, 还要解决中文显示问题, 较为麻烦;


示例文件: 

- [example.ipynb](./example.ipynb)




# 方案三：Typst

- 既能快速写作, 也能精细排版;
- 适合写论文, 报告, 或者简历;

依赖:

- Tinymist Typst (VSCode 插件)
- Typst: `winget install Typst`

补充:

- 默认模式下和 Markdown 一样方便;
- 公式的语法比 LaTeX 简洁;
- 可以用代码微调格式, 美化布局;
- 有丰富的第三方模板和库, 能在线导入使用;
- AI 不太熟悉 Typst 最新语法, 生成的代码总是有BUG;

示例文件: [example.typ](./example.typ)