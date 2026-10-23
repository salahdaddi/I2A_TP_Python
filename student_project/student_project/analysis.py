"""Functions for calculating student ages and class statistics using NumPy and pandas."""
from datetime import date
import numpy as np
import pandas as pd


def calculate_age(birth_date, reference_date=None):
    """Calculate age in whole years on reference_date (today by default)."""
    reference_date = reference_date or date.today()
    age = reference_date.year - birth_date.year
    if (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def add_ages(students, reference_date=None):
    """Add an age field to each student record and return the records."""
    for student in students:
        student["age"] = calculate_age(student["birth_date"], reference_date)
    return students


def analyze_class(students):
    """Summarize average grades and ages using NumPy and pandas."""
    if not students:
        raise ValueError("At least one student is required for analysis.")

    df = pd.DataFrame(students)
    averages = df["average_grade"].to_numpy(dtype=float)
    ages = df["age"].to_numpy(dtype=float)

    return {
        "mean_average_grade": float(np.mean(averages)),
        "median_average_grade": float(np.median(averages)),
        "standard_deviation": float(np.std(averages, ddof=0)),
        "minimum_average_grade": float(np.min(averages)),
        "maximum_average_grade": float(np.max(averages)),
        "mean_age": float(df["age"].mean()),
    }


def format_report(students, stats, reference_date=None):
    """Build a readable text report for the generated class."""
    reference_date = reference_date or date.today()
    lines = [
        "STUDENT CLASS STATISTICAL REPORT",
        "=" * 34,
        f"Report date: {reference_date.isoformat()}",
        f"Number of students: {len(students)}",
        "",
        "Class statistics",
        "-" * 16,
        f"Mean of student grade averages: {stats['mean_average_grade']:.2f}",
        f"Median of student grade averages: {stats['median_average_grade']:.2f}",
        f"Population standard deviation of grade averages: {stats['standard_deviation']:.2f}",
        f"Minimum student grade average: {stats['minimum_average_grade']:.2f}",
        f"Maximum student grade average: {stats['maximum_average_grade']:.2f}",
        f"Mean age: {stats['mean_age']:.2f} years",
        "",
        "Student records",
        "-" * 15,
    ]
    for student in students:
        lines.append(
            f"{student['student_id']} | Birth date: {student['birth_date'].isoformat()} "
            f"| Age: {student['age']} | Grades: "
            f"{student['grade_1']}, {student['grade_2']}, {student['grade_3']} "
            f"| Average: {student['average_grade']:.2f}"
        )
    return "\n".join(lines) + "\n"
