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
    
    def add(self, student: Student) -> None:
        self._students.append(student)
    
    def get_unique_groups(self) -> List:
        unique_groups_set = set()
        for student in self._students:
            unique_groups_set.add(student.group)
        return sorted(unique_groups_set)
