/*
石子游戏
描述

将N(1<=N<=100)个石子摆成一圈.现在要将石子有次序地合并成一堆.

规定每次只能选相邻的两堆合并成新的一堆,并将新的一堆的石子数记为该次合并的得分.

请你计算这个游戏的最小得分和最大得分.


输入

数据的第1行是正整数N(1<=N<=100),表示有N堆石子.

第2行有N个整数.第i个整数ai(1<=ai<=10)​表示第i堆石子的个数.


输出

输出共2行,第1行为最小得分,第2行为最大得分.


输入样例 1 

4
4 5 9 4
输出样例 1

43
54
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 0x3f3f3f3f;

int main() {
    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(2 * n + 1);
    vector<int> sum(2 * n + 1, 0);

    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        a[i + n] = a[i]; // 断环成链，复制一份
    }

    // 计算前缀和
    for (int i = 1; i <= 2 * n; ++i) {
        sum[i] = sum[i - 1] + a[i];
    }

    // dp_min 初始化为正无穷，dp_max 初始化为 0
    vector<vector<int>> dp_min(2 * n + 1, vector<int>(2 * n + 1, INF));
    vector<vector<int>> dp_max(2 * n + 1, vector<int>(2 * n + 1, 0));

    // 自合并变一堆的得分为 0
    for (int i = 1; i <= 2 * n; ++i) {
        dp_min[i][i] = 0;
        dp_max[i][i] = 0;
    }

    // 区间 DP：先枚举区间长度 len，再枚举起点 i
    for (int len = 2; len <= n; ++len) { 
        for (int i = 1; i + len - 1 <= 2 * n; ++i) {
            int j = i + len - 1;
            int total_weight = sum[j] - sum[i - 1];
            
            // 枚举分割点 k
            for (int k = i; k < j; ++k) {
                dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j] + total_weight);
                dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j] + total_weight);
            }
        }
    }

    // 统计答案：在所有长度为 n 的区间中求最值
    int ans_min = INF;
    int ans_max = 0;
    for (int i = 1; i <= n; ++i) {
        ans_min = min(ans_min, dp_min[i][i + n - 1]);
        ans_max = max(ans_max, dp_max[i][i + n - 1]);
    }

    cout << ans_min << endl;
    cout << ans_max << endl;

    return 0;
}