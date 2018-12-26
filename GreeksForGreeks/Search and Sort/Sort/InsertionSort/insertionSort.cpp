#include"insertionSort.h"
#include<iostream>

void insertionSort(int arr[], int arr_size)
{
	for (int i = 1; i < arr_size; ++i)
	{
		for (int j = 0; j < i; ++j)
		{
			if (arr[j] > arr[i])
			{
				int n = i;
				auto key = arr[i];	
				while (n > j)
				{
					arr[n] = arr[n-1]; //有优先运算顺序
					--n;
				}					
				arr[j] = key;
				break;
			}	
			
		}
		
	}
}


void insertionSort_2(int arr[], int arr_size)
{
	for (int i = 1; i < arr_size; ++i)
	{
		int j = i - 1;
		auto key = arr[i];
		while (j >= 0 && arr[j] > key)
		{
			arr[j + 1] = arr[j];
			--j;
		}
		arr[j+1] = key;
	}
}