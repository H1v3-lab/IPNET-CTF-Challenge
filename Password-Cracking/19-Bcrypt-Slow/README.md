# 19 - Bcrypt Slow

## Nom du Challenge
Bcrypt Slow

## Description
Un service clandestin utilise bcrypt avec un cost élevé. Le challenge est d'optimiser la stratégie de cracking.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. bcrypt est volontairement lent.
2. Mode Hashcat 3200.
3. Réduis les candidats avec rockyou ciblé.

## Solution (Write-up)
```bash
john --format=bcrypt --wordlist=/usr/share/wordlists/rockyou.txt bcrypt.hash
hashcat -m 3200 -a 0 bcrypt.hash /usr/share/wordlists/rockyou.txt --optimized-kernel-enable
```
