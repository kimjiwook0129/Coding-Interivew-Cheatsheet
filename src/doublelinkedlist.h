#ifndef _DOUBLELINKEDLIST_H_
#define _DOUBLELINKEDLIST_H_

#include "linkedlist.h"

template <typename T>
class DoubleLinkedList : public LinkedList {
   private:
    ListNode tail = nullptr;
};

#endif