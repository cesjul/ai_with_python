from pathlib import Path

PATH = Path(__file__).parent 
DOC_PATH = PATH / 'documento.txt'

with open(DOC_PATH, 'w', encoding='utf=8') as file:
    file.writelines(['Escrevendo uma frase \r\n', 
                     'Escrevendo outra frase\r\n'])
    
with open(DOC_PATH, 'a', encoding='utf-8') as file:
    file.writelines(['Adicionando mais coisas\r\n',
                     'Mais uma coisa\r\n'])
    
with open(DOC_PATH, 'r') as file:
    print(file.read())