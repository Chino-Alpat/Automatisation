import csv

critique_michel = {}


if __name__ == '__main__':
   print("lecture note de michel")
   with open('film-de-michel.csv', newline='', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile, delimiter=';')
      for row in reader:
         critique_michel[row['Titre']] = {"réalisateur": row['Réalisateur'],"note": row['note']}
   print(critique_michel)
