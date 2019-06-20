#include <stdio.h>
int main() {
	int n;
	scanf("%d", &n);

	int *towers = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &towers[i]);
	}

	for (int i = 0; i < n; i++) {
		int dst = 0;
		for (int j = i - 1; j > -1; j--) {
			if (towers[i] <= towers[j]) {
				dst = j + 1;
				break;
			}
		}
		printf("%d ", dst);
	}

	delete[] towers;
}