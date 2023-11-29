import discord
import openai
import os

# 必要なIntentsを設定
intents = discord.Intents.default()  # 一般的なIntentsを有効化
# intents = discord.Intents.all()  # すべてのIntentsを有効化する場合

# Discord ClientをIntentsと共に初期化
client = discord.Client(intents=intents)

# 環境変数からAPIキーを取得
openai_api_key = os.environ['GPT_API_KEY']
discord_bot_token = os.environ['DISCORD_BOT_TOKEN']

# 反応する絵文字を設定
target_emoji = ":star2:"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_reaction_add(reaction, user):
    # 指定した絵文字に反応する場合の処理
    if reaction.emoji == target_emoji:
        message = reaction.message
        openai.api_key = openai_api_key  # OpenAI APIキーを設定
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[{"role": "system", "content": "You are a helpful assistant."},
        #               {"role": "user", "content": message.content}]
        # )
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4-0314",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.content}}
            ]
            )

        await message.channel.send(completion.choices[0].message)

# ボットを実行
client.run(discord_bot_token)
