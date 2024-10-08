CHALLENGE=easy_crackme
BUILD=build

CC=gcc

SRC=$(CHALLENGE).c
BIN=$(BUILD)/$(CHALLENGE)

.DEFAULT_GOAL := challenge
.PHONY : clean all

$(BUILD):
	mkdir $(BUILD)

$(BIN): $(SRC) | $(BUILD)
	@echo "Compiling..."
	$(CC) -o $@ $(SRC)

challenge: $(BIN)
	rm -f $(OBJ)

clean:
	rm -rf $(BUILD)
