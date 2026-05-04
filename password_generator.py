import random
import string
import json

def generate_password(length, digits=True, letters=True, special=True):
    if length < 8 or length > 20:
        raise ValueError("Длина пароля должна быть от 8 до 20 символов.")
    
    chars = ''
    if digits:
        chars += string.digits
    if letters:
        chars += string.ascii_letters
    if special:
        chars += string.punctuation

    if not chars:
        raise ValueError("Не выбран ни один тип символов.")
    
    return ''.join(random.choices(chars, k=length))

def add_to_history(password):
    history = load_history()
    history.append(password)
    save_history(history)

def load_history():
    try:
        with open('history.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_history(history):
    with open('history.json', 'w') as f:
        json.dump(history, f, indent=2)
