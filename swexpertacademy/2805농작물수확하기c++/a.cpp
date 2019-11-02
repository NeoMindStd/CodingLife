#include <stdio.h>

int main() {
	int testCase;
	scanf(" %d", &testCase);
	for (int T = 1; T <= testCase; T++) {
		int n, m=0;
		scanf(" %d", &n);
		int **a = new int*[n];

		for (int i = 0; i < n; i++) {
			a[i] = new int[n];
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%1d", &a[i][j]);
			}
		}		

		for (int i = 0; i <= n / 2; i++) {
			for (int j = n / 2 - i; j <= n / 2 + i; j++) {
				m += a[i][j];
			}
		}
		for (int i = n / 2+1; i < n; i++) {
			for (int j = n / 2 - (n-i-1); j <= n / 2 + (n-i-1); j++) {
				m += a[i][j];
			}
		}

		printf("#%d %d\n", T, m);
	}

	return 0;
}