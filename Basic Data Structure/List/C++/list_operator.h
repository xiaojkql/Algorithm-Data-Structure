// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
NodePosi(T) List<T>::operator[](int n) const
{
    NodePosi(T) p = header;
    while (n--)
    {
        p = p->succ;
    }
    return p;
}
