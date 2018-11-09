#include<iostream>
#include"interpolationSearch.h"

int main()
{
	using namespace std;
	int arr[] = { 10, 12, 13, 16, 18, 19, 20, 21, 22, 23,
		24, 33, 35, 42, 47 };
	int n = sizeof(arr) / sizeof(arr[0]);
	
	for(int x:arr)
	{ 
	int index = interpolationSearch_iter(arr, x, 0, n);
	cout << index << endl;
	}
	
	for (int x : arr)
	{
		int index = interpolationSearch_iter2(arr, x, 0, n-1);
		cout << index << endl;
	}

	cin.get();
	return 0;
}