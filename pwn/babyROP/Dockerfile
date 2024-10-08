FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y patchelf binutils python3 strace ltrace python-is-python3 git gcc make
RUN rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/johnsonjh/ynetd.git /ynetd
RUN cd /ynetd && make

RUN useradd -m -s /bin/bash -u 1000 pwn3r

WORKDIR /home/pwn3r/

COPY ./flag.txt ./ 
COPY ./build/babyROP ./ 
COPY ./libc.so.6 ./
COPY ./ld-linux-x86-64.so.2 ./

RUN patchelf --set-interpreter ./ld-linux-x86-64.so.2 --replace-needed libc.so.6 ./libc.so.6 ./babyROP
RUN chmod +x babyROP libc.so.6 ld-linux-x86-64.so.2 
RUN chown pwn3r:pwn3r ./babyROP ./flag.txt

RUN chmod a-w ./
RUN chmod a+x ./
USER pwn3r

EXPOSE 1343

CMD ["/ynetd/./ynetd","-p","1343","/home/pwn3r/babyROP"]

