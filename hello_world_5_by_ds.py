import os

# 1. Создаём папку 'test'
if not os.path.exists('test'):
    os.mkdir('test')

# 2. Создаём в ней файл
file_path = os.path.join('test', 'sample.txt')
with open(file_path, 'w') as f:
    f.write("Hello OS module!")

# 3. Проверяем размер
print(f"File size: {os.path.getsize(file_path)} bytes")
print(f"Full path: {os.path.abspath(file_path)}")