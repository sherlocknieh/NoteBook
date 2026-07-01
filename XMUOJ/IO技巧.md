# 输入
```python
n = int(input())
m, n = map(int, input().split())
a = list(map(int,input().split()))

a = [int(x) for x in input().split()]    # 也可以用列表推导式


# 全部读入再处理:
import sys
input_data = sys.stdin.read().splitlines()

m, n = map(int, input_data[0].split())
a = list(map(int, input_data[1].split()))
```

# 输出
```python
数列:
print(*a)   # 把数列解包为参数

# 小数点后保留两位:
print("%.2f" % x)   # 旧式格式化输出
print(f"{x:.2f}")   # f-string格式化输出
```



# C语言输入输出
# 输入
```C
int n;
scanf("%d", &n);
int m, n;
scanf("%d %d", &m, &n);

int *a = (int*)malloc(n * sizeof(int));

for(int i=0; i<n; i++)
    scanf("%d", &a[i]);
```
# 输出
```C
for(int i=0; i<n; i++)
    printf("%d ", a[i]);
printf("\n");

// 小数点后保留两位:
printf("%.2f\n", x);
```

# C++ 输入
```C++
int n;
cin >> n;
int m, n;
cin >> m >> n;

vector<int> a(n);
for(int i=0; i<n; i++)
    cin >> a[i];
```

