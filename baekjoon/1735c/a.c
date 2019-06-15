#include <stdio.h>

int euclidean(int a, int b) {
	return a % b ? euclidean(b, a%b) : b;
}

int main() {
	int a0, a1, b0, b1;

	scanf("%d %d %d %d", &a0, &a1, &b0, &b1);

	int r0 = (a0*b1) + (b0*a1);
	int r1 = a1 * b1;

	int g = euclidean(r0, r1);
	r0 /= g;
	r1 /= g;

	printf("%d %d", r0, r1);

	return 0;
}