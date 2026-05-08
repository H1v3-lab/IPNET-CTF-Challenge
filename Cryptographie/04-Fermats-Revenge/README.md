# 04 - Fermat's Revenge

## Nom du Challenge
Fermat's Revenge

## Description
Deux nombres premiers trop proches ont été utilisés pour une clé opérationnelle. L'adversaire pensait le défaut invisible.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Quand p≈q, pense à Fermat.
2. Cherche a^2 - n = b^2.
3. Itère a à partir de ceil(sqrt(n)).

## Solution (Write-up)
```bash
python - <<'PY'
from math import isqrt
from Crypto.Util.number import inverse, long_to_bytes
n=...
e=65537
c=...
a=isqrt(n)
if a*a<n: a+=1
while True:
    b2=a*a-n
    b=isqrt(b2)
    if b*b==b2:
        p=a-b
        q=a+b
        break
    a+=1
phi=(p-1)*(q-1)
d=inverse(e,phi)
print(long_to_bytes(pow(c,d,n)))
PY
```
