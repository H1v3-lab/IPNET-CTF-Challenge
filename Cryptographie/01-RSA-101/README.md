# 01 - RSA 101

## Nom du Challenge
RSA 101

## Description
Une cellule de cyber-espionnage intercepte une clé RSA incomplète. Les agents ont p, q et e, mais pas d pour déchiffrer le message volé.

## Difficulté
Facile

## Points
50 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Calcule d à partir de φ(n).
2. φ(n) = (p-1)(q-1).
3. Utilise inverse(e, φ(n)) de Crypto.Util.number.

## Solution (Write-up)
```bash
python - <<'PY'
from Crypto.Util.number import inverse
p=...
q=...
e=65537
phi=(p-1)*(q-1)
d=inverse(e, phi)
print(d)
PY
```
