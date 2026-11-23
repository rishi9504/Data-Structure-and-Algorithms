"""Build a read-only Trees snapshot from the host repo tracker and notes.
No inferred acceptance or personal confidence. External snapshot is optional.
"""
from pathlib import Path
import json, re, subprocess, datetime
APP=Path(__file__).resolve().parents[1]
REPO=APP.parents[1]
TREE=REPO/'Striver/BinaryTrees'
BASE='https://github.com/rishi9504/Data-Structure-and-Algorithms/blob/main/Striver/BinaryTrees/'
def slug(s):
    return re.sub(r'[^a-z0-9 -]', '', s.lower()).replace(' ', '-')
# Canonical LeetCode slugs, not directory numeric prefixes.
slugs={94:'binary-tree-inorder-traversal',100:'same-tree',101:'symmetric-tree',102:'binary-tree-level-order-traversal',103:'binary-tree-zigzag-level-order-traversal',104:'maximum-depth-of-binary-tree',105:'construct-binary-tree-from-preorder-and-inorder-traversal',106:'construct-binary-tree-from-inorder-and-postorder-traversal',110:'balanced-binary-tree',114:'flatten-binary-tree-to-linked-list',124:'binary-tree-maximum-path-sum',144:'binary-tree-preorder-traversal',145:'binary-tree-postorder-traversal',199:'binary-tree-right-side-view',222:'count-complete-tree-nodes',236:'lowest-common-ancestor-of-a-binary-tree',297:'serialize-and-deserialize-binary-tree',543:'diameter-of-binary-tree',662:'maximum-width-of-binary-tree',863:'all-nodes-distance-k-in-binary-tree',987:'vertical-order-traversal-of-a-binary-tree'}
easy={94,100,101,104,110,144,145,222,543}
hard={124,297,987}
problems=[]
for row in (TREE/'tracker.md').read_text().splitlines():
    if not row.startswith('| ') or '[solution]' not in row: continue
    topic,title,num,pattern,notes,solution,confidence,last=[x.strip() for x in row.strip('|').split('|')]
    solution_path=re.search(r'\((.*?)\)',solution)[1]
    note_path=re.search(r'\((.*?)\)',notes)[1]
    file,anchor=note_path.split('#')
    content=(TREE/file).read_text()
    sections=re.split(r'^## ',content,flags=re.M)[1:]
    selected=next((x for x in sections if slug(x.splitlines()[0])==anchor),None)
    if selected is None: raise ValueError('Missing note anchor '+note_path)
    lc=int(num) if num.isdigit() else None
    ident='lc-'+str(lc) if lc else slug(title)
    # Morris is a distinct technique, not another instance of LC94.
    code=(TREE/solution_path).read_text()
    problems.append(dict(id=ident,title=title,topic=topic,pattern=pattern,lc=lc,slug=slugs.get(lc),difficulty='Hard' if lc in hard else 'Easy' if lc in easy else 'Medium' if lc else 'Technique',notes='## '+selected.strip(),code=code,noteUrl=BASE+note_path,solutionUrl=BASE+solution_path,trackerConfidence=confidence,leetcodeUrl='https://leetcode.com/problems/'+slugs[lc]+'/' if lc else None,artifacts=[]))
assert len({p['id'] for p in problems})==len(problems)
external_path=APP/'scripts/leetcode-tree.json'
external=json.loads(external_path.read_text()) if external_path.exists() else None
if external:
    assert not external.get('truncated'), 'Incomplete external snapshot'
    for p in problems:
        if not p['slug']: continue
        for entry in external['tree']:
            path=entry['path']
            folder=path.split('/')[0]
            if entry['type']=='blob' and re.sub(r'^\d+-','',folder)==p['slug'] and path.endswith(('.py','.cpp','.java','.js','.ts')):
                p['artifacts'].append({'path':path,'url':'https://github.com/rishi9504/Leetcode/blob/'+external['sha']+'/'+path,'sha':entry['sha']})
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
out={'schemaVersion':1,'generatedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'learningCommit':commit,'leetcodeCommit':external['sha'] if external else None,'problems':problems}
(APP/'src/data/catalog.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(f'Catalog: {len(problems)} questions; {sum(bool(p["artifacts"]) for p in problems)} matched external solution folders. Acceptance not inferred.')
