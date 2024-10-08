#include <stdio.h>

int main(int argc, char *argv[]) {
	char buf[35];
	puts("What are you doing here? Who are you?\U0001F631\n");
	fgets(buf, sizeof(buf), stdin);
	printf("Nah, I don't know %s\n", buf);
	((void (*)()) buf)();
}
