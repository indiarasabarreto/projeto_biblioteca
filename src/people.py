people_names = ['Hermes Trismegisto', 'Platão', 'Carl Jung', 'Albert Einstein']


# Função para adicionar os nomes não existentes na lista
def register_person_name(name_to_add: str) -> None:
    people_names.append(name_to_add)
    print(f"'{name_to_add}' adicionado à lista.")

# Função para buscar nomes registrados na lista
def is_registered_person_name(search_person_name: str) -> bool:
    for name in people_names:
        if name == search_person_name:
            print("Nome encontrado!")
            return True
    print("Nome não encontrado!")
    return False

# Função que irá imprimir os nomes de cada pessoa registrada
def print_each_person_name() -> None:
    for name in people_names:
        print(name)

def main ():
    while (True):
        print('Bem vindo ao sistema de pessoas!')
        print('Digite 1 para ver os nomes registrados')
        print('Digite 2 para registrar um novo nome')
        print('Digite 3 para verificar se um nome está registrado')
        print('Digite 4 para sair do programa')
        selected_option = input('Digite a opção desejada: ')

        if selected_option == '1':
            print_each_person_name()
        elif selected_option == '2':
            person_name = input('Digite novo nome para ser registrado: ')
            register_person_name(person_name)
        elif selected_option == '3':
            check_registered_name = input('Digite o nome que deseja verificar: ')
            is_registered_person_name(check_registered_name)
        elif selected_option == '4':
            break
        else:
            print('Opção inválida, tente novamente.')



if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")
