import json
from django.core.serializers import deserialize
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

file_path = 'backup_pretty.json'
with open(file_path, 'r') as file:
    json_data = file.read()

objects = deserialize('json', json_data)

for obj in objects:
    try:
        obj.save()
    except Exception as e:
        print(f"Помилка при збереженні об'єкта {obj.object}: {e}")


print("Дані успішно відновлено з файлу.")
