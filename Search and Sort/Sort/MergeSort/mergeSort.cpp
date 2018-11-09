#include"mergeSort.h"
#include<iostream>
//Çø¼ä [lo, hi]
void mergeSort(int arr[], int lo, int hi)
{
	if (lo == hi)
		return;
	int mi = (lo + hi)/2;
	mergeSort(arr, lo, mi);
	mergeSort(arr, mi + 1, hi);
	merge(arr, lo, mi, hi);
	std::cout << lo << " " << mi << " " << hi << std::endl;
	for (lo; lo <= hi; lo++)
		std::cout << arr[lo] << " ";
	std::cout << std::endl;
}

void merge(int arr[], int lo, int mi, int hi)
{

	int *arrTemp = new int[mi - lo + 1];
	for (int i = 0; i < mi - lo + 1; ++i)
		arrTemp[i] = arr[i+lo];

	int mi_temp = mi;
	++mi;
	for (int i = lo; i <= mi_temp; ++i)
	{
		if (mi > hi)
			break;

		while (mi<=hi && arrTemp[i-lo] > arr[mi])
		{
			auto key = arr[mi];
			int m = mi;
			while (m > i)
			{
				arr[m] = arr[m - 1];
				--m;
			}	
			arr[i] = key;
			mi = mi + 1;
			break;
		}
	}
	if (mi <= hi)
	{
		for(int i = mi;i<=hi;++i)
			for (int j = lo; j < i; ++j)
			{
				if (arr[j] > arr[i])
				{
					int n = i;
					auto key = arr[i];
					while (n > j)
					{
						arr[n] = arr[n - 1];
						n = n - 1;
					}
					arr[j] = key;
				}
			}
	}

}