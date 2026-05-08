# 09 - Known Plaintext

## Nom du Challenge
Known Plaintext

## Description
Une partie du message chiffré est connue grâce à une fuite HUMINT. Le reste du flag doit être reconstruit.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Tu connais un préfixe du plaintext.
2. Modélise la partie inconnue comme une variable.
3. Teste Coppersmith/small roots pour retrouver le suffixe.

## Solution (Write-up)
```bash
python - <<'PY'
from Crypto.Util.number import bytes_to_long
n=...
e=3
c=...
known=b'IPNET{'
print('Utiliser Sage: f.small_roots(X=2^k, beta=1)')
PY
```
