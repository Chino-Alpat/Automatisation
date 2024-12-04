import google.generativeai as genai
import sys
from config.ai_config import create_chat_session, send_and_print_message
from prompts.prompt_basic import Basicprompt
import os
from gtts import gTTS
import vlc
import time
import serial
import random

api_key="AIzaSyCBOjlgF8QUmauLHFZDkozMF3FTPgITQfo"

 
def text_lecture(text_name, text_to_read):
    wait_time = len(text_to_read)*4/35
    file_name = text_name + '.mp3'
    print(wait_time)
    tts = gTTS(text_to_read + "            .", lang='fr',tld="ca")
    tts.save(file_name)
    player = vlc.MediaPlayer(file_name)
    ser = serial.Serial('COM3', 19200)
    time.sleep(2)
    player.play()
    list_move = random.sample(range(0, 80), k=50)
    t_end = time.time() + wait_time
    while time.time() < t_end:
        ser.write(str(list_move).encode())
        time.sleep(2)
    time.sleep(wait_time)
    

if __name__ == '__main__':
    print("test")
    session=init_session()
    reponse1=send_and_print_message("Init_session", session, "comment tu t'appelle déjà ?")
    reponse2=send_and_print_message("Init_session", session, "parle moi de l'automatisation de test stp")
