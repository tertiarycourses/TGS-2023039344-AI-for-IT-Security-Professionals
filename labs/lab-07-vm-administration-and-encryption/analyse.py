#!/usr/bin/env python3
"""Offline teaching model using synthetic fixtures; this is not an Azure emulator or an AI model.
Run: python3 analyse.py --input mock-data.json --output results.json
No cloud deployment and no network access.
"""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',default='mock-data.json');p.add_argument('--output',default='results.json');a=p.parse_args()
source=Path(a.input);raw=source.read_bytes();rows=json.loads(raw);out=[]
for r in rows:
    issues=[]
    if r['public_admin']: issues.append('PUBLIC_ADMIN')
    if r['jit_minutes']>60: issues.append('LONG_WINDOW')
    if not r['encrypted']: issues.append('ENCRYPTION_REVIEW')
    out.append({'id':r['id'],'decision':','.join(issues) if issues else 'BASELINE_OK'})
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
