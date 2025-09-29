artists_by_genre = {
    'rock': [],
    'mpb': [],
    'metal': []
}

#utils
def lower_genre(genre: str) -> str:
    return genre.lower()

def get_by_genre(genre: str) -> list[str]:
    return artists_by_genre.get(lower_genre(), [])

def set_by_genre(artist_name: str, genre: str) -> None:
    lowered_genre = lower_genre()

    if lowered_genre in artists_by_genre:
        artists_by_genre[lowered_genre].append(artist_name)
    else:
        artists_by_genre[lowered_genre] = [artist_name] 

# services
def register_artist_by_genre(artist_name: str, genre: str) -> None:
    set_by_genre(artist_name, genre)
    return

def get_artists_by_genre(genre: str) -> list[str]:
    return get_by_genre(genre)
    
def search_artist_by_genre(artist_name: str, genre: str) -> str | None:
    artists = get_by_genre(genre)

    for artist in artists:
        if artist == artist_name:
            return artist_name
    return

def invalid_option_selected() -> None:
    print('Opção Inválida. Não entendi...')


def main ():
    print('Bem vindo!')
    print(f'Artistas por gênero {artists_by_genre}')

    while(True):
        
        print('*' * 50)
        print('Digite 1 para registrar artista a um gênero')
        print('Digite 2 para visualizar artistas por gênero')
        print('Digite 3 para buscar artista por gênero')
        print('Digite X para sair do menu')
        print('*' * 50)

        selected_option = input('Digite a opção desejada: ')

        if selected_option == '1':
            artist_name = input('Digite o artista que deseja registrar: ')
            genre = input('Digite gênero desejado: ')
            register_artist_by_genre(artist_name, genre)
            print(artists_by_genre)
        elif selected_option == '2':
            genre_artist = input('Digite o gênero desejado: ')
            artists = get_artists_by_genre(genre_artist)
            print(artists)
        elif selected_option == '3':
            artist = input('Digite artista que deseja encontrar: ')
            genre = input('Digite gênero: ')
            result = search_artist_by_genre(artist, genre)
        
            if result:
                print(result)
            else:
                print('Artista não encontrado')
            
        elif selected_option.lower() == 'x':
            print('Saindo do menu...')
            break
        else:
            invalid_option_selected()
        


if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")