import tkinter as tk
from tkinter import messagebox
from requests_html import HTMLSession


def get_links():
    url = url_entry.get()
    session = HTMLSession()
    r = session.get(url)
    r.html.render()

    with open("links.txt", "a", encoding="utf-8") as file:
        for link in r.html.absolute_links:
            file.write(link + "\n")

    messagebox.showinfo("Success", "Results saved to links.txt")


# creating window
root = tk.Tk()
root.title("Links Extractor")

# window size
root.geometry("200x80")

# creating interface
url_label = tk.Label(root, text="Enter website URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

get_links_button = tk.Button(root, text="Get Links", command=get_links)
get_links_button.pack()

# run
root.mainloop()
