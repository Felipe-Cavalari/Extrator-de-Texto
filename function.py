import PyPDF2
import pandas as pd

#Função responsável pela extração de texto do PDF
def Ict_Text_extractor(file, txt_file):
    print('extraindo arquivo ICT')
    with open(file, 'rb') as pdf:
        pdf_extract = PyPDF2.PdfReader(pdf)
        page_number = len(pdf_extract.pages)

        with open(txt_file, 'a', encoding='utf-8') as txt:
            for index in range(page_number):
                            #obtendo a pagina do loop
                page = pdf_extract.pages[index]

                            #extraindo o texto
                page_text = page.extract_text()

                            #Escrevendo no arquivo por loop
                txt.write(page_text)

                txt.write('\n----- Página {} -----\n\n'.format(index+1))
    
    print('Texto extraído com sucesso')



def Ict_index_extractor(excel_file):
    None


def Yes_or_No(choice):
    while choice.lower() not in ["sim", "não", "nao"]:
        choice = input("Digite 'sim' ou 'não': ")
        if choice.lower() == "sim":
            print("Você escolheu sim!")
        elif choice.lower() == "não":
            print("Você escolheu não!")
        else:
            print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
        return choice