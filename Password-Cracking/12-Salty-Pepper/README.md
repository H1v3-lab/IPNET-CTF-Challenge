# 12 - Salty Pepper

## Nom du Challenge
Salty Pepper

## Description
Le service de contre-espionnage a ajouté un salt connu au mauvais endroit dans un SHA-1. Le schéma exact est à retrouver.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Teste salt+password puis password+salt.
2. SHA-1 = mode 100 dans Hashcat (non salé).
3. Prépare une wordlist transformée si nécessaire.

## Solution (Write-up)
```bash
SALT='opsec'
awk -v s="$SALT" '{print s$0}' /usr/share/wordlists/rockyou.txt > /tmp/rockyou_salted.txt
john --wordlist=/tmp/rockyou_salted.txt --format=Raw-SHA1 hash.txt
hashcat -m 100 -a 0 hash.txt /tmp/rockyou_salted.txt
```
