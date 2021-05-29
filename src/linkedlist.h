#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

#include "node.h"

template <typename T>
class LinkedList {
   private:
    typedef Node<T> *ListNode;
    ListNode head = nullptr;
    ListNode tail = nullptr;
};

#endif