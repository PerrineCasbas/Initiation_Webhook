# Initiation aux Webhooks

Bienvenue à l'atelier d'initiation aux webhooks sur Discord ! Dans cet atelier, nous allons apprendre à créer un webhook Discord pour envoyer des messages et nous allons également créer un bot de quiz Discord en utilisant Python.

## Étape 1: Création d'un Webhook Discord

### Préparation:
- Pour commencer, rejoignez notre serveur Discord déjà créé: [Rejoindre le serveur](https://discord.gg/wCPz3p73).
- Un canal spécifique, `quizz`, est disponible pour la création de webhooks.

### Création d'un Webhook Discord:
1. **Accédez au Canal `quizz`:**
   - Rendez-vous dans le canal `quizz` sur le serveur Discord.

2. **Création du Webhook:**
   - Cliquez sur les paramètres du canal (icône d'engrenage à côté du nom du canal).
   - Choisissez `Intégrations` puis `Créer un Webhook`.
   - Personnalisez votre Webhook en lui donnant un nom et une icône, puis copiez l'URL du webhook.

3. **GitHub Repository:**
   - Vous pouvez trouver tous les fichiers dont vous avez besoin, y compris `DiscordQuizzBot.py`, dans notre dépôt GitHub: [GitHub Repository](https://github.com/PerrineCasbas/Initiation_Webhook?tab=readme-ov-file).

## Étape 2: Utilisation de Python pour un Quiz Discord

Maintenant que vous avez créé un Webhook Discord et avez tout en main, nous pouvons commencer. Cependant, il est important de noter que pour créer un quiz interactif, nous devons avoir un bot Discord, car les webhooks ont des limitations en termes d'interaction avec les utilisateurs. Nous utiliserons donc principalement le bot pour gérer le quizz, mais nous utiliserons les webhooks pour envoyer des messages et afficher les questions et les réponses.

1. **Configuration du bot Discord:**
   - Assurez-vous d'avoir Python installé sur votre système.
   - Ouvrez le fichier `DiscordQuizzBot.py` fournis.

2. **Installation des dépendances:**
   - Exécutez la commande `pip install discord.py` pour installer la bibliothèque Discord.py si ce n'est pas déjà fait.

3. **Exécution du Bot:**
   - Exécutez `DiscordQuizzBot.py` pour démarrer le bot Discord.

## Étape 3: Création du Quiz Discord

Pour réaliser cette étape, nous allons créer un bot Discord qui permet d'envoyer un quizz via un webhook, collecter les réponses des utilisateurs à l'aide de réactions, et afficher les scores à la fin. Suivez ces étapes :

- le bot surveille le canal `quizz` pour détecter quand au moins 2 personnes au bout de X second ont réagi à un message du webhook.
- Lorsque le seuil est atteint, le bot peut envoyer un autre webhook avec la première question du quizz.
- Le bot peut ajouter des réactions aux messages du webhook pour représenter les choix de réponses possibles.
- Les utilisateurs sélectionnent leur réponse en cliquant sur la réaction correspondante.
- Le bot surveille les réactions des utilisateurs et enregistre leurs réponses.
- Vous pouvez définir un délai (X secondes) pour que les utilisateurs réagissent à chaque question.
- Une fois que toutes les questions ont été posées, le bot peut calculer les scores en fonction des réponses correctes et les afficher à la fin du quizz en utilisant un autre webhook.
- Le bot peut également annoncer le gagnant et clôturer le quizz.

## Bonus:

Le bot peut être capable d'avoir des paramètres, des scores différents en fonction des questions des groupes, etc... et même d'envoyer les résultats sur Supabase pour les stocker définitivement.
