/******************************************************************************************
 * Data Structures in C++
 * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
 * Junhui DENG, deng@tsinghua.edu.cn
 * Computer Science & Technology, Tsinghua University
 * Copyright (c) 2006-2013. All rights reserved.
 ******************************************************************************************/

#pragma once

typedef int Rank; //秩 typedef 类型名  别型名
#define ListNodePosi(T) ListNode<T>* //列表节点位置  #define 别名  所要表示的东西

// ListNode 是一个对象，对象内部包含数据成员，也包含成员函数
// 数据成员中有两项是指针，指向前后继的地址
// 牢记有两项表示的是指针


// 需要定义一个节点表示，列表中的节点对象
template <typename T> 
struct ListNode { //列表节点模板类（以双向链表形式实现） 
// 成员 双向列表，有单个成员项，一个表示节点处的数据，一个连接前面，一个连接后面
   T data; 
   ListNodePosi(T) pred; 
   ListNodePosi(T) succ; //数值、前驱、后继
// 构造函数
   // 默认构造函数
   ListNode() {} //针对header和trailer的构造
   ListNode ( T e, ListNodePosi(T) p = NULL, ListNodePosi(T) s = NULL )
      : data ( e ), pred ( p ), succ ( s ) {} //默认构造器  用数据项构造一个节点，可以包含该节点的前后继
// 操作接口
   ListNodePosi(T) insertAsPred ( T const& e ); //紧靠当前节点之前插入新节点
   ListNodePosi(T) insertAsSucc ( T const& e ); //紧随当前节点之后插入新节点
};

#include "listNode_implementation.h"