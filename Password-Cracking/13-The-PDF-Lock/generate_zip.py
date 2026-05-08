#!/usr/bin/env python3
from pathlib import Path
import subprocess

password = 'IPNET{pdf_lock_broken}'
base = Path(__file__).resolve().parent
pdf_file = base / 'secret.pdf'
zip_file = base / 'secret.zip'

pdf_file.write_text('Confidential briefing\nFlag: IPNET{pdf_lock_broken}\n', encoding='utf-8')
subprocess.run(['zip','-j','-P',password,str(zip_file),str(pdf_file)], check=True)
print(f'Created {zip_file.name} with password {password}')
