/******************************************************************************************
 * Data Structures in C++
 * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
 * Junhui DENG, deng@tsinghua.edu.cn
 * Computer Science & Technology, Tsinghua University
 * Copyright (c) 2006-2013. All rights reserved.
 ******************************************************************************************/

#pragma once

#include "listNode.h" //�����б�ڵ���

template <typename T> 
class List { //�б�ģ����

	// ˫���б����������ݳ�Ա��Ԫ�ص���Ŀ��ͷβ�ڵ�
private:
   int _size; 
   ListNodePosi(T) header; 
   ListNodePosi(T) trailer; //��ģ��ͷ�ڱ���β�ڱ�

protected:
   void init(); //�б���ʱ�ĳ�ʼ��
   int clear(); //������нڵ�
   void copyNodes ( ListNodePosi(T), int ); //�����б�����λ��p���n��
   void merge ( ListNodePosi(T)&, int, List<T>&, ListNodePosi(T), int ); //�鲢
   void mergeSort ( ListNodePosi(T)&, int ); //�Դ�p��ʼ������n���ڵ�鲢����
   void selectionSort ( ListNodePosi(T), int ); //�Դ�p��ʼ������n���ڵ�ѡ������
   void insertionSort ( ListNodePosi(T), int ); //�Դ�p��ʼ������n���ڵ��������

public:
// ���캯��
   List() { init(); } //Ĭ��
   List ( List<T> const& L ); //���帴���б�L
   List ( List<T> const& L, Rank r, int n ); //�����б�L���Ե�r�����n��
   List ( ListNodePosi(T) p, int n ); //�����б�����λ��p���n��

// ��������
   ~List(); //�ͷţ�����ͷ��β�ڱ����ڵģ����нڵ�

// ֻ�����ʽӿ�
   Rank size() const { return _size; } //��ģ
   bool empty() const { return _size <= 0; } //�п�
   T& operator[] ( Rank r ) const; //���أ�֧��ѭ�ȷ��ʣ�Ч�ʵͣ�
   ListNodePosi(T) first() const { return header->succ; } //�׽ڵ�λ��
   ListNodePosi(T) last() const { return trailer->pred; } //ĩ�ڵ�λ��
   bool valid ( ListNodePosi(T) p ) //�ж�λ��p�Ƿ����Ϸ�
   { return p && ( trailer != p ) && ( header != p ); } //��ͷ��β�ڵ��ͬ��NULL
   int disordered() const; //�ж��б��Ƿ�������
   ListNodePosi(T) find ( T const& e ) const //�����б����
   { return find ( e, _size, trailer ); }
   ListNodePosi(T) find ( T const& e, int n, ListNodePosi(T) p ) const; //�����������
   ListNodePosi(T) search ( T const& e ) const //�����б����
   { return search ( e, _size, trailer ); }
   ListNodePosi(T) search ( T const& e, int n, ListNodePosi(T) p ) const; //�����������
   ListNodePosi(T) selectMax ( ListNodePosi(T) p, int n ); //��p����n-1�������ѡ�������
   ListNodePosi(T) selectMax() { return selectMax ( header->succ, _size ); } //���������

// ��д���ʽӿ�
   ListNodePosi(T) insertAsFirst ( T const& e ); //��e�����׽ڵ����
   ListNodePosi(T) insertAsLast ( T const& e ); //��e����ĩ�ڵ����
   ListNodePosi(T) insertA ( ListNodePosi(T) p, T const& e ); //��e����p�ĺ�̲���
   ListNodePosi(T) insertB ( ListNodePosi(T) p, T const& e ); //��e����p��ǰ������


   T remove ( ListNodePosi(T) p ); //ɾ���Ϸ�λ��p���Ľڵ�,���ر�ɾ���ڵ�


   void merge ( List<T>& L ) { merge ( first(), size, L, L.first(), L._size ); } //ȫ�б�鲢
   void sort ( ListNodePosi(T) p, int n ); //�б���������
   void sort() { sort ( first(), _size ); } //�б���������
   int deduplicate(); //����ȥ��
   int uniquify(); //����ȥ��
   void reverse(); //ǰ���ã�ϰ�⣩
// ����
   void traverse ( void (* ) ( T& ) ); //����������ʵʩvisit����������ָ�룬ֻ����ֲ����޸ģ�
   template <typename VST> //������
   void traverse ( VST& ); //����������ʵʩvisit�������������󣬿�ȫ�����޸ģ�
}; //List

#include "List_implementation.h"
