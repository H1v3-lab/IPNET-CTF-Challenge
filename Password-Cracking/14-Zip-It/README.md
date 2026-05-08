# 14 - Zip It!

## Nom du Challenge
Zip It!

## Description
Une archive ZIP contenant des preuves réseau est protégée. Le mot de passe se cache dans la wordlist standard.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. zip2john extrait un hash exploitable.
2. Hashcat mode 13600 cible WinZip AES.
3. Teste d'abord avec John pour aller vite.

## Solution (Write-up)
```bash
zip2john evidence.zip > zip.hash
john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
hashcat -m 13600 -a 0 zip.hash /usr/share/wordlists/rockyou.txt
```
