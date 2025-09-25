music_genres = [{'Rock', 'Jazz', 'Blues', 'Soul', 'Metal', 'Hip-hop', 'RnB'}]


def register_new_genre(add_new_genre: str) -> None:
    music_genres.append(add_new_genre)
    return


def search_genre(genre_to_search: str) -> str | None: 
    for genre in music_genres: 
        if genre_to_search == genre:
            return genre
    return

def show_sorted_genre() -> list[str]:
    return sorted(music_genres)
    
def show_reversed_sorted_genre() -> list[str]:
    return sorted(music_genres, reverse=True)

def invalid_option_selected() -> None:
    print('Opção Inválida. Não entendi...')


def main ():
    print('Bem vindo!')
    print(f'Gêneros musicais cadastrados {music_genres}')

    while(True):
        
        print('*' * 50)
        print('Digite 1 para buscar gênero')
        print('Digite 2 para registrar gênero')
        print('Digite 3 para ver todos os gêneros cadastrados em ordem alfabética')
        print('Digite 4 para ver gêneros cadastrados em ordem contrária')
        print('Digite X para sair do menu')
        print('*' * 50)

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
        elif selected_option == '3':
           sorted_genre = show_sorted_genre()
           print(f'Gêneros em ordem alfabética: {sorted_genre}')
        elif selected_option == '4':
            reversed_genre = show_reversed_sorted_genre()
            print(f'Gêneros em ordem contrária: {reversed_genre}')
        elif selected_option.lower() == 'x':
            print('Saindo do menu...')
            break
        else:
            invalid_option_selected()
        




if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")