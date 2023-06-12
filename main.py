from pyrogram import Client,filters


api_id=
api_hash=
bot_token=
app=Client('reminder',api_id=api_id,api_hash=api_hash,bot_token=bot_token)

@app.on_message(filters.text)
async def handle_message(client,message):
    if message.text=="/start":
        await message.reply("Your bot is ready now")


@app.on_message(filters.text)
async def start(client,message):
    a=message.text
    print(a)
app.run()
