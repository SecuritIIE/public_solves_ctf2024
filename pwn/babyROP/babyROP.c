#include <stdlib.h>
#include <stdio.h>

void disable_buffering();

int main(int argc, char *argv[]) {

    disable_buffering();

    char buffer[16];
    printf("Hi there. Are you lost?\n");
    scanf("%s", buffer);
    puts("See ya ! \n");

    return 0;
}

void disable_buffering() {

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}
