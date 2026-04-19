import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Тест по Информатике 10 класс", page_icon="💻")

st.markdown("""

    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">

    <style>

    html, body, [class*="css"] {

        font-family: 'Montserrat', sans-serif;

    }

    .stApp {

        background-color: #f0f2f6;

    }

    .main-title {

        color: #1E3A8A;

        text-align: center;

        font-weight: 700;

    }

    .question-box {

        background-color: white;

        padding: 20px;

        border-radius: 10px;

        box-shadow: 0 4px 6px rgba(0,0,0,0.1);

        margin-bottom: 20px;

    }

    </style>

    """, unsafe_allow_html=True)

questions = [

    {"q": "1. Какая система счисления используется в ЭВМ?", "type": "radio",
     "options": ["Десятичная", "Двоичная", "Восьмеричная"], "a": "Двоичная"},

    {"q": "2. Чему равен 1 Мбайт?", "type": "radio", "options": ["1000 Кбайт", "1024 Кбайт", "1024 байт"],
     "a": "1024 Кбайт"},

    {"q": "3. Выберите языки программирования (несколько вариантов):", "type": "multiselect",
     "options": ["Python", "HTML", "C++", "HTTP"], "a": ["Python", "C++"]},

    {"q": "4. Как называется центральная часть компьютера?", "type": "text", "a": "процессор"},

    {"q": "5. Инверсия - это логическое...", "type": "radio", "options": ["Сложение", "Умножение", "Отрицание"],
     "a": "Отрицание"},

    {"q": "6. Какое расширение имеют исполняемые файлы в Windows?", "type": "text", "a": "exe"},

    {"q": "7. Выберите устройства ввода информации:", "type": "multiselect",
     "options": ["Монитор", "Клавиатура", "Мышь", "Принтер"], "a": ["Клавиатура", "Мышь"]},

    {"q": "8. Чему равно 10 в двоичной системе в десятичной?", "type": "radio", "options": ["2", "4", "8"], "a": "2"},

    {"q": "9. Алгоритм, вызывающий сам себя, называется...", "type": "text", "a": "рекурсия"},

    {"q": "10. Какой цикл в Python проверяет условие?", "type": "radio", "options": ["for", "while", "if"],
     "a": "while"},

    {"q": "11. Конъюнкция - это логическое...", "type": "radio", "options": ["И", "ИЛИ", "НЕ"], "a": "И"},

    {"q": "12. Минимальная единица измерения информации:", "type": "text", "a": "бит"},

    {"q": "13. Протокол передачи гипертекста:", "type": "radio", "options": ["FTP", "HTTP", "TCP"], "a": "HTTP"},

    {"q": "14. Выберите логические операции:", "type": "multiselect",
     "options": ["Дизъюнкция", "Интеграция", "Импликация"], "a": ["Дизъюнкция", "Импликация"]},

    {"q": "15. Скорость передачи данных измеряется в...", "type": "radio", "options": ["бит/с", "байт", "Герц"],
     "a": "бит/с"},

    {"q": "16. Как называется набор правил написания кода?", "type": "text", "a": "синтаксис"},

    {"q": "17. Программа для просмотра веб-страниц:", "type": "text", "a": "браузер"},

    {"q": "18. Дизъюнкция - это логическое...", "type": "radio", "options": ["И", "ИЛИ", "НЕ"], "a": "ИЛИ"}

]

st.markdown("<h1 class='main-title'>Итоговый тест по информатике</h1>", unsafe_allow_html=True)

st.sidebar.title("Описание")

st.sidebar.info("""

**Целевая аудитория:** Учащиеся 10-х классов.

**Возраст:** 15-17 лет.

**Тема:** Основы информатики и ИКТ.

""")

if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

user_answers = {}

for i, item in enumerate(questions):

    st.markdown(f"### Вопрос №{i + 1}")

    if item["type"] == "radio":

        user_answers[i] = st.radio(item["q"], item["options"], key=f"q{i}")

    elif item["type"] == "multiselect":

        user_answers[i] = st.multiselect(item["q"], item["options"], key=f"q{i}")

    elif item["type"] == "text":

        user_answers[i] = st.text_input(item["q"], key=f"q{i}").strip().lower()

if st.button("Завершить тест"):

    end_time = time.time()

    duration = int(end_time - st.session_state.start_time)

    score = 0

    results = []

    for i, item in enumerate(questions):

        correct = False

        u_ans = user_answers[i]

        if item["type"] == "multiselect":

            if sorted(u_ans) == sorted(item["a"]):
                correct = True

        else:

            if str(u_ans).lower() == str(item["a"]).lower():
                correct = True

        if correct:
            score += 1

        results.append({"q": item["q"], "correct_a": item["a"], "user_a": u_ans, "is_correct": correct})

    st.divider()

    st.balloons()

    st.header("Результаты теста")

    col1, col2, col3 = st.columns(3)

    col1.metric("Баллы", f"{score} / {len(questions)}")

    col2.metric("Точность", f"{int(score / len(questions) * 100)}%")

    col3.metric("Время", f"{duration} сек")

    st.subheader("Разбор ошибок:")

    for res in results:
        with st.expander(f"{res['q']} - {'✅ Правильно' if res['is_correct'] else '❌ Ошибка'}"):
            st.write(f"**Ваш ответ:** {res['user_a']}")

            st.write(f"**Правильный ответ:** {res['correct_a']}")



else:

    st.write(f"⏳ Тест идет. Прошло времени: {int(time.time() - st.session_state.start_time)} сек.")

