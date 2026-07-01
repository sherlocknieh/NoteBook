import sys

def find(x, p):
    """并查集查找操作（含路径压缩）"""
    # 如果当前节点不是自身的父亲，则递归查找其根节点，并将沿途节点的父亲直接指向根节点
    if p[x] != x:
        p[x] = find(p[x], p)
    return p[x]

def main():
    # 快速读入全部输入数据
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    # 提取 n 和 m
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 提取所有的边，每3个一组 (u, v, w)
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, v))  # 将权重 w 放在第一位，方便后面直接 sort()
        idx += 3
        
    # 1. 按照边权从小到大排序
    edges.sort()
    
    # 2. 初始化并查集，节点编号通常从 1 到 n
    p = list(range(n + 1))
    
    res = 0  # 记录最小生成树的权重之和
    cnt = 0  # 记录当前成功加入树的边数
    
    # 3. 遍历排序后的边
    for w, u, v in edges:
        root_u = find(u, p)
        root_v = find(v, p)
        
        # 如果不在同一个连通块中，说明加入这条边不会形成环
        if root_u != root_v:
            p[root_u] = root_v  # 合并连通块
            res += w            # 累加权重
            cnt += 1            # 计数加 1
            
            # 如果已经找够了 n - 1 条边，可以提前结束循环
            if cnt == n - 1:
                break
                
    # 4. 判断是否成功构成了包含所有点的生成树
    if cnt < n - 1:
        print("impossible")
    else:
        print(res)

if __name__ == "__main__":
    main()