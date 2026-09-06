#!/usr/bin/env python3
"""Offline teaching model using synthetic fixtures; this is not an Azure emulator or an AI model.
Run: python3 analyse.py --input mock-data.json --output results.json
No cloud deployment and no network access.
"""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',default='mock-data.json');p.add_argument('--output',default='results.json');a=p.parse_args()
source=Path(a.input);raw=source.read_bytes();rows=json.loads(raw);out=[]
rules=[(100,'web','app',443,'ALLOW'),(110,'app','data',1433,'ALLOW')]
for r in rows:
    match=next((x for x in sorted(rules) if (r['src'],r['dst'],r['port'])==x[1:4]),None)
    out.append({'id':r['id'],'decision':match[4] if match else 'DENY','rule':match[0] if match else 'default'})
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
