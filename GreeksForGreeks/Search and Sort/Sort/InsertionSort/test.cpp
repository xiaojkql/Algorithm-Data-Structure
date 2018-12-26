#include<iostream>
#include"insertionSort.h"

int main()
{
	using namespace std;
	
	int arr[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };
	int arr1[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int n = sizeof(arr) / sizeof(arr[0]);
	insertionSort(arr, n);
	
	for (auto c : arr)
		cout << c << " ";
	cout << endl;

	insertionSort_2(arr1, n);
	for (auto c : arr1)
		cout << c << " ";
	cout << endl;


	cin.get();
	return 0;
}