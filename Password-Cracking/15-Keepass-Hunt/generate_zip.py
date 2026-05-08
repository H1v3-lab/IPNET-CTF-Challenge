#!/usr/bin/env python3
from pathlib import Path
import subprocess

password = 'IPNET{keepass_master_found}'
base = Path(__file__).resolve().parent
kdbx = base / 'vault.kdbx'
archive = base / 'vault.zip'

kdbx.write_bytes(b'KDBX_PLACEHOLDER\nFlag=IPNET{keepass_master_found}\n')
subprocess.run(['zip','-j','-P',password,str(archive),str(kdbx)], check=True)
print(f'Created {archive.name} with password {password}')
