# === Stage 1: Каркас модуля ===
# Project: SchoolTimetable
from dataclasses import dataclass, field


@dataclass
class Lesson:
    subject: str
    grade: str
    room: str
    teacher: str


def make_demo_lessons() -> list[Lesson]:
    return [
        Lesson(subject="Математика", grade="9А", room="305", teacher="Иванова М.С."),
        Lesson(subject="Физика", grade="9А", room="210", teacher="Петров А.В."),
        Lesson(subject="Литература", grade="9Б", room="118", teacher="Сидорова Е.И."),
    ]


def main() -> None:
    lessons = make_demo_lessons()
    for lesson in lessons:
        print(f"{lesson.subject} | {lesson.grade} | каб.{lesson.room} | {lesson.teacher}")


if __name__ == "__main__":
    main()
