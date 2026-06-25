// 2.3 平面最近点对
// 给定若干点位坐标，寻找距离最近的两点之间的距离
// 寻找效率好于 O(n^2) 的算法。

// 输入:
// 第一行是一个整数n，代表平面上点的数量
// 接下来n行，每行两个整数 x y，代表平面上一个点的横纵坐标

// 3
// 1 1
// 2 2
// 3 3


// 输出: (精确到小数点后4位)
// 1.4142


// 思路：分治法
// 先把所有点按照x坐标排序;
// 然后从中间分成两半, 递归求解左半部和右半部的最近点对距离;
// 然后在分界线附近寻找可能的更近的点对。
// 分界线附近找点时, 只找离分界线小于d的点;


#include <bits/stdc++.h>
using namespace std;

// 定义点数据结构
struct Point {
    double x, y;
};

// 计算两点之间的距离
double dist(const Point& a, const Point& b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

// 递归函数，求解区间 [l, r) 内的最近点对距离
double closestPairRec(vector<Point>& points, int l, int r) {
    // 基本情况：如果点的数量不多于3个，直接暴力计算
    if (r - l <= 3) {
        double d = INFINITY;
        for (int i = l; i < r; i++) {
            for (int j = i + 1; j < r; j++) {
                d = min(d, dist(points[i], points[j]));
            }
        }
        return d;
    }
    // 分治：找到中点，递归求解左右两半的最近点对距离
    int mid = (l + r) / 2;
    double midX = points[mid].x;
    double dLeft = closestPairRec(points, l, mid);
    double dRight = closestPairRec(points, mid, r);
    // 取最小距离
    double d = min(dLeft, dRight);

    // 获取分界线附近的点, 只要距离分界线小于d的点
    vector<Point> strip;
    for (int i = l; i < r; i++) {
        if (abs(points[i].x - midX) < d) {
            strip.push_back(points[i]);
        }
    }
    // 按y坐标排序
    sort(strip.begin(), strip.end(), [](const Point& a, const Point& b) {
        return a.y < b.y;
    });
    // 在分界线附近检查可能的更近点对, 只检查y坐标差小于d的点
    for (size_t i = 0; i < strip.size(); i++) {
        for (size_t j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) < d; j++) {
            d = min(d, dist(strip[i], strip[j]));
        }
    }
    
    return d;
}

// 入口函数，先按x坐标排序，然后调用递归函数
double closestPair(vector<Point>& points) {
    sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
        return a.x < b.x;
    });
    return closestPairRec(points, 0, points.size());
}

// 本地测试
void test() {
    vector<Point> points = {{1, 1}, {2, 2}, {3, 3}};
    cout << fixed << setprecision(4) << closestPair(points) << endl;
}

int main() {
    int n;
    // 输入点的数量
    if (!(cin >> n)) return 0;

    vector<Point> points(n);
    // 输入各点坐标
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }
    
    // 输出最近点对距离, 保留4位小数
    cout << fixed << setprecision(4) << closestPair(points) << endl;
    return 0;
}