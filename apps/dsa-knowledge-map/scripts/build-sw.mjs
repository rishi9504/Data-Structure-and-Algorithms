import {readdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const files=[];async function walk(dir){for(const x of await readdir(dir,{withFileTypes:true})){if(x.isDirectory())await walk(`${dir}/${x.name}`);else if(x.name!=='sw.js')files.push(`${dir}/${x.name}`);}}await walk('dist');
const revision=createHash('sha256');for(const f of files.sort())revision.update(await readFile(f));
const cache='recall-'+revision.digest('hex').slice(0,16),assets=files.map(f=>'/'+f.slice(5));
await writeFile('dist/sw.js',`const CACHE=${JSON.stringify(cache)};const ASSETS=${JSON.stringify(assets)};self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(ASSETS)));});self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('recall-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});self.addEventListener('fetch',event=>{if(event.request.method!=='GET'||new URL(event.request.url).origin!==self.location.origin)return;if(event.request.mode==='navigate'){event.respondWith(fetch(event.request).catch(()=>caches.match('/index.html')));return;}event.respondWith(caches.match(event.request).then(hit=>hit||fetch(event.request)));});`);
console.log(`Offline cache: ${assets.length} local assets, ${cache}`);
