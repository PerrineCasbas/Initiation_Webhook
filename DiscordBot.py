import discord

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_reaction_add(reaction, user):
    print(f'User {user.id} reacted with {reaction.emoji} to message {reaction.message.id}')

client.run('MTIwMTg1NzIwOTA4MDc0NTk5Ng.G_t5rM.tBjWPz81SOySo7Xkvhmp_RHTsCstNKOkP7WkR4')
