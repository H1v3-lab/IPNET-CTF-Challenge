# 17 - Custom Rule

## Nom du Challenge
Custom Rule

## Description
Le mot de passe provient de rockyou mais l'attaquant ajoute systématiquement 2024 en suffixe.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Crée des candidats avec une règle simple.
2. Hashcat peut appliquer $2024 via rules.
3. John supporte aussi les règles dynamiques.

## Solution (Write-up)
```bash
echo '$2024' > /tmp/append2024.rule
hashcat -m 1400 -a 0 hash.txt /usr/share/wordlists/rockyou.txt -r /tmp/append2024.rule
john --wordlist=/usr/share/wordlists/rockyou.txt --rules hash.txt
```
