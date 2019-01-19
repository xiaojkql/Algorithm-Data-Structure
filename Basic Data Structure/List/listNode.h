// Author: Qin Yuan
// Time:
#pragma once

#define NodePosi(T) ListNode<T> *

template <typename T>
struct ListNode
{
    // 数据成员
    T data;
    ListNode<T> *pred;
    ListNode<T> *succ;

    // 构造、析构函数
    ListNode() {}
    // 用数据项，前后继创建节点
    ListNode(T e, NodePosi(T) _p = nullptr, NodePosi(T) _s = nullptr) : data(e), pred(_p), succ(_s) {}
    ~ListNode() {}

    // 成员函数
    void insertAfter(T const &e)
    {
        NodePosi(T) node = new ListNode<T>;
        node->data = e;
        node->pred = this;
        succ = node;
    }

    void insertBefor(T const &e)
    {
        node = new NodePosi<T>;
        node->data = e;
        node->succ = this;
        pred = node;
    }
};
