#ifndef _NODE_H_
#define _NODE_H_

template <typename T>

class Node {
   private:
    T data;
    Node *next;

   public:
    Node(T val);
    Node();
    T getData();
    void setData(T val);
    Node *getNext();
    void setNext(Node *node);
    ~Node();
};

#endif