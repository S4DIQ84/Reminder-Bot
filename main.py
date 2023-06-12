from pyrogram import Client,filters


api_id=20370928
api_hash='e68490404862c9c342adc76f870814bd'
bot_token='6115040897:AAEvsjVIvqP6Up76QwuUeKTL3VNNExguaxE'
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
