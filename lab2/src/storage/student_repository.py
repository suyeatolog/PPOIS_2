from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Optional

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
    
    def find_students(self, last_name: Optional[str] = None, group: Optional[str] = None, min_total_work: Optional[int] = None, max_total_work: Optional[int] = None) -> List[Student]:
        found_students = []
        for student in self._students:
            match_last_name = not last_name or last_name.lower() in student.last_name.lower()
            match_group = not group or student.group == group
            total_work = student.total_social_work
            match_min_work = min_total_work is None or total_work >= min_total_work
            match_max_work = max_total_work is None or total_work <= max_total_work

            if match_last_name and match_group and match_min_work and match_max_work:
                found_students.append(student)
        return found_students
    
    def remove_students(self, students_to_remove: List[Student]) -> int:
        count = 0
        for student in students_to_remove:
            if student in self._students:
                self._students.remove(student)
                count += 1
        return count
    
    def find_and_remove_students(self, **criteria) -> int:
        students_to_remove = self.find_students(**criteria)
        removed_count = self.remove_students(students_to_remove)
        return removed_count
