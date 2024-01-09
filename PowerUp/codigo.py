import pyautogui
import pandas
from time import sleep

pyautogui.PAUSE = 0.5

# pressionar a tecla windows
pyautogui.press('win')

# escrever o nome do navegador
pyautogui.write('opera')

# abrir o navegador
pyautogui.press('enter')
sleep(2)

# escrever o link no navegador
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

# acessar o link
pyautogui.press('enter')

sleep(5)
# clicar na area de email
pyautogui.click(x=631, y=361)

# escrever o email
pyautogui.write('email@gmail.com')

# passar pro campo da senha
pyautogui.press('tab')

# escrever a senha
pyautogui.write('1234567890')

# clicar em logar
pyautogui.click(x=702, y=523)
sleep(3)

# ler a base de dados e armazenar na variavel tabela
tabela = pandas.read_csv('produtos.csv')
for linha in tabela.index:
    pyautogui.click(x=659, y=241)

    # Código
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # Marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    # Tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # Categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # Preço
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    # Custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # Observações
    observacao = tabela.loc[linha, 'obs']
    if not pandas.isna(observacao):
        pyautogui.write(observacao)
    
    # Cadastrar
    pyautogui.click(x=632, y=462)

    # Rolar pra cima
    pyautogui.scroll(5000)

