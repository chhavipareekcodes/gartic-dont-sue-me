import discord 
import random
import os 



drawings={

    "buriburi" : "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/2-shinchan-mohi-gautam.jpg"

}


globalAnswer=None


client=discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"bot logged in as {client.user}")


@client.event
async def on_message(message):

    global globalAnswer

    if message.author==client.user:
        return

    if message.content.startswith("-gartic"):
        await message.channel.send(content="welcome to gartic!")
        await message.channel.send(content="-start to begin the game")     

    if message.content.startswith("-start"):
        await message.channel.send(content="make a guess using '='")
        answer,drawing=random.choice(list(drawings.items()))
        globalAnswer=answer
        await message.channel.send(drawing)
    
    if message.content.startswith("="):
        if globalAnswer==message.content[1:]:
            await message.channel.send(f"{message.author.mention} guessed it!")
             

    if message.content.startswith("-end"):
        return 


TOKEN=os.environ.get('authToken')
client.run(TOKEN)
