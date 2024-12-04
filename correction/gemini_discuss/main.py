import google.generativeai as genai
import sys
from config.ai_config import create_chat_session, send_and_print_message
from prompts.prompt_basic import Basicprompt
from utils.text_lecture import text_lecture
import os
from gtts import gTTS
import vlc
import time
import serial
import random

api_key="AIzaSyCBOjlgF8QUmauLHFZDkozMF3FTPgITQfo"

 
def init_session():
    """Initialise la session de chat avec l'API de l'IA.
    Returns:
        la session créé 
    """
    if not api_key:
        print('Votre clé API n\'est pas définie.')
        sys.exit(1)  # Quitter le programme si la clé API n'est pas définie
    
    # Initialisation du prompt pour les sessions
    pt = Basicprompt()
    
    # Création de 5 sessions de chat avec l'API
    session = create_chat_session(api_key)

    # Initialisation des sessions avec les prompts appropriés
    send_and_print_message("Init_session", session, pt.session_init)

    return session

if __name__ == '__main__':
    print("test")
    session=init_session()
    reponse1=send_and_print_message("Init_session", session, "comment tu t'appelle déjà ?")
    #reponse2=send_and_print_message("Init_session", session, "chante joyeux anniversaire pour mon collègue Andréas stp")
    print(reponse1)
    print(len(reponse1))
    #ser = serial.Serial('COM3', 19200)
    time.sleep(2)
    text_lecture("reponse_1" ,reponse1)
    #ser.write(str(list_move).encode())
    #text_lecture("reponse_2", reponse2)

    """
    ser = serial.Serial('COM3', 19200)
    time.sleep(2)
    ser.write(str([80, 0, 50, 0, 80, 00, 80, 0, 80, 0, 50, 0, 80, 00, 80, 0, 80, 0, 50, 0, 80, 00, 80, 0, 80, 0, 50, 0, 80, 00, 80, 0, 80, 0, 50, 0, 80, 00, 80, 0, 80, 0, 50, 0, 80, 0, 80, 0]).encode())
    time.sleep(2)"""