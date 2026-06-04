# ACW1087 修剪草坪

- 比赛：算法设计与分析2026第七次实验课（曹刘娟、张德富、沈思淇）
- 题型：OI
- 难度：Mid
- 语言：C, C++, Java, Python3

## 题目描述

<p>海拉鲁草坪大赛在即，林克翻出仓库里的智能割草机器人 —— 这些机器人排成 1 到 N 号的队列，每个机器人 i 的割草效率为 Eᵢ。</p><p>但机器人的 AI 能源模块有设计缺陷：如果连续启动超过 K 个机器人，它们会因能源矩阵过载进入「待机充电模式」，无法继续工作！</p><p><strong>机器人操作规则</strong></p><p>机器人排成一列，效率值为 E₁到 Eₙ；</p><p>不能连续启动超过 K 个机器人（比如 K=2 时，启动 3 个连续会触发过载待机）；</p><p>求能启动的机器人最大效率总和。</p>

## 输入描述

<p>第一行：N（机器人数量）和 K（最大连续启动数）</p><p>接下来 N 行：每行一个数 Eᵢ（第 i 个机器人的效率）</p>

## 输出描述

<p>一个整数，即不触发过载的最大效率和</p><p><strong>数据范围</strong></p><p>1≤N≤10^5</p><p>0≤Ei≤10^9</p>

## 样例

### 样例 1

#### 输入

```text
5 2
1
2
3
4
5
```

#### 输出

```text
12
```

## 提示

<p><a href="https://www.acwing.com/problem/content/1089/" target="_blank">原题链接</a><br /></p><p><a href="https://www.acwing.com/video/430/" target="_blank">Y总讲解</a><br /></p><p><a href="https://www.acwing.com/solution/content/5362/" target="_blank">参考题解</a><br /></p><p><a href="https://www.acwing.com/activity/content/code/content/128401/" target="_blank">Y总代码</a><br /></p>
