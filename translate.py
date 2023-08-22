import openai
import tkinter as tk
from tkinter import ttk
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text():
    text = text_entry.get()
    language = language_entry.get()

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate '{text}' to {language}.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    translation = response.choices[0].text.strip()

    if translation:
        translated_text_label.configure(text=f"{translation}")
    else:
        translated_text_label.configure(text="Translation failed.")

root = tk.Tk()
root.title("Language Translator")

# Change the background color here
root.configure(background="#708090")

# Create style for widgets
style = ttk.Style()

# Change the foreground (text) and background color for entries here
style.configure("TEntry", foreground="black", background="black")

# Change the foreground (text) color for labels here, and background to match the root window
style.configure("TLabel", foreground="black", background="#708090")

text_label = ttk.Label(root, text="Enter the text to be translated:")
text_label.pack()
text_entry = ttk.Entry(root, width=50, style="TEntry")
text_entry.pack()

language_label = ttk.Label(root, text="Enter the language you want to translate to:")
language_label.pack()
language_entry = ttk.Entry(root, width=50, style="TEntry")
language_entry.pack()

translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

output_label = ttk.Label(root, text="Output:")
output_label.pack()

# Change the font here if desired
translation_label = ttk.Label(root, text="", wraplength=500, justify="left")
translation_label.pack()
translation_label.configure(font=("Arial", 12))

translated_text_label = ttk.Label(root, text="")
translated_text_label.pack()

pronunciation_label = ttk.Label(root, text="")
pronunciation_label.pack()

root.mainloop()
