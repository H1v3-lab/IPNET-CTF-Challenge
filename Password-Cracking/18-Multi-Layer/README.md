# 18 - Multi-Layer

## Nom du Challenge
Multi-Layer

## Description
Un premier hash MD5 révèle un sel nécessaire pour casser un second SHA-512. La chaîne d'attaque est en deux étapes.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Cracke d'abord le MD5.
2. Réutilise le résultat comme sel du second hash.
3. Automatise avec un petit script shell.

## Solution (Write-up)
```bash
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt step1.hash
SALT=$(john --show step1.hash | cut -d: -f2 | head -n1)
awk -v s="$SALT" '{print $0 s}' /usr/share/wordlists/rockyou.txt > /tmp/rockyou_layer2.txt
hashcat -m 1700 -a 0 step2.hash /tmp/rockyou_layer2.txt
```
