# 13 - The PDF Lock

## Nom du Challenge
The PDF Lock

## Description
Un dossier classifié PDF a été exfiltré mais reste chiffré. L'objectif est d'ouvrir le document sans alerter la cible.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Convertis le PDF avec pdf2john.
2. Ensuite lance John avec rockyou.txt.
3. Le flag est le mot de passe trouvé.

## Solution (Write-up)
```bash
pdf2john secret.pdf > pdf.hash
john --wordlist=/usr/share/wordlists/rockyou.txt pdf.hash
john --show pdf.hash
```
