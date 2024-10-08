import dis

flag = "FSIIECTF{6d211d61d642be9f891db55710ef0ade}"

def fail():
    return

def success():
    return

def flagChecker(flag):
    # Prefix and Suffix Check
    if flag[:9] != "FSIIECTF{":
        fail()
    
    if flag[-1:] != "}":
        fail()

    # Character Frequency and Position Checks
    if flag[9] != '6' or flag[15] != '6' or flag[18] != '6':
        fail()

    if flag[10] != 'd' or flag[14] != 'd' or flag[17] != 'd' or flag[28] != 'd' or flag[39] != 'd':
        fail()

    if flag[11] != '2' or flag[20] != '2':
        fail()

    if flag[12] != '1' or flag[13] != '1' or flag[16] != '1' or flag[27] != '1' or flag[33] != '1':
        fail()

    if flag[19] == chr(ord(flag[15])-2):
        success()

    if flag[21] != 'b' or flag[29] != 'b':
        fail()

    if flag[22] != 'e' or flag[35] != 'e' or flag[40] != 'e':
        fail()

    if flag[23] != '9' or flag[26] != '9':
        fail()

    if flag[24] != 'f' or flag[36] != 'f':
        fail()

    if flag[25] == chr(flag[40]-45):
        success()

    if flag[30] != '5' or flag[31] != '5':
        fail()
   
    if flag[32] == chr(ord(flag[30])+2):
        success()

    if flag[38] == chr(ord(flag[26])+40):
        success()

    if flag[34] != '0' or flag[37] != '0':
        fail()

    # If all checks pass, we assume the flag is correct
    success()

# To check how the bytecode looks
code = flagChecker.__code__
dis.dis(code)
