#include <stdio.h>

// Optimal Buffer Size
// https://www.zabkat.com/blog/buffered-disk-access.htm
#define BS 524288

int cnt, rc;
char inb[BS];

inline char readCh() {
	if (cnt%BS == 0) {
		cnt = 0;
		rc = fread(inb, 1, BS, stdin);
	}
	return cnt < rc ? inb[cnt++] : 0;
}

inline int _readInt(int *ptr) {
	int n = 0, c = 0;
	*ptr = 0;
	while (1) {
		char read = readCh();
		if (read < '0' || read > '9') { *ptr = n; return n == 0 ? 0 : !c; }
		else read -= '0', n *= 10, n += read;
		c++;
	}
	*ptr = n;
	return 0;
}

inline int readInt() { int ptr; while (_readInt(&ptr)); return ptr; }

int main() {
	int n, T, r;
	long long int sum = 0;

	T = readInt(); n = T;
	while (T--) r = readInt(), sum += r;
	printf("%d\n%lld\n", n, sum);

	return 0;
}