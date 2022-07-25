#U can add more partials to generate nick. Run this script. When you ran out of ideas, just type break to end script.
import os
import sys
while True:
    
    file = open(os.path.join(sys.path[0], "nickPartials.txt"),"r+")
    strings = file.read()
    search_word = input("enter a word you want to search in file: ")
    if(search_word =="break"):
        break
    if(search_word in strings):
        print("word found")
    else:
        print("word not found")
        file.write(search_word +'\n')