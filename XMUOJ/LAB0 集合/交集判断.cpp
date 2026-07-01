/* 输入格式:
n m
A1 A2 ... An
b1 b2 ... bm

含义:
n 为 A 的长度, m 为 b 的长度, m < n;
A 是一个数组, b 是一组下标, 表示 A 的一个子集; (下标从 1 开始计数)
如果 A 中最大值对应的下标出现在 b 中，则输出 Yes，否则输出 No。

输入:
5 3
6 8 10 7 10
1 2 3

输出:
Yes

解释:
A 中最大值为 10, 对应的下标为 3 和 5
b 中包含下标 3, 所以输出 Yes。
*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,m;
    cin >> n >> m;
    vector<int> a(n);
    
    int max_value = INT_MIN;
    for (int i = 0; i < n; i++){
        cin >> a[i];
        max_value = max(max_value, a[i]);
    }

    for (int i = 0; i < m; i++){
        int index;
        cin >> index;
        if (a[index - 1] == max_value){
            cout << "Yes" << endl;
            return 0;
        }
    }
    
    cout << "No" << endl;
    return 0;
}


