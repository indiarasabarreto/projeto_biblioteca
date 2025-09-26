# Livro
# - id
# - titulo
# - autor
# - editora
# - categoria



books = []


def register_book_by_title(title: str, book: str) -> None:
    register_book_by_title[book.lower()].append(title)
    return

# def show_book_by_title(title: str) -> list[str]:
#     return register_book_by_title[title.lower()]






def main():
    print("Bem-vindo à biblioteca!")

    registered_book = input('Digite o nome do livro para registrar: ')
    print(registered_book)

   

if __name__ == "__main__":
    print("Iniciando programa...")
    main()
    print("Programa finalizado.")

