CHALLENGE=code_me
USER=pwn3r
USER_CRACKED=$(USER)-cracked

CC=gcc
CFLAGS=-m32 -no-pie -fno-stack-protector
LDFLAGS=-z execstack

SRC=$(CHALLENGE).c
OBJ=$(SRC:.c=.o)
BIN=$(CHALLENGE)

.DEFAULT_GOAL := challenge
.PHONY : clean all

$(BIN):
	@echo "Compiling..."
	$(CC) -o $@ $(SRC) $(LDFLAGS) $(CFLAGS)

challenge: $(BIN)
	@echo "Applying permissions..."
	rm -f $(OBJ)
	chown $(USER_CRACKED):$(USER) $(BIN) flag.txt Makefile $(SRC)
	chmod 400 flag.txt
	chmod 440 $(SRC) Makefile
	chmod 550 $(BIN)
	chmod u+s $(BIN)
