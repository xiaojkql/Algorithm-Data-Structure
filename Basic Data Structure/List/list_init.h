// Author: Qin Yuan
// Time:

template <typename T>
void List<T>::init()
{
    header = new ListNode();
    trailer = new ListNode();
    header->succ = trailer;
    trailer->pred = header;
}
