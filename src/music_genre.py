music_genres = ['Rock', 'Jazz', 'Blues', 'Soul', 'Metal', 'Hip-hop', 'RnB']


def register_new_genre(add_new_genre: str) -> None:
    music_genres.append(add_new_genre)
    return


def search_genre(genre_to_search: str) -> str | None: 
    for genre in music_genres: 
        if genre_to_search == genre:
            return genre
    return

def show_sorted_genre() -> list[str]:
    pass


def main ():
    print('Bem vindo!')
    while(True):
        
        print('Digite 1 para buscar gênero')
        print('Digite 2 para registrar gênero')
        print('Digite X para sair do menu')

        selected_option = input('Digite a opção desejada: ')

        if selected_option == '1':
            genre_to_search = input('Digite o gênero que deseja buscar: ')
            founded_genre = search_genre(genre_to_search)

            if founded_genre:
                print(f'Gênero encontrado: {founded_genre}')
            else:
                print('Gênero não encontrado.')
        elif selected_option == '2':
            genre_to_register = input('Digite o gênero que deseja registrar: ')
            register_new_genre(genre_to_register)
            print(f'Novo gênero registrado: {genre_to_register}')
        elif selected_option.lower() == 'x':
            print('Saindo do menu...')
            break
        




if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")