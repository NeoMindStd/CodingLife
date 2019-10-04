#include <stdio.h>
#define max(x, y) x > y ? x : y

int main() {
	int T;
	scanf(" %d", &T);
	for (int Ti = 1; Ti <= T; Ti++) {
		int size, mem = 0;
		scanf(" %d", &size);
		for (int i = 0; i < size; i++) {
			int num;
			scanf(" %d", &num);
			mem = max(mem+num, mem*num);
		}
		printf("#%d %d\n", Ti, mem);
	}

	return 0;
}