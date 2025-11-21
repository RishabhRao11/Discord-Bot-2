import discord, os, asyncio
from webserver import keep_alive
from discord.ext import commands
import random
import better_profanity
from better_profanity import profanity


intents = discord.Intents().default()
intents.members = True

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mata mata turtle"))
  print('Bot is ready')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.author.bot:
    return
  else:
    
    if message.content.startswith('<add') or message.content.startswith('<remove'):

      if str(message.author.id) == '722679891253788693' or str(message.author.id) == '537140267501748234' or str(message.author.id) == '694801360800972840' or str(message.author.id) == '607044842064838663':

        if '<add' in message.content:

          msg = message.content.replace('<add', '').strip().lower()
          with open('bad_words.txt', 'a', encoding='utf-8') as file:
            file.write('\n'+msg)
          await message.channel.send('word has been added')
          return
      elif str(message.author.id) != '722679891253788693' or str(message.author.id) != '537140267501748234' or str(message.author.id) != '694801360800972840' or str(message.author.id) != '607044842064838663':

        await message.channel.send('only admins can use this command')
        return

      if str(message.author.id) == '722679891253788693':
        if '<remove' in message.content:
          bad_words=[]
          msg = message.content.replace('<remove', '').strip().lower()
          with open('bad_words.txt', 'r+') as file:
            for i in file.readlines():
              bad_words.append(i)
            try:  
              bad_words.remove(msg)
              file.truncate(0)
              file.write(''.join(bad_words))
            except ValueError:
              await message.channel.send('the word isnt there in the bad words database')
              return

          await message.channel.send('action complete')
          return
      elif str(message.author.id) != '722679891253788693':
        await message.channel.send('only <@722679891253788693> can use this command')
        return
    


    profanity.load_censor_words_from_file('bad_words.txt')

    if profanity.contains_profanity(message.content):
      await message.delete()
    
    mention = f'<@!{client.user.id}>'
    if mention in message.content:
      random_sentences = ['heya', 'why the ping?', 'can i watch mata mata turtle in peace?', 'smh']
      random_sentence = random.choice(random_sentences)
      await message.channel.send(random_sentence)
    numbers = range(100)
    if random.choice(numbers) == 2:
      await message.add_reaction('🥚')
      

keep_alive()
client.run(os.getenv('TOKEN'))