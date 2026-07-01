// 最小费用覆盖特征集合

// 输入:
// 4 3
// 5 C
// 6 B
// 16 BAC
// 4 A

// 第一行两个整数 T, n
// T 表示配料数量
// n = 3 表示必需配料为 A、B、C。
// 接下来 T 行，每行包含 w:价格 s:包含的配料


// 输出:
// 15
// 选择第 1、2、4 种配料，总价 5 + 6 + 4 = 15，优于买第 3 种配料。


// 输入:
// 1 2
// 10 A

// 输出:
// -1

// n = 2 表示必需配料为 A、B;
// 商店只有含 A 的配料，无法满足要求，输出 -1.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T, n;
    cin >> T >> n;
    
    vector<pair<int, string>> ingredients;
    for (int i = 0; i < T; i++) {
        int w;
        string s;
        cin >> w >> s;
        ingredients.push_back({w, s});
    }
    
    vector<int> dp(1 << n, INT_MAX);
    dp[0] = 0;
    
    for (auto [w, s] : ingredients) {
        int mask = 0;
        for (char c : s) {
            mask |= 1 << (c - 'A');
        }
        for (int i = 0; i < (1 << n); i++) {
            if (dp[i] != INT_MAX) {
                dp[i | mask] = min(dp[i | mask], dp[i] + w);
            }
        }
    }
    
    int result = dp[(1 << n) - 1];
    if (result == INT_MAX) {
        cout << -1 << endl;
    } else {
        cout << result << endl;
    }
    
    return 0;
}