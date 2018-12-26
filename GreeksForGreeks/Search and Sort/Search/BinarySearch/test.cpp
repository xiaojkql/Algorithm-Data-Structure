#include<iostream>
#include"binarySearch.h"

int main()
{
	using namespace std;
	int a[] = { 2, 3, 4, 10, 40 };
	int hi = sizeof(a) / sizeof(a[0]);
	int index = binarySearch_recur(a, 40, 0, hi);
	int index1 = binarySearch_recur(a, 1, 0, hi);

	int index2 = binarySearch_recur2(a, 1, 0, hi - 1);
	cout << index << " " << index1 << " " << index2 << endl;

	int index_it = binarySearch_iter(a, 2, 0, hi);
	int index_it1 = binarySearch_iter(a, 1, 0, hi);
	
	cout << index_it << " " << index_it1 << endl;
	cin.get();
	return 0;
}