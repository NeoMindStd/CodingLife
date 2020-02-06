#include <iostream>
#include <string>

#define max(x,y) x>y?x:y

using namespace std;

class BigInt {
public:
	string value;
	BigInt() {
		value = "0";
	}
	BigInt(string &string) {
		value = string;
	}

	BigInt operator + (BigInt& operand) {
		int size = max(value.length(), operand.value.length());
		int* result = new int[size];
		int c = 0;
		for (int i = 0; i < size; i++) {
			result[size - i - 1] = c;
			if (value.length() > i) result[size - i - 1] += value[value.length()-i-1] - '0';
			if (operand.value.length() > i) result[size - i - 1] += operand.value[operand.value.length()-i-1] - '0';
			c = result[size - i - 1] / 10;
			result[size - i - 1] %= 10;
		}
		string s = to_string(c);
		for (int i = 0; i < size; i++) {
			s+=to_string(result[i]);
		}
		while (s[0] == '0' && s.length() > 1) {
			s=s.substr(1, s.length() - 1);
		}
		delete result;
		return BigInt(s);
	}

	BigInt operator * (BigInt& operand) {
		BigInt ac = BigInt();
		for (int i = 0; i < operand.value.length(); i++) {
			int* temp = new int[value.length() + 1];
			temp[value.length()] = 0;
			for (int j = 0; j < value.length(); j++) {
				temp[value.length() - j] += (value[value.length() - j - 1]-'0') * (operand.value[operand.value.length() - i - 1] - '0');
				temp[value.length() - j - 1] = temp[value.length() - j] / 10;
				temp[value.length() - j] %= 10;
			}
			string s = to_string(temp[0]);
			for (int k = 1; k < value.length() + 1; k++) {
				s += to_string(temp[k]);
			}
			for (int k = 0; k < i; k++) {
				s += "0";
			}
			BigInt t = BigInt(s);
			ac = ac + t;
		}
		return ac;
	}

	bool operator > (BigInt& operand) {
		if (value.length() == operand.value.length()) {
			for (int i = 0; i < value.length(); i++) {
				if (value[i] == operand.value[i]) continue;
				return value[i] >= operand.value[i];
			}
		}
		return value.length() > operand.value.length();
	}
};

int main() {
	string a, b, r;
	cin >> a >> b >> r;
	
	BigInt A = BigInt(a), B = BigInt(b), R = BigInt(r);
	BigInt AB = A * B;
	if (AB > R) cout << "overflow";
	else cout << AB.value;

	return 0;
}