# 标题

### 题目

题目描述

### 回答

> 这是一个引用块，可以用来引用文本或者代码。

### 代码

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
```

### 公式

- 行内公式：$E=mc^2$
- 块级公式：

$$f(x) = \int_{-\infty}^{\infty} e^{-t^2} dt$$

- 矩阵：
$$
\begin{bmatrix}
a & b \\ c & d
\end{bmatrix}
$$

- 箭头：

$$ x \xrightarrow{m} y $$


# 绘图

## Mermaid

```mermaid
graph TD
    A[矩形] --> B(圆形)
    A --> C{三角形}
    B --> D[填充蓝色]
    C --> E[填充红色]
```

```mermaid
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
```


## TikZ

```tikz
\begin{document}
\begin{tikzpicture}
  % Rectangle
  \draw[thick] (0,0) rectangle (2,1.5);
  % Circle
  \draw[fill=blue!20] (4,0.75) circle (0.75);
  % Triangle
  \draw[fill=red!20] (6,0) -- (7.5,0) -- (6.75,1.5) -- cycle;
\end{tikzpicture}
\end{document}
```

## HTML+CSS 增强排版

