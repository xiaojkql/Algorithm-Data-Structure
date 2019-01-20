// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
void List<T>::clear()
{
    while (_size--)
    {
        p = header->succ;
        header->succ = p->succ;
        delete p;
    }
}
