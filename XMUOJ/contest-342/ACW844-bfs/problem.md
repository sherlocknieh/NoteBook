# ACW844 BFS试炼之走迷宫

- 比赛：算法设计与分析2026第四次实验课（曹刘娟、张德富、沈思淇）
- 题型：OI
- 难度：Mid
- 语言：C, C++, Python3

## 题目描述

<p style="margin-left: 0px;">给定一个n*m的二维整数数组，用来表示一个迷宫，数组中只包含0或1，其中0表示可以走的路，1表示不可通过的墙壁。</p><p>最初，有一个人位于左上角(1, 1)处，已知该人每次可以向上、下、左、右任意一个方向移动一个位置。</p><p>请问，该人从左上角移动至右下角(n, m)处，至少需要移动多少次。</p><p>数据保证(1, 1)处和(n, m)处的数字为0，若不存在从左上角到右下角的通路，请输出0。</p><p><span style="color: rgb(227, 55, 55);">数据范围：1&lt;=n&lt;=10</span></p>

## 输入描述

<p>第一行包含两个整数n和m。</p><p>接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。</p>

## 输出描述

<p><span style="color: rgb(51, 51, 51);">输出一个整数，表示从左上角移动至右下角的最少移动次数。</span><br /></p>

## 样例

### 样例 1

#### 输入

```text
5 5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
```

#### 输出

```text
8
```

## 提示

<p><a href="https://www.acwing.com/problem/content/846/" target="_blank">原题链接</a></p><p><a href="https://www.acwing.com/video/276/" target="_blank">Y总讲解</a></p><p><a href="https://www.acwing.com/activity/content/code/content/8077906/" target="_blank">参考代码</a></p>
