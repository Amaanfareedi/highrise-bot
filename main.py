import os, threading, http.server, socketserver
def run_dummy():
    port = int(os.environ.get("PORT", 10000))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()
threading.Thread(target=run_dummy, daemon=True).start()

from highrise import BaseBot
import asyncio

EMOTE_LIST = [
"kiss","laugh","sit","fairytwirl","fairyfloat","launch","cutesalute","atattention","tiktok","smooch",
"pushit","foryou","touch","kawaii","repose","sleigh","hyped","jingle","gottago","timejump",
"scritchy","bitnervous","iceskating","partytime","arabesque","bashful","revelations","watchyourback","creepypuppet","saunter",
"surprise","celebrate","penguin","boxer","airguitar","stargaze","ditzy","uwu","fashion","icecream",
"sayso","zombierun","astronaut","punk","zerogravity","beautiful","casual","wink","fightme","icon",
"flirtywave","greedy","viralgroove","weird","shuffle","gagging","raise","savage","blackpink","model",
"dontstartnow","pennywise","bow","russian","curtsy","snowball","snowangel","charging","letsgoshopping","confused",
"enthused","telekinesis","float","teleporting","swordfight","maniac","energyball","worm","singalong","frog",
"lambi","macarena","shakehead","nod","hello","runhop","donttouch","outfit","thumbsup","passionatesmooch",
"pose12","miningfail","shy","runforward","fishingpull","idlespace","thewave","tiktok5","fading","dinner",
"winkpose","opera","hiphopdance","angry","tiktok15","tiktok6","breakscreen","juggling","thief","sheephop",
"walkforward","shocked","flirt","gooey","outfit2","fireworks","musclepose","rough","fishingidle","tk7",
"dropped","miningsuccess","oops","wavey","anime","receivehappy","cold","twitched","fishingcast","surf",
"shush","handwalk","kid","pokedance","pose11","sitchair","tiktok16","shuffledance","tiktok3","headless",
"tiktok1","cartwheel","tired","electrified","dramatic","hopscotch","purr","armcannon","zombie","cutee",
"hot","pose8","miningmine","fishingpullsmall","tiktok7","cold2","ghostfloat","relaxed","attentive","posh",
"shrink","sleepy","pouty","tired2","taploop","shy2","bummed","chillin","annoyed","aerobics","ponder",
"heropose","relaxing","cozynap","feelbeat","irritated","ibelieve","think","theatrical","tapdance","superrun",
"superpunch","sumo","thumbsuck","splits","secretshake","ropepull","roll","rofl","robotdance","rainbow",
"propose","peekaboo","peace","panic","ninjarun","nightfever","monsterfail","levelup","amused","superkick",
"jump","judochop","jetpackfly","hugyourself","harlemshake","happyy","handstand","moonwalk","gangnam","faint",
"clumsy","fall","exasperated","elbowsbump","disco","blastoff","faintdrop","collapse","revival","dab",
"bunnyhop","boo","homerun","apart","point","sneeze","smirk","sick","gasp","punch","pray","stinky",
"naughty","mindblown","lying","levitate","firelunge","giveup","stunned","clap","arrogance","voguehands",
"smoothwalk","ringonit","orangejuice","rockout","handsinair","duckwalk","pushups","salutee","ghost","heartshape",
"hug","eyeroll","embarrassed","sexydance","puppet","fightidle","frustrated","stargazing","slap","facepalm",
"hearteyes","heartfingers","trampoline","howl1","howl2","laidback","hipshake","celebrating","celebrateidle","swingnet3",
"swingsneak","swingnet2","swingnet1","riflethrow","coolguy","disappointed","laid2","fruity","warrior3","warrior2",
"treepose","sugarstun","novabop","blossomreach","sakurastep","petalperch","runningman","yogasurprise","midnightpoise","midnightstrut",
"midnightallure","springsun","bloomflutter","bloomcharm","bloomradiance","foldarmfly","divamoment","float2","rainstruck1","rainstruck2",
"chaoscutie","sweettease","sweetstrike","sweetfix","sweetlure","justvibing","cheer","magnetic","hotcocoa","silentjudging",
"comehere","backoff","spokkyswagger","yoinked","daydreaming","spiderman","rest","floss","sweetheartpose","celebration",
"curiouser","reachforthestars","twerk","graceful","woah","laidback2","lust","mine","martialart","knocking",
"popularvibe","frolicking","flex","swagbounce","cursing","headball","griddy","spiritual","blowkisses","hero",
"trueheart","robotic","swinging","freshprince","ballet","breakdance","tk4","idletk6","selfietime","yapping",
"doomscroll","resttext","infinitescroll","wait","crouched","hccjet","crowdjammer","sweetjammer","uhmmm","zenmode",
"hrstar","paparazzi","afk","moodswing","adoringfans","sixseven","nosixseven","scubadance","modelwalk","fitcheck",
"sob","flexinghard","spilltea"
]

