#include <stdio.h>

int main() {
	int n;
	scanf(" %d", &n);
	
	int nums[10001] = { 0, };

	for (int i = 0; i < n; i++) {
		int index;
		scanf(" %d", &index);
		nums[index]++;
	}

	for (int i = 1; i < 10001; i++) {
		for (int j = 0; j < nums[i]; j++) {
			printf("%d\n", i);
		}
	}

	return 0;
}