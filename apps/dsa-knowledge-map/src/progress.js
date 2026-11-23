export const KEY='recall-progress-v1';
export const STATES=['unrated','relearn','revise','confident'];
export const LABELS={unrated:'Not assessed',relearn:'Relearn',revise:'Revise',confident:'Can derive'};
export function validateProgress(data){
 if(!data||data.schemaVersion!==1||!data.records||typeof data.records!=='object'||Array.isArray(data.records))throw Error('This is not a Recall v1 backup.');
 const clean={};
 for(const [id,r] of Object.entries(data.records)){
  if(!/^[a-z0-9-]{1,100}$/.test(id)||!r||!STATES.includes(r.status)||typeof r.note!=='string'||r.note.length>20000||!Array.isArray(r.reviews)||r.reviews.length>10000)throw Error('Backup contains an invalid record.');
  for(const a of r.reviews)if(!a||!['again','hard','good','easy'].includes(a.rating)||typeof a.at!=='string'||!Number.isFinite(Date.parse(a.at))||!/^\d{4}-\d{2}-\d{2}$/.test(a.due))throw Error('Backup contains an invalid review.');
  clean[id]={status:r.status,note:r.note,reviews:r.reviews.map(a=>({rating:a.rating,at:a.at,due:a.due}))};
 }
 return clean;
}
export function dayKey(date=new Date()) {return `${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`;}
export function schedule(rating,date=new Date()) {if(!['again','hard','good','easy'].includes(rating))throw Error('Unknown rating');const next=new Date(date);next.setDate(next.getDate()+({again:1,hard:3,good:7,easy:14}[rating]));return dayKey(next);}
export function isDue(r,date=new Date()){return !r?.reviews?.length||r.reviews.at(-1).due<=dayKey(date);}
export function mergeProgress(old,incoming){const next={...old};for(const [id,r] of Object.entries(incoming)){const prior=old[id];const reviews=[...new Map([...(prior?.reviews||[]),...r.reviews].map(a=>[a.at+'|'+a.rating,a])).values()].sort((a,b)=>Date.parse(a.at)-Date.parse(b.at));next[id]={...r,reviews};}return next;}
