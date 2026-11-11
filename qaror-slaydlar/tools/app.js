(function(){
  var W=1526,H=860;
  var deckEl=document.getElementById('deck');
  var DECK=JSON.parse(deckEl.textContent);
  var root=document.getElementById('slides');
  var bar=document.getElementById('bar');
  var bEdit=document.getElementById('bEdit'),bSave=document.getElementById('bSave'),bCancel=document.getElementById('bCancel'),status=document.getElementById('status');
  var edits={};var editing=false;var art=null;var cmt=null;var readOnly=false;

  if(location.hash==='#export')document.body.classList.add('export');

  function blocks(rootEl){
    var out=[];
    (function walk(el){
      var t=el.tagName.toLowerCase();
      if(t==='i'||t==='svg')return;
      for(var i=0;i<el.childNodes.length;i++){var n=el.childNodes[i];if(n.nodeType===3&&/\S/.test(n.textContent)){out.push(el);return;}}
      for(var j=0;j<el.children.length;j++)walk(el.children[j]);
    })(rootEl);
    return out;
  }
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  function clean(el){
    var out='';
    el.childNodes.forEach(function(n){
      if(n.nodeType===3){out+=esc(n.textContent);return;}
      if(n.nodeType!==1)return;
      var t=n.tagName.toLowerCase();
      if(t==='br'){out+='<br>';return;}
      var inner=clean(n);
      if(t==='b'||t==='strong'||t==='span'){
        var tag=t==='strong'?'b':t;var st=n.getAttribute('style');
        out+='<'+tag+(st?' style="'+st.replace(/"/g,'&quot;')+'"':'')+'>'+inner+'</'+tag+'>';
      }else if(t==='div'||t==='p'){out+=(out?'<br>':'')+inner;}
      else out+=inner;
    });
    return out;
  }
  function textOf(html){return html.replace(/<br>/g,' ').replace(/<[^>]+>/g,'').replace(/&nbsp;/g,' ');}

  function src(id){return document.getElementById(id).textContent.replace(/<\\\//g,'</');}
  function caption(slide){var h=slide.querySelector('.sh h2'),p=slide.querySelector('.sh .pg');return (p?p.textContent+' · ':'')+(h?h.textContent:'');}

  function render(){
    root.textContent='';
    DECK.slides.forEach(function(s){
      var sec=document.createElement('section');sec.className='sw';
      var cap=document.createElement('div');cap.className='cap';
      var lab=document.createElement('span');cap.appendChild(lab);
      var cb=document.createElement('button');cb.type='button';cb.className='tb sm cbtn';cb.textContent='Изоҳ қолдириш';cb.hidden=!cmt;
      cap.appendChild(cb);
      var stage=document.createElement('div');stage.className='stage';
      stage.innerHTML=s.html;
      var slide=stage.firstElementChild;
      lab.textContent=caption(slide);
      cb.addEventListener('click',function(){if(!cmt)return;cmt.openComposer({element:slide}).catch(function(e){if(e&&e.code==='unavailable'){cmt=null;document.querySelectorAll('.cbtn').forEach(function(b){b.hidden=true;});}});});
      blocks(slide).forEach(function(el,i){
        var key=s.id+':'+i;el.setAttribute('data-k',key);
        if(edits[key]!=null)el.innerHTML=edits[key];
      });
      sec.appendChild(cap);sec.appendChild(stage);root.appendChild(sec);
    });
    setEditable(editing);fit();
  }
  function setEditable(on){
    root.querySelectorAll('[data-k]').forEach(function(el){if(on)el.setAttribute('contenteditable','true');else el.removeAttribute('contenteditable');});
  }
  function fit(){
    root.querySelectorAll('.stage').forEach(function(st){
      var sl=st.firstElementChild;var s=document.body.classList.contains('export')?1:st.clientWidth/W;
      sl.style.transform='scale('+s+')';st.style.height=(H*s)+'px';
    });
  }
  function count(){return Object.keys(edits).length;}
  function refresh(){
    var n=count();
    bEdit.textContent=editing?'Таҳрирни якунлаш':'Таҳрирлаш';
    bEdit.setAttribute('aria-pressed',String(editing));
    bSave.disabled=!n||readOnly;bCancel.hidden=!n;
    document.body.classList.toggle('editing',editing);
    if(readOnly)status.textContent='Фақат кўриш режими — сақлаш ҳуқуқи йўқ';
    else if(n)status.textContent=n+' та ўзгариш сақланмаган';
    else status.textContent=editing?'Матнни босиб ўзгартиринг':'';
  }

  root.addEventListener('input',function(e){
    var el=e.target.closest&&e.target.closest('[data-k]');if(!el)return;
    var h=clean(el);if(!/\S/.test(textOf(h)))h='​';
    edits[el.getAttribute('data-k')]=h;refresh();
  });
  root.addEventListener('keydown',function(e){
    if(!editing)return;
    if(e.key==='Enter'){e.preventDefault();document.execCommand('insertLineBreak');}
    if(e.key==='Escape'&&document.activeElement)document.activeElement.blur();
  });
  root.addEventListener('paste',function(e){
    if(!editing)return;e.preventDefault();
    var t=(e.clipboardData||window.clipboardData).getData('text/plain');document.execCommand('insertText',false,t);
  });
  bEdit.addEventListener('click',function(){editing=!editing;setEditable(editing);refresh();});
  bCancel.addEventListener('click',function(){edits={};render();refresh();});

  function buildDoc(){
    var slides=DECK.slides.map(function(s){
      var d=new DOMParser().parseFromString('<!doctype html><body>'+s.html+'</body>','text/html');
      var sl=d.body.firstElementChild;
      blocks(sl).forEach(function(el,i){var k=s.id+':'+i;if(edits[k]!=null)el.innerHTML=edits[k];});
      return {id:s.id,html:sl.outerHTML};
    });
    var json=JSON.stringify({slides:slides}).replace(/<\//g,'<\\/');
    var head='<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>'+document.getElementById('reset').textContent+'</style></head><body>';
    return head+src('pagehead')
      +'<style id="st">'+document.getElementById('st').textContent+'</style>'
      +src('shell')
      +'<script type="application/json" id="deck">'+json+'<\/script>'
      +'<script type="text/plain" id="reset">'+document.getElementById('reset').textContent+'<\/script>'
      +'<script type="text/plain" id="pagehead">'+src('pagehead').replace(/<\//g,'<\\/')+'<\/script>'
      +'<script type="text/plain" id="shell">'+src('shell').replace(/<\//g,'<\\/')+'<\/script>'
      +'<script id="app">'+document.getElementById('app').textContent+'<\/script></body></html>';
  }
  bSave.addEventListener('click',function(){
    if(!art||!count())return;
    bSave.disabled=true;status.textContent='Сақланмоқда…';
    art.publish(buildDoc()).then(function(){status.textContent='Сақланди';}).catch(function(e){
      var c=e&&e.code;
      if(c==='conflict'){status.textContent='Бошқа версия сақланган — саҳифа янгиланади';return;}
      if(c==='not_writer'||c==='not_granted'||c==='consent_required'||c==='capability_disabled'||c==='not_declared'){readOnly=true;refresh();return;}
      status.textContent='Сақлаб бўлмади ('+(c||'хато')+'). Қайта уриниб кўринг.';bSave.disabled=false;
    });
  });

  render();refresh();
  window.addEventListener('resize',fit);
  if(window.ResizeObserver)new ResizeObserver(fit).observe(root);
  if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);

  if(window.claude&&window.claude.use){
    window.claude.use('artifact').then(function(a){art=a;if(!a){bSave.hidden=true;bEdit.hidden=true;}}).catch(function(){});
    window.claude.use('comments').then(function(c){cmt=c;document.querySelectorAll('.cbtn').forEach(function(b){b.hidden=!c;});}).catch(function(){});
  }else{bSave.hidden=true;}
})();