EMOTE_BY_NUM = {str(i+1): name for i, name in enumerate(EMOTE_LIST)}
def get_emote_id(name):
    name=name.lower()
    return [name,f"emote-{name}",f"dance-{name}",f"idle-{name}",f"emote-looping-{name}"]

class MyBot(BaseBot):
    def __init__(self):
        super().__init__()
        self.loops={}
        self.loop_all_task=None
    async def on_start(self, session_metadata):
        print(f"BOT ONLINE! {len(EMOTE_LIST)} emotes")
        await self.highrise.chat(f"Bot Online! {len(EMOTE_LIST)} emotes!")
    async def send_emote_try(self, emote_name, target_id):
        for eid in get_emote_id(emote_name):
            try:
                await self.highrise.send_emote(eid, target_id)
                return True
            except: continue
        return False
    async def loop_emote(self, emote_name, target_id):
        while True:
            await self.send_emote_try(emote_name, target_id)
            await asyncio.sleep(4.5)
    async def on_chat(self, user, message: str):
        msg=message.lower().strip()
        if not msg: return
        parts=msg.split()
        cmd=parts[0]
        if msg=="stop":
            if user.id in self.loops:
                self.loops[user.id].cancel()
                del self.loops[user.id]
                await self.highrise.chat(f"@{user.username} stopped")
            return
        if msg=="stoploopall":
            if self.loop_all_task:
                self.loop_all_task.cancel()
                self.loop_all_task=None
            for t in list(self.loops.values()): t.cancel()
            self.loops.clear()
            await self.highrise.chat("All loops stopped")
            return
        emote_name=None
        if cmd in EMOTE_BY_NUM: emote_name=EMOTE_BY_NUM[cmd]
        elif cmd in EMOTE_LIST: emote_name=cmd
        elif len(parts)>=2 and (parts[0] in EMOTE_LIST or parts[0] in EMOTE_BY_NUM):
             if "@" in msg or parts[1]=="all":
                 emote_name=EMOTE_BY_NUM.get(parts[0],parts[0])
        if "@" in msg and emote_name:
            try:
                target_username=msg.split("@")[-1].split()[0]
                room_users=(await self.highrise.get_room_users()).content
                target=next((u for u,_ in room_users if u.username.lower()==target_username.lower()),None)
                if target:
                    if user.id in self.loops: self.loops[user.id].cancel()
                    task=asyncio.create_task(self.loop_emote(emote_name,target.id))
                    self.loops[user.id]=task
            except: pass
            return
        if msg.endswith(" all") and emote_name:
            try:
                room_users=(await self.highrise.get_room_users()).content
                for u,_ in room_users: await self.send_emote_try(emote_name,u.id)
            except: pass
            return
        if msg.startswith("loopall "):
            emote_part=msg.replace("loopall ","").strip()
            emote_name2=EMOTE_BY_NUM.get(emote_part,emote_part)
            async def loop_all():
                while True:
                    try:
                        room_users=(await self.highrise.get_room_users()).content
                        for u,_ in room_users: await self.send_emote_try(emote_name2,u.id)
                    except: pass
                    await asyncio.sleep(5)
            if self.loop_all_task: self.loop_all_task.cancel()
            self.loop_all_task=asyncio.create_task(loop_all())
            return
        if emote_name and len(parts)==1:
            if user.id in self.loops: self.loops[user.id].cancel()
            task=asyncio.create_task(self.loop_emote(emote_name,user.id))
            self.loops[user.id]=task
