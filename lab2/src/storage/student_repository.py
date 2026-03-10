from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List

from domain.student import Student


@dataclass(slots=True)
class StudentRepository:
    _students: List[Student] = field(default_factory=list)

    def replace_all(self, students: Iterable[Student]) -> None:
        self._students = list(students)

    def all(self) -> list[Student]:
        return list(self._students)

