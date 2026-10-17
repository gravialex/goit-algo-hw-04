import os
import shutil
import sys

def parse_args():
    """Функція для обробки аргументів командного рядка."""
    if len(sys.argv) < 2:
        print("Помилка-Не вказано вихідну директорію.")
        sys.exit(1)

    source = sys.argv[1]
    
    # Якщо другу теку не передали, то за замовчуванням 'dist'
    if len(sys.argv) >= 3:
        dest = sys.argv[2]
    else:
        dest = "dist"

    return source, dest


def copy_files_recursively(current_dir, dest_root):
  """Рекурсивна функція для читання папок і копіювання файлів."""
  
  print(f"Читаємо : {current_dir}")

  try:
    # Отримуємо список усіх файлів і папок у поточній директорії
    items = os.listdir(current_dir)
  except PermissionError:
    print(f"ПОМИЛКА-> Немає прав доступу до папки {current_dir}")
    return
  except Exception as e:
    print(f"ПОМИЛКА-> при читанні {current_dir}: {e}")
    return

  for item in items:
    item_path = os.path.join(current_dir, item)

    #  папка - викликаємо функцію рекурсивно
    if os.path.isdir(item_path):
      copy_files_recursively(item_path, dest_root)

    #  файл - копіюємо і сортуємо за розширенням
    elif os.path.isfile(item_path):
      try:
        file_ext = os.path.splitext(item)[1]
        
        if file_ext == "":
          ext_name = "no_extension"
        else:
          # Прибираємо крапку на початку
          ext_name = file_ext[1:].lower()

        # Створюємо шлях до нової папки для цього розширення
        target_folder = os.path.join(dest_root, ext_name)

        # Створюємо папку
        if not os.path.exists(target_folder):
          os.makedirs(target_folder)
          print(f"Створено нову папку: {target_folder}")

        # Rуди скопіюємо файл
        destination_file = os.path.join(target_folder, item)

        # Якщо файл з таким ім'ям вже є в папці - зміна ім'я
        if os.path.exists(destination_file):
          base_name, extension = os.path.splitext(item)
          parent_folder_name = os.path.basename(current_dir)
          new_file_name = f"{parent_folder_name}_{base_name}{extension}"
          destination_file = os.path.join(target_folder, new_file_name)

        # Копіюємо файл
        shutil.copyfile(item_path, destination_file)
        print(f"Скопійовано файл: {item_path} -> {destination_file}")

      except PermissionError:
        print(f"ПОМИЛКА-> Немає прав на копіювання файлу {item_path}")
      except Exception as e:
        print(f"ПОМИЛКА з файлом {item_path}: {e}")


def main():
  # Отримуємо шляхи від користувача
  source_dir, dest_dir = parse_args()

  # чи взагалі існує вихідна папка
  if not os.path.exists(source_dir):
    print(f"ПОМИЛКА-> Вихідна папка '{source_dir}' не існує!")
    sys.exit(1)

  print(f"Звідки копіюємо: {source_dir}")
  print(f"Куди сортуємо: {dest_dir}")

  copy_files_recursively(source_dir, dest_dir)

if __name__ == "__main__":
  main()