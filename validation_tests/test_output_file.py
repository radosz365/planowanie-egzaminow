import pytest
import pandas as pd

schedule_file = "datasets/schedule1000.csv"


def load_schedule():
    """Load the schedule CSV into a Pandas DataFrame."""
    return pd.read_csv(schedule_file)


def test_no_lecturer_conflicts():
    """Ensure no lecturer has two exams in the same time slot."""
    data = load_schedule()
    conflicts = data.groupby(["datetime", "lecturer"]).size()
    assert all(
        conflicts <= 1
    ), "A lecturer has more than one exam in the same time slot."


def test_no_classroom_conflicts():
    """Ensure no classroom has two exams in the same time slot."""
    data = load_schedule()
    conflicts = data.groupby(["datetime", "classroom"]).size()
    assert all(
        conflicts <= 1
    ), "A classroom has more than one exam in the same time slot."


def test_no_group_conflicts_same_slot():
    """Ensure no group has two exams in the same time slot."""
    data = load_schedule()
    conflicts = data.groupby(["datetime", "group"]).size()
    assert all(conflicts <= 1), "A group has more than one exam in the same time slot."


def test_no_group_multiple_exams_per_day():
    """Ensure no group has more than one exam on the same day."""
    data = load_schedule()
    data["date"] = data["datetime"].str.split(" ").str[0]
    conflicts = data.groupby(["date", "group"]).size()
    assert all(conflicts <= 1), "A group has more than one exam on the same day."


def test_no_exams_on_weekends():
    """Ensure no exams are scheduled on weekends."""
    data = load_schedule()
    data["date"] = pd.to_datetime(data["datetime"].str.split(" ").str[0])
    weekends = data["date"].dt.weekday >= 5
    assert not any(weekends), "An exam is scheduled on a weekend."


if __name__ == "__main__":
    pytest.main()
