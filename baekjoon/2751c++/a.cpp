#include <stdio.h>

#define parent(n) (int)(n/2)
#define left(n) 2*n
#define right(n) 2*n+1

using namespace std;

class Heap {
private:
	int* heap;
	int size = 0;

	void swap(int* a, int* b) {
		int tmp;
		tmp = *a;
		*a = *b;
		*b = tmp;
	}

public:
	Heap(int n) {
		heap = new int[n];
	}

	void push(int n) {
		heap[++size] = n;
		push_renew(size, parent(size));
	}

	void push_renew(int a, int b) {
		if (a <= 1 || heap[a] >= heap[b]) return;
		else {
			swap(&heap[a], &heap[b]);
			push_renew(b, parent(b));
		}
	}

	int pop() {
		if (size > 0) {
			swap(&heap[1], &heap[size--]);
			pop_renew(1);
			return heap[size + 1];
		}
		return 0;
	}

	void pop_renew(int a) {
		if (a >= left(parent(size))) {
			return;
		}
		else {
			if (size >= right(a) && heap[left(a)] >= heap[right(a)]) {
				if (heap[a] > heap[right(a)]) {
					swap(&heap[a], &heap[right(a)]);
					pop_renew(right(a));
				}
				return;
			}
			else {
				if (size >= left(a) && heap[a] > heap[left(a)]) {
					swap(&heap[a], &heap[left(a)]);
					pop_renew(left(a));
				}
				return;
			}
			return;
		}
		return;
	}
};

int main() {
	int n;
	scanf(" %d", &n);

	Heap heap = Heap(n);

	int a;
	for (int i = 0; i < n; i++) {
		scanf(" %d", &a);
		heap.push(a);
	}

	for (int i = 0; i < n; i++) {
		printf("%d\n", heap.pop());
	}

	return 0;
}