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
        for book in books:
            if book == title_to_search:
                print("Livro encontrado!")
                return True
        print("Livro não encontrado!")
        return False
            

def main():
    while (True):
        print(f'Livros disponíveis: {books}')
        book_title = input("Digite o título do livro: ")
        is_book_found = search_book_title(book_title)

        if not is_book_found:
            register_book(book_title)       
   

if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")

