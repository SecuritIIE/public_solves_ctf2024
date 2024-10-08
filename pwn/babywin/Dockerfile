FROM debian:latest

RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install -y binutils make gcc-multilib gdb strace ltrace libc6 libc6-i386 nano vim python3 python-is-python3

ARG PASSWORD=pwn3r
RUN useradd -m -s /bin/bash -u 1000 pwn3r
RUN useradd -m -s /bin/bash -u 1001 pwn3r-cracked
RUN echo "pwn3r:${PASSWORD}" | chpasswd

RUN mkdir /run/sshd
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

WORKDIR /home/pwn3r/

COPY ./babywin.c ./
COPY ./flag.txt ./
COPY ./Makefile ./

RUN make

RUN chmod a-w ./
RUN chmod a+x ./

EXPOSE 1338

CMD ["/usr/sbin/sshd", "-D"]
