const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');
(async()=>{
 const b=await chromium.launch({headless:true,channel:'msedge'}),p=await b.newPage({viewport:{width:1280,height:900}});
 await p.clock.install();await p.goto(process.env.PLAYTEST_URL || require('node:url').pathToFileURL(require('node:path').resolve('index.html')).href);await p.waitForFunction(()=>window.climb?.snapshot().assetsReady);await p.clock.runFor(200);
 // Pixel position selected by inspecting the START cue in the rendered screenshot,
 // without querying hold coordinates or the game's screen transform.
 await p.mouse.move(200,550);await p.mouse.down();await p.mouse.move(488,390);await p.mouse.up();
 assert.match(await p.locator('#toast').innerText(),/Left grip set/);await p.clock.runFor(1000);
 await p.mouse.move(100,500);await p.mouse.down({button:'right'});await p.clock.runFor(900);
 await p.screenshot({path:'tests/discovery-next.png'});
 await p.mouse.move(588,356);await p.mouse.up({button:'right'});assert.match(await p.locator('#toast').innerText(),/Right grip set/);console.log('SCREENSHOT-SELECTED FIRST TWO GRIPS PASS');await b.close();
})().catch(e=>{console.error(e);process.exit(1)});

