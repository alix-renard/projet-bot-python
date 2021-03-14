import random
from discord.ext import commands

TOKEN = "ODE4ODgyNjE4ODU0NjA0ODMw.YEeh3g.zcdj1bYgXVuHa-d8HkJ4adzKUyQ"

bot = commands.Bot(command_prefix='!')

questions = [
    'I\'m the human form of the 💯 emoji.',
    'Bingpot!',
    'Cool. Cool cool cool cool cool cool cool, no doubt no doubt no doubt no doubt.',
]
response_count = 0

# la commande !help affichera toutes les commandes et leur descriptions
@bot.command(name='99', help='Répondre avec une citation au hasard à la commande 99')
async def nine_nine(ctx):
    response = random.choice(questions)
    await ctx.send(response)


@bot.command(name='test', help='Répondre la valeur saisie par l\'utilisateur à la commande test')
async def test(ctx, arg):
    await ctx.send(arg)

# commande 'quizz' pour lancer le quizz et va poser la 1ere question


# commande 'r' qui recupere la réponse a ,b ou c
# qui stoque le nombre de responses
# qui pose une nouvelle question


bot.run(TOKEN)