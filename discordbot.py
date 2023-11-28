import discord
import openai
import os

client = discord.Client()
openai_api_key = os.environ['GPT_API_KEY']  # OpenAI APIキーを設定
discord_bot_token = os.environ['DISCORD_BOT_TOKEN'] # Discord BOTトークンを設定
target_emoji = "👍"  # 反応する絵文字を設定

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == target_emoji:
        message = reaction.message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": message.content}]
        )
        await message.channel.send(response.choices[0].message['content'])

client.run(discord_bot_token)
