import os
import re
import pandas as pd
import tkinter as tk
import time
from tkinter import filedialog
from function import Ict_Text_extractor, Yes_or_No

#Perguntando se o usuário vai mandar alguma tabela de input para buscar os indices
if not os.path.exists('./Banco de dados/'):
    print('A pasta do banco de dados não existe, criando....')
    os.makedirs('./Banco de dados')
    print('A pasta do banco de dados foi criada')

if not os.path.exists('./Banco de dados/Platts - Lista de Índices'):
    print('arquivo de indices não encontrado')
    print('_______________________________________________________')
    print('lembrando que o arquivo precisa ter o nome de Platts - Lista de Índices')
    time.sleep(3)
    Platts_index = filedialog.askopenfilename(title='Selecione o Platts - Lista de incides', type=['Excel'])
    

else:
    print('contem arquivo de indices no banco de dados')
    choice = input('Deseja enviar um novo arquivo com novos indices? ')
    Yes_or_No(choice)
    if choice == 'sim':
        print('sim')
    elif choice == 'nao' or 'não':
        print('não')

#Gerando variavel para selecionar o arquivo para ser extraido
file = filedialog.askopenfilename(title='Selecione o Pdf')

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








