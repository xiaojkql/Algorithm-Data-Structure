#include<iostream>
#include"exponentialSearch.h"

int main()
{
	using namespace std;
	int arr[] = { 2, 3, 4, 10, 40, 60};
	int n = sizeof(arr) / sizeof(arr[0]);
	for (int x : arr)
	{
		int index = exponentialSearch(arr, x, 0, n - 1);
		cout << index << "  ";
	}
	int index = exponentialSearch(arr, 50, 0, n - 1);
	cout << endl << index << endl;

	for (int x : arr)
	{
		int index = exponentialSearch_open(arr, x, 0, n);
		cout << index << "  ";
	}

	index = exponentialSearch_open(arr, 100, 0, n);
	cout << endl << index << endl;

	cin.get();
	return 0;
}