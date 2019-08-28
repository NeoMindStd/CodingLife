#include <stdio.h>

#define HEAP_SIZE 100001

#define parent(n) (int)(n/2)
#define left(n) 2*n
#define right(n) 2*n+1

using namespace std;

class Heap {
private:
	int heap[HEAP_SIZE];
	int size = 0;

	void swap(int* a, int* b) {
		int tmp;
		tmp = *a;
		*a = *b;
		*b = tmp;
	}

public:
	Heap() {}

	void push(int n) {
		heap[++size] = n;
		push_renew(size, parent(size));
	}

	void push_renew(int a, int b) {
		if (a <= 1 || heap[a] <= heap[b]) return;
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
			if (size >= right(a) && heap[left(a)] <= heap[right(a)]) {
				if (heap[a] < heap[right(a)]) {
					swap(&heap[a], &heap[right(a)]);
					pop_renew(right(a));
				}
				return;
			}
			else {
				if (size >= left(a) && heap[a] < heap[left(a)]) {
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
	Heap heap = Heap();

	int n;
	scanf(" %d", &n);

	for (int i = 0; i < n; i++) {
		int a;
		scanf(" %d", &a);
		if (a != 0) {
			heap.push(a);
		}
		else {
			printf("%d\n", heap.pop());
		}
	}

	return 0;
}