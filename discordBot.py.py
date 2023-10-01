# This example requires the 'message_content' intent.
# 1143450280810250281
# be7543c85172fc5b6c36a3333f937195736cf183b160b5cc6b4101592e8ed8e1

# token - MTE0MzQ1MDI4MDgxMDI1MDI4MQ.GtFH7e.bciT0BfZ1-f9YOPbanRlTXg5Ub3mtcr52hj9Do

# https://discord.com/channels/1143449498786476043/1143449499394646059
# https://replit.com/@ShikhaVerma5/DiscordBotChatGPT
import discord
import os
import openai


char = " "
openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("mySecretKey")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.content}:{message.content}"
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
           if self.user in message.mentions:
              print(chat)
              response = openai.Completion.create(
                  model="text-davinci-003",
                  prompt= f"{chat}\nshikhaGPT2023: ",
                  temperature=1,
                  max_tokens=256,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0
              )
              channel = message.channel
              messageToSend = response.choices[0].text
              await channel.send(messageToSend)  
         
        
      

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)