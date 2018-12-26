#include"lineSearch.h"

int lineSearch(int a[],int elem, int arr_size)
{
	for (int i = 0; i < arr_size; ++i)
		if (a[i] == elem)
			return i;
	return -1;
}