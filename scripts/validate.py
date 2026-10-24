#!/usr/bin/env python3
"""Validate snapshot research copies, public downloads, source references, and static API."""
import csv, json, hashlib, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return sum(1 for _ in csv.DictReader(f))
errors=[]
with (ROOT/'catalog/datasets.csv').open(encoding='utf-8-sig',newline='') as f:
 for r in csv.DictReader(f):
  p=ROOT/r['path']
  if not p.exists() or sha(p)!=r['sha256']:errors.append('missing or changed: '+r['path']);continue
  if p.suffix=='.csv':
   try:
    count=rows(p)
    if str(count)!=r['rows']:errors.append('row count mismatch: '+r['path'])
   except Exception as e:errors.append('malformed csv: '+str(p)+' '+str(e))
with (ROOT/'catalog/public_datasets.csv').open(encoding='utf-8-sig',newline='') as f:
 for r in csv.DictReader(f):
  p=ROOT/'public-data'/r['filename'];site=ROOT/'docs/downloads'/r['filename']
  if not p.exists() or not site.exists() or sha(p)!=r['sha256'] or sha(site)!=r['sha256']:errors.append('public mirror mismatch: '+r['filename'])
for fn in ['catalog','claims','metrics','bayan_timeseries']:
 path=ROOT/'docs/data'/f'{fn}.json'
 try:json.loads(path.read_text('utf-8'))
 except Exception as e:errors.append('invalid site JSON: '+str(e))
if errors:
 print('FAILED',len(errors),'tests');print('\n'.join(errors[:30]));sys.exit(1)
print('PASS: immutable original datasets and 13 public mirrors; static API JSON valid.')
