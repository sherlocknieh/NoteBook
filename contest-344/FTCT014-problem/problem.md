# FTCT014 厦门大学的年夜饭

- 比赛：算法设计与分析2026第五次实验课（曹刘娟、张德富、沈思淇）
- 题型：OI
- 难度：Low
- 语言：C, C++, Java, Python3

## 题目描述

<p><span style="color: rgb(73, 80, 96);">寒假留校，厦门大学向留校师生发放年夜饭的免费就餐券，只能用一个餐盘凭借就餐券打不同的菜肴，假设每一道菜肴都有相应的价格，装在不同体积的菜碟中，只能一样打一份；而餐盘的容量有限，请问如何搭配出总价格最高的菜肴？</span><b></b><br /></p><p><span style="color: rgb(73, 80, 96);"><br /></span></p><p><span style="color: rgb(73, 80, 96);">出题者：王新同学</span></p>

## 输入描述

<p><span style="color: rgb(73, 80, 96);">第一行两个整数</span><span style="color: rgb(73, 80, 96);">N,V(1&lt;=N&lt;=8,1&lt;=V&lt;=2000000000),</span><span style="color: rgb(73, 80, 96);">表示菜肴的数量和餐盘的容量。</span></p><p><span style="color: rgb(73, 80, 96);">接下来</span><span style="color: rgb(73, 80, 96);">N</span><span style="color: rgb(73, 80, 96);">行</span><span style="color: rgb(73, 80, 96);">:</span></p><p><span style="color: rgb(73, 80, 96);">每行有两个整数</span><span style="color: rgb(73, 80, 96);">v,w(1&lt;=v&lt;=1000000000,1&lt;=w&lt;=1000000),</span><span style="color: rgb(73, 80, 96);">表示盛装菜肴的菜碟体积和菜肴的价格。</span><b><br /></b></p>

## 输出描述

<p><span style="color: rgb(73, 80, 96);">输出最大价格。</span><b></b><br /></p>

## 样例

### 样例 1

#### 输入

```text
4 5
1 2
2 4
3 4
4 5
```

#### 输出

```text
8
```

## 提示

<p>N很小可以回溯</p><p><br /></p><p>实际情况是2022年春节，学校提供3天共9顿免费的餐券，价值大概是早餐7元，中午和下午的是12元。</p>
