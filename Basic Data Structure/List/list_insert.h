// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
NodePosi(T) List<T>::insertAsFirst(T const &e)
{
    return insertSucc(header, e);
}

template <typename T>
NodePosi(T) List<T>::insertAsLast(T const &e)
{
    return insertPred(e, trailer);
}

template <typename T>
NodePosi(T) List<T>::insertPred(NodePosi(T) p, T const &e)
{
    NodePosi(T) node = new ListNode<T>(e, p->pred, p);
    p->pred->succ = node;
    p->pred = node;
    return node;
}

template <typename T>
NodePosi(T) List<T>::insertSucc(NodePosi(T) p, T const &e)
{
    NodePosi(T) node = new ListNode<T>(e, p, p->succ);
    p->succ->pred = node;
    p->succ = node;
    return node;
}
