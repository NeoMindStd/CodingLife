#include <stdio.h>

#define scanf scanf_s

using namespace std;

int n;

class Node {
public:
	Node* parent;
	Node** children;
	int data;

	Node() {}
	Node(Node* _parent, int _data) {
		parent = _parent;
		data = _data;
		left = nullptr;
		right = nullptr;
	}
};

class Stack {
private:
	Node* stack;

public:
	int size = 0;

	Stack(int n) {
		stack = new Node[n]();
		size = n;
	}

	void push(Node n) {
		stack[size++] = n;
	}

	Node pop() {
		return stack[--size];
	}
};

class Tree {
private:
	Node* tree;

public:
	Tree() {
		tree = new Node(nullptr, 1);
	}

	void push(int a, int b) {
		Stack* stack = new Stack(n);
		stack->push(*tree);
		while (stack->size > 0) {
			Node node = stack->pop();
			if (node.data == a) {
				if (node.left != nullptr) node.left = new Node(&node, b);
				else if (node.right != nullptr) node.right = new Node(&node, b);
				break;
			}
			else if (node.data == b) {
				if (node.left != nullptr) node.left = new Node(&node, a);
				else if (node.right != nullptr) node.right = new Node(&node, a);
				break;
			}
			if (node.left != nullptr) stack->push(*node.left);
			if (node.right != nullptr) stack->push(*node.right);
		}
		delete stack;
	}

	void print() {
		int num = 2;
		while (num <= n) {
			Stack* stack = new Stack(n);
			stack->push(*tree);
			while (stack->size > 0) {
				Node node = stack->pop();
				if (node.data == num) {
					printf("%d\n", node.parent->data);
					break;
				}
			}
			delete stack;
		}
	}
};

int main() {
	scanf(" %d", &n);

	Tree* tree = new Tree();

	int a, b;
	for (int i = 1; i < n; i++) {
		scanf(" %d %d", &a, &b);
		tree->push(a, b);
	}

	printf("\n\n");
	tree->print();

	return 0;
}