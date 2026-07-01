// # 输入
// # 第一行包含两个整数n和m。
// # 接下来n行，每行包含m个整数（0或1），表示完整的二维数组迷宫。
// # 5 5
// # 0 1 0 0 0
// # 0 1 0 1 0
// # 0 0 0 0 0
// # 0 1 1 1 0
// # 0 0 0 1 0

// # 输出
// # 8
// # 输出一个整数，表示从左上角移动至右下角的最少移动次数。

#include<bits/stdc++.h>
using namespace std;

struct Node {
    int x, y, steps;
};

int main()
{
    int n,m;
    cin >> n >> m;
    vector<vector<int>> maze(n, vector<int>(m));
    for(int i=0; i<n; i++){
    for(int j=0; j<m; j++){
    cin >> maze[i][j];}}
    
    // 4 个方向: 上、左、下、右
    int dx[4] = {-1,0,1,0};
    int dy[4] = {0,-1,0,1};

    queue<Node> q;
    q.push({0, 0, 0});
    while(!q.empty()){
        auto top = q.front();
        q.pop();
        int x = top.x;
        int y = top.y;
        int steps = top.steps;

        if(x == n-1 && y == m-1){
            cout << steps << endl;
            return 0;
        }

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < m && maze[nx][ny] == 0){
                maze[nx][ny] = 1; // Mark as visited
                q.push({nx, ny, steps + 1});
            }
        }
    }
    return 0;
}