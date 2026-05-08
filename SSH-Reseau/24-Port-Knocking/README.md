# 24 - Port Knocking

## Nom du Challenge
Port Knocking

## Description
Le port SSH est fermé sur un serveur de transit. Une séquence de knocks réseau active temporairement l'accès.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Observe les logs réseau pour l'ordre des ports.
2. nmap ne suffit pas tant que la séquence n'est pas faite.
3. Automatise les knocks puis connecte-toi vite.

## Solution (Write-up)
```bash
for p in 7000 8000 9000; do nc -zv 10.10.10.24 $p; done
nmap -p 22 10.10.10.24
ssh analyst@10.10.10.24
```
