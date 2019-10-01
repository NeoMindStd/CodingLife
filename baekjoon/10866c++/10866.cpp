#include "string"
#include "iostream"

#define scanf scanf_s

using namespace std;

class Deque {
private:
	int* deque;
	int length;
	int head = 0;
	int rear = 0;

public:
	Deque(int n) {
		deque = new int[n];
		length = n;
		head = 0;
		rear = 0;
	}

	void push_front(int n) {
		deque[(--head+length) % length] = n;
	}

	void push_back(int n) {
		deque[(rear++ + length) % length] = n;
	}

	int pop_front() {
		return empty() ? -1 : deque[(head++ + +length) % length];
	}

	int pop_back() {
		return empty() ? -1 : deque[(--rear + +length) % length];
	}

	int getSize() {
		return rear - head;
	}

	int empty() {
		return head == rear;
	}

	int front() {
		return empty() ? -1 : deque[(head + length) % length];
	}

	int back() {
		return empty() ? -1 : deque[(rear - 1 + length) % length];
	}
};

int main() {
	ios_base::sync_with_stdio(false);

	int n;
	cin >> n;
	cin.ignore(5, '\n');

	Deque deque = Deque(n);

	for (int i = 0; i < n; i++) {
		string command;
		getline(cin, command);

		switch (command.front()) {
		case 'p':
			switch (command.at(5)) {
			case 'f':
				deque.push_front(atoi(command.substr(11).c_str()));
				break;
			case 'b':
				deque.push_back(atoi(command.substr(10).c_str()));
				break;
			case 'r':
				cout << deque.pop_front() << "\n";
				break;
			case 'a':
				cout << deque.pop_back() << "\n";
				break;
			}
			break;
		case 's':
			cout << deque.getSize() << "\n";
			break;
		case 'e':
			cout << deque.empty() << "\n";
			break;
		case 'f':
			cout << deque.front() << "\n";
			break;
		case 'b':
			cout << deque.back() << "\n";
			break;
		}
	}

	return 0;
}