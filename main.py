import discord 
import random


drawings={

    "buriburi" : "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/2-shinchan-mohi-gautam.jpg"

}




client=discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"bot logged in as {client.user}")


@client.event
async def on_message(message):

    if message.author==client.user:
        return

    if message.content.startswith("-gartic"):
        await message.channel.send(content="welcome to gartic!")
        await message.channel.send(content="-start to begin the game")
        await message.channel.send(content="make a guess using '='")

    if message.content.startswith("-start"):
        answer=random.choice(list(drawings.items()))
        drawing=drawings[answer]
        await message.channel.send(drawing)
    
    if message.content.startswith("="):
        if answer==message.content:
            await message.channel.send(message.author," guessed it!")

    if message.content.startswith("-end"):
        return


# client.run('token')