// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
void List<T>::copyFrom(List<T> const &ls, NodePosi(T) p, int n)
{
    while (n--)
    {
        trailer->pred->succ = (p = p->succ);
        p->pred = trailer->pred;
        trailer->pred = p;
        p->succ = trailer;
    }
}
