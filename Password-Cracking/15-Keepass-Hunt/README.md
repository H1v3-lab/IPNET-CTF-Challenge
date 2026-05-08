# 15 - Keepass Hunt

## Nom du Challenge
Keepass Hunt

## Description
Une base KeePass volée d'un poste infiltré contient des accès critiques. La passphrase doit être récupérée.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Utilise keepass2john sur le .kdbx.
2. John gère bien ce format avec rockyou.
3. Le flag est la master password.

## Solution (Write-up)
```bash
keepass2john vault.kdbx > keepass.hash
john --wordlist=/usr/share/wordlists/rockyou.txt keepass.hash
john --show keepass.hash
```
