#include <stdio.h>

int main() {
	int n, r;
	scanf("%d", &n);
	switch (n) {
	case 1:
		r = 65;
		break;
	case 2:
		r = 17;
		break;
	case 3:
		r = 4;
		break;
	case 4:
		r = 4;
		break;
	case 5:
		r = 64;
		break;
	}
	printf("%d", r);
	return 0;
}