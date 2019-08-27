#include "iostream"
#include "string"

#define QUEUE_SIZE 10000

using namespace std;

class Queue {
private:
	int queue[QUEUE_SIZE];
	int head = 0;
	int rear = 0;

public:
	Queue() {}

	void enQueue(int n) {
		queue[rear++] = n;
	}

	int deQueue() {
		return empty() ? -1 : queue[head++];
	}

	int getSize() {
		return rear - head;
	}

	int empty() {
		return head == rear;
	}

	int front() {
		return empty() ? -1 : queue[head];
	}

	int back() {
		return empty() ? -1 : queue[rear - 1];
	}

	void print() {
		cout << "[";
		for (int i = 0; i < rear; i++) {
			cout << queue[i];
		}
		cout << "]" << endl;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	Queue queue = Queue();

	int n;
	cin >> n;
	cin.ignore(5, '\n');

	for (int i = 0; i < n; i++) {
		string command;
		getline(cin, command);

		switch (command.front()) {
		case 'p':
			if (command.at(1) == 'u') {
				queue.enQueue(atoi(command.substr(5).c_str()));
			}
			else {
				cout << queue.deQueue() << endl;
			}
			break;
		case 's':
			cout << queue.getSize() << endl;
			break;
		case 'e':
			cout << queue.empty() << endl;
			break;
		case 'f':
			cout << queue.front() << endl;
			break;
		case 'b':
			cout << queue.back() << endl;
			break;
		}
	}

	return 0;
}