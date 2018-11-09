#include"jumpSearch.h"
#include<cmath>
#include<algorithm>
#include<iostream>

int jumpSearch(int arr[], int elem, int arr_size)
{
	// 每一个区间的长度 block_Size
	int step = std::sqrt(arr_size);
	int pos = step;
	int prev = 0;

	// 找到刚好大于elem的 lower_bound
	while (arr[std::min(pos, arr_size) - 1] < elem)
	{
		prev = pos;
		pos += step;
		if (prev >= arr_size)
			return -1;
	}

	while (prev < std::min(pos, arr_size))
	{
		if (arr[prev] == elem)
			return prev;
		++prev;
	}

	return -1;
}