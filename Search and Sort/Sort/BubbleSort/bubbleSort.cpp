#include"bubbleSort.h"
#include<algorithm>

void bubbleSort(int arr[], int arr_size)
{
	for(int i = 0;i<arr_size;++i)
		for (int j = arr_size-1; j>i; --j)
		{
			if (arr[j] < arr[j-1])
				std::swap(arr[j], arr[j-1]);
		}
}


void bubbleSort_opt_1(int arr[], int arr_size)
{
	bool swapped = false;
	for (int i = 0; i < arr_size; ++i)
	{
		swapped = false;
		for (int j = arr_size - 1; j > i; --j)
		{
			if (arr[j] < arr[j - 1])
				std::swap(arr[j], arr[j - 1]);
			swapped = true;
		}
		if (swapped == false)
			break;
	}
}

void bubbleSort_opt_2(int arr[], int arr_size)
{
	for (int i = 0; i < arr_size; ++i)
	{
		int m = 0;
		for (int j = 0; j < arr_size - i-1; ++j)
			if (arr[j] > arr[j + 1])
			{
				std::swap(arr[j], arr[j + 1]);
				m = j;
			}
		if (m != 0)
			i = arr_size - m - 2;
				
	}
}

void bubbleSort_opt_3(int arr[], int arr_size)
{
	int n = arr_size;
	for (int m; 1 < n; n = m) // Öð²½Ëõ¶Ì½»»»¿Õ¼ä
	{
		for (int i = m = 1; i < n; ++i)
		{
			if (arr[i] < arr[i - 1])
			{
				std::swap(arr[i], arr[i - 1]);
				m = i;
			}
		}
	}
}

void bubbleSort_opt_4(int arr[], int arr_size)
{
	for (bool sorted = false; sorted = !sorted;arr_size--)
	{
		sorted = true;
		for(int i=0;i<arr_size-1;++i)
			if (arr[i] > arr[i + 1])
			{
				std::swap(arr[i + 1], arr[i]);
				sorted = false;
			}
	}
}