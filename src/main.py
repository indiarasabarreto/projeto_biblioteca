# Livro
# - id
# - titulo
# - autor
# - editora
# - categoria

print("Bem-vindo à biblioteca!")

books = ['O Caibalion', 'O Alquimista']


def register_book(title_to_add: str) -> None:
    books.append(title_to_add)
    print(f"Livro '{title_to_add}' adicionado à biblioteca.")


def search_book_title(title_to_search: str) -> bool:
    pass 

def main():
    while (True):
        print(f'Livros disponíveis: {books}')
        book_title = input("Digite o título do livro: ")
        for book in books:
            if book == book_title:
                print("Livro encontrado!")
        else:
            print("Livro não encontrado!")
            register_book(book_title)
        
   


if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")

