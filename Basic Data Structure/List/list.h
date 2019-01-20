
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
  void copyFrom(List<T> const &ls, NodePosi(T) p, int n);
  void clear();

public:
  // 构造函数
  List();
  List(List<T> const &ls); //从一条列表直接创建

  // 析构函数
  ~List();

  // 只读访问接口
  int size() const;
  bool empty() const;
  NodePosi(T) first() const;
  NodePosi(T) last() const;
  NodePosi(T) operator[](int n) const;

  // 可写访问接口
  NodePosi(T) insertAsFirst(T const &e);
  NodePosi(T) insertAsLast(T const &e);
  NodePosi(T) insertPred(NodePosi(T) p, T const &e);
  NodePosi(T) insertSucc(NodePosi(T) p, T const &e);

  // 删除节点p
  T remove(NodePosi(T) p);

  // 遍历操作
  void traverse(void (*VST)(T &e));//用函数的指针传入

  template<typename VST>
  void traverse(VST& vst); //传入的是一个类型对象
};

#include "list_implementation.h"
