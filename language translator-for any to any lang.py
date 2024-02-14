from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
from tkinter import filedialog
import codecs

# create a translator object
translator = Translator()


def translate_text():
    # get the input text from the user
    input_text = input_textbox.get("1.0", END)

    # get the source and target language codes
    source_lang = source_language_combobox.get()
    target_lang = target_language_combobox.get()

    # translate the input text using the Google Translate API
    translated_text = translator.translate(input_text, src=source_lang, dest=target_lang).text

    # display the translated text
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", translated_text)


def openFile():
    tf = filedialog.askopenfilename(
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    if tf:  # Check if a file was selected
        try:
            with codecs.open(tf, 'r', encoding='utf-8') as file:
                data = file.read()
                input_textbox.delete("1.0", "end")
                input_textbox.insert("1.0", data)
        except UnicodeDecodeError:
            # Handle the case where the file is not UTF-8 encoded
            messagebox.showerror("Error", "Failed to decode the file as UTF-8")


def clear():
    input_textbox.delete("1.0", "end")
    output_textbox.delete("1.0", "end")


# create the main window
window = Tk()
window.title("CS-FCITR Language Translator (From any language to other language)")
window.resizable(False, False)
window.iconbitmap('language_translator.ico')

# Labels for Input and Output Text
input_label = Label(window, text="Input Text:")
input_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

output_label = Label(window, text="Output Text:")
output_label.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="w")

# Input Box and Output Box
input_textbox = Text(window, width=35, height=10)
input_textbox.grid(row=1, column=0, padx=10, pady=(0, 10))

output_textbox = Text(window, width=35, height=10)
output_textbox.grid(row=1, column=2, padx=10, pady=(0, 10))

# Translate Button
translate_button = Button(window, text="Translate", command=translate_text)
translate_button.grid(row=1, column=1, padx=10, pady=10)

# Source Language and Target Language Labels and Comboboxes
source_language_label = Label(window, text="Source Language:")
source_language_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
source_language_combobox = ttk.Combobox(window, values=["en", "ur", "ja", "ar", "fr", "es", "de", "zh-TW", "zh-CN", "hi", "ru", "ko"], state="readonly")
source_language_combobox.current(0)
source_language_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")

target_language_label = Label(window, text="Target Language:")
target_language_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
target_language_combobox = ttk.Combobox(window, values=["en", "ur", "ja", "ar", "fr", "es", "de", "zh-TW", "zh-CN", "hi", "ru", "ko"], state="readonly")
target_language_combobox.current(0)
target_language_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Open File and Clear Buttons
button_frame = Frame(window)
button_frame.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

open_file_button = Button(button_frame, text="Open File", command=openFile)
open_file_button.pack(side=LEFT, padx=5)

clear_button = Button(button_frame, text="Clear", command=clear, fg="black")
clear_button.pack(side=LEFT, padx=5)

exit_button = Button(button_frame, text="Exit", command=window.destroy, fg="black")
exit_button.pack(side=LEFT, padx=5)

# run the main event loop
window.mainloop()