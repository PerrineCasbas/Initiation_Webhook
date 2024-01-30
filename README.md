# Initiation aux Webhooks

## Step 1: Webhook sur Discord

### Préparation:
- Utilisez le serveur Discord déjà créé: [Rejoindre le serveur](https://discord.gg/wCPz3p73).
- Un canal spécifique, `step1`, est disponible pour la création de webhooks.

### Création d'un Webhook Discord:
1. **Accès au Canal `step1`:**
   - Allez dans le canal `step1` sur le serveur Discord.

2. **Création du Webhook:**
   - Cliquez sur les paramètres du canal (icône d'engrenage à côté du nom du canal).
   - Choisissez `Intégrations` puis `Créer un Webhook`.
   - Personnalisez votre Webhook (nom, icône) et copiez l'URL.

3. **Configuration du Webhook GitHub:**
   - Dans votre repo GitHub, accédez à `Settings` > `Webhooks`.
   - Sélectionnez `Add Webhook` et collez l'URL du Webhook Discord.
   - Configurez les événements à notifier.

## Step 2: Webhook sur Supabase

1. **Préparez votre compte Supabase:**
   - Assurez-vous d'avoir un compte Supabase.

2. **Créer des Tables:**
   - `basic_info`: Contient `id_repository`, `name_repository`, `message`.
   - `file_modified`: Contient `id` (auto-incrémenté), `modified_file`, `date`.
   - /!\ Faites attention aux types de données.

3. **Créer une Edge Function:**
   - Utilisez cette fonction pour recevoir les données de GitHub.
   - [Guide de démarrage rapide Supabase Functions](https://supabase.com/docs/guides/functions/quickstart)

4. **Déployer sur Supabase:**
   - Suivez les instructions pour le déploiement.
   - [Guide de déploiement](https://supabase.com/docs/guides/functions/deploy)

5. **Remplir les Tables:**
   - Utilisez les données reçues pour remplir vos tables.
   - Consultez `API docs` et `basic info` dans Supabase.