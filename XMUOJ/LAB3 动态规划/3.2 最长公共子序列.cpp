// 最长公共子序列

// 输入:
// 4 5
// acbd
// abedc

// 输出:
// 3

#include <bits/stdc++.h>
using namespace std;

int main() {

    int m, n;
    cin >> m >> n;

    string A, B;
    cin >> A >> B;

    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

    // F([acbd],[abedc]) = max(F([acbd],[abed]), F([acb],[abedc]), 1+F([acb],[abed]) if A[-1] == B[-1])
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (A[i - 1] == B[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[m][n] << endl;
    return 0;
}