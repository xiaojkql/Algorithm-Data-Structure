#include"interpolationSearch.h"
#include<iostream>
// 在区间[lo,hi)中寻找elem

// 采用迭代版本
int interpolationSearch_iter(int arr[], int elem, int lo, int hi)
{
	if (elem < arr[lo] && elem>arr[hi-1])
		return -1;
	//if (elem == arr[hi - 1])
		//return hi - 1;

	while (lo < hi)
	{
		//std::cout << lo << " " << hi << std::endl;
		int mi = lo + double(elem - arr[lo]) / (arr[hi-1] - arr[lo])*(hi - lo - 1);
		//std::cout << mi << std::endl;
		if (arr[mi] == elem)
			return mi;
		if (arr[mi] < elem)
			lo = mi + 1;
		else
			hi = mi; // hi永元是大于 elem的
	}
	return -1;
}


// [lo , hi]
// 直接划分得出mi
int interpolationSearch_iter2(int arr[], int elem, int lo, int hi)
{
	while (lo <= hi && elem>=arr[lo] && arr[hi]>=elem)
	{
		int mi = lo + double(elem - arr[lo]) / (arr[hi] - arr[lo])*(hi - lo);
		if (arr[mi] == elem)
			return mi;
		if (arr[mi] < elem)
			lo = mi + 1;
		else
			hi = mi - 1;
	}
	return -1;
}