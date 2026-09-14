const { chromium }=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert=require('node:assert/strict');
(async()=>{
const browser=await chromium.launch({headless:true,channel:'msedge'});
const page=await browser.newPage({viewport:{width:1280,height:900}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.clock.install();await page.goto(process.env.PLAYTEST_URL || require('node:url').pathToFileURL(require('node:path').resolve(__dirname,'../index.html')).href);await page.clock.runFor(200);
const snap=()=>page.evaluate(()=>climb.snapshot());
const wait=ms=>page.clock.runFor(ms);
async function aim(id){const p=await page.evaluate(id=>climb.screen(id),id);await page.mouse.move(p.x,p.y);}
async function key(k){await page.keyboard.press(k);await wait(20);}
async function pull(ms=1350){await page.keyboard.down('w');await wait(ms);await page.keyboard.up('w');await wait(120);}
async function transfer(id,hand,old){await aim(id);await key(hand);let s=await snap();assert.equal(s.hands[hand==='q'?0:1]?.id,id,`grab ${id}: ${JSON.stringify(s.player)}`);if(old)await key(old);await pull();}
await aim(1);await key('q');assert.equal((await snap()).hands[0],null);assert.match(await page.locator('#toast').innerText(),/OUT OF REACH/);
await transfer(0,'q');assert.equal((await snap()).hands[1],null);
await transfer(1,'e','q');assert.equal((await snap()).hands[0],null);
// Two grips can coexist, release only one.
await aim(0);await key('q');assert.ok((await snap()).hands.every(Boolean));await pull(1800);let braced=await snap();for(const grip of braced.hands){let anchor=braced.holds[grip.id];assert.ok(Math.hypot(braced.player.x-anchor.x,braced.player.y-anchor.y)<=grip.length+1,'two-hand pull respects both arm constraints');}await key('q');await pull();
let held='e';
for(let id=2;id<15;id++){const next=held==='q'?'e':'q';await transfer(id,next,held);held=next;}
await key(held);await wait(2000);let success=await snap();assert.equal(success.won,true,'full ascent must settle on upper deck');console.log('ASCENT',JSON.stringify(success));
await page.screenshot({path:'tests/summit.png'});
await key('r');await wait(100);assert.equal((await snap()).won,false);held='q';await transfer(0,held);for(let id=1;id<=4;id++){let next=held==='q'?'e':'q';await transfer(id,next,held);held=next;}
const before=await snap();await key(held);await wait(450);const falling=await snap();assert.ok(falling.player.y>before.player.y+10);assert.ok(falling.player.vy>100);await aim(3);await key('q');assert.ok((await snap()).hands[0],'recatch lower hold during real fall');await pull();held='q';for(let id=4;id<15;id++){const next=held==='q'?'e':'q';await transfer(id,next,held);held=next;}await key(held);await wait(2000);assert.equal((await snap()).won,true,'recovery then summit');console.log('RECOVERY PASS');
await key('r');await wait(100);held=null;for(let id=0;id<=6;id++){const next=held==='q'?'e':'q';await transfer(id,next,held);held=next;}await key(held);await wait(1800);assert.equal((await snap()).player.y,897,'fall lands on rest deck');assert.ok((await snap()).player.ground);await aim(5);await key('q');await pull();await page.keyboard.down('d');let gap=false;for(let i=0;i<70;i++){await wait(20);let s=await snap(),h=s.holds[15];if(Math.hypot(s.player.x-h.x,s.player.y-h.y)<157){await aim(15);await key('e');gap=true;break;}}await page.keyboard.up('d');assert.ok(gap,'gap route reachable with lean');await key('q');await pull();await page.keyboard.down('a');let exit=false;for(let i=0;i<70;i++){await wait(20);let s=await snap(),h=s.holds[7];if(Math.hypot(s.player.x-h.x,s.player.y-h.y)<157){await aim(7);await key('q');await key('e');exit=true;break;}}await page.keyboard.up('a');assert.ok(exit,'gap route rejoins scaffold');await pull();await wait(2500);held='q';for(let id=8;id<15;id++){const next=held==='q'?'e':'q';await transfer(id,next,held);held=next;}await key(held);await wait(2000);assert.equal((await snap()).won,true,'rest recovery and gap route continue to summit');console.log('REST PLATFORM + GAP ROUTE + SUMMIT PASS');
await key('r');await wait(100);await aim(0);await page.mouse.click((await page.evaluate(()=>climb.screen(0))).x,(await page.evaluate(()=>climb.screen(0))).y);assert.ok((await snap()).hands[0]);await aim(0);await page.mouse.click((await page.evaluate(()=>climb.screen(0))).x,(await page.evaluate(()=>climb.screen(0))).y,{button:'right'});assert.ok((await snap()).hands[1]);await key('r');await transfer(0,'q');await page.keyboard.down('w');await key('p');const frozen=await snap();await wait(1200);assert.deepEqual((await snap()).player,frozen.player);await key('p');await page.keyboard.up('w');await wait(100);assert.equal((await snap()).paused,false);
await page.evaluate(()=>dispatchEvent(new Event('blur')));assert.equal((await snap()).paused,true);await page.locator('#resume').click();await key('r');
await page.setViewportSize({width:600,height:750});await wait(200);await page.screenshot({path:'tests/narrow.png'});await transfer(0,'q');assert.ok((await snap()).hands[0]);
await page.setViewportSize({width:1280,height:900});await key('r');await wait(200);await page.screenshot({path:'tests/start.png'});assert.deepEqual(errors,[]);console.log('PAUSE RESET RESIZE BROWSER ERRORS PASS');await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});


