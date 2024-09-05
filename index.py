import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

encoding_map = {
    'a': '~', 'b': '⍤', 'c': '⍤⍤', 'd': '⍤⍤⍤', 'e': '⍤⍤⍤⍤',
    'f': '⍤⍤⍤⍤⍤', 'g': '⍤⍤⍤⍤⍤⍤', 'h': '⍤⍤⍤⍤⍤⍤⍤', 'i': '⍤⍤⍤⍤⍤⍤⍤⍤',
    'j': '⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'k': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'l': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤',
    'm': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'n': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'o': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤',
    'p': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'q': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'r': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤',
    's': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 't': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'u': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤',
    'v': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'w': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'x': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤',
    'y': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 'z': '⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤⍤', 
    'A': '⨀', 'B': '⨁', 'C': '⨁⨁', 'D': '⨁⨁⨁', 'E': '⨁⨁⨁⨁',
    'F': '⨁⨁⨁⨁⨁', 'G': '⨁⨁⨁⨁⨁⨁', 'H': '⨁⨁⨁⨁⨁⨁⨁', 'I': '⨁⨁⨁⨁⨁⨁⨁⨁',
    'J': '⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'K': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'L': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁',
    'M': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'N': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'O': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁',
    'P': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'Q': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'R': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁',
    'S': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'T': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'U': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁',
    'V': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'W': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'X': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁',
    'Y': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 'Z': '⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁⨁', 
    '0': '◉', '1': '◉◉', '2': '◉◉◉', '3': '◉◉◉◉', '4': '◉◉◉◉◉',
    '5': '◉◉◉◉◉◉', '6': '◉◉◉◉◉◉◉', '7': '◉◉◉◉◉◉◉◉', '8': '◉◉◉◉◉◉◉◉◉', '9': '◉◉◉◉◉◉◉◉◉◉',
    '가': '♢', '나': '♢♢', '다': '♢♢♢', '라': '♢♢♢♢', '마': '♢♢♢♢♢',
    '바': '♢♢♢♢♢♢', '사': '♢♢♢♢♢♢♢', '아': '♢♢♢♢♢♢♢♢', '자': '♢♢♢♢♢♢♢♢♢', '차': '♢♢♢♢♢♢♢♢♢♢',
    '카': '♢♢♢♢♢♢♢♢♢♢♢', '타': '♢♢♢♢♢♢♢♢♢♢♢♢♢', '파': '♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢', '하': '♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢♢',
    
    # 한글 모음
    'ㅏ': '★', 'ㅐ': '★★', 'ㅑ': '★★★', 'ㅒ': '★★★★', 'ㅓ': '★★★★★',
    'ㅔ': '★★★★★★', 'ㅕ': '★★★★★★★', 'ㅖ': '★★★★★★★★', 'ㅗ': '★★★★★★★★★',
    'ㅘ': '★★★★★★★★★★', 'ㅙ': '★★★★★★★★★★★', 'ㅚ': '★★★★★★★★★★★★',
    'ㅛ': '★★★★★★★★★★★★★', 'ㅜ': '★★★★★★★★★★★★★★', 'ㅝ': '★★★★★★★★★★★★★★★',
    'ㅞ': '★★★★★★★★★★★★★★★★', 'ㅟ': '★★★★★★★★★★★★★★★★★', 'ㅠ': '★★★★★★★★★★★★★★★★★★',
    'ㅡ': '★★★★★★★★★★★★★★★★★★★', 'ㅢ': '★★★★★★★★★★★★★★★★★★★★', 'ㅣ': '★★★★★★★★★★★★★★★★★★★★★',
    
    # 한글 종성
    'ㄱ': '△', 'ㄲ': '△△', 'ㄳ': '△△△', 'ㄴ': '△△△△', 'ㄵ': '△△△△△',
    'ㄶ': '△△△△△△', 'ㄷ': '△△△△△△△', 'ㄸ': '△△△△△△△△', 'ㄹ': '△△△△△△△△△',
    'ㄺ': '△△△△△△△△△△', 'ㄻ': '△△△△△△△△△△△', 'ㄼ': '△△△△△△△△△△△△',
    'ㄽ': '△△△△△△△△△△△△△', 'ㄾ': '△△△△△△△△△△△△△△', 'ㄿ': '△△△△△△△△△△△△△△△',
    'ㅀ': '△△△△△△△△△△△△△△△△', 'ㅁ': '△△△△△△△△△△△△△△△△△', 'ㅂ': '△△△△△△△△△△△△△△△△△△',
    'ㅃ': '△△△△△△△△△△△△△△△△△△△', 'ㅄ': '△△△△△△△△△△△△△△△△△△△△', 'ㅅ': '△△△△△△△△△△△△△△△△△△△△△',
    'ㅆ': '△△△△△△△△△△△△△△△△△△△△△△', 'ㅇ': '△△△△△△△△△△△△△△△△△△△△△△△',
    'ㅈ': '△△△△△△△△△△△△△△△△△△△△△△△△', 'ㅉ': '△△△△△△△△△△△△△△△△△△△△△△△△△', 'ㅊ': '△△△△△△△△△△△△△△△△△△△△△△△△△△',
    'ㅋ': '△△△△△△△△△△△△△△△△△△△△△△△△△△△', 'ㅌ': '△△△△△△△△△△△△△△△△△△△△△△△△△△△△', 'ㅍ': '△△△△△△△△△△△△',
    '!': '!', '@': '@', '#': '#', '$': '$', '%': '%',
    '^': '^', '&': '&', '*': '*', '(': '(', ')': ')',
    '-': '-', '_': '_', '=': '=', '+': '+', '{': '{',
    '}': '}', '[': '[', ']': ']', '|': '|', '\\': '\\',
    ':': ':', ';': ';', '"': '"', '\'': '\'', '<': '<',
    '>': '>', ',': ',', '.': '.', '/': '/', '?': '?'
}

