# 20 - The Repository

## Nom du Challenge
The Repository

## Description
Le hash cracké donne le nom d'un répertoire GitHub secret utilisé par une cellule de fuite.

## Difficulté
Expert

## Points
500 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Le mot de passe décodé ressemble à un nom de repo.
2. Cracke le hash comme un classique dictionnaire.
3. Le flag reprend la valeur exacte trouvée.

## Solution (Write-up)
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-SHA256 repo.hash
REPO=$(john --show repo.hash | cut -d: -f2 | head -n1)
echo "https://github.com/H1v3-lab/${REPO}"
# Flag: IPNET{mot_de_passe_ou_cle}
```
