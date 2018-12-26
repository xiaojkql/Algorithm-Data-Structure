#include"exponentialSearch.h"
#include<algorithm>

// [lo, hi]
int exponentialSearch(int arr[], int elem, int lo, int hi)
{
	// if (arr[0] == elem)
		// return 0;
	if (arr[hi] < elem && arr[lo]>elem)
		return -1;
	int pos = 1;
	while (pos<(hi-lo+1) && arr[pos] < elem)
		pos *= 2;
	return binarySearch(arr, elem, pos / 2, std::min(pos, hi));
}


// [lo,hi)
int exponentialSearch_open(int arr[], int elem, int lo, int hi)
{
	if (arr[0] > elem && arr[hi - 1] < elem)
		return -1;
	int pos = 1;
	while (pos < hi && arr[pos] < elem)
		pos *= 2;
	return binarySearch(arr, elem, pos / 2, std::min(elem, hi - 1));
}


//[lo, hi]
int binarySearch(int arr[], int elem, int lo, int hi)
{
	while (lo <= hi)
	{
		int mi = (lo + hi) / 2;
		if (arr[mi] == elem)
			return mi;
		if (arr[mi] < elem)
			lo = mi + 1;
		else
			hi = mi - 1;
	}
	return -1;
}