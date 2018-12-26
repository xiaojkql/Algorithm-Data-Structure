#include<iostream>
#include"bubbleSort.h"

int main()
{
	using namespace std;
	
	int arr[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };
	int arr1[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int arr2[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int arr3[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int arr4[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int n = sizeof(arr) / sizeof(arr[0]);
	bubbleSort(arr, n);

	for (auto c : arr)
		cout << c << " ";
	cout << endl;

	bubbleSort_opt_1(arr1, n);
	for (auto c : arr1)
		cout << c << " ";
	cout << endl;

	bubbleSort_opt_2(arr2, n);
	for (auto c : arr2)
		cout << c << " ";
	cout << endl;

	bubbleSort_opt_3(arr3, n);
	for (auto c : arr3)
		cout << c << " ";
	cout << endl;

	bubbleSort_opt_4(arr4, n);
	for (auto c : arr4)
		cout << c << " ";
	cout << endl;

	cin.get();
	return 0;
}