# 23 - SSH Config Leak

## Nom du Challenge
SSH Config Leak

## Description
Une machine d'analyse contient des traces de credentials dans des fichiers shell et SSH mal nettoyés.

## Difficulté
Facile

## Points
50 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Inspecte .ssh/config et les historiques shell.
2. Cherche password, pass, IdentityFile.
3. Le flag est le secret trouvé dans les logs.

## Solution (Write-up)
```bash
grep -RinE 'password|passphrase|IdentityFile|HostName|user' ~/.ssh ~/.bash_history /var/log 2>/dev/null
python - <<'PY'
import re, pathlib
for p in [pathlib.Path.home()/'.ssh/config', pathlib.Path.home()/'.bash_history']:
    if p.exists():
        data=p.read_text(errors='ignore')
        for m in re.findall(r'(password\s*[:=]?\s*\S+)', data, flags=re.I):
            print(m)
PY
```
