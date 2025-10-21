# Overly Verbose GPA Calculator

A Python script that calculates your GPA, analyzes semester performance, and determines whether your goal GPA is achievable by improving only one grade.

---

## Features

- **Input Validation**
  - Ensures all grades are numeric values between `0.0` and `4.0`.
  - Rejects invalid inputs and prompts the user again until valid data is provided.
- **GPA Calculation**
  - Computes both the overall GPA and semester-specific GPAs.
- **Semester Analysis**
  - Allows users to select either the first or second half of their classes for focused GPA analysis.
  - Compares semester GPA against the overall GPA to show improvement or decline.
- **Goal GPA Check**
  - Lets the user set a goal GPA between `0.0` and `4.0`.
  - Tests whether that goal is achievable by improving just one grade to `4.0`.
  - Reports which class(es) could be raised to meet the goal.
  - Informs the user if the goal is already met or not achievable with a single grade change.

---

## Example Run

