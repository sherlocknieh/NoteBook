// 调制四果汤（最小费用覆盖特征集合）
// 将 Python 实现转换为等价的 C++ 实现

#include <bits/stdc++.h>
using namespace std;

int main() {
    int T, n;
    if (!(cin >> T >> n)) return 0;
    
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