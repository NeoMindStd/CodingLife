#include "iostream"
#include "string"
#include "cmath"

#define max(x, y) x>y ? x : y

using namespace std;

const int LL = 18;	// LongLong Ÿ��

int main() {
	string a, b;
	cin >> a >> b;

	int len_a = a.length(), len_b = b.length();
	int arr_a_size = ceil((double)len_a / LL), arr_b_size = ceil((double)len_b / LL);
	int arr_size = max(arr_a_size, arr_b_size);

	long long int *lla = new long long int[arr_a_size], *llb = new long long int[arr_b_size];

	string *result = new string[arr_size ];
	int c;

	// ���ڿ��� �ڿ������� LL �ڸ��� ����
	for (int i = 1; i <= arr_a_size; i++) {
		if (i < arr_a_size) {
			lla[arr_a_size - i] = stoll(a.substr(len_a - i * LL, LL));
		}
		else {
			lla[0] = stoll(a.substr(0, len_a % LL));
		}
	}
	for (int i = 1; i <= arr_b_size; i++) {
		if (i < arr_b_size) {
			llb[arr_b_size - i] = stoll(b.substr(len_b - i * LL, LL));
		}
		else {
			llb[0] = stoll(b.substr(0, len_b % LL));
		}
	}

	// ���ڿ��� ���������� ��ȯ���� ����. �����ܿ��� ĳ���� �������ڸ��� ����
	// ĳ���� �ӽú����� ����(���� 10������ ���� ���� ��)
	// ���(���� 10������ ���� ������)�� �迭�� �������� ����
	// �迭�� �ٿ��� ���

	c = 0;
	for (int i = 0; i < arr_size; i++) {
		long long int tmp;
		tmp = c + (i < arr_a_size ? lla[i] : 0) + (i < arr_b_size ? llb[i] : 0);
		c = lla[i] < pow(10, LL) ? 0 : 1;
		result[i] = to_string(tmp%(long long int)pow(10, LL));
	}

	for (int i = 0; i < arr_size; i++) {
		cout << result[i];
	}
	cout << "\n";

	return 0;
}