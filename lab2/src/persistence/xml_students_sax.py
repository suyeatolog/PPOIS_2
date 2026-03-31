from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional
from xml.sax import handler, make_parser
from xml.dom import minidom

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

    def startElement(self, name: str, attrs) -> None:  # noqa: N802
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


def write_students_to_xml(path: str, students: list[Student]) -> None:
    doc = minidom.Document()
    root = doc.createElement("students")
    doc.appendChild(root)

    for student in students:
        student_elem = doc.createElement("student")

        last_name_elem = doc.createElement("last_name")
        last_name_elem.appendChild(doc.createTextNode(student.last_name))
        student_elem.appendChild(last_name_elem)

        first_name_elem = doc.createElement("first_name")
        first_name_elem.appendChild(doc.createTextNode(student.first_name))
        student_elem.appendChild(first_name_elem)

        middle_name_elem = doc.createElement("middle_name")
        middle_name_elem.appendChild(doc.createTextNode(student.middle_name))
        student_elem.appendChild(middle_name_elem)

        group_elem = doc.createElement("group")
        group_elem.appendChild(doc.createTextNode(student.group))
        student_elem.appendChild(group_elem)

        for idx, semester_value in enumerate(student.social_work_by_semester, start=1):
            semester_elem = doc.createElement("semester")
            semester_elem.setAttribute("index", str(idx))
            semester_elem.appendChild(doc.createTextNode(str(semester_value)))
            student_elem.appendChild(semester_elem)

        root.appendChild(student_elem)

    with open(path, "w", encoding="utf-8") as f:
        doc.writexml(f, indent="  ", addindent="  ", newl="\n", encoding="utf-8")

