#include <stdio.h>

#define scanf scanf_s

class Stack {
public:
	static const int SIZE = 16*16;
	int arr[SIZE];
	int top = -1;

	void push(int n) { arr[++top] = n; }
	int pop() { return arr[top--];  }
};


int main() {
	int n, r = 0;
	scanf(" %d", &n);
	int** a = new int*[n];
	for (int i = 0; i < n; i++)  a[i] = new int[n];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf(" %d", &a[i][j]);

	printf("%d", r);

	return 0;
}