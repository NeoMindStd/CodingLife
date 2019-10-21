#include <stdio.h>

int main() {
	int testCase;
	scanf(" %d", &testCase);

	for (int T = 1; T <= testCase; T++) {
		int n, b, e, result = 0;
		scanf(" %d %d %d", &n, &b, &e);

		for (int i = 0; i < n; i++) {
			int cl, val;
			scanf(" %d", &cl);

			val = int(b / float(cl))*cl;

			if ((val >= b-e && val <= b+e) || (val+cl >= b-e && val+cl <= b+e)) result++;
		}

		printf("#%d %d\n", T, result);
	}

	return 0;
}