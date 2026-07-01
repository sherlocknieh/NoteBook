/*
输入:
n
a[n]
输出:
b[n]

b[i] 表示 a 中所有比 a[i] 大的数的和(严格大于 a[i])，如果没有比 a[i] 大的数，则 b[i] = 0。

样例1:
5
2 3 3 4 4
输出
14 8 8 0 0

样例2:
10
31 42 59 26 53 58 97 93 23 54
输出
456 414 190 487 361 249 0 97 513 307
*/


#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].first;
        a[i].second = i;
    }

    // 按照数值从大到小（降序）排序
    sort(a.rbegin(), a.rend());

    // 初始化答案数组
    vector<ll> b(n, 0);
    
    // 计算前缀和
    ll prefix_sum = 0;
    for (int i = 0; i < n; ++i) {
        int val = a[i].first;
        int idx = a[i].second;
        b[idx] = prefix_sum;
        prefix_sum += val;
        if (i > 0 && a[i].first == a[i - 1].first) {
            // 如果当前元素与前一个元素相同，则不更新前缀和
            b[idx] = b[a[i - 1].second];
        }
    }

    // 输出结果，以空格分隔
    for (int i = 0; i < n; ++i) {
        cout << b[i] << (i == n - 1 ? '\n' : ' ');
    }

    return 0;
}