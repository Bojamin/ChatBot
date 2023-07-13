Pour démarrer le projet : 

python main.py 

Ce POC en python de poser des questions et d'avoir la réponse la plus proche de la question posée. Si il n'y a aucune réponse correspondante il est possible de rentrer une réponse tant qu'elle ne contient pas de mot de la blacklist. On peut sortir du chatbot en écrivant end. 

Le chatbot est entrainé avec le modèle "modele.json" qui lui fournit une base de réponse depuis laquelle il pourra répondre aux questions. Evidemment cela marche même si la question n'est pas la même. 

Exemple : 

Question: Ou trouver la déclaration publiée dans les journaux clandestins ?
Bot: https://www.charles-de-gaulle.org/wp-content/uploads/2017/03/Declaration-publiee-dans-les-journaux-clandestins-en-France.pdf
Question: Donne moi la déclaration publiée dans les journaux clandestins ?
Bot: https://www.charles-de-gaulle.org/wp-content/uploads/2017/03/Declaration-publiee-dans-les-journaux-clandestins-en-France.pdf
Question: Quel est le lien de la déclaration publiée dans les journaux ?
Bot: https://www.charles-de-gaulle.org/wp-content/uploads/2017/03/Declaration-publiee-dans-les-journaux-clandestins-en-France.pdf