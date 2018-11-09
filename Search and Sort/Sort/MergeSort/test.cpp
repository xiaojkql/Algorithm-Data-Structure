#include<iostream>
#include"mergeSort.h"

int main()
{
	using namespace std;
	
	int arr[] = { 38, 27, 43, 3, 9, 82, 10 };
	int arr1[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };

	int n = sizeof(arr1) / sizeof(arr1[0]);
	
	mergeSort(arr1, 0, n - 1);
	for (auto c : arr1)
		cout << c << " ";
	cout << endl;
	cin.get();
	return 0;
}