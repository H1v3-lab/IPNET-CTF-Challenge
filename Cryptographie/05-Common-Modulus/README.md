# 05 - Common Modulus

## Nom du Challenge
Common Modulus

## Description
Deux équipes utilisent le même n avec des exposants publics différents. Un message diplomatique a été chiffré deux fois.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Même n + e1,e2 copremiers = fail.
2. Utilise Bézout sur e1 et e2.
3. Combine c1 et c2 avec les coefficients trouvés.

## Solution (Write-up)
```bash
python - <<'PY'
from Crypto.Util.number import long_to_bytes
from math import gcd
n=...
e1=...
e2=...
c1=...
c2=...
assert gcd(e1,e2)==1

def egcd(a,b):
    if b==0: return (1,0,a)
    x,y,g=egcd(b,a%b)
    return (y, x-(a//b)*y, g)

u,v,_=egcd(e1,e2)
m=(pow(c1,u,n)*pow(c2,v,n))%n
print(long_to_bytes(m))
PY
```
