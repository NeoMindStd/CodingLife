#include <stdio.h>

int main(){
	char string[100];
	scanf("%s", string);
	
	int nullFlag = 0;
	
	for(int i = 0; i < 10; i++) {
		for(int j = 0; j < 10; j++) {
			char ch = string[i*10+j];
			nullFlag = ch=='\0';
			if(nullFlag) break;
			printf("%c", ch);
		}
		if(nullFlag) break;
		printf("\n");
	}
	
	return 0;
}