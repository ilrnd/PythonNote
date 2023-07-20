import os
import numpy as np
import pandas as pd
import datetime
os.system('clear')
file_path = "notebook.csv"  

def add_note(subject, note):
    article_read = pd.read_csv(file_path,delimiter=';')
    uniq_id = len(article_read.index) + 1
    df = pd.DataFrame({'uniq_id': [uniq_id],
                       'subject': [subject],
                       'note': [note],
                       'date': [datetime.datetime.now()]}) #.strftime('%m/%d/%y %H:%M:%S')
    df.to_csv(file_path, mode='a', index=False, header=False, sep=';')

def open_notes():
    df = pd.read_csv(file_path, delimiter=';')
    print(df.sort_values(by='date').to_string(index=False))
    
def find_note(search):
    df = pd.read_csv(file_path,delimiter=';')
    if df['note'].str.contains(search,case=False).any():
        print(df[df['note'].str.contains(search,case=False)].to_string(index=False))
    else:
        print("Not found")
        
def del_note(del_id):
    df = pd.read_csv(file_path, delimiter=';')
    if del_id in df['uniq_id'].values:
        df = df.drop(df[df.uniq_id == del_id].index)
        df.to_csv(file_path, index=False, header=True, sep=";")    
    else:
        print("Deleting uniq_id not found")
    


while True:
    command = input("\nInput the command (add - add note, open - open all notes, find - search note\n del - delete note, change - note's change q - exit): ")
    if command == 'q':
        break
    if command == 'add':
        add_note(subject = input("Subject: "), note = input("Note: "))
        print("Note added")
    if command == 'open':
        open_notes()
    if command == 'find':
        find_note(input('Find: '))
    if command == 'del':
        open_notes()
        del_note(int(input("Inpud iniq_id for delete it: ")))
    if command == 'change':
        open_notes()
        find_note(input('Find note to change (keyword): '))
        del_note(int(input("Inpud iniq_id for change it: ")))
        add_note(subject = input("Subject: "), note = input("Note: "))
        print("Note changed")
        
        
        



