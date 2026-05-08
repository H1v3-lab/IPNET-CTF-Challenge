# 08 - RSA Sign

## Nom du Challenge
RSA Sign

## Description
Un portail d'espionnage valide mal les signatures RSA. Une falsification permettrait d'injecter un ordre.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Observe la vérification PKCS#1 v1.5 incomplète.
2. Les padding checks faibles sont exploitables.
3. Forge une signature dont le cube commence bien.

## Solution (Write-up)
```bash
python - <<'PY'
from Crypto.Util.number import bytes_to_long, long_to_bytes
import gmpy2
prefix = b'\x00\x01\xff\x00ASN1_SHA256...'
block = prefix + b'FLAG=IPNET{mot_de_passe_ou_cle}' + b'\x00'*64
s = int(gmpy2.iroot(bytes_to_long(block), 3)[0])
print(long_to_bytes(s))
PY
```
