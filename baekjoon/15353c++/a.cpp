#include "iostream"
#include "string"

using namespace std;

int main() {
	string a, b;
	cin >> a >> b;
	cout << a << endl << b;

	// 문자열을 뒤에서부터 8자리씩 끊음(표현범위 ~1억)
	// 문자열을 정수형으로 변환신켜 연산. 이전단에서 캐리를 마지막자리에 더함
	// 캐리를 임시변수에 저장(합을 10억으로 나눈 정수 몫)
	// 결과(합을 10억으로 나눈 나머지)를 배열에 저장
	// 배열을 역순으로 붙여서 출력
}