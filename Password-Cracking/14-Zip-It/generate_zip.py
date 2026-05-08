#!/usr/bin/env python3
from pathlib import Path
import subprocess

password = 'IPNET{zip_it_unpacked}'
base = Path(__file__).resolve().parent
payload = base / 'evidence.txt'
archive = base / 'evidence.zip'

payload.write_text('Network evidence package\nFlag: IPNET{zip_it_unpacked}\n', encoding='utf-8')
subprocess.run(['zip','-j','-P',password,str(archive),str(payload)], check=True)
print(f'Created {archive.name} with password {password}')
