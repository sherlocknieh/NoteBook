#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m, n;
    while (cin >> k >> m >> n) {
        vector<vector<int>> graph(m + 1);
        for (int i = 0; i < k; ++i) {
            int u, v;
            cin >> u >> v;
            if (1 <= u && u <= m && 1 <= v && v <= n) {
                graph[u].push_back(v);
            }
        }

        vector<int> match(n + 1, -1);

        function<bool(int, vector<char>&)> dfs = [&](int u, vector<char>& visited) {
            for (int v : graph[u]) {
                if (visited[v]) {
                    continue;
                }
                visited[v] = true;
                if (match[v] == -1 || dfs(match[v], visited)) {
                    match[v] = u;
                    return true;
                }
            }
            return false;
        };

        int max_match = 0;
        for (int u = 1; u <= m; ++u) {
            vector<char> visited(n + 1, false);
            if (dfs(u, visited)) {
                ++max_match;
            }
        }

        cout << max_match << '\n';
    }

    return 0;
}
