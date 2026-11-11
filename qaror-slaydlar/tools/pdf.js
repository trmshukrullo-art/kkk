const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async()=>{
  const [html,out]=process.argv.slice(2);
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.route(/fonts\.googleapis\.com/, r=>r.abort());
  await p.goto('file://'+html+'#export',{waitUntil:'networkidle'});
  for(const w of [300,400,500,600,700,800]) await p.addStyleTag({url:'https://cdn.jsdelivr.net/npm/@fontsource/montserrat@5.0.18/'+w+'.css'});
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(800);
  await p.addStyleTag({content:'@page{size:1920px 1080px;margin:0} html,body{background:#fff!important} .stage{width:1920px!important;height:1080px!important;overflow:hidden;break-after:page} .stage:last-of-type{break-after:auto} .slide{transform:scale('+(1920/1526)+')!important}'});
  await p.pdf({path:out,width:'1920px',height:'1080px',printBackground:true,margin:{top:0,right:0,bottom:0,left:0}});
  await b.close();
})();
