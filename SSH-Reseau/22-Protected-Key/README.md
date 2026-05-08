# 22 - Protected Key

## Nom du Challenge
Protected Key

## Description
Vous avez récupéré la clé privée SSH de l'administrateur, mais elle est verrouillée par une passphrase.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Une clé privée commence souvent par -----BEGIN OPENSSH PRIVATE KEY-----.
2. ssh2john transforme la clé en hash crackable.
3. Cherche la passphrase dans rockyou.txt.

## Solution (Write-up)
```bash
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
john --show id_rsa.hash
# Flag: IPNET{mot_de_passe_ou_cle}
```
