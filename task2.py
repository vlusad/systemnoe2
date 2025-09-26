import os


def create_zero_file_compact():
    """Компактная версия с основными проверками"""

    # Получаем входные данные
    path = input("Путь для сохранения (Enter - здесь): ").strip() or "."
    name = input("Имя файла (Enter - zeros.bin): ").strip() or "zeros.bin"

    try:
        size_mb = int(input("Размер в MB (Enter - 10): ").strip() or "10")
    except ValueError:
        print("❌ Ошибка: введите число")
        return

    # Создаем папку если нужно
    os.makedirs(path, exist_ok=True)

    full_path = os.path.join(path, name)

    # Создаем файл
    try:
        print(f"Создаю файл {size_mb}MB...")
        with open(full_path, 'wb') as f:
            f.write(b'\x00' * (size_mb * 1024 * 1024))  # Бинарные нули

        print(f"✅ Готово: {full_path}")

    except Exception as e:
        print(f"❌ Ошибка создания: {e}")


# Запуск
create_zero_file_compact()