// 2.5 残缺棋盘游戏

// 使用这四种拼图对一个 2^k x 2^k 且缺失一个格子的棋盘进行铺设:

// 1
//  @
// @@

// 2
// @
// @@

// 3
// @@
//  @

// 4
// @@
// @

// 输入棋盘大小和缺失格子的位置:
// 2
// 2 2

// 第一行是整数 k, 表示棋盘的大小为 2^k x 2^k ;
// 第二行两个整数x和y, 表示棋盘上缺失的格子的位置（x行y列）。
// 行和列的编号都从1开始。

// 输出铺设方案: (按字典序输出)
// 1 1 4
// 1 4 3
// 3 3 1
// 4 1 2
// 4 4 1

// 每行为 x y c, 
// x y 为拼图拐角的坐标，c为使用的拼图类型（1, 2, 3, 4)

// 输入2:
// 2
// 1 4

// 输出2:
// 1 1 4
// 2 3 2
// 3 2 2
// 4 1 2
// 4 4 1

// 思路: 分治
// 将棋盘分成四个象限
// 根据缺失格子所在的象限, 在棋盘中心放置一个缺口朝向该象限的拼图;
// 记下放置的拼图坐标和类型;
// 把棋盘分解为四个小棋盘继续递归;
// 最后对所有拼图进行排序并输出.

// bx, by: 棋盘左上角坐标
// px, py: 缺口的坐标
// n: 棋盘大小为 n x n (n=2^k)

#include <bits/stdc++.h>
using namespace std;

vector<tuple<int, int, int>> tiles;

void TileBoard(int x, int y, int px, int py, int n) {
    int Q = 4;
    int vx = 1, vy = 1;

    if (px - x < n / 2) {
        Q = Q / 2;
        vx -= 1;
    }
    if (py - y < n / 2) {
        Q = Q - 1;
        vy -= 1;
    }

    tiles.emplace_back(x + n / 2 - vx, y + n / 2 - vy, Q);

    if (n == 2) return;

    if (Q == 1) {
        TileBoard(x, y, px, py, n / 2);
    } else {
        TileBoard(x, y, x + n / 2 - 1, y + n / 2 - 1, n / 2);
    }
    if (Q == 2) {
        TileBoard(x, y + n / 2, px, py, n / 2);
    } else {
        TileBoard(x, y + n / 2, x + n / 2 - 1, y + n / 2, n / 2);
    }
    if (Q == 3) {
        TileBoard(x + n / 2, y, px, py, n / 2);
    } else {
        TileBoard(x + n / 2, y, x + n / 2, y + n / 2 - 1, n / 2);
    }
    if (Q == 4) {
        TileBoard(x + n / 2, y + n / 2, px, py, n / 2);
    } else {
        TileBoard(x + n / 2, y + n / 2, x + n / 2, y + n / 2, n / 2);
    }
}

void test() {
    TileBoard(1, 1, 1, 4, 4);
    sort(tiles.begin(), tiles.end(), [](const auto& a, const auto& b) {
        if (get<0>(a) != get<0>(b)) return get<0>(a) < get<0>(b);
        return get<1>(a) < get<1>(b);
    });
    for (const auto& t : tiles) {
        cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
    }
}

int main() {
    int k, x, y;
    cin >> k >> x >> y;
    TileBoard(1, 1, x, y, 1 << k);
    sort(tiles.begin(), tiles.end(), [](const auto& a, const auto& b) {
        if (get<0>(a) != get<0>(b)) return get<0>(a) < get<0>(b);
        return get<1>(a) < get<1>(b);
    });
    for (const auto& t : tiles) {
        cout << get<0>(t) << " " << get<1>(t) << " " << get<2>(t) << endl;
    }
    return 0;
}