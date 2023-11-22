from django.core.serializers import serialize
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()

from product.models import Product

# Вибір усіх об'єктів з моделі
data = Product.objects.all()

# Серіалізація даних
serialized_data = serialize('json', data)

# Форматування JSON
pretty_json = json.dumps(json.loads(serialized_data), indent=4)

# Запис у файл
file_path = 'backup_pretty.json'
with open(file_path, 'w') as file:
    file.write(pretty_json)

print(f"Дані збережено у файлі {file_path}")
