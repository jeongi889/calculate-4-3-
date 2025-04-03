import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # 결과 표시창
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # 현재 입력 상태
        self.current_operation = ""
        self.memory = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        # 결과 표시 레이블
        result_label = ttk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Arial", 20),
            anchor="e",
            padding=10
        )
        result_label.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
        
        # 기본 버튼 텍스트
        basic_buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'M+',
            '1', '2', '3', '-', 'M-',
            '0', '.', '=', '+', 'MR'
        ]
        
        # 공학용 버튼 텍스트
        scientific_buttons = [
            'sin', 'cos', 'tan', 'log', 'ln',
            'x²', '√', '1/x', 'π', 'e',
            '(', ')', 'x^y', 'n!', '±'
        ]
        
        # 공학용 버튼 생성
        row = 1
        col = 0
        for button_text in scientific_buttons:
            button = ttk.Button(
                self.root,
                text=button_text,
                command=lambda x=button_text: self.scientific_click(x)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # 기본 버튼 생성
        for button_text in basic_buttons:
            button = ttk.Button(
                self.root,
                text=button_text,
                command=lambda x=button_text: self.button_click(x)
            )
            button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1
        
        # 그리드 가중치 설정
        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        current = self.result_var.get()
        
        if value == '=':
            try:
                result = eval(current)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif value == 'C':
            self.clear()
        elif value == 'M+':
            self.memory += float(current)
        elif value == 'M-':
            self.memory -= float(current)
        elif value == 'MR':
            self.result_var.set(str(self.memory))
        else:
            if current == "0" or current == "Error":
                self.result_var.set(value)
            else:
                self.result_var.set(current + value)
    
    def scientific_click(self, value):
        current = self.result_var.get()
        try:
            if value == 'sin':
                result = math.sin(math.radians(float(current)))
            elif value == 'cos':
                result = math.cos(math.radians(float(current)))
            elif value == 'tan':
                result = math.tan(math.radians(float(current)))
            elif value == 'log':
                result = math.log10(float(current))
            elif value == 'ln':
                result = math.log(float(current))
            elif value == 'x²':
                result = float(current) ** 2
            elif value == '√':
                result = math.sqrt(float(current))
            elif value == '1/x':
                result = 1 / float(current)
            elif value == 'π':
                result = math.pi
            elif value == 'e':
                result = math.e
            elif value == 'x^y':
                self.current_operation = '^'
                return
            elif value == 'n!':
                result = math.factorial(int(float(current)))
            elif value == '±':
                result = -float(current)
            elif value in ['(', ')']:
                self.result_var.set(current + value)
                return
            
            self.result_var.set(str(result))
        except:
            self.result_var.set("Error")
    
    def clear(self):
        self.result_var.set("0")
        self.current_operation = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop() 