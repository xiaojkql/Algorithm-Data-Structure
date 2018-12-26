#include<iostream>
#include"selectionSort.h"

int main()
{
	using namespace std;
	
	int arr[] = { 12,45,78,5,2,0,78,61,45,3,45,
		78,425,45,7,4,5,6,9,1,2,3,4,8,2,0 };
	int n = sizeof(arr) / sizeof(arr[0]);
	selectionSort(arr, n);

	for (auto c : arr)
		cout << c << " ";
	cout << endl;
	


	cin.get();
	return 0;
}