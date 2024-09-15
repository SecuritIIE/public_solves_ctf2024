## Solve

RDP sessions store a bitmap cache by default in the C:\Users\USERNAME\AppData\Local\Microsoft\Terminal Server Client\Cache folder on the local computer (where the RDP connection originates). You can often find useful information in there about what somebody did when connected to a RDP session on a remote computer.

You're provided with a snapshot of a user's folder, which has previously connected to the domain controller via RDP. Because of this, there is a file in the Cache directory above called Cache0000.bin.

To extract the bitmap files from this cache, use this tool: https://github.com/ANSSI-FR/bmc-tools

Here is the command : `python3 bmc-tools.py -s AppData -d out -b` because AppData is where the cache data can be found.

The directory contains a lot of images, so to make it easier to spot the correct ones, the -b flag combines them into a collage, Cache0000.bin_collage.bmp.

If you zoom in at the center top of the collage, you can see a powershell window open that is running net user svc_admin password123! /add.

The flag is the username svc_admin, but md5 hashed and with FSIIECTF{...}, which gives :

FSIIECTF{c928f2fefc32c8391b21df9a8f420b73}
