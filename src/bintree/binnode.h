/******************************************************************************************
 * Data Structures in C++
 * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
 * Junhui DENG, deng@tsinghua.edu.cn
 * Computer Science & Technology, Tsinghua University
 * Copyright (c) 2006-2013. All rights reserved.
 ******************************************************************************************/

#pragma once

#define BinNodePosi(T) BinNode<T>* //�ڵ�λ��
#define stature(p) ((p) ? (p)->height : -1) //�ڵ�߶ȣ��롰�����߶�Ϊ-1����Լ����ͳһ��
typedef enum { RB_RED, RB_BLACK} RBColor; //�ڵ���ɫ

template <typename T> struct BinNode { //�������ڵ�ģ����
// ��Ա��Ϊ���������ͳһ���ţ����߿ɸ�����Ҫ��һ����װ��
   T data; //��ֵ
   BinNodePosi(T) parent; BinNodePosi(T) lc; BinNodePosi(T) rc; //���ڵ㼰���Һ���
   int height; //�߶ȣ�ͨ�ã�
   int npl; //Null Path Length����ʽ�ѣ�Ҳ��ֱ����height���棩
   RBColor color; //��ɫ���������
// ���캯��
   BinNode() :
      parent ( NULL ), lc ( NULL ), rc ( NULL ), height ( 0 ), npl ( 1 ), color ( RB_RED ) { }
   BinNode ( T e, BinNodePosi(T) p = NULL, BinNodePosi(T) lc = NULL, BinNodePosi(T) rc = NULL,
             int h = 0, int l = 1, RBColor c = RB_RED ) :
      data ( e ), parent ( p ), lc ( lc ), rc ( rc ), height ( h ), npl ( l ), color ( c ) { }
// �����ӿ�
   int size(); //ͳ�Ƶ�ǰ�ڵ����������༴����Ϊ���������Ĺ�ģ
   BinNodePosi(T) insertAsLC ( T const& ); //��Ϊ��ǰ�ڵ�����Ӳ����½ڵ�
   BinNodePosi(T) insertAsRC ( T const& ); //��Ϊ��ǰ�ڵ���Һ��Ӳ����½ڵ�
   BinNodePosi(T) succ(); //ȡ��ǰ�ڵ��ֱ�Ӻ��
   template <typename VST> void travLevel ( VST& ); //������α���
   template <typename VST> void travPre ( VST& ); //�����������
   template <typename VST> void travIn ( VST& ); //�����������
   template <typename VST> void travPost ( VST& ); //�����������
// �Ƚ������е�����������һ���������в��䣩
   bool operator< ( BinNode const& bn ) { return data < bn.data; } //С��
   bool operator== ( BinNode const& bn ) { return data == bn.data; } //����
   /*DSA*/
   /*DSA*/BinNodePosi(T) zig(); //˳ʱ����ת
   /*DSA*/BinNodePosi(T) zag(); //��ʱ����ת
};

#include "BinNode_implementation.h"
