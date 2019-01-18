#pragma once

template <typename T>
void Vector<T>::copy_from(T const *arr, Rank lo, Rank hi)
{
    if (Default_Capacity > hi - lo)
    {
        _capacity = Default_Capacity;
    }
    else
    {
        _capacity = (hi - lo)*2;
    }
    _elem = new T[_capacity];
    _size = 0;
    for (lo; lo < hi; ++lo)
    {
        _elem[_size++] = arr[lo];
    }
}
