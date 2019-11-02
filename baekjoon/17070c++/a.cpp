#include <stdio.h>

class PosData {
public:
	int r, c, t, d;
	PosData() {
		r = c = t = d = 0;
	}
	PosData(int r, int c, int t, int d) {
		this->r = r;
		this->c = c;
		this->t = t;
		this->d = d;
	}
	PosData(PosData* posData) {
		this->r = posData->r;
		this->c = posData->c;
		this->t = posData->t;
		this->d = posData->d;
	}
};

template <typename T>
class Stack {
public:
	static const int SIZE = 16 * 16;

	void push(T n) { arr[++top] = n; }
	T pop() { return arr[top--]; }
	bool isEmpty() { return top == -1; }
	bool isFull() { return top == SIZE - 1; }
	void init() { top = -1; }
	void print() {
		printf("\n");
		for (int i = 0; i <= top; i++) {
			printf("(%d, %d, %d, %d), ", arr[i].r, arr[i].c, arr[i].t, arr[i].d);
		}
		printf("\n");
	}
private:
	T arr[SIZE];
	int top = -1;
};


int main() {
	int n, cnt = 0;
	scanf(" %d", &n);
	int** a = new int*[n];
	for (int i = 0; i < n; i++)  a[i] = new int[n];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf(" %d", &a[i][j]);

	Stack<PosData> stack = Stack<PosData>();
	stack.push(PosData(0, 1, 0, 0));
	PosData current, next;
	while (!stack.isEmpty()) {
		current = stack.pop();
		while (current.d < 3) {
			next = PosData(current);
			if (next.d == 0 && next.t != 2 && next.c < n - 1 && a[next.r][next.c + 1] == 0) {
				next.c++;
				next.t = next.t == 2 ? 1 : 0;
				next.d = 0;
				if (next.r == n - 1 && next.c == n - 1) {
					cnt++;
					break;
				}
				current.d++;
				stack.push(current);
				current = PosData(next);
			}
			else if (next.d == 1 && next.c < n - 1 && next.r < n - 1 &&
				a[next.r + 1][next.c + 1] == 0 && a[next.r + 1][next.c] == 0 && a[next.r][next.c + 1] == 0) {
				next.r++;
				next.c++;
				next.t = 1;
				next.d = 0;
				if (next.r == n - 1 && next.c == n - 1) {
					cnt++;
					break;
				}
				current.d++;
				stack.push(current);
				current = PosData(next);
			}
			else if (next.d == 2 && next.t != 0 && next.r < n - 1 && a[next.r + 1][next.c] == 0) {
				next.r++;
				next.t = next.t == 0 ? 1 : 2;
				next.d = 0;
				if (next.r == n - 1 && next.c == n - 1) {
					cnt++;
					break;
				}
				current.d++;
				stack.push(current);
				current = PosData(next);
			}
			else {
				current.d++;
			}
		}
	}

	printf("%d", cnt);

	return 0;
}