// Deterministic educational traces. Never execute imported Python or user code.
export const MODES = {'lc-144':'preorder','lc-94':'inorder','lc-145':'postorder','lc-102':'level','lc-103':'zigzag','lc-199':'right','lc-104':'depth','lc-543':'diameter','lc-124':'gain','lc-110':'balanced'};
export const DEFAULTS = {gain:[-10,9,20,null,null,15,7],diameter:[1,2,3,4,5],balanced:[1,2,2,3,3,null,null,4,4]};
export const DEFAULT_TREE = [1,2,3,4,5,null,7];
export function parseTree(input) {
  const a = typeof input === 'string' ? JSON.parse(input) : input;
  if (!Array.isArray(a) || a.length > 63 || a.some(x => x !== null && (!Number.isSafeInteger(x) || Math.abs(x) > 1000000))) throw Error('Use a JSON array of at most 63 integers (−1,000,000 to 1,000,000) or null.');
  if (!a.length || a[0] === null) {
    if (a.slice(1).some(x => x !== null)) throw Error('An empty root cannot have children.');
    return {root:null,nodes:[],edges:[]};
  }
  let id = 0;
  const root = {id:String(id++),value:a[0],left:null,right:null,depth:0};
  const queue=[root], nodes=[root], edges=[];
  let i=1;
  while (queue.length && i<a.length) {
    const n=queue.shift();
    for (const side of ['left','right']) {
      if (i>=a.length) break;
      const v=a[i++];
      if(v!==null) {const child={id:String(id++),value:v,left:null,right:null,depth:n.depth+1};n[side]=child;nodes.push(child);queue.push(child);edges.push([n.id,child.id]);}
    }
  }
  if(a.slice(i).some(x=>x!==null)) throw Error('Some nodes have no parent. Use level-order input with null for missing children.');
  let col=0;
  const position=n=>{if(!n)return;position(n.left);n.x=++col;position(n.right);};position(root);
  return {root,nodes,edges};
}
export function makeTrace(mode, input) {
  const tree=parseTree(input), frames=[], visited=[], stack=[], returned={}, output=[];
  let best=mode==='gain'?-Infinity:0;
  const emit=(line,message,active=null,extra={})=>frames.push({line,message,active,visited:[...visited],stack:[...stack],returned:{...returned},output:structuredClone(output),best: Number.isFinite(best)?best:null,...extra});
  emit(0,'Ready. Follow what each node receives, computes, and returns.');
  if(['level','zigzag','right'].includes(mode)){
    const q=tree.root?[tree.root]:[];let depth=0;
    emit(1,'Start with the root in the queue.',null,{queue:q.map(n=>n.id)});
    while(q.length){const size=q.length,level=[];emit(3,`Level ${depth}: freeze the queue size at ${size}.`,null,{queue:q.map(n=>n.id)});
      for(let i=0;i<size;i++) {const n=q.shift();stack.splice(0);visited.push(n.id);level.push(n.value);emit(5,`Remove ${n.value} from the front.`,n.id,{queue:q.map(n=>n.id),level:[...level]});
        if(n.left)q.push(n.left);if(n.right)q.push(n.right);emit(8,'Append existing children, left before right.',n.id,{queue:q.map(n=>n.id),level:[...level]});}
      if(mode==='right')output.push(level[level.length-1]);else output.push(mode==='zigzag'&&depth%2?[...level].reverse():level);
      emit(9,mode==='zigzag'&&depth%2?'Reverse this level’s values; keep the queue order unchanged.':mode==='right'?'Keep the last value in the level.':'Commit this level to the answer.',null,{queue:q.map(n=>n.id)});depth++;
    }
    emit(10,'Queue empty. All levels are complete.',null,{queue:[],result:structuredClone(output)});
  }else if(['preorder','inorder','postorder'].includes(mode)){
    const visit=n=>{if(!n){emit(2,'None returns immediately.');return;}
      stack.push(n.id);emit(1,`Enter node ${n.value}.`,n.id);
      const take=line=>{visited.push(n.id);output.push(n.value);emit(line,`Append ${n.value} to the traversal.`,n.id);};
      if(mode==='preorder')take(3);visit(n.left);if(mode==='inorder')take(4);visit(n.right);if(mode==='postorder')take(5);
      stack.pop();returned[n.id]='done';emit(6,`Return from ${n.value}.`,n.id);
    };visit(tree.root);emit(7,'Traversal complete.',null,{result:[...output]});
  }else{
    const solve=n=>{if(!n){emit(2,'Empty subtree returns 0.');return 0;}stack.push(n.id);emit(1,`Enter ${n.value}; first collect both child answers.`,n.id);
      const rawL=solve(n.left);emit(3,`Left child returns ${rawL}.`,n.id);
      const rawR=solve(n.right);emit(4,`Right child returns ${rawR}.`,n.id);
      let value;
      if(mode==='gain'){const l=Math.max(rawL,0),r=Math.max(rawR,0),candidate=n.value+l+r;best=Math.max(best,candidate);value=n.value+Math.max(l,r);emit(5,`Clamp gains to ${l} and ${r}. Through-node candidate = ${n.value} + ${l} + ${r} = ${candidate}. Best = ${best}.`,n.id,{left:l,right:r,candidate});}
      else if(mode==='diameter'){best=Math.max(best,rawL+rawR);value=1+Math.max(rawL,rawR);emit(5,`Through-node path = ${rawL} + ${rawR} = ${rawL+rawR} edges. Best = ${best}.`,n.id,{left:rawL,right:rawR,candidate:rawL+rawR});}
      else if(mode==='balanced'){value=rawL===-1||rawR===-1||Math.abs(rawL-rawR)>1?-1:1+Math.max(rawL,rawR);emit(5,value===-1?'Unbalanced subtree: propagate −1, not a height.':`Heights ${rawL} and ${rawR} differ by at most 1.`,n.id,{left:rawL,right:rawR});}
      else {value=1+Math.max(rawL,rawR);emit(5,`Height = 1 + max(${rawL}, ${rawR}) = ${value}.`,n.id,{left:rawL,right:rawR});}
      visited.push(n.id);returned[n.id]=value;stack.pop();emit(6,`Return ${value} to the parent${mode==='gain'?'; only one branch can extend upward':''}.`,n.id);return value;
    };
    const value=solve(tree.root);const result=mode==='gain'?(tree.root?best:null):mode==='diameter'?best:mode==='balanced'?value!==-1:value;
    emit(7,tree.root?'Finished. Every child answer has reached its parent.':'Empty tree: no nodes to visit.',null,{result});
  }
  return {tree,frames};
}
export function traceCode(mode){
 if(['preorder','inorder','postorder'].includes(mode))return ['answer = []','def dfs(node):','    if node is None: return','    '+(mode==='preorder'?'answer.append(node.val)':'dfs(node.left)'), '    '+(mode==='preorder'?'dfs(node.left)':mode==='inorder'?'answer.append(node.val)':'dfs(node.right)'), '    '+(mode==='postorder'?'answer.append(node.val)':'dfs(node.right)'), '    return','dfs(root)'];
 if(['level','zigzag','right'].includes(mode))return ['answer = []','queue = deque([root]) if root else deque()','while queue:','    size, level = len(queue), []','    for _ in range(size):','        node = queue.popleft()','        level.append(node.val)','        if node.left: queue.append(node.left)','        if node.right: queue.append(node.right)',mode==='right'?'    answer.append(level[-1])':mode==='zigzag'?'    answer.append(level if len(answer)%2 == 0 else level[::-1])':'    answer.append(level)','# answer now contains all levels'];
 return [mode==='gain'?'best = [float("-inf")]':mode==='diameter'?'best = [0]':'# Empty subtree has height 0','def dfs(node):','    if node is None: return 0',mode==='gain'?'    left = max(0, dfs(node.left))':'    left = dfs(node.left)',mode==='gain'?'    right = max(0, dfs(node.right))':'    right = dfs(node.right)',mode==='gain'?'    best[0] = max(best[0], node.val + left + right)':mode==='diameter'?'    best[0] = max(best[0], left + right)':mode==='balanced'?'    if min(left, right) == -1 or abs(left-right) > 1: return -1':'    height = 1 + max(left, right)',mode==='gain'?'    return node.val + max(left, right)':'    return 1 + max(left, right)',mode==='gain'||mode==='diameter'?'dfs(root); answer = best[0]':mode==='balanced'?'answer = dfs(root) != -1':'answer = dfs(root)'];
}
