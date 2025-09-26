def create_zero_file_highlevel(filename, size_kb=1):
    """
    Высокоуровневое создание файла с нулями
    """
    size_bytes = size_kb * 1024

    with open(filename, 'w') as file:
        file.write('0' * size_bytes)

    print(f"Файл {filename} создан, размер: {size_kb} KB")


# Использование
create_zero_file_highlevel('zeros.txt')