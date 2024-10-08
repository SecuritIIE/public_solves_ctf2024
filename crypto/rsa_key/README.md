# Wiener Attack - @Night (4nuit)

The aim for the player is to reconstruct the private key using Wiener attack.

The challenger has to:

- read the public key (for instance using PyCryptoDome ImportKey()), 

- using the continuous fractions attack (for instance with owiener.py, findable on github) to recover d and phi (bruteforce)

- solve a polynomial equation to recover n = p*q knowning phi 

- log into the container to cat the flag. 

## Setup

```bash
docker-compose up
```

```bash
ngrok tcp 22
ssh -p 1???? dockeruser@?.tcp.eu.ngrok.io
```

## Challenge

```bash
python gen_keys.py
```

## Solution

```bash
python sol.py
```

## Nettoyage

```bash
./clean.sh
```
