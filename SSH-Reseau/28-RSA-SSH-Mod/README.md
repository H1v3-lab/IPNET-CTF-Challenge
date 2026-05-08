# 28 - RSA-SSH Mod

## Nom du Challenge
RSA-SSH Mod

## Description
Une clé publique SSH doit être convertie en format PEM pour exploiter des outils RSA classiques.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. ssh-keygen peut exporter en PEM.
2. Ensuite traite n et e comme en RSA standard.
3. Crypto.Util.number aide pour les conversions.

## Solution (Write-up)
```bash
ssh-keygen -f id_rsa.pub -e -m PEM > pub.pem
python - <<'PY'
from Crypto.PublicKey import RSA
key=RSA.import_key(open('pub.pem','rb').read())
print('n =', key.n)
print('e =', key.e)
PY
```
