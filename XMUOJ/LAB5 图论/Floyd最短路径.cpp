/*描述

给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。

再给定 k 个询问，每个询问包含两个整数 x 和 y，表示查询从点 x 到点 y 的最短距离，如果路径不存在，则输出 impossible。

数据保证图中不存在负权回路。

数据范围

1≤n≤200,

1≤k≤n^2,

1≤m≤20000,

图中涉及边长绝对值均不超过 10000。


输入

第一行包含三个整数 n, m, k。

接下来 m 行，每行包含三个整数 x, y, z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

接下来 k 行，每行包含两个整数 x, y，表示询问点 x 到点 y 的最短距离。


输出

共 k 行，每行输出一个整数，表示询问的结果，若询问两点间不存在路径，则输出 impossible。


输入样例:
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3

输出样例:
impossible
1
*/
#include <bits/stdc++.h>
using namespace std;


const int INF = 0x3f3f3f3f;

int n, m, k;

// 构建容器
int dist[205][205];

// 输入数据
int main() {
    int n, m, k;
    cin >> n >> m >> k;

    // 初始化距离矩阵
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            if(i == j) dist[i][j] = 0;
            else dist[i][j] = INF;
        }
    }

    // 读取边信息
    for(int i = 1; i <= m; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        dist[x][y] = min(dist[x][y], z); // 处理重边，取最小值
    }

    // Floyd-Warshall算法计算最短路径
    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    // 处理查询
    for(int i = 1; i <= k; i++) {
        int x, y;
        cin >> x >> y;
        if(dist[x][y] > INF/2) { // 如果距离大于INF的一半，说明不存在路径
            cout << "impossible" << endl;
        } else {
            cout << dist[x][y] << endl;
        }
    }
}