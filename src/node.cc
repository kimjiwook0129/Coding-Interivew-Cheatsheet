#include "node.h"

template <typename T>

Node::Node(T val) : data(val), next(nullptr) {}

Node::Node(T val) : data(val), next(nullptr) {}

Node::Node() : data(0), next(nullptr) {}

T Node::getData() { return data; }

void Node::setData(T val) { data = val; }

Node *Node::getNext() { return next; }

void Node::setNext(Node *node) { next = node; }

~Node::Node() {}