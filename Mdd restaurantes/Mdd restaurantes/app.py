import os

restaurantes  = [{'nome':'Hamburger', 'categoria':'lanche', 'ativo':False}, 
                 {'nome':'pizza', 'categoria':'italiana', 'ativo':False}, 
                 {'nome':'coca', 'categoria':'bebida', 'ativo':True}]

def exibir_nome_do_programa():
    """Essa função cria o titulo do programa """
    print("""
█▀▄▀█ █▀▄ █▀▄   █▀▀ █▀█ █▀█ █▀▄
█░▀░█ █▄▀ █▄▀   █▀░ █▄█ █▄█ █▄▀\n""")

def exibir_opcoes(): 
    """Essa função exibe as opções do código """

    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurantes")
    print("4. Sair\n") 


def encerrar_app():
    exibir_subtitulo("Encerrando App")

def voltar_menu_principal():
    """Essa função retorna ao Main menu"""

    input("\nPressione uma tecla para retornar o menu inicial ")
    main()

def opcao_invalida():
    """Essa função dita se a opção é valida"""
    
    print("Opção Invalida\n")

    voltar_menu_principal()

def exibir_subtitulo(texto):
    """Essa função exibe os titulos da opções"""
    
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
def cadastrar_novo_restaurante():
    """Essa função cadastra novos restaurantes
    
        inputs:
        -nome do restaurante
        -categoria

        outputs:
        
        Insere o nome e categoria dos restaurantes
    
    """
    
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_do_restaurante = input("Insira o nome do seu restaurante: ")
    categoria = input(f"\nInsira a categoria do restaurante ({nome_do_restaurante}): ")
    
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante ({nome_do_restaurante}) foi cadastrado com sucesso\n")

    voltar_menu_principal()

def listar_restaurantes():
    """Essa função lista os restaurantes """

    exibir_subtitulo("Lista de restaurantes")

    print(f"{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Funcionamento'.ljust(20)}\n")
    for restaurante in restaurantes:
        nome_restaurante_lista = restaurante ["nome"]
        categoria = restaurante ["categoria"]
        ativo = "Aberto" if restaurante ["ativo"] else "Fechado"
        print(f"-> {nome_restaurante_lista.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}")

    voltar_menu_principal()

def alterar_estado_do_restaurante():
    """Essa função ativa e desativa um restaurante"""
    
    exibir_subtitulo("Alterando funcionamento do restaurante")

    nome_restaurante = input("Digite o nome do restaurante para alterar o funcionamento: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ["nome"]:
            restaurante_encontrado = True
            restaurante ["ativo"] = not restaurante ["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativo com sucesso" if restaurante ["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi identificado no sistema")

    voltar_menu_principal()



def opcao_selecionada(): 
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            encerrar_app()
        else: 
            opcao_invalida()
    except: 
         opcao_invalida()   

def main(): 
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    opcao_selecionada()


if __name__ == "__main__":
    main()