# 디코딩 매핑
decoding_map = {v: k for k, v in encoding_map.items()}



# 텍스트 인코딩 함수
def encode_text(text, encoding_map):
    encoded_str = ''
    for char in text:
        encoded_str += encoding_map.get(char, '') + '/'  # 매핑이 없으면 빈 문자열
    return encoded_str.strip('/')

# 텍스트 디코딩 함수
def decode_text(encoded_text, decoding_map):
    decoded_str = ''
    segments = encoded_text.split('/')
    for segment in segments:
        if segment:
            decoded_str += decoding_map.get(segment, '')  # 매핑이 없으면 빈 문자열
    return decoded_str

# 인코딩 버튼 클릭 시 호출되는 함수
def encode_button_click():
    input_str = input_text.get(1.0, tk.END).strip()  # 입력 텍스트 가져오기
    encoded_str = encode_text(input_str, encoding_map)  # 인코딩 수행
    output_text.delete(1.0, tk.END)  # 기존 출력 지우기
    output_text.insert(tk.END, encoded_str)  # 인코딩된 텍스트 삽입

# 디코딩 버튼 클릭 시 호출되는 함수
def decode_button_click():
    input_str = input_text.get(1.0, tk.END).strip()  # 입력 텍스트 가져오기
    decoded_str = decode_text(input_str, decoding_map)  # 디코딩 수행
    output_text.delete(1.0, tk.END)  # 기존 출력 지우기
    output_text.insert(tk.END, decoded_str)  # 디코딩된 텍스트 삽입

def load_file():
    """파일 불러오기 함수"""
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            input_text.delete(1.0, tk.END)  # 기존 텍스트 지우기
            input_text.insert(tk.END, file.read())  # 파일 내용 불러오기

def save_file():
    """파일 저장하기 함수"""
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(output_text.get(1.0, tk.END))  # 출력 텍스트 저장

# Tkinter 기본 설정
root = tk.Tk()
root.title("SMP(Secret Message Post) Version 0.01")


input_label = ttk.Label(root, text="입력 텍스트", font=("Helvetica", 12))
input_label.pack()

input_text = tk.Text(root, height=10, width=50, font=("Helvetica", 12))
input_text.pack()

encode_button = ttk.Button(root, text="인코딩", command=encode_button_click)
encode_button.pack(pady=10)  # 버튼 사이 간격 추가

decode_button = ttk.Button(root, text="디코딩", command=decode_button_click)
decode_button.pack(pady=10)  # 버튼 사이 간격 추가

# 불러오기 및 내보내기 버튼
load_button = ttk.Button(root, text="불러오기", command=load_file)
load_button.pack(pady=5)  # 버튼 사이 간격 추가

save_button = ttk.Button(root, text="내보내기", command=save_file)
save_button.pack(pady=5)  # 버튼 사이 간격 추가

output_label = ttk.Label(root, text="결과 텍스트", font=("Helvetica", 12))
output_label.pack()

output_text = tk.Text(root, height=10, width=50, font=("Helvetica", 12))
output_text.pack()

footer_label = ttk.Label(root, text="© 2024 TnznI_", font=("Helvetica", 10), anchor="center")
footer_label.pack(side="bottom", pady=10)  # 바닥에 배치

root.mainloop()
