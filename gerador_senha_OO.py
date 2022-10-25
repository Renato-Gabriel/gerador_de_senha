from random import choice, shuffle
from pyperclip import copy 
import psycopg2

class Postgresql:

    def __init__(self):
        """Init definido para conectar o python ao banco de dados e criar um cursor.""" 
        self.conexao = psycopg2.connect(host='localhost',database = '#####' ,user='#####',password='#####')
        self.cursor = self.conexao.cursor()      
    
    def Select(self,sql_select):
        """Retornar a senha atual."""
        self.sql_select = sql_select
        self.select = self.cursor.execute(self.sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def Insert(self, confirmation):
        """Inserir uma nova senha nos registro da tabela pw."""
        self.confirmation = confirmation

        if confirmation == 1:
            a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            b = ['0','1','2','3','4','5','6','7','8','9']
            c = ['!','@','#','$','%','&','*']
            lista = []

            for x in range(0,3):
                x = choice(a)
                lista.append(x)

            for x in range(0,3):
                x = choice(b)
                lista.append(x)

            x = choice(a)
            x = x.upper()
            lista.append(x)

            x = choice(c)
            lista.append(x)

            shuffle(lista)
            senha = ''.join(lista)
            copy(senha)
            print('NOVA SENHA:', senha,'\n')
            self.insert = self.cursor.execute(f"INSERT INTO passgen (pw) VALUES ('{senha}')")
            self.conexao.commit()
            
        elif confirmation == 2:
            print('\nNÃO foi gerada uma nova senha')
            print('\n','-'*20,'PASSWORD ACCESS','-'*20,'\n\n','1 - Consultar senha\n','2 - Gerar nova senha\n','3 - Sair\n')
        
        elif confirmation is not 1 or 2:
            print("Opção inválida")
            print('\n','-'*20,'PASSWORD ACCESS','-'*20,'\n\n','1 - Consultar senha\n','2 - Gerar nova senha\n','3 - Sair\n')


#instanciar o objeto postgresql a classe Postgresql() 
postgresql = Postgresql()

print('\n','-'*20,'PASSWORD ACCESS','-'*20,'\n\n','1 - Consultar senha\n','2 - Gerar nova senha\n','3 - Sair\n')

exit = False
entrada = int(input('Selecione uma das opções: '))

while not exit:
    if entrada == 1:
        b = postgresql.Select("SELECT pw FROM passgen ORDER BY id DESC LIMIT 1")
        print(f'Sua senha atual é: - {b[0]} - Copiado para área de transferência.\n') 
        copy(b[0])
        entrada = int(input('Selecione uma das opções: '))

    elif entrada == 2:
        print(f'\nTem certeza que deseja gerar uma nova senha?\n1 - SIM\n2 - NÃO\n')
        c = int(input('Selecione uma das opções: '))
        postgresql.Insert(confirmation=c)
        entrada = int(input('Selecione uma das opções: '))

    elif entrada == 3:
        exit = True
    
    elif entrada is not 1 or 2 or 3:
        print("Opção inválida\n")
        entrada = int(input('Selecione uma das opções: '))