"""Refresh a bounded public tree snapshot; no repository writes or code execution."""
import json, os, urllib.request
from pathlib import Path
BASE='https://api.github.com/repos/rishi9504/Leetcode'
def fetch(path):
    headers={'Accept':'application/vnd.github+json','User-Agent':'recall-catalog'}
    token=os.environ.get('GITHUB_TOKEN')
    if token: headers['Authorization']='Bearer '+token
    with urllib.request.urlopen(urllib.request.Request(BASE+path,headers=headers),timeout=30) as response:
        return json.load(response)
repo=fetch('')
branch=fetch('/branches/'+repo['default_branch'])
commit=branch['commit']['sha']
data=fetch('/git/trees/'+commit+'?recursive=1')
if data.get('truncated'): raise SystemExit('Incomplete GitHub tree. Existing snapshot preserved. Use bounded subtree fetching before importing this source.')
snapshot={'sha':commit,'truncated':False,'tree':[{'path':x['path'],'type':x['type'],'sha':x['sha']} for x in data['tree']]}
path=Path(__file__).with_name('leetcode-tree.json');temporary=path.with_suffix('.tmp')
temporary.write_text(json.dumps(snapshot)+'\n');temporary.replace(path)
print('Leetcode snapshot refreshed at commit '+commit[:8]+'. Run npm run catalog next.')
