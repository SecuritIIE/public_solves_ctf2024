#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

void win() {
	setreuid(geteuid(), geteuid());
	system("/bin/bash");
}

void hello() {
	printf("Hello");
}

void main()
{
	puts("What's your name?\n"); 
	int var;
	void (*func)()=hello;
	char buf[20];
	fgets(buf,25,stdin);
	func();
	printf("%s\n",buf);
}
