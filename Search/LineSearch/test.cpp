#include<iostream>
#include"lineSearch.h"

int main()
{
	using namespace std;
	int a[] = { 10, 20, 80, 30, 60, 50,
		110, 100, 130, 170 };
	int i = lineSearch(a, 60, sizeof(a) / sizeof(a[0]));
	/*
	* size(string)字符串长度
	* sizeof(var)变量的字节数
	*/
	cout << i << endl;
	cin.get();
	return 0;
}