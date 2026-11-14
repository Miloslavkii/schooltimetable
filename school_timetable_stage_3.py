# === Stage 3: Хранилище в памяти ===
# Project: SchoolTimetable
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Lesson:
    subject: str
    classroom: str
    teacher: str
    _id: Optional[str] = None

    def __post_init__(self):
        if self._id is None:
            self._id = str(len(self._id_counter) + 1)

    @property
    def id(self) -> str:
        return self._id

    def update(self, subject=None, classroom=None, teacher=None):
        if subject is not None:
            self.subject = subject
        if classroom is not None:
            self.classroom = classroom
        if teacher is not None:
            self.teacher = teacher
        return self


_id_counter = 0


class LessonStore:
    def __init__(self):
        self._lessons: Dict[str, Lesson] = {}
        global _id_counter
        _id_counter = 0

    def add(self, lesson: Lesson) -> Lesson:
        if lesson._id is None:
            lesson._id = str(len(self._lessons) + 1)
        self._lessons[lesson._id] = lesson
        return lesson

    def get(self, lesson_id: str) -> Optional[Lesson]:
        return self._lessons.get(lesson_id)

    def list(self) -> List[Lesson]:
        return list(self._lessons.values())

    def update(self, lesson_id: str, **kwargs) -> Optional[Lesson]:
        lesson = self.get(lesson_id)
        if lesson is None:
            return None
        lesson.update(**kwargs)
        return lesson

    def remove(self, lesson_id: str) -> bool:
        return self._lessons.pop(lesson_id, None) is not None
