// 矩阵链乘法问题

// 输入
// 6
// 30 35
// 35 15
// 15 5
// 5 10
// 10 20
// 20 25

// 第一行输入矩阵的总个数n
// 后n行是每个矩阵的行列维数

// 输出少乘法次数
// 15125

// 动态规划算法, A 是矩阵链的维数表, n 是矩阵链的长度

#include <bits/stdc++.h>
using namespace std;

int matrix_chain_order(int A[][2], int n)
{
    int memo[n][n];
    memset(memo, 0, sizeof(memo));
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            for (int k = i; k < j; k++) {
                int q = memo[i][k] + memo[k + 1][j] + A[i][0] * A[k][1] * A[j][1];
                if (memo[i][j] == 0 || q < memo[i][j]) {
                    memo[i][j] = q;
                }
            }
        }
    }
    return memo[0][n-1];
}

void test()
{
    int n = 6;
    int A[n][2] = { {30, 35}, {35, 15}, {15, 5}, {5, 10}, {10, 20}, {20, 25} };
    cout << matrix_chain_order(A, n) << endl;
}

int main()
{
    test();
    int n;
    cin >> n;
    int A[n][2];
    for (int i = 0; i < n; i++) {
        cin >> A[i][0] >> A[i][1];
    }
    cout << matrix_chain_order(A, n) << endl;
    return 0;
}
