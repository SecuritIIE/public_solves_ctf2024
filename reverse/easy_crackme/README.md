## Solution

This is a basic C crackme comparing each caracter on stdin with ascii chars to evaluate the flag.
However, these are not made in order and some arithmetic operations are involved.

The player can notify them using the binutils such as:

```bash
objdump -d build/easy_crackme  | grep cmp #x64 assembly comparison
```

If one of these are false, the program prints the wrong sentence.

```bash
objdump -d build/easy_crackme  | grep jne #x64 assembly jump if not equal
```

Several solutions are possible:

	- debugging each `jne` and set it to `je` (too much here ...)
	- use Ghidra and try to copy from the pseudo code the letters in the right order
	- use Ghidra (or IDA) and copy/paste the comparisons to solve it with z3
	- use angr (based on z3, automatically solve)
	
For the 2 last ones (z3 intended), z3 is a SMT solver that helps a lot.
See

![solve_z3.py](./solve_z3.py)
![solve_angr.py](./solve_angr.py)

