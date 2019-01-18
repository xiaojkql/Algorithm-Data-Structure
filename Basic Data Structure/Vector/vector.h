// Author: Qin Yuan
// Time:

// vecor class

#pragram once

typedef int Rank;          // 自己定义一个类型
#define Default_Capacity 3 // vector 默认的容量

template <typename T> // 声明模板，vector 存储的类型为 T
class Vector
{
  protected:
    //class的内部变量
    Rank _size;     //表示向量中实时存储的元素数量
    Rank _capacity; // 实时控制该向量内部数组的大小，便于增加，减少元素
    T *_elem;       // Vector是基于内部数组实现的，需要一个内部数组变量

    //  Vector一些接口函数的辅助函数
    void copy_from(T const *arr, Rank lo, Rank hi);

  public:
    //构造函数：
    // 默认构造函数
    Vector(Rank _s = 0, Rank _c = Default_Capacity, T v = 0) : _size(_s), _capacity(_c)
    {
        _elem = new T[_capacity];
        for (Rnak i = 0; i < _size; ++i)
            _elem[i] = v;
    }
    // 从一个数组复制过来
    Vector(T const *arr, Rank n) { copy_from(arr, 0, n); }
    // 从一个数组的一部分复制过来
    Vector(T const *arr, Rank lo, Rank hi) { copy_from(arr, lo, hi); }
    // 从另一个vector复制过来
    Vector(Vector<T> const &_vec) { copy_from(_vec._elem, 0, _vec._size); }
    //从另一个vector的一部分复制过来
    Vector(Vector<T> const &_vec, Rank lo, Rank hi) { copy_from(_vec._elem, lo, hi); }
};
