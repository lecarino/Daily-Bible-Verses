import requests
from twilio.rest import Client
import csv
import random
import re
#Twilio Account
account_sid = 'ACCOUNT SID'
auth_token = 'AUTH_TOKEN'

# verses_data = [
#     {"Book": "Colossians", "Chapter": 3, "Verse": 23, "Text": "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters,"},
#     {"Book": "John", "Chapter": 3, "Verse": 16, "Text": "For God so loved the world that He gave his one and only Son, that whoever believes in him shall not perish but have eternal life."},
# ]
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     fieldnames = ["Book", "Chapter", "Verse", "Text"]
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     # Write header
#     writer.writeheader()

#     # Write data
#     # for verse in verses_data:
#     #     writer.writerow(verse)
# print(f"CSV file '{csv_file_path}' created successfully.")

def Send_Text():
    csv_file_path = 'bible_verses.csv'
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        verses_list = list(reader)
        random_verse = random.choice(verses_list)

        text_message = f"{random_verse['Book']} {random_verse['Chapter']}:{random_verse['Verse']} \n{random_verse['Text']}"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body= text_message,
        from_='TWILIO PHONE NUMBER',
        to='PERSONAL PHONE NUMBER'
        )

def add_verses():
    csv_file_path = 'bible_verses.csv'
    while True:
        book = input("Please type in the Bible book you want to put in the database:")
        if book.isalpha():
            break
        else:
            print('Please type in a book name.')
    while True:
        chapter = input("Please type in the chapter you want to put in the database:")
        if chapter.isdigit():
            break
        else:
            print('Please type in a Chapter number')
    #Need to add parsing for verses like '1-3'
    verse = input("Please type in the Bible verse number/s you want to put in the database:")

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        verses_list = list(reader)
    
    # Check if the verse exists in the database
    if any(row["Book"] == book and row["Chapter"] == chapter and row["Verse"] == verse for row in verses_list):
        print('That Bible verse is already in the database.')
        return
    
    text = input("Please type in the text:")
    # Append the new verse to the CSV file
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["Book", "Chapter", "Verse", "Text"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Write data
        writer.writerow({"Book": book, "Chapter": chapter, "Verse": verse, 'Text': text})

    print('Bible verse added to the database successfully.')


if __name__ == "__main__":
    Send_Text()