#ifndef _DOUBLENODE_H_
#define _DOUBLENODE_H_

template <typename T>

class DoubleNode : public Node {
   private:
    Node *prev;

   public:
    DoubleNode(T val) : data(val), next(nullptr), prev(nullptr) {}
    DoubleNode() : data(0), next(nullptr), prev(nullptr) {}
    T getData() { return data; }
    void setData(T val) { data = val; }
    Node *getNext() { return next; }
    void setNext(Node *node) { next = node; }
    ~Node() {}
};

#endif