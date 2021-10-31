from random import randint
import os
from timeit import default_timer as timer

Word_List = ["The" ,"quick" ,"brown" ,"fox" ,"jumped" ,"over" ,"the" ,"lazy", "dog"]

words = int(input("How many words? "))

def MakeList(Word_List,words):
    new_word = []
    for i in range(0,words):
        index = randint(0,len(Word_List)-1)
        new_word.append(Word_List[index])
        


    return new_word
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def game(words):
    NumOfWords = len(words)
    start = timer()
    for i in range(0,len(words)):
        word = words[i]
        clearConsole()
        print("Word: ",words[i])
        user_word = ''
        while (user_word != word):
            user_word = input("Type here: ")
    end = timer()
    time = end - start 
    time = time / 60 
    speed = NumOfWords / time
    speed = round(speed,2)
    print("Speed: ", speed , "WPM")
if __name__ == "__main__":
    my_list = MakeList(Word_List,words)
    game(my_list)