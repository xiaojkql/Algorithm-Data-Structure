// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
List<T>::List()
{
    init();
}

template <typename T>
List<T>::List(List<T> const &ls)
{
    init();
    copyFrom(ls, ls.header, ls._size);
}

template <typename T>
List<T>::~List()
{
    clear();
    delete header;
    delete trailer;
}
