from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    last_name: str
    first_name: str
    middle_name: str
    group: str
    social_work_by_semester: List[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.social_work_by_semester:
            self.social_work_by_semester = [0] * 10
        elif len(self.social_work_by_semester) != 10:
            raise ValueError(
                "social_work_by_semester must contain exactly 10 items"
            )

    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()

    @property
    def total_social_work(self) -> int:
        return sum(self.social_work_by_semester)

    def to_table_row(self) -> list[str]:
        return [
            self.full_name,
            self.group,
            *[str(value) for value in self.social_work_by_semester],
        ]

