import tkinter as tk
from tkinter import scrolledtext

from transformers import T5ForConditionalGeneration, T5Tokenizer

class GrammarCorrectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Grammar Correction App")

        # Make the window 3x larger
        master.geometry("600x300")

        self.label = tk.Label(master, text="Enter text to correct grammar:", font=("Arial", 14))
        self.label.pack(pady=10)  # Added vertical spacing

        # Use scrolledtext for multiline input
        self.entry = scrolledtext.ScrolledText(master, width=50, height=5, font=("Arial", 12))
        self.entry.pack(pady=10)  # Added vertical spacing

        self.button = tk.Button(master, text="Correct Grammar", command=self.correct_grammar, font=("Arial", 14))
        self.button.pack(pady=10)  # Added vertical spacing

        # Use Text widget for multiline output
        self.result_text = tk.Text(master, wrap=tk.WORD, font=("Arial", 12), height=5, width=50)
        self.result_text.pack(pady=10)  # Added vertical spacing

        # Specify the local directory where you saved the model
        self.local_directory = "C:/Users/userx/OneDrive/Desktop/AI/lab4/t5_base_grammar_correction"

        # Load the locally stored model and tokenizer
        self.model = T5ForConditionalGeneration.from_pretrained(self.local_directory)
        self.tokenizer = T5Tokenizer.from_pretrained(self.local_directory)

    def correct_grammar(self):
        input_sentence = self.entry.get("1.0", tk.END).strip()  # Get the entire text from the scrolledtext widget

        # Tokenize and generate correction
        input_ids = self.tokenizer.encode("grammar correction: " + input_sentence, return_tensors="pt")
        output_ids = self.model.generate(input_ids, max_new_tokens=150)  # Adjust max_new_tokens as needed
        correction = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # Clear previous content and insert new content
        self.result_text.config(state=tk.NORMAL)  # Allow modification
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"{correction}")
        self.result_text.config(state=tk.DISABLED)  # Disable modification

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarCorrectionApp(root)
    root.mainloop()



