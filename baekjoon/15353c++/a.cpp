#include "iostream"
#include "cstring"

#define max(x, y) x>y ? x : y

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	char a[10002], b[10002], result[10002];
	result[10001] = '0';
	cin >> a >> b;
	int len_a = strlen(a);
	int len_b = strlen(b);
	int len_max = max(len_a, len_b);

	int ac;
	int i;
	for (i = 0; i < len_max; i++) {
		ac = (result[10001 - i] - '0');
		if (i < len_a) {
			ac += a[len_a - i - 1] - '0';
		}
		if (i < len_b) {
			ac += b[len_b - i - 1] - '0';
		}

		result[10001 - i] = (ac % 10) + '0';
		result[10000 - i] = (ac / 10) + '0';
	}
	int start = result[10001 - i] == '0' ? 10002 - i : 10001 - i;
	for (int i = start; i < 10002; i++) {
		cout << result[i];
	}
}