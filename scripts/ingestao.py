import csv
import os

METADATA_FILE = os.path.join('..', 'dados', 'metadata.csv')

def ler_metadata(caminho):

    with open(caminho, mode='r', encoding='utf8') as file:
        leitor = csv.DictReader(file)
        for linha in leitor:

            print(f"Processando documento {linha['document_id']}: {linha['title']}")

if __name__ == '__main__':

    if os.path.exists(METADATA_FILE):
        ler_metadata(METADATA_FILE)  
    else:
        print("Arquivo metadata.csv não encontrado.")
