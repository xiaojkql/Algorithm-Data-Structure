
#pragma once

#include "listNode.h"

template <typename T>
class List
{
  protected:
    int _size;
    NodePosi(T) header;
    NodePosi(T) trailer;

    // 辅助函数，用列表ls，节点p作为首节点，向后复制n个节点
    void init();
    void copyFrom(List<T> const &ls,NodePosi(T) p,int n);
    void clear();

  public:
    // 构造函数
    List();
    List(ListNode<T> const &ls); //从一条列表直接创建

    // 析构函数
    ~List();

    // 只读访问接口
    int size() const;
    bool empty() const;

    // 可写访问接口
    // 删除节点p
    T remove(NodePosi(T) p);
};

#include "list_implementation.h"
