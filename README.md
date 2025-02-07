# Scrapy2

## 📌 Описание
Этот проект использует **Scrapy** для парсинга каталога осветительных приборов с сайта [divan.ru](https://www.divan.ru/category/svet). Сайт содержит информацию о светильниках, их ценах и ссылках, которые сохраняются в CSV файл.

## 🚀 Установка и запуск

### 1. Убедитесь, что у вас установлен Python  
- Проверьте версию Python:
  ```sh
  python --version
  ```
  Проект протестирован на Python 3.8+.

### 2. Клонируйте репозиторий
```sh
  git clone https://github.com/Alexandr-sys2024/Scrapy2.git
  cd Scrapy2
```

### 3. Установите зависимости
```sh
  pip install -r requirements.txt
```

### 4. Запустите Scrapy Spider
```sh
  scrapy crawl divannewpars
```

### 5. Получите результаты
После выполнения парсинга, данные будут сохранены в файл `divanpars/spiders/luminaires.csv`.

## 📂 Структура файлов
- `divanpars/spiders/divannewpars.py` – основной скрипт парсинга (Spider).
- `divanpars/spiders/luminaires.csv` – файл с результатами парсинга.
- `divanpars/settings.py` – настройки проекта Scrapy.
- `.gitignore` – список файлов, игнорируемых Git.
- `LICENSE` – информация о лицензии проекта.
- `scrapy.cfg` – конфигурация проекта Scrapy.

## 🔥 Рекомендации
- Убедитесь, что у вас есть доступ к интернету.
- Для предотвращения блокировки сайта рекомендуется установить задержку между запросами (настройка `DOWNLOAD_DELAY`).

## 📜 Лицензия
Этот проект распространяется по лицензии MIT. Подробнее см. в файле `LICENSE`.

## ✨ Автор
[Aleksandr-sys2024](https://github.com/Alexandr-sys2024)