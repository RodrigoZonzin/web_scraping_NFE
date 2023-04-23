import consulta
import os

entrada = 1;
while(entrada != 0):
    print("0:Sair \t 1:Adicionar dados \t 2:Consultar dados");
    entrada = int(input("Sua escolha\n"));

    if(entrada == 1):
        os.system('clear')
        url = str(input("Copie a URL aqui\n")); 
        escolhe_loja = int(input("Qual foi a loja?\n1-BH 2-Eskynao 3-Rei das Frutas 4-outro\n")); 
        if escolhe_loja == 1: 
            loja = "BH";
        if escolhe_loja == 2: 
            loja = "Eskynao";
        if escolhe_loja == 3: 
            loja = "Rei das Frutas";
        if escolhe_loja == 4: 
            loja = input("Qual o nome do estabelecimento?\n");
        
        #CHAMA A FUNCAO E CONFERE RETORNO
        if(consulta.adiciona_dado(url, loja) == 1):
            print("Adicionado com sucesso!");
        else:
            print("Erro! :(\n");
    
    if(entrada == 2):
        os.system('clear')
        print("Por favor confira o arquivo basedeados.csv\n");
    