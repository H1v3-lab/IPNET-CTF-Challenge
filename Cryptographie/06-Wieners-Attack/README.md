# 06 - Wieners Attack

## Nom du Challenge
Wieners Attack

## Description
Une clé RSA générée dans l'urgence a un d trop petit. Les communications d'un agent dormant doivent être relues.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Petit d peut se retrouver via fractions continues.
2. Teste un script Wiener existant.
3. Valide les candidats avec l'équation de φ(n).

## Solution (Write-up)
```bash
python - <<'PY'
from owiener import attack
from Crypto.Util.number import long_to_bytes
n=...
e=...
c=...
d=attack(e,n)
print(long_to_bytes(pow(c,d,n)))
PY
```
