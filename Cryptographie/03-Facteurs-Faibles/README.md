# 03 - Facteurs Faibles

## Nom du Challenge
Facteurs Faibles

## Description
Le module RSA d'un serveur d'écoute est ridiculement petit. Les analystes pensent que n peut être factorisé rapidement.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Factorise n avant toute chose.
2. Tu peux vérifier avec factordb puis reproduire localement.
3. Une fois p et q trouvés, calcule d et déchiffre.

## Solution (Write-up)
```bash
python - <<'PY'
from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes
n=...
e=65537
c=...
f=factorint(n)
p,q=list(f.keys())
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
PY
```
