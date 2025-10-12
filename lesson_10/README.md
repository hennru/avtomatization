# Lesson 10 — Allure + PageObject (русский)

## Описание
Проект содержит автотесты с использованием Page Object Pattern и Allure-отчётов:
- test_calculator.py — тест онлайн калькулятора (slow-calculator)
- test_saucedemo.py — тест интернет-магазина (saucedemo)

## Установка зависимостей
Рекомендуется использовать виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Запуск тестов и генерация Allure результатов
```bash
pytest -v --alluredir=allure-results
```

## Просмотр отчёта Allure
1. Установите Allure CLI (если ещё не установлен).
   - Mac (brew): `brew install allure`
   - Windows: скачайте бинарники с https://github.com/allure-framework/allure2/releases и добавьте в PATH
   - Linux: инструкции на официальном сайте Allure

2. Запустите просмотр отчёта:
```bash
allure serve allure-results
```
или
```bash
allure generate allure-results -o allure-report
allure open allure-report
```

## Примечания
- Проект запускает реальные браузеры через webdriver-manager (Chrome). Убедитесь, что у вас установлен Google Chrome.
- Папки `allure-results` и `allure-report` не должны попадать в репозиторий.
