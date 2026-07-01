/* 最长双向递减子序列
8
8 8 5 10 6 3 9 12

最少需要移除几个数字, 使剩余的数字构成一个最长的双向递减子序列(先递增后递减序列);
(允许递增或递减的部分为空);
(允许非严格递增或递减, 即允许相邻数字相等)

输出:
4

解释: 保留 [5,10,6,3] 构成一个最长的双调子序列, 长度为 4, 需要移除 8-4=4 个数字。

输入:
13
308 186 283 113 338 39 364 14 364 99 164 81 187
输出:
7

*/

// 思路: 取第 i 个数字作为峰值, 计算以第 i 个数字为峰值的最长双调子序列长度;
// 先计算以 a[i] 为结尾的最长递增子序列长度 up[i]; 
// 再计算以 a[i] 为开头的最长递减子序列长度 dn[i];
// 再遍历所有的 i, 计算 up[i] + dn[i] - 1 的最大值, 即为最长双调子序列长度;


#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> up(n, 1), dn(n, 1);

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (a[i] >= a[j]) {
                up[i] = max(up[i], up[j] + 1);
            }
        }
    }

    for (int i = n - 2; i >= 0; --i) {
        for (int j = i + 1; j < n; ++j) {
            if (a[i] >= a[j]) {
                dn[i] = max(dn[i], dn[j] + 1);
            }
        }
    }

    int max_length = 0;
    for (int i = 0; i < n; ++i) {
        max_length = max(max_length, up[i] + dn[i] - 1);
    }

    cout << n - max_length << endl;

    return 0;
}