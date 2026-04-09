from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
from xml.sax import handler, make_parser

from domain.student import Student


@dataclass(slots=True)
class _StudentDraft:
    last_name: str = ""
    first_name: str = ""
    middle_name: str = ""
    group: str = ""
    semesters: List[Optional[int]] = None

    def __post_init__(self) -> None:
        if self.semesters is None:
            self.semesters = [None] * 10


class _StudentsHandler(handler.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.students: list[Student] = []
        self._current: Optional[_StudentDraft] = None
        self._current_tag: Optional[str] = None
        self._char_buffer: list[str] = []
        self._current_semester_index: Optional[int] = None

    def startElement(self, name: str, attrs) -> None:
        self._current_tag = name
        self._char_buffer.clear()

        if name == "student":
            self._current = _StudentDraft()
        elif name == "semester":
            idx_raw = attrs.get("index")
            try:
                idx = int(idx_raw)
            except (TypeError, ValueError):
                idx = 0
            self._current_semester_index = idx

    def characters(self, content: str) -> None:
        if self._current_tag is None:
            return
        self._char_buffer.append(content)

    def endElement(self, name: str) -> None:
        text = "".join(self._char_buffer).strip()

        if self._current is not None:
            if name == "last_name":
                self._current.last_name = text
            elif name == "first_name":
                self._current.first_name = text
            elif name == "middle_name":
                self._current.middle_name = text
            elif name == "group":
                self._current.group = text
            elif name == "semester":
                if (
                    self._current_semester_index is not None
                    and 1 <= self._current_semester_index <= 10
                ):
                    try:
                        value = int(text)
                    except ValueError:
                        value = 0
                    self._current.semesters[self._current_semester_index - 1] = value
                self._current_semester_index = None
            elif name == "student":
                semesters = [v if v is not None else 0 for v in self._current.semesters]
                self.students.append(
                    Student(
                        last_name=self._current.last_name,
                        first_name=self._current.first_name,
                        middle_name=self._current.middle_name,
                        group=self._current.group,
                        social_work_by_semester=semesters,
                    )
                )
                self._current = None

        self._current_tag = None
        self._char_buffer.clear()


def read_students_from_xml(path: str) -> list[Student]:
    parser = make_parser()
    h = _StudentsHandler()
    parser.setContentHandler(h)
    parser.parse(path)
    return h.students