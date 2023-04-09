import ascii_art
import random
from time import sleep


WORDS = ["elma", "kalem", "buğra", "ışık", "dolap", "başarı", "televizyon", "sevinç"]
MAX_FAILS = 7

def game_ending():
    sleep(1)
    print("Yeni oyun başlıyor...\n")
    sleep(1)
    print("-----------------------\n")



print("\033[1;36m"+ascii_art.BANNER+"\033[0m"+" \033[1;31mBy Burra\033[0m\n\n")

while True:
    word = random.choice(WORDS)

    hidden_word = "_"*len(word)
    print(word)
    print("Bulunacak kelime: "+hidden_word)
    fails = 0

    game_end = False
    found_indexes = []
    found_chars = []

    while not game_end:
        char_input = input("Harf giriniz: ")
        if(len(char_input) != 1 or not char_input.isalpha()):
            print("Geçersiz karakter\n")
            continue
        char_input = char_input.lower()
        any_found = False
        currently_found_indexes = []
        for index, char in enumerate(word):
            if char == char_input:
                currently_found_indexes.append(index)
                found_indexes.append(index)
                any_found = True

        if any_found is False:
            fails += 1
            print("Harf bulunamadı!")
            print(ascii_art.HANGMANPICS[fails-1] + "\n")
            print(hidden_word+"\n")

        else:
            if char_input in found_chars:
                print("Bu harfi zaten buldunuz")
                continue

            for found_index in currently_found_indexes:
                hidden_word = hidden_word[:found_index] + char_input + hidden_word[found_index+1:]
            
            print("Harf bulundu!: " + hidden_word + "\n")
            if hidden_word == word:
                print("Kazandınız! Kelime: " + word)
                game_ending()
                game_end = True

        if fails >= MAX_FAILS:
            print("Kaybettiniz. Cevap: " + word)
            game_ending()
            game_end = True
