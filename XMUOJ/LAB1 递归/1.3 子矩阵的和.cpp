#include <bits/stdc++.h>
using namespace std;

static long long prefix_sum[1005][1005];

void algorithm() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) {
        return 0;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            long long x;
            cin >> x;
            prefix_sum[i][j] = x + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1];
        }
    }

    while (q--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        long long ans = prefix_sum[x2][y2]
                      - prefix_sum[x1 - 1][y2]
                      - prefix_sum[x2][y1 - 1]
                      + prefix_sum[x1 - 1][y1 - 1];
        cout << ans << '\n';
    }
}

void test() {
    string input = "3 4 2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n1 1 2 2\n2 2 3 4";
    cin.clear();
    cin.str(input);
    algorithm();
}

int main() {
    // 如果有 TEST 宏定义，运行测试函数, 否则运行主函数
    #ifdef TEST
        test();
    #else
        algorithm();
    #endif
    return 0;
}

