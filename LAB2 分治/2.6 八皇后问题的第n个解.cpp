// 输入一个数 m，输出八皇后问题的第 m 个解(字符串)。

// 输入: 第一行代表有 n 组输入数据, 其余 n 行每输入一个数 m, 输出第 m 个解。
// 2
// 1
// 92

// 输出:
// 15863724
// 84136275


#include <bits/stdc++.h>
using namespace std;


int queen[8];         // 用 queen[i] 记录第 i 行的皇后在第几列
int counter;          // 计数器，记录已找到的解的个数
int target;           // 目标解的编号
string result;        // 存储第 target 个解


// 检查在 (r, c) 位置放置皇后是否安全
bool is_safe(int r, int c) {
    // 逐行检查
    for (int i = 0; i < r; i++) {
        // 检查第 i 行的皇后是否在同一列或对角线上
        if (queen[i] == c || abs(queen[i] - c) == abs(i - r)) {
            return false;
        }
    }
    return true;
}

// 回溯算法求解八皇后
void backtrack(int row) {
    // 已找到第 target 个解
    if (counter == target) {
        return;
    }
    // 已放置完 8 个皇后，找到一个解
    if (row == 8) {
        counter++;
        if (counter == target) {
            // 将解转换为字符串
            result = "";
            for (int i = 0; i < 8; i++) {
                result += char('1' + queen[i]);
            }
        }
        return;
    }
    // 尝试在当前行的每一列放置皇后
    for (int c = 0; c < 8; c++) {
        if (is_safe(row, c)) {
            queen[row] = c;
            backtrack(row + 1);
            if (counter == target) {
                return;  // 已找到，停止搜索
            }
        }
    }
}

// 获取八皇后问题的第 m 个解
void get_queen_solution(int m) {
    target = m;
    // 初始化计数器和棋盘状态
    counter = 0;
    memset(queen, 0, sizeof(queen));
    result = "";
    // 从第 0 行开始递归回溯
    backtrack(0);
}

void test() {
    get_queen_solution(1);
    cout << result << endl;
    get_queen_solution(92);
    cout << result << endl;
}

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> target;
        get_queen_solution(target);
        cout << result << endl;
    }
}

int main() {
    test();
    //solve();
    return 0;
}
