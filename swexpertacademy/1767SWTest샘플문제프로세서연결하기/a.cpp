#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int n, cMax, lMin;
int** a;
static const int mvR[4] = { -1,0,1,0 };
static const int mvC[4] = { 0,1,0,-1 };

struct core {
	int r, c;
};

vector<core> cores;

int countLine() {
	int l = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (a[i][j] == 2) l++;
		}
	}
	return l;
}

void tryConnect(int connected, int idx) {
	if (idx >= cores.size()) {
		if (cMax < connected) {
			cMax = connected;
			// lMin 변경
			lMin = countLine();
		}
		else if (cMax == connected) {
			// lMin과 현재 연결된 라인 수 따져서 변경여부 결정
			lMin = min(countLine(), lMin);
		}
		return;
	}

	for (int d = 0; d < 4; d++) {
		int r = cores[idx].r, c = cores[idx].c;
		bool isConnectable = false;
		while (a[r + mvR[d]][c + mvC[d]] == 0) {
			r += mvR[d];
			c += mvC[d];
			if (r == 0 || c == 0 || r == n - 1 || c == n - 1) {
				isConnectable = true;
				break;
			}
		}
		if (isConnectable) {
			// 전선 연결시키기
			int r = cores[idx].r, c = cores[idx].c;
			while (a[r + mvR[d]][c + mvC[d]] == 0) {
				r += mvR[d];
				c += mvC[d];
				a[r][c] = 2;
				if (r == 0 || c == 0 || r == n - 1 || c == n - 1) {
					connected++;
					break;
				}
			}
		}

		tryConnect(connected, idx + 1);

		if (isConnectable) {
			// 전선 지우기
			int r = cores[idx].r, c = cores[idx].c;
			while (a[r + mvR[d]][c + mvC[d]] == 2) {
				r += mvR[d];
				c += mvC[d];
				a[r][c] = 0;
				if (r == 0 || c == 0 || r == n - 1 || c == n - 1) {
					connected--;
					break;
				}
			}
		}
	}
}

int main() {
	int testCase;
	scanf(" %d", &testCase);
	for (int T = 1; T <= testCase; T++) {
		cMax = 0, lMin = 2147483647;
		cores.clear();
		scanf(" %d", &n);
		a = new int*[n];
		for (int i = 0; i < n; i++) {
			a[i] = new int[n];
			for (int j = 0; j < n; j++) {
				scanf(" %d", &a[i][j]);
				if (a[i][j] == 1 && i > 0 and j > 0 && i < n - 1 && j < n - 1)
					cores.push_back({ i,j });
			}
		}

		tryConnect(0, 0);

		printf("#%d %d\n", T, lMin);
	}

	return 0;
}