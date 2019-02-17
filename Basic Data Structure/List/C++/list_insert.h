// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
NodePosi(T) List<T>::insertAsFirst(T const &e)
{
    return header->insertAfter(e);
}

template <typename T>
NodePosi(T) List<T>::insertAsLast(T const &e)
{
    return trailer->insertBefore(e);
}

template <typename T>
NodePosi(T) List<T>::insertPred(NodePosi(T) p, T const &e)
{
	return p->insertBefore(e);
}

template <typename T>
NodePosi(T) List<T>::insertSucc(NodePosi(T) p, T const &e)
{
	return p->insertAfter(e);
}
