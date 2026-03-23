import axios from 'axios';

const API = 'http://localhost:8000/api';

const app = document.getElementById('app')!;

async function refresh(){
  const res = await axios.get(`${API}/requests`);
  renderList(res.data || []);
}

function renderList(items:any[]){
  app.innerHTML = `
    <h1>AI Green Corridor - Demo</h1>
    <button id="new">New Request</button>
    <button id="seed">Seed Sample</button>
    <div id="list"></div>
  `;

  const list = document.getElementById('list')!;

  if(items.length===0)
    list.innerHTML = '<p>No requests</p>';
  else
    list.innerHTML = items.map(i=>`
      <div style="border:1px solid #ccc;padding:8px;margin:6px;">
        <b>ID:</b> ${i.id}
        | <b>Loc:</b> ${i.location}
        | <b>Status:</b> ${i.status}
        | <b>Green:</b> ${i.green_route? '✅':'❌'}
      </div>
    `).join('');

}

refresh();