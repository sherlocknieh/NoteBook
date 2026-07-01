// 共享单车

// 输入:
// 10 2
// 1 0 0 0 5 4 0 1 2 0
// 1 5
// 2 7
// 2

// 第一行为 n(天数), k(骑行卡的种类数)。
// 接下来一行有 n 个整数，表示从第 1 天至第 n 天，每天使用共享单车的次数 di。
// 接下来 K 行，每行 2 个整数，表示 ti (骑行卡的有效期)和 ci (骑行卡的价格)。
// 接最后一行表示单次使用的价格 P0

// 输出最小花费:
// 15


// 第1天,单次付费，花费2元。
// 第5、6天，购买两天的骑行卡，花费7元。
// 第8天，单次付费，花费2元。
// 第9天，单次付费，花费4元。

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,k;
    cin >> n >> k;

    vector<int> times(n);
    for (int i = 0; i < n; i++) cin >> times[i];

    vector<int> days(k);
    vector<int> cost(k);
    for (int i = 0; i < k; i++)
    {
        cin >> days[i] >> cost[i];
    }
    int P0;
    cin >> P0;

    // F(i) = min(P0*times[i] + F(i+1), cost[j] + F(i+days[j]))

    vector<int> dp(n, 0);
    for (int i = n - 1; i >= 0; i--)
    {
        dp[i] = P0*times[i];
        if(i+1<n) dp[i] += dp[i+1];
        for (int j = 0; j < k; j++)
        {
            int temp = cost[j];
            int next_day = i+days[j];
            if(next_day<n) temp += dp[next_day];
            dp[i] = min(dp[i],temp);
        }
    }
    cout << dp[0] << endl;
    return 0;
}