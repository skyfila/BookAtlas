from bs4 import BeautifulSoup
import requests

NYT_BESTSELLERS_URL = "https://www.nytimes.com/books/best-sellers/"

response = requests.get(NYT_BESTSELLERS_URL)
soup = BeautifulSoup(response.text, "html.parser")
genres = soup.find_all("div", class_="css-v2kl5d")[1:]

genre_dict = {}
for genre in genres[:-1]:
    temp = {}
    for book in genre:

        genre_list = book.h2.text

        temp2 = {}
        for books in book.ol:
            # print(books)
            book_title = books.h3.text

            img = books.img.attrs["src"]

            p_list = books.css.select("p", class_="css-1nxjbfc")[1:]
            author = p_list[0].text
            desc = p_list[1].text

            temp2[book_title] = {"author": author, "desc": desc, "img":img}
            genre_dict[genre_list] = temp2


# for keys, values in genre_dict.items():
#     print(keys)
#     for key, value in values.items():
#         print(key)
#         print(value)
#         print("\n")
