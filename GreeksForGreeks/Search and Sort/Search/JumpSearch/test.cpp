#include<iostream>
#include"jumpSearch.h"

int main()
{
	using namespace std;
	int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21,
		34, 55, 89, 144, 233, 377, 610 };
	int x = 55;
	int n = sizeof(arr) / sizeof(arr[0]);

	int index = jumpSearch(arr, 610, n);
	cout << index << endl;

	cin.get();
	return 0;
}