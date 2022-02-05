#include <stdio.h>
/*
CSE:TestCases$ gcc -std=c11 decl.c -o main && ./main
-1556096215 


CSE:TestCases$ clang -std=c11 decl.c -o main && ./main
7 
 */
void f(void){
	extern int h(int,int);
}

int main(int argc,char * argv[]){
	printf("%d \n", h(3.0,4.0));
	return 0;
}

int h(int a,int b){
	return a+b;
}

