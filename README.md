# paste-runner
Скрипт, який дозволяє приймати повідомлення з Telegram і автоматично публікувати їх у вигляді публічних паст на [Pastebin.com](https://pastebin.com).

## Вимоги

- Аккаунт на [pastebin.com](https://pastebin.com)
- Створений Telegram-бот через [@BotFather](https://t.me/BotFather)

## Встановлення

1. Склонуйте репозиторій або збережіть скрипт:

   ```bash
   git clone https://github.com/your-username/pasterunner-script.git
   cd pasterunner-script

2. Встановіть залежності
    ```bash
    pip install python-telegram-bot requests

3. Отримайте ключі:

- **Telegram Bot Token** — у [@BotFather](https://t.me/BotFather)
- **Pastebin Developer API Key** — з [https://pastebin.com/doc_api](https://pastebin.com/doc_api)
- **Pastebin User Key** — генерується через get_user_credentials.py

4. Впишіть ключі у скрипт `pasterunner.py`:

```python
API_DEV_KEY = 'your_pastebin_dev_key'
API_USER_KEY = 'your_pastebin_user_key'
TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'

5. Для запуску використовуйте main.py.
