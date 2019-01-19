#include <iostream>
int main()
{
    int *p = new int;
    *p = 10;
    std::cout << *p << std::endl;

    double *pd = new double(10.1);
    std::cout<<*pd<<std::endl;
}
