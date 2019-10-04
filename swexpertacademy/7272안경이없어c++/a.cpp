#include <iostream>
#include <string>

using namespace std;

static const string h[3] = { 
	string("CEFGHIJKLMNSTUVWXYZ"),
	string("ADOPQR") ,
	string("B")
};

int main() {
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);
	int T;
	cin >> T;
	for (int Ti = 1; Ti <= T; Ti++) {
		string a, b;
		cin >> a >> b;
		if (a.length() != b.length()) {
			cout << "#" << Ti << " " << "DIFF" << "\n";
		}
		else {
			bool flag;
			for (int i = 0; i < a.length(); i++) {
				for (int j = 0; j < 3; j++) {
					flag = (h[j].find(a.at(i)) == string::npos) == (h[j].find(b.at(i)) == string::npos);
					if (!flag) break;
				}
				if (!flag) break;
			}
			cout << "#" << Ti << " " << (flag ? "SAME" : "DIFF") << "\n";
		}
	}

	return 0;
}