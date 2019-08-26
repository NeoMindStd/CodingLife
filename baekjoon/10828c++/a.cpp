#include "iostream"
#include "string"

#define STACK_SIZE 10000

using namespace std;

class Stack {
private:
	int stack[STACK_SIZE];
	int size = 0;

public:
	Stack() {}

	void push(int n) {
		stack[size++] = n;
	}

	int pop() {
		return size > 0 ? stack[--size] : -1;
	}

	int getSize() {
		return size;
	}

	int empty() {
		return size != 0 ? 0 : 1;
	}

	int top() {
		return size > 0 ? stack[size - 1] : -1;
	}

	void print() {
		cout << "[";
		for (int i = 0; i < size; i++) {
			cout << stack[i];
		}
		cout << "]" << endl;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	Stack stack = Stack();

	int n;
	cin >> n;
	cin.ignore(5, '\n');

	for (int i = 0; i < n; i++) {
		string command;
		getline(cin, command);
		
		switch (command.front()) {
		case 'p':
			if (command.at(1) == 'u') {
				stack.push(atoi(command.substr(5).c_str()));
			}
			else {
				cout << stack.pop() << endl;
			}
			break;
		case 's':
			cout << stack.getSize() << endl;
			break;
		case 'e':
			cout << stack.empty() << endl;
			break;
		case 't':
			cout << stack.top() << endl;
			break;
		}
	}

	return 0;
}