#!/usr/bin/env python3
"""Offline teaching model using synthetic fixtures; this is not an Azure emulator or an AI model.
Run: python3 analyse.py --input mock-data.json --output results.json
No cloud deployment and no network access.
"""
import argparse,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--input',default='mock-data.json');p.add_argument('--output',default='results.json');a=p.parse_args()
source=Path(a.input);raw=source.read_bytes();rows=json.loads(raw);out=[]
tp=sum(r['label'] and r['predicted'] for r in rows);fp=sum(not r['label'] and r['predicted'] for r in rows);fn=sum(r['label'] and not r['predicted'] for r in rows);tn=sum(not r['label'] and not r['predicted'] for r in rows)
out=[{'id':'evaluation','TP':tp,'FP':fp,'FN':fn,'TN':tn,'precision':round(tp/(tp+fp),4) if tp+fp else None,'recall':round(tp/(tp+fn),4) if tp+fn else None,'decision':'REVIEW_ERRORS'}]
report={'source_sha256':hashlib.sha256(raw).hexdigest(),'simulation':True,'results':out}
Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
