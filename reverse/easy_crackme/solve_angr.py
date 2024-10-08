#!/usr/bin/python

import angr
import claripy

def main():
    # Load the binary
    project = angr.Project('./build/easy_crackme', auto_load_libs=False)

    # Create a symbolic buffer for input (assume the flag length is 43, the length of the original flag)
    flag_length = 43
    flag_chars = [claripy.BVS(f'flag_{i}', 8) for i in range(flag_length)]
    flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])  # Concatenate flag chars and add newline

    # Create an initial state with the symbolic input
    state = project.factory.full_init_state(
        args=['./crackme'],
        stdin=flag
    )

    # Constrain the flag to be printable characters
    for k in flag_chars:
        state.solver.add(k >= 0x20)  # ASCII space
        state.solver.add(k <= 0x7e)  # ASCII ~

    # Explore the binary to find the successful execution path
    simgr = project.factory.simgr(state)
    simgr.explore(find=lambda s: b'Congratulations' in s.posix.dumps(1))

    # If a solution is found, dump the flag
    if simgr.found:
        solution_state = simgr.found[0]
        flag_solution = solution_state.solver.eval(flag, cast_to=bytes)
        print(f'Flag found: {flag_solution.decode()}')
    else:
        print('Flag not found.')

if __name__ == '__main__':
    main()
