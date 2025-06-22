# 🛠 Django Backend — Інструкція для фронтендера

Цей проєкт — бекенд на Django/Django REST Framework. Ця інструкція допоможе тобі запустити його локально на своєму комп'ютері.

---

## ⚙️ Вимоги

- Python 3.10+ (рекомендовано)
- pip (менеджер пакетів Python)
- Git

---

## 🚀 Кроки для запуску

### 1. Клонуй репозиторій

```bash
    git clone https://github.com/metja/ApshaGranProject.git
    cd backend_app
```

### 2. Створи та активуй віртуальне середовище 
```bash
  - Windows:
        python -m venv venv
        venv\Scripts\activate
  
  - Linux/macOS:
      python3 -m venv venv
      source venv/bin/activate

```

### 3. Встанови всі залежності
```bash
    pip install -r requirements.txt
```
### 4. Створи базу даних та застосуй міграції

```bash
    python manage.py migrate
```
### 5. (Необов'язково)Створи суперкористувача
```bash
    python manage.py createsuperuser
```
### 6. Запусти сервер
```bash
   python manage.py runserver
```
### 7. Сервер буде доступний за адрусою
   http://127.0.0.1:8000/api/doc/swagger-ui/
