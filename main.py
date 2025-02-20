def books_reader():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def words_counter(text: str)->int:
    text = text.split()
    print(len(text))




def main():
    text = books_reader()
    words_counter(text)



main()