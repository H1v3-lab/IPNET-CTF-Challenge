# 10 - LSB Oracle

## Nom du Challenge
LSB Oracle

## Description
Un serveur d'interception répond uniquement pair/impair sur le plaintext déchiffré. Cette fuite binaire suffit à tout extraire.

## Difficulté
Expert

## Points
500 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Un bit d'info par requête est déjà beaucoup.
2. Multiplie c par (2^e)^i mod n.
3. Fais une recherche dichotomique sur l'intervalle du message.

## Solution (Write-up)
```bash
python - <<'PY'
from decimal import Decimal, getcontext
getcontext().prec = 4096
n=...
e=65537
c=...
# Remplacer n/e/c par les entiers fournis dans l'énoncé avant exécution.
# Implémenter oracle(ci) selon le service cible (retour 0/1 pair-impair).
# oracle(ci) doit retourner 0 si le plaintext déchiffré est pair, 1 sinon.
# Exemple: bit = int(requests.get(f'http://oracle.local/check?c={ci}').text)
low, high = Decimal(0), Decimal(n)
mult = pow(2,e,n)
ci = c
for _ in range(n.bit_length()):
    ci = (ci * mult) % n
    bit = oracle(ci)
    mid = (low + high) / 2
    if bit == 0:
        high = mid
    else:
        low = mid
print(int(high))
PY
```
