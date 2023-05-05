import random
import time
from nextcord import Interaction
from nextcord.ext import commands
import nextcord
typel = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
base = ''
used = []
cancel = False
codegenrunning = False

client = commands.Bot(command_prefix="<>", intents=nextcord.Intents.all())

class cancelbutton(nextcord.ui.View):
    @nextcord.ui.button(label='Cancel', style=nextcord.ButtonStyle.danger)
    async def cancel(self, ctx : Interaction, button : nextcord.ui.button):
        global cancel
        cancel = True

@client.slash_command(description='test')
async def runcodegen(ctx : Interaction, aos : int, aocis : int):
    global base
    global used
    global cancel
    global codegenrunning
    if codegenrunning is True:
        me = await ctx.response.send_message('CodeGen Already Running')
        time.sleep(0.5)
        await me.delete()
        return
    codegenrunning = True
    
    
    
    button = cancelbutton()
    
    AOS = aos
    AOCIS = aocis
    
    AOSM = AOS * AOCIS

    start_time = time.time()
    me = await ctx.response.send_message('Starting....', view=button)
    while True:
        for i in range(0, AOS):
            for ie in range(0, AOCIS):
                addonindex = random.randint(0, len(typel) - 1)
                addon = typel[addonindex]
                base = base + addon
            if i != AOS - 1:
                base = base + '-'    
        result = base                  
        if result in used:
            await me.edit(f'Dupe!  result is {result} The {used.index(result)} which was generated')
            time.sleep(0.4)
        if result not in used:
            used.append(result)
            await me.edit(f'Added: {result}   Index: {used.index(result)}')
        if len(used) == len(typel)**AOSM:
            end_time = time.time()
            timeforprocess = end_time - start_time
            await me.edit(f'Done {timeforprocess}S')
            break
        if cancel is True:
            cancel = False
            result = ''
            await me.edit('Canceled. deleting...')
            time.sleep(1.5)
            await me.delete()
            AOS = 0
            AOCIS = 0
            used = []
            codegenrunning = False
            break
        
   
        base = ''
        time.sleep(0.3)
    AOS = 0
    AOCIS = 0
    used = []
    codegenrunning = False

client.run('BOT TOKEN')
