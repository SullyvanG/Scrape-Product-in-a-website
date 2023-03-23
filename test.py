import requests
from bs4 import BeautifulSoup
import tkinter as tk

def search_beautetest():
    query = entry.get()
    url = f"https://www.beaute-test.com/trouve.php?motcle={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    product_list = soup.select_one(".product-list.mb-30")
    if product_list is not None:
        product_titles = product_list.select(".product-card__title")
        product_names = [title.text.strip() for title in product_titles]
        for i, name in enumerate(product_names):
            tk.Label(window, text=name).grid(row=i+1, column=0)
    else:
        tk.Label(window, text="Aucun résultat trouvé pour votre recherche.").grid(row=1, column=0)

window = tk.Tk()
window.title("Beauté-test search")
label = tk.Label(window, text="Entrez votre recherche:")
label.grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)
button = tk.Button(window, text="Rechercher", command=search_beautetest)
button.grid(row=0, column=2)
window.mainloop()
