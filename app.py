import pandas as pd

# URL
url = "https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html"
# Extraer todas las tablas que coincidan
# tables = pd.read_html(url, attrs={"id": "weather_records"})

# print(f"Número de tablas encontradas: {len(tables)}\n")

# Leer la tabla 1 HTML directamente con pandas
weather_records = pd.read_html(url, attrs={"id": "weather_records"})[0]
# Imprimir el DataFrame completo
print(weather_records)
