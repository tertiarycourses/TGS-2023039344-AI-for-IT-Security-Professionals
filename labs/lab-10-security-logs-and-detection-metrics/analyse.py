#!/usr/bin/env python3
"""Offline teaching model using synthetic fixtures; this is not an Azure emulator or an AI model.
Run: python3 analyse.py --input mock-data.json --output results.json
No cloud deployment and no network access.
"""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',default='mock-data.json');p.add_argument('--output',default='results.json');a=p.parse_args()
source=Path(a.input);raw=source.read_bytes();rows=json.loads(raw);out=[]
for user in sorted({r['user'] for r in rows}):
    events=sorted([r for r in rows if r['user']==user and r['failed']],key=lambda r:r['minute'])
    peak=max((sum(0<=x['minute']-e['minute']<5 for x in events) for e in events),default=0)
    out.append({'id':user,'peak':peak,'decision':'ALERT' if peak>=5 else 'NO_ALERT'})
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
