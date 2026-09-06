#!/usr/bin/env python3
"""Offline teaching model using synthetic fixtures; this is not an Azure emulator or an AI model.
Run: python3 analyse.py --input mock-data.json --output results.json
No cloud deployment and no network access.
"""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',default='mock-data.json');p.add_argument('--output',default='results.json');a=p.parse_args()
source=Path(a.input);raw=source.read_bytes();rows=json.loads(raw);out=[]
allowed={'read_incident','contain_test'}
for r in rows:
    decision='DENY_TOOL' if r['tool'] not in allowed else ('DENY_BINDING' if r['target']!=r['approved_target'] else ('DENY_EXPIRED' if r['expired'] else 'ALLOW'))
    out.append({'id':r['id'],'decision':decision})
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
