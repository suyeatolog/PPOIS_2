from __future__ import annotations

from typing import List
from xml.dom import minidom

from domain.student import Student


def write_students_to_xml(path: str, students: List[Student]) -> None:
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