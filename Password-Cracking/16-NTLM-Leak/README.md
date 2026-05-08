# 16 - NTLM Leak

## Nom du Challenge
NTLM Leak

## Description
Un dump mémoire d'un poste Windows compromis révèle des NTLM. Il faut retrouver le mot de passe opérateur.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. NTLM = mode 1000 dans Hashcat.
2. Conserve uniquement la partie hash utile.
3. Lance une attaque dictionnaire rockyou.

## Solution (Write-up)
```bash
echo 'b4b9b02e6f09a9bd760f388b67351e2b' > ntlm.hash
john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt ntlm.hash
hashcat -m 1000 -a 0 ntlm.hash /usr/share/wordlists/rockyou.txt
```
