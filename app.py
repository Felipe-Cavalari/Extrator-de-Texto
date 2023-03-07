import os, re, shutil, time
import pandas as pd
from tkinter import filedialog
from function import Ict_Text_extractor, Yes_or_No, Ict_index_extractor

#Perguntando se o usuário vai mandar alguma tabela de input para buscar os indices
if not os.path.exists('./Banco de dados/'):
    print('A pasta do banco de dados não existe, criando....')
    os.makedirs('./Banco de dados')
    print('A pasta do banco de dados foi criada')
else:
    print('A pasta do banco de dados já existe')

#salvando o arquivo de index na pasta banco
if not os.path.exists('./Banco de dados/Platts - Lista de Índices.xlsx'):
    print('arquivo de indices não encontrado')
    print('_______________________________________________________')
    print('lembrando que o arquivo precisa ter o nome de Platts - Lista de Índices e ser em formato xlsx')
    time.sleep(2)
    Platts_indices = filedialog.askopenfilename(title='Selecione o Platts - Lista de incides', filetypes=[('Excel Files', '*.xlsx *.xls')])
    file_name = os.path.basename(Platts_indices)
    db_file_path = './Banco de dados/' + file_name
    shutil.copy(Platts_indices, db_file_path)
    
else:
    print('contem arquivo de indices no banco de dados')
    choice = input('Deseja enviar um novo arquivo com novos indices? ')
    Yes_or_No(choice)
    if choice == 'sim':
        print('sim')
    elif choice == 'nao' or 'não':
        print('Você escolheu não enviar um novo arquivo!')
        

db_file = ('./Banco de dados/Platts - Lista de Índices.xlsx')
print('Arquivo selecionado: ' + db_file + "\n")

#Função para extraír os indices do excel

all_index = Ict_index_extractor(db_file, 0)

print(all_index)

#Gerando variavel para selecionar o arquivo para ser extraido
print('Selecione o arquivo PDF')
file = filedialog.askopenfilename(title='Selecione o Pdf', filetypes=[('PDF Files', '*.pdf')])

file_name = os.path.basename(file)
#separando data do nome do arquivo
file_name_dict = re.split('[._]', file_name)
file_date = file_name_dict[1]

#caminho para salvar os dados extraidos
txt_path = './Dados extraidos'
if not os.path.exists(txt_path):
    print('criando diretório')
    os.makedirs(txt_path)
else:
    print('Diretorio ja existe')


#criando arquivo onde os dados vão ser colocados
txt_file = txt_path + '/' + file_name_dict[0] + "_" + file_name_dict[1] + '_Results.txt'

#verificando se existe algum arquivo de texto com o mesmo nome
if not os.path.exists(txt_file):
    print('criando o arquivo')
    open(txt_file, 'w').close()
else:
    print('Arquivo com mesmo nome já existe, limpando conteudo do mesmo!')
    open(txt_file, 'w').close()


#Realizando a extração

Ict_Text_extractor(file, txt_file)








