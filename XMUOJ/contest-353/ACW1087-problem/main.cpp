#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    if (!(cin >> N >> K)) return 0;
    vector<ll> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    
    // 动态规划, O(NK)
    vector<ll> dp(K + 1, 0);
    for (int i = 0; i < N; ++i) {
        ll save = dp[K];
        for (int j = K; j >= 1; --j) {
            dp[j] = max(save, A[i] + dp[j - 1]);
        }
        dp[0] = save;
    }

    cout << dp[K] << '\n';
    return 0;
}