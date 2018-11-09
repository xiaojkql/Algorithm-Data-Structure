#include"selectionSort.h"
#include<algorithm>

// [lo, hi)
void selectionSort(int arr[], int arr_size)
{
	for (int i = 0; i < arr_size-1; ++i)
	{
		int min_index = i;
		for (int j = i + 1; j < arr_size; ++j)
		{
			if (arr[j] < arr[min_index])
				min_index = j;
		}
		if (min_index != i)
			std::swap(arr[i], arr[min_index]); // swap()本身传递的就是引用，不需要在引用一次
	}
}