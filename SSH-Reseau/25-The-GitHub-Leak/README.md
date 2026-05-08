# 25 - The GitHub Leak

## Nom du Challenge
The GitHub Leak

## Description
Une clé privée SSH a été poussée puis supprimée d'un dépôt. L'historique Git contient encore la preuve.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Les secrets supprimés restent dans les anciens commits.
2. Utilise git log et git show sur chaque révision.
3. Convertis la clé trouvée puis cracke sa passphrase si besoin.

## Solution (Write-up)
```bash
git --no-pager log --oneline --all
git --no-pager grep -n "BEGIN OPENSSH PRIVATE KEY" $(git rev-list --all)
git --no-pager show <commit>:id_rsa > leaked_id_rsa
ssh2john leaked_id_rsa > leaked.hash
john --wordlist=/usr/share/wordlists/rockyou.txt leaked.hash
```
