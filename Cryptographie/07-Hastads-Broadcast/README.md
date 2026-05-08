# 07 - Håstad's Broadcast

## Nom du Challenge
Håstad's Broadcast

## Description
Le même ordre chiffré avec e=3 a été diffusé à trois relais. Les trois interceptions sont disponibles.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Combine les trois chiffrés par CRT.
2. Ensuite prends la racine cubique.
3. Le message est identique dans les trois flux.

## Solution (Write-up)
```bash
python - <<'PY'
import gmpy2
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
n1=...
n2=...
n3=...
c1=...
c2=...
c3=...
C,_=crt([n1,n2,n3],[c1,c2,c3])
m,ok=gmpy2.iroot(int(C),3)
if ok:
    print(long_to_bytes(int(m)))
PY
```
