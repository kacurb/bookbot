def books_reader():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def words_counter(text: str)->int:
    text = text.split()
    print(len(text))

def char_counter(text: str)->dict:
    result = {}
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'z', 'y', 'x', 'v', 'q']
    for i in text.lower():
        if i in alpha:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
    for j in result:    
        print(f"The '{j}' character was found {result[j]} times")
    
    



def main():
    text = books_reader()
    char_counter(text)



main()