#include <stdio.h>
#define scanf scanf_s

float avg(int scores[1000], int count) {
	int sum = 0;
	for(int i = 0; i < count; i++)
		sum += scores[i];
	return sum / (float)count;
}

int main() {
	int n;
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++) {
		int count;
		scanf("%d", &count);
		int scores[1000];
		for(int j = 0; j < count; j++) {
			scanf("%d", &scores[j]);
		}
		float mean = avg(scores, count);
		int meanOverCount = 0;
		for (int j = 0; j < count; j++) {
			if ((float)scores[j] > mean) {
				meanOverCount++;
			}
		}
		printf("%.3f%%\n", meanOverCount / (float)count * 100);
	}
	
	return 0;
}