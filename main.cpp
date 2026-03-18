// 输入: 输入数据有行，每行的第一个数 n 表示打分人数，然后是 n 个分值。
// - n 是一个在 (2, 100] 之间的整数。
// - 打分是 [0, 100] 之间的浮点数。

// 输出: 对于每组输入数据，去掉一个最高分和一个最低分，然后计算平均得分。
// - 结果保留2位小数，每组输出占一行。

// 输入样例 
// 3 96 98 97
// 4 96 99 98 97

// 输出样例
// 97.00
// 97.50

#include <stdio.h>

int main()
{
    int n;
    double score[100];
    double sum, avg;
    while (1)
    {
        int ret = scanf("%d", &n);
        if (ret == EOF){break;}
        
        scanf("%lf", &score[0]);
        double max, min;
        sum = score[0];
        max = score[0];
        min = score[0];
        for (int i = 1; i < n; i++)
        {
            scanf("%lf", &score[i]);
            sum += score[i];
            if (score[i] > max)
            {
                max = score[i];
            }
            if (score[i] < min)
            {
                min = score[i];
            }
        }
        avg = (sum - max - min) / (n - 2);
        printf("%.2f\n", avg);
    }
    return 0;
}