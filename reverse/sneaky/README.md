## Solution

### 1st Step

First use [Detect it Easy](https://github.com/horsicq/Detect-It-Easy) to identify the type of file.

```
diec -rd sneaky 
Cannot load database: /opt/detect-it-easy/db_custom
ELF64
    Packer: UPX(4.24)[NRV,brute]
```

UPX is a packer which has packed the binary. Or if we use `strings` on the binary we'll find the packer name too.
To unpack it:

```bash
upx -d sneaky
```

We have now another binary, and `strings` informs us that it contains  `cython` code.
That means the original binary was probably a python script compiled with `pyinstaller`.

So unpack the program using [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor)
You will find many files but focus on `snakey.pyc`

### 2nd Step

Reverse `sneaky.pyc` using https://docs.python.org/2/library/dis.html documentation

The python bytecode is under the form:

```txt
Line_number	>>(=Labelled Instruction)	Address Instruction	Instruction	Opcode	(Parameter value)
```

For instance 

```
 59     >>  814 LOAD_FAST                0 (flag)
            816 LOAD_CONST              47 (34)
            818 BINARY_SUBSCR
            822 LOAD_CONST              48 ('0')
            824 COMPARE_OP              55 (!=)
            828 POP_JUMP_IF_TRUE         8 (to 846)
            830 LOAD_FAST                0 (flag)
            832 LOAD_CONST              49 (37)
            834 BINARY_SUBSCR
            838 LOAD_CONST              48 ('0')
            840 COMPARE_OP              55 (!=)
            844 POP_JUMP_IF_FALSE       10 (to 866)

45     >>  634 LOAD_GLOBAL              1 (NULL + fail)
           644 CALL                     0
           652 POP_TOP
```

means

```py
if flag[34] != '0' or flag[37] != '0':
    fail()
```

### 3d Step

Then write constraints and solve using z3:

```bash
python solve.py
```

To ensure that this challenge is correct, compare constraints in `challenge_generator.py` and solve.py`.
