#include <stdio.h>
#define max(a, b) a>b ? a : b
#define min(a, b) a<b ? a : b

int main() {
	int testCase;
	scanf(" %d", &testCase);

	for (int T = 1; T <= testCase; T++) {
		int mx=0, mn=9999999;

		for (int i = 0; i < 10; i++) {
			int n, ca=0;
			scanf(" %d", &n);
			while (n > 0) {
				ca += n % 10;
				n /= 10;
			}
			mx = max(mx, ca);
			mn = min(mn, ca);
		}

		printf("#%d %d %d\n", T, mx, mn);
	}
}