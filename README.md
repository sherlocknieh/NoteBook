# NoteBook

VSCode 中文+公式+代码+插图混合写作方案实践

## 方案一：[Markdown.md](.examples/Markdown.md)

依赖:

- VSCode 插件:
  - Markdown Preview Enhanced
    - 支持 LaTeX + Mermaid + TikZ 的显示
    - 支持导出 PDF (利用浏览器的打印功能)

评价:

- 适合写作业/笔记/文档/论文草稿(堆内容阶段);
- AI 支持性较好, 生成效率高;
- 默认布局虽然不够美观, 但是能看;
- 只有需要微调格式/美化布局时才能感受到不够用;


问题:

- Mermaid 和 TikZ 图不能居中显示;

- 作业习题排版问题:

  - 习题的描述区和答案区没有很好的视觉区分手段:
    - 在答案区域使用引用包裹, 可以实现视觉区分, 但是每新增一行都要打一个 '>', 不方便编辑;
    - 改为在题目描述区域使用引用, 可以减少 '>' 的使用, 但是真的很难看;

  - 题号和题目描述不能写在同一行:
    - 题号独占一行, 可以使用标题效果, 方便代码折叠以及快速导航, 但是有点丑; 写在同一行更美观, 但是会失去标题效果及其带来的便利;
  
  - 目前最佳实践:
    - 题号单独一行, 使用四级或五级标题;
    - 题目描述写在标题下方, 不使用引用;
    - 题目和答案之间写一个答, 独占一行;
    - 答案正文使用引用包裹, 写在答下方;
    - 答案中的代码块不需要包裹在引用中;
    - 答案如果有分段小标题, 不需要引用;

## 方案二：[Jupyter Notebook.ipynb](.examples/Notebook.ipynb)


依赖:

- 系统依赖:
  - Python: `winget install Python`


- VSCode插件:
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
