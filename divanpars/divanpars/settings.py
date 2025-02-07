# Scrapy settings for divanpars project

BOT_NAME = "divanpars"

SPIDER_MODULES = ["divanpars.spiders"]
NEWSPIDER_MODULE = "divanpars.spiders"

ROBOTSTXT_OBEY = True

# Ограничиваем частоту запросов, чтобы избежать блокировки
DOWNLOAD_DELAY = 2  # 2 секунды задержки между запросами
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8

# Включаем логирование для отладки
LOG_LEVEL = 'INFO'

# Запрещаем редиректы
REDIRECT_ENABLED = False

# Кодировка для экспорта данных
FEED_EXPORT_ENCODING = "utf-8"

# Используем асинхронный реактор для работы Scrapy
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Fingerprint для Scrapy 2.7+
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"