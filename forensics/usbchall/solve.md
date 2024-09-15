## Solve

Mount the usb key image :

`unzip usb_key.zip`
`mkdir /mnt/usb_key`
`sudo mount -o loop mysterious_usb.image /mnt/usb_key`

Examine the metadata of the image :

`exiftool /mnt/usb_key/bankstatement.jpg`
See the "Comment" field which includes the flag.

Flag is : FSIIECTF{ff71ec3784ad8e923b0c7ab2044e3bde70a96e472f87a026576482c946dbbb53}
