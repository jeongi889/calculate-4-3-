# calculate-4-3-
# 공학용 계산기 코드 설명

## 1. 필요한 모듈 임포트
```python
import tkinter as tk
from tkinter import ttk
import math
```

## 2. Calculator 클래스 정의
```python
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
```

## 3. 위젯 생성 메서드
```python
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
```

## 4. 버튼 생성 및 배치
```python
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
```

## 5. 버튼 클릭 이벤트 처리
```python
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
```

## 6. 공학용 함수 처리
```python
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
```

## 7. 초기화 메서드
```python
def clear(self):
    self.result_var.set("0")
    self.current_operation = ""
```

## 8. 메인 실행 코드
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
```

## 주요 기능 설명

1. **기본 연산**
   - 사칙연산 (+, -, *, /)
   - 소수점 계산
   - 괄호 연산

2. **공학용 함수**
   - 삼각함수 (sin, cos, tan)
   - 로그 함수 (log, ln)
   - 제곱 및 제곱근 (x², √)
   - 역수 계산 (1/x)
   - 팩토리얼 (n!)
   - 상수 (π, e)

3. **메모리 기능**
   - M+: 메모리에 더하기
   - M-: 메모리에서 빼기
   - MR: 메모리 값 불러오기

4. **기타 기능**
   - 부호 변경 (±)
   - 초기화 (C)
   - 에러 처리
