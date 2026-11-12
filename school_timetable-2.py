# === Stage 2: Проверка полей ===
# Project: SchoolTimetable
from typing import List, Optional


def normalize_subject(value: str) -> str:
    text = value.strip().lower()
    replacements = {
        "математика": "математика",
        "мат": "математика",
        "алгебра": "математика",
        "геометрия": "математика",
        "русский язык": "русский язык",
        "русский": "русский язык",
        "литература": "русский язык",
        "английский": "английский язык",
        "физика": "физика",
        "химия": "химия",
        "биология": "биология",
        "информатика": "информатика",
        "история": "история",
        "география": "география",
        "физкультура": "физкультура",
        "физ-ра": "физкультура",
        "окружающий мир": "окружающий мир",
        "окружающие": "окружающий мир",
    }
    return replacements.get(text, text)


def normalize_class(value: str) -> str:
    text = value.strip().lower()
    if not text:
        raise ValueError("Класс не может быть пустым")
    digits = "".join(ch for ch in text if ch.isdigit())
    if not digits:
        raise ValueError("В классе должна быть указана цифра, например 5а или 11б")
    letters = "".join(ch for ch in text if ch.isalpha())
    if not letters:
        raise ValueError("Укажи букву класса, например 5а или 11б")
    if len(text) > 2:
        raise ValueError("Формат класса: цифра и одна буква, например 5а")
    return digits + letters


def normalize_room(value: str) -> str:
    text = value.strip()
    if not text:
        raise ValueError("Кабинет не может быть пустым")
    if not (text.isdigit() or text.replace("-", "").replace("/", "").isdigit()):
        raise ValueError("Кабинет должен быть номером, например 101 или 205")
    return text


def normalize_teacher(value: str) -> str:
    text = value.strip()
    if not text:
        raise ValueError("Учитель не может быть пустым")
    return text


def validate_lesson(
    subject: Optional[str],
    klass: Optional[str],
    room: Optional[str],
    teacher: Optional[str],
) -> dict:
    if subject is None or subject == "":
        raise ValueError("Предмет обязателен")
    if klass is None or klass == "":
        raise ValueError("Класс обязателен")
    if room is None or room == "":
        raise ValueError("Кабинет обязателен")
    if teacher is None or teacher == "":
        raise ValueError("Учитель обязателен")

    normalized_subject = normalize_subject(subject)
    normalized_klass = normalize_class(klass)
    normalized_room = normalize_room(room)
    normalized_teacher = normalize_teacher(teacher)

    return {
        "subject": normalized_subject,
        "klass": normalized_klass,
        "room": normalized_room,
        "teacher": normalized_teacher,
    }
