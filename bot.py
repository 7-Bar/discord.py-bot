import discord
import interactions
import responses


async def send_message(message, user_message, is_private,):
    try:
        response = responses.get_response(user_message)
        if response == "`PLEASE STOP SWEARING`":
            await message.author.send(f"{message.author.mention} {response}")    # sends to DM
            await message.channel.send(f"{message.author.mention} {response}")   # sends to channel
        else:
            await message.author.send(response) if is_private else await message.channel.send(response)
        print(f"sent {response} to {message.author}")
    except Exception as E:
        print(E)


def run_discord_bot():
    TOKEN = # my token
    bot = interactions.Client(TOKEN)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is up and running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        if responses.get_response(user_message) == "":               # this makes the bot not respond to messages that are not swears
            return
        elif user_message[0] == "?":
            user_message = user_message[1]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
