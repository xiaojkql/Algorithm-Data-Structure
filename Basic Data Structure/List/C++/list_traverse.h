// Author: Qin Yuan
// Time:

#pragma once

template <typename T>
void List<T>::traverse(void (*VST)(T &e))
{
    NodePosi(T) p = header;
    int n = _size;
    while (n--)
    {
        p = p->succ;
        VST(P->data);
    }
}


// 注意这里的template的先后顺序
template<typename T>
template<typename VST>
void List<T>::traverse(VST &visit)
{
    NodePosi(T) p = header;
    int n = _size;
    while(n--)
    {
        p=p->succ;
        visit(p->data);
    }
}
