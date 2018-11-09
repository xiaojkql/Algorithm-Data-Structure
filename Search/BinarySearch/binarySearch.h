#pragma once

// 数组传递的就是指针所以不需要用引用
// 若要用引用传递则要明确指出数组的大小 int (&arr)[40];

// 区间 [lo, hi)内寻找
int binarySearch_recur(int [], int, int, int);
int binarySearch_iter(int[], int, int, int);

// 区间 [lo, hi] 内寻找
int binarySearch_recur2(int[], int, int, int);