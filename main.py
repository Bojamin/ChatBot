import json
import signal
import sys
from difflib import get_close_matches
from typing import Optional

class ChatBot:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.modele = self.load_modele()

    def load_modele(self) -> dict:
        """Charge le modèle depuis le fichier JSON."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_modele(self):
        """Sauvegarde le modèle dans le fichier JSON."""
        with open(self.file_path, 'w') as file:
            json.dump(self.modele, file, indent=2)

    def add_question(self, question: str, reponse: str):
        """Ajoute une question et sa réponse au modèle."""
        self.modele["questions"].append({"question": question, "reponse": reponse})

    def find_match(self, user_question: str) -> Optional[str]:
        """Trouve la question la plus proche dans le modèle."""
        questions = [q["question"] for q in self.modele["questions"]]
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def get_reponse_for_question(self, question: str) -> Optional[str]:
        """Retourne la réponse correspondante à une question du modèle."""
        for q in self.modele["questions"]:
            if q["question"] == question:
                return q["reponse"]
        return None

    def load_blacklist(self):
        """Charge la liste des mots interdits depuis le fichier blacklist.txt."""
        with open('blacklist.txt', 'r') as file:
            return file.read().splitlines()

    def is_reponse_appropriate(self, reponse: str, blacklist: list[str]) -> bool:
        """Vérifie si une réponse est appropriée."""
        return not any(word in reponse.lower() for word in blacklist)

    def run(self):
        """Lance le chatbot."""
        blacklist = self.load_blacklist()

        while True:
            user_input = input("Question: ")

            if user_input.lower() == 'end':
                break
            
            best_match = self.find_match(user_input)

            if best_match:
                reponse = self.get_reponse_for_question(best_match)
                print(f"Bot: {reponse}")
            else:
                print("Bot: Je ne connais pas la réponse. Pouvez vous me l'apprendre ?")
                new_reponse = input("Rentrer ou taper 'passer' : ")

                if new_reponse.lower() != 'passer':
                    if self.is_reponse_appropriate(new_reponse, blacklist):
                        self.add_question(user_input, new_reponse)
                        print("Bot: Merci j'ai appris quelque chose de nouveau")
                    else:
                        print("Bot: Désolé, la réponse est inappropriée.")

        self.save_modele()

if __name__ == "__main__":
    bot = ChatBot('modele.json')

    def save_and_exit(signal, frame):
        bot.save_modele()
        sys.exit(0)

    signal.signal(signal.SIGINT, save_and_exit)

    bot.run()
