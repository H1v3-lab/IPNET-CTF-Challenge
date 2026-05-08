# 11 - Basic MD5

## Nom du Challenge
Basic MD5

## Description
Un agent a laissé un hash MD5 brut dans un ticket interne. Le mot de passe est censé venir de rockyou.txt.

## Difficulté
Facile

## Points
50 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. MD5 correspond au mode 0 dans Hashcat.
2. Commence par une attaque dictionnaire simple.
3. John sait aussi lire un fichier de hash brut.

## Solution (Write-up)
```bash
echo '5f4dcc3b5aa765d61d8327deb882cf99' > hash.txt
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-MD5 hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
