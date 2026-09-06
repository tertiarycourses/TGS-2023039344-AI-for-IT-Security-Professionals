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
    coverage=r['events_seen']/r['events_expected'] if r['events_expected'] else None
    decision='WAIT_APPROVAL' if not r['approved'] else ('ACTION_FAILED' if not r['action_ok'] else ('RECOVERED' if r['retest_ok'] and coverage is not None and coverage>=0.9 else 'VERIFY_REQUIRED'))
    out.append({'id':r['id'],'coverage':coverage,'decision':decision})
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
