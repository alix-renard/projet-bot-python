import random
from discord.ext import commands

TOKEN = "ODE4ODgyNjE4ODU0NjA0ODMw.YEeh3g.2X1GTML3HMX0hu4KEQ3qxT8bmRA"

bot = commands.Bot(command_prefix='!')

questions = [
    'Qui a gagné le concour à trois points lors du all star game de 2021?  \n1) Stephan Curry \n2) Zake Lavyne \n3) James Harden',
    'Quel pays a gagné la coupe du monde en 2014? \n1) La France \n2) L\'Allemagne \n3) Le Brésil',
    'Ou ce situe Krung Thep Mahanakhon Amon Rattanakosin Mahinthara Ayutthaya Mahadilok Phop Noppharat Ratchathani Burirom Udomratchaniwet Mahasathan Amon Piman Awatan Sathit Sakkathattiya Witsanukam Prasit? \n1) Thailande \n2) Haïti \n3) Nouvelle-Zélande ',
]
reponses = [1,2,1]
index_questions_poses = []
reponses_aux_questions_poses = []

# Retourne la liste des questions restantes a poser
def questions_restantes():
  questions_restantes = []
  for i in range(0,len(questions)):
    if i not in index_questions_poses:
      questions_restantes.append(questions[i])
  return questions_restantes

# commande 'quizz' pour lancer le quizz et va poser la 1ere question et la stoquer
@bot.command(name='quiz', help='lance le quiz')
async def quiz(ctx):
  del index_questions_poses[:]
  del reponses_aux_questions_poses[:]
  await ctx.send('le quiz demarre, envoie ta réponse à l\'aide de la commande !r')
  question = random.choice(questions_restantes())
  index_question = questions.index(question)
  index_questions_poses.append(index_question)
  await ctx.send(question)


# commande 'r' qui recupere la réponse a ,b ou c
# qui stoque le nombre de responses
# si le nombre de questions est inferieur à 3 on pose une autre question et stoque la question
# sinon on affiche le résultat du quizz
@bot.command(name='r', help='repond au quiz')
async def reponse(ctx, reponse :int):
  reponses_aux_questions_poses.append(reponse)
  if len(index_questions_poses)<3:
    question = random.choice(questions_restantes())
    index_question = questions.index(question)
    index_questions_poses.append(index_question)
    await ctx.send(question)
  else:
    nb_bonnes_reponses = 0
    for i in range(0,3):
      index_question_pose = index_questions_poses[i]
      rep = reponses_aux_questions_poses[i]
      bonne_reponse = reponses[index_question_pose]
      if rep == bonne_reponse:
        nb_bonnes_reponses = nb_bonnes_reponses + 1
    await ctx.send('tu as ' + str(nb_bonnes_reponses) + ' bonnes reponses')
    await ctx.send('le quiz est fini')



bot.run(TOKEN)