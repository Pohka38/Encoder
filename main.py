import tkinter as tk  # Подключаем модуль Tkinter для GUI-интерфейса
from tkinter import ttk  # Дополнительные элементы управления Tkinter
import base64  # Модуль для работы с Base64 кодировкой
import hashlib  # Библиотека для хеширования (например, SHA-256)
import pyperclip  # Добавляем библиотеку для работы с буфером обмена

# Функция для преобразования текста в Base64
def b64_encode():
    """
    Кодирует введённую пользователем строку в формат Base64.
    """
    try:
        # Получаем содержимое текстового поля, очищаем лишние символы
        data = input_field.get("1.0", tk.END).strip()

        # Преобразуем строку в байтовый объект, кодируем её в Base64 и снова возвращаем в строку
        encoded_data = base64.b64encode(data.encode()).decode()

        # Обновляем текстовую метку результатом
        result_label.config(text=f'Base64 Encoded:\n{encoded_data}')

    except Exception as e:
        # Если возникла ошибка, показываем её в текстовом поле
        result_label.config(text=f'Error: {e}')


# Функция для обратного преобразования из Base64 в обычную строку
def b64_decode():
    """
    Декомпозирует строку из формата Base64 обратно в простой текст.
    """
    try:
        # Читаем значение из текстового поля
        data = input_field.get("1.0", tk.END).strip()

        # Расшифровка Base64 строки и преобразование обратно в строку
        decoded_data = base64.b64decode(data).decode()

        # Отображение результата
        result_label.config(text=f'Base64 Decoded:\n{decoded_data}')

    except Exception as e:
        # Если возникает ошибка, выводим её
        result_label.config(text=f'Error: {e}')


# Функция для вычисления SHA-256 хэша
def sha256_hash():
    """
    Рассчитывает SHA-256 хэш введённой строки.
    """
    # Чтение значения из текстового поля
    data = input_field.get("1.0", tk.END).strip()

    # Создание хэша строки с использованием алгоритма SHA-256
    hashed_data = hashlib.sha256(data.encode()).hexdigest()

    # Вывод результата
    result_label.config(text=f'SHA-256 Hash:\n{hashed_data}')

    # Копирование текста в буфер обмена
def copy_to_clipboard():
        """
        Копирует отображаемый результат в буфер обмена.
        """
        if result_label['text']:
            pyperclip.copy(result_label['text'])

# Основная настройка окна приложения
root = tk.Tk()  # Создаём основное окно Tkinter
root.title("Encryption & Hashing Tool")  # Устанавливаем заголовок окна
root.geometry('400x350')  # Определяем размер окна

# Элемент для ввода текста пользователем
input_field = tk.Text(root, height=5, width=40)
input_field.pack(pady=10)  # Размещаем элемент на экране с отступом внизу

# Кнопка для кодировки в Base64
b64_encode_button = tk.Button(
    root,
    text="Base64 Encode",  # Надпись на кнопке
    command=b64_encode  # Связанная функция
)
b64_encode_button.pack(pady=5)  # Размещение кнопки с отступом вверху и внизу

# Кнопка для декодирования из Base64
b64_decode_button = tk.Button(
    root,
    text="Base64 Decode",  # Надпись на кнопке
    command=b64_decode  # Связанная функция
)
b64_decode_button.pack(pady=5)  # Размещение кнопки с отступом вверху и внизу

# Кнопка для расчёта SHA-256 хэша
sha256_hash_button = tk.Button(
    root,
    text="SHA-256 Hash",  # Надпись на кнопке
    command=sha256_hash  # Связанная функция
)
sha256_hash_button.pack(pady=5)  # Размещение кнопки с отступом вверху и внизу


# Кнопка для копирования результата в буфер обмена
copy_button = tk.Button(
    root,
    text="Копировать результат",
    command=copy_to_clipboard
)
copy_button.pack(pady=5)

# Метка для вывода результата операций
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)  # Размещение метки с отступом внизу

# Главный цикл Tkinter для запуска окна
if __name__ == "__main__":
    root.mainloop()  # Запускаем основной цикл приложения