// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
T List<T>::remove(NodePosi(T) p)
{
    p->pred->succ = p->succ;
    p->succ->pred = p->pred;
    T a = p->data;
    delete p;
    return a;
}
