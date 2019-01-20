// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
NodePosi(T) List<T>::first() const
{
    return header->pred;
}

template <typename T>
NodePosi(T) List<T>::last() const
{
    return trailer->pred;
}
