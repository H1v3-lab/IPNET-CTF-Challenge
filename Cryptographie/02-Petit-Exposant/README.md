# 02 - Petit Exposant

## Nom du Challenge
Petit Exposant

## Description
Un opérateur ennemi a utilisé RSA avec e=3 et un message trop court. Le trafic chiffré a été capturé avant suppression.

## Difficulté
Facile

## Points
50 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Cherche une racine cubique entière.
2. Si m^3 < n, pas besoin de clé privée.
3. Teste gmpy2.iroot(c, 3).

## Solution (Write-up)
```bash
python - <<'PY'
import gmpy2
from Crypto.Util.number import long_to_bytes
c=...
m,ok=gmpy2.iroot(c,3)
if ok:
    print(long_to_bytes(int(m)))
PY
```
