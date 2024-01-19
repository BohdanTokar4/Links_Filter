import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def extract_links_from_webpage(url, output_file):
    try:
        # Отримання HTML-коду з веб-сторінки
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Виділення посилань за допомогою BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Знаходження всіх тегів <a> та виділення атрибуту href
        links = set()
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href'].strip()
            if link.startswith('/'):
                link = url + link
            links.add(link)

        # Запис посилань у текстовий файл
        with open(output_file, 'w') as list_filtered:
            list_filtered.write('\n'.join(links))

        messagebox.showinfo('Успішно', 'Посилання успішно витягнуті та збережені у файлі!')
    except Exception as e:
        messagebox.showerror('Помилка', f'Виникла помилка: {str(e)}')


def on_search_button_click():
    url = entry_url.get()
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    extract_links_from_webpage(url, output_file)


# Створення основного вікна
root = tk.Tk()
root.title('Витягнення Посилань з Веб-Сторінки')

# Створення та розміщення елементів вікна
label_url = tk.Label(root, text='URL веб-сторінки:')
label_url.pack(pady=5)

entry_url = tk.Entry(root, width=40)
entry_url.pack(pady=5)

search_button = tk.Button(root, text='Пошук', command=on_search_button_click)
search_button.pack(pady=10)

# Запуск основного циклу обробки подій
root.mainloop()
