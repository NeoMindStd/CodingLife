#include <stdio.h>

int count(int a[], int n, int k, int i, int sum, bool cf) {
	if (i >= n) return 0;
	return (cf && sum == k ? 1 : 0) + count(a, n, k, i + 1, sum + a[i+1], true) + count(a, n, k, i + 1, sum, false);
}

int main() {
	int testCase;
	scanf(" %d", &testCase);
	for (int T = 1; T <= testCase; T++) {
		int n, k;
		scanf(" %d %d", &n, &k);
		int *a = new int[n];
		for (int i = 0; i < n; i++) {
			scanf(" %d", &a[i]);
		}
		
		printf("#%d %d\n", T, count(a,n,k,0,a[0],true)+count(a, n, k, 0, 0, false));
	}

	return 0;
}