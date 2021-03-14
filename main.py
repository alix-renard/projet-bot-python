import random
from discord.ext import commands

TOKEN = "ODE4ODgyNjE4ODU0NjA0ODMw.YEeh3g.eMaG4fLP_F4uizC5j44vvXaCCmw"

bot = commands.Bot(command_prefix='!')

questions = [
    'I\'m the human form of the 💯 emoji.',
    'Bingpot!',
    'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.',
]
questions_poses = []
reponses = []

# la commande !help affichera toutes les commandes et leur descriptions
@bot.command(name='99', help='Répondre avec une citation au hasard à la commande 99')
async def nine_nine(ctx):
  response = random.choice(questions)
  await ctx.send(response)


@bot.command(name='test', help='Répondre la valeur saisie par l\'utilisateur à la commande test')
async def test(ctx, arg):
  await ctx.send(arg)

# commande 'quizz' pour lancer le quizz et va poser la 1ere question et la stoquer
@bot.command(name='quiz', help='lance le quiz')
async def quiz(ctx):
  await ctx.send('le quiz demarre')
  question = random.choice(questions)
  questions_poses.append(question)
  await ctx.send(question)


# commande 'r' qui recupere la réponse a ,b ou c
# qui stoque le nombre de responses
# si le nombre de questions est inferieur à 3 on pose une autre question et stoque la question
# sinon on affiche le résultat du quizz
@bot.command(name='r', help='repond au quiz')
async def reponse(ctx, arg):
  reponse = arg
  reponses.append(reponse)
  if len(questions_poses)<3:
    question = random.choice(questions)
    questions_poses.append(question)
    await ctx.send(question)
  else:
    bonne_reponse = 0
    for r in reponses:
      if r == 'a':
        bonne_reponse = bonne_reponse + 1
    await ctx.send('tu as ' + str(bonne_reponse) + ' bonnes reponses')
    await ctx.send('le quiz est fini')



bot.run(TOKEN)