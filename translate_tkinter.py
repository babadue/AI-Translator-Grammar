import torch
from transformers import MarianMTModel, MarianTokenizer, MarianConfig

class Translator:
    def __init__(self, model_en_to_cn_path, model_cn_to_en_path):
        self.model_en_to_cn = self.load_model(model_en_to_cn_path)
        self.model_cn_to_en = self.load_model(model_cn_to_en_path)
        self.tokenizer_en = MarianTokenizer.from_pretrained(model_en_to_cn_path)
        self.tokenizer_cn = MarianTokenizer.from_pretrained(model_cn_to_en_path)

    def load_model(self, model_path):
        config = MarianConfig.from_pretrained(model_path)
        model = MarianMTModel.from_pretrained(model_path, config=config)
        return model

    def translate_en_to_cn(self, text):
        return self.translate(text, self.model_en_to_cn, self.tokenizer_en)

    def translate_cn_to_en(self, text):
        return self.translate(text, self.model_cn_to_en, self.tokenizer_cn)

    def translate(self, text, model, tokenizer):
        text_to_translate = text
        input_ids = tokenizer.encode(text_to_translate, return_tensors="pt")

        with torch.no_grad():
            outputs = model.generate(input_ids)

        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        return translated_text



import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class WinFormsTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Translation App")
        master.geometry("500x400")  # Set initial window size

        # Add vertical gap
        ttk.Label(master, text="").pack()

        self.input_label = ttk.Label(master, text="Enter Text:")
        self.input_label.pack()

        # Increase the size, height, and font size of the input text box
        input_font = tkfont.Font(family="Helvetica", size=12)  # Adjust the family and size
        self.input_text = tk.Text(master, width=60, height=5, font=input_font)
        self.input_text.pack()

        # Add vertical gap
        ttk.Label(master, text="").pack()

        # Create a variable to track the current translation direction
        self.translation_direction = tk.StringVar(value="en_to_cn")

        # Create buttons for translation directions
        self.translate_button_en_to_cn = ttk.Button(master, text="English to Chinese", command=self.translate_en_to_cn)
        self.translate_button_en_to_cn.pack()

        self.translate_button_cn_to_en = ttk.Button(master, text="Chinese to English", command=self.translate_cn_to_en)
        self.translate_button_cn_to_en.pack()

        # Add vertical gap
        ttk.Label(master, text="").pack()
        # ttk.Label(master, text="").grid(row=4, column=0, columnspan=2)  # Use grid to specify row, column, and columnspan

        self.output_label = ttk.Label(master, text="Translation:")
        self.output_label.pack()

        # Increase the size, height, and font size of the output text box
        output_font = tkfont.Font(family="Helvetica", size=12)  # Adjust the family and size
        self.output_text = tk.Text(master, width=60, height=5, font=output_font, state="disabled")
        self.output_text.pack()

        # Specify the path to your local models
        self.model_en_to_cn_path = "C:/Users/userx/OneDrive/Desktop/AI/lab4/opus-mt-en-zh"
        self.model_cn_to_en_path = "C:/Users/userx/OneDrive/Desktop/AI/lab4/opus-mt-zh-en"
        self.translator = Translator(self.model_en_to_cn_path, self.model_cn_to_en_path)

    def translate_en_to_cn(self):
        self.translation_direction.set("en_to_cn")
        self.perform_translation()

    def translate_cn_to_en(self):
        self.translation_direction.set("cn_to_en")
        self.perform_translation()

    def perform_translation(self):
        input_text = self.input_text.get("1.0", tk.END).strip()  # Get text from the Text widget
        direction = self.translation_direction.get()

        if direction == "en_to_cn":
            output_text = self.translator.translate_en_to_cn(input_text)
        elif direction == "cn_to_en":
            output_text = self.translator.translate_cn_to_en(input_text)
        else:
            output_text = "Invalid translation direction"

        # Update the output Text widget
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output_text)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = WinFormsTranslatorApp(root)
    root.mainloop()
