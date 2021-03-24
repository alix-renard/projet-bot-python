import random
from discord.ext import commands

TOKEN = "" # https://discord.com/developers/applications

# crée le bot et en designant le prefix pour toutes les commandes
bot = commands.Bot(command_prefix='!')
# le tableau de toutes les questions disponibles
questions = [
    'Qui a gagné le concour à trois points lors du all star game de 2021?  \n1) Stephan Curry \n2) Zake Lavyne \n3) James Harden',
    'Quel pays a gagné la coupe du monde en 2014? \n1) La France \n2) L\'Allemagne \n3) Le Brésil',
    'Ou ce situe Krung Thep Mahanakhon Amon Rattanakosin Mahinthara Ayutthaya Mahadilok Phop Noppharat Ratchathani Burirom Udomratchaniwet Mahasathan Amon Piman Awatan Sathit Sakkathattiya Witsanukam Prasit? \n1) Thailande \n2) Haïti \n3) Nouvelle-Zélande ',
]
# le tableau contenant les bonnes réponses
reponses = [1,2,1]
# pour stocker les questions posé c'est plus simple de stocker l'index de la question
index_questions_poses = []
# on stocke les réponses
reponses_aux_questions_poses = []

# fonction qui retourne la liste des questions restantes à poser
def questions_restantes():
  questions_restantes = []
  # pour chaque question
  for i in range(0,len(questions)):
    # on regarde si elle n'est pas dans le tableau des questions posé
    if i not in index_questions_poses:
      # on l'ajoute au tableau questions restantes
      questions_restantes.append(questions[i])
  # on retourne les questions restantes
  return questions_restantes

# commande 'quiz' pour lancer le quiz et va poser la 1ere question et la stoquer
#
# décorateur de fonction pour créer une commande discord
@bot.command(name='quiz', help='lance le quiz')
async def quiz(ctx): # ctx = contexte discord permet de renvoyer un message dans discord
  # vide les deux tableau
  del index_questions_poses[:]
  del reponses_aux_questions_poses[:]
  # envoie le message a discord
  await ctx.send('le quiz demarre, envoie ta réponse à l\'aide de la commande !r')
  # prend une question aléatoire dans les questions restantes
  question = random.choice(questions_restantes())
  # cherche l'index de cette question dans sont tableau
  index_question = questions.index(question)
  # ajoute cette index au tableau des questions posé
  index_questions_poses.append(index_question)
  # pose la question dans discord
  await ctx.send(question)


# commande 'r' qui recupere la réponse 1, 2 ou 3
@bot.command(name='r', help='repond au quiz')
# si le premier paramètre est toujour le contexte, le second est le texte saisie après la commande (:int = oblige que ce paramètre soit un nombre)
async def reponse(ctx, reponse :int):
  # on ajoute la réponse au tableau
  reponses_aux_questions_poses.append(reponse)
  # si on pose moins de 3 questions
  if len(index_questions_poses)<3:
    # alors on répète les étapes permettant de poser une question
    question = random.choice(questions_restantes())
    index_question = questions.index(question)
    index_questions_poses.append(index_question)
    await ctx.send(question)
  # sinon on termine le quiz
  else:
    # on va compter le nombre de bonne réponses
    nb_bonnes_reponses = 0
    # pour chaque question posé
    for i in range(0,3):
      # on cherche la bonne réponse
      bonne_reponse = reponses[index_questions_poses[i]]
      # on cherche la réponse de l'utilisateur
      rep = reponses_aux_questions_poses[i]
      # on regarde si l'utilisateur a bien répondu
      if rep == bonne_reponse:
        # on ajoute une bonne réponse
        nb_bonnes_reponses = nb_bonnes_reponses + 1
    # on envoie le nbr de bonne réponse
    await ctx.send('tu as ' + str(nb_bonnes_reponses) + ' bonnes reponses')
    await ctx.send('le quiz est fini')



bot.run(TOKEN)