"""Functions for generating synthetic student records using NumPy."""
import numpy as np


def random_birth_date(start_year=2000, end_year=2006, rng=None):
    """Return a random valid Python date between start_year and end_year, inclusive."""
    from datetime import date

    rng = rng if rng is not None else np.random.default_rng()
    start = np.datetime64(f"{start_year}-01-01", "D")
    end = np.datetime64(f"{end_year + 1}-01-01", "D")
    days = int((end - start).astype(int))
    chosen = start + np.timedelta64(int(rng.integers(0, days)), "D")
    return date.fromisoformat(str(chosen))


def generate_student(student_id, rng=None):
    """Generate one student with a birth date, three grades, and grade average."""
    rng = rng if rng is not None else np.random.default_rng()
    birth_date = random_birth_date(rng=rng)
    grades = rng.integers(0, 21, size=3).tolist()
    return {
        "student_id": student_id,
        "birth_date": birth_date,
        "grade_1": int(grades[0]),
        "grade_2": int(grades[1]),
        "grade_3": int(grades[2]),
        "average_grade": round(float(np.mean(grades)), 2),
    }


def generate_students(count=10, seed=None):
    """Generate count students. Pass a seed to make results reproducible."""
    rng = np.random.default_rng(seed)
    return [generate_student(f"S{i:03d}", rng=rng) for i in range(1, count + 1)]
