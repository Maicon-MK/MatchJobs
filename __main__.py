import tkinter as tk
from tkinter import messagebox
from src.interview import Interview
from src.data import Data

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("300x250")
        self.title("MatchJobs")
        self.configure(bg='white')
        self.name = None
        self.interview = None
        self.question_index = 0
        self.create_start_page()

    def create_start_page(self):
        self.start_frame = tk.Frame(self, bg='white')
        self.start_frame.pack(fill='both', expand=True)
        tk.Label(self.start_frame, text="MatchJobs", font=("Helvetica", 16), bg='white', fg='red').pack(pady=10)
        tk.Label(self.start_frame, text="Qual é o seu nome?", bg='white').pack()
        self.name_entry = tk.Entry(self.start_frame)
        self.name_entry.pack()
        tk.Button(self.start_frame, text="OK", command=self.start_interview, bg='red', fg='white').pack(pady=10)

    def start_interview(self):
        self.name = self.name_entry.get().capitalize().strip()
        if not self.name:
            messagebox.showinfo("Erro", "Por favor, insira o seu nome.")
            return

        self.interview = Interview(self.name)
        self.start_frame.pack_forget()
        self.qa_frame = tk.Frame(self, bg='white')
        self.qa_frame.pack(fill='both', expand=True)
        self.question_label = tk.Label(self.qa_frame, bg='white')
        self.question_label.pack()
        self.answer_var = tk.StringVar()

        for i, option in enumerate(self.interview.questions.valid_options):
            rb = tk.Radiobutton(self.qa_frame, text=option, variable=self.answer_var, value=option, bg='white')
            rb.pack(anchor='w')

        tk.Button(self.qa_frame, text="Próximo", command=self.next_question, bg='red', fg='white').pack(pady=10)
        self.display_question()

    def display_question(self):
        question_text = self.interview.questions.questions[self.question_index]
        options_text = "\n".join(f"{opt}. {desc}" for opt, desc in zip(
            self.interview.questions.valid_options,
            self.interview.questions.intense_options))
        self.question_label.config(text=f"{question_text}\n{options_text}")

    def next_question(self):
        answer = self.answer_var.get()
        if not answer:
            messagebox.showinfo("Erro", "Por favor, selecione uma opção.")
            return

        self.interview.utils.verification(answer)
        self.answer_var.set('')

        if (self.question_index + 1) < len(self.interview.questions.questions):
            self.question_index += 1
            self.display_question()
        else:
            results = self.interview.utils.results()
            Data().export(results)
            messagebox.showinfo("Sucesso", "A entrevista foi concluída com sucesso!")

app = Application()

if __name__ == "__main__":
    app.mainloop()
