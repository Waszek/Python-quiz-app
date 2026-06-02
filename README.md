# Quiz Application

A simple interactive quiz application built in Python that demonstrates Object-Oriented Programming (OOP) principles and JSON file handling.

## Project Overview

This quiz application prompts the user for personal information (name and age), then presents a series of multiple-choice questions loaded from a JSON file. The app tracks and displays the user's final score.

## Prerequisites

- Python 3.x
- No external dependencies (uses only Python standard library)

## Installation & Setup

### 1. Clone the Repository from GitHub

```bash
git clone https://github.com/Waszek/Python-quiz-app.git
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
```

Activate the virtual environment:

**On Windows (PowerShell):**

```bash
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```bash
.venv\Scripts\activate.bat
```

**On macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Run the Application

```bash
python demo.py
```

## How to Use

1. Enter your first name when prompted
2. Enter your age (must be a number)
3. Answer each quiz question by entering the corresponding letter (a, b, c, or d)
4. View your final score at the end

## Project Structure

```
firstProject/
├── demo.py           # Main application file
├── questions.json    # Quiz questions and answers
└── README.md         # This file
```

## Technical Implementation

### Object-Oriented Programming (OOP)

The application uses OOP through the `Question` class:

```python
class Question:
    def __init__(self, text, option, correct_answer):
        self.text = text
        self.option = option
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
```

**OOP Benefits Used:**

- **Encapsulation**: Question data (text, options, correct answer) is bundled within the class
- **Methods**: The `check_answer()` method encapsulates the logic for validating user responses
- **Reusability**: Creating multiple Question objects from JSON data without code duplication

### JSON File Handling

Questions are stored in `questions.json` in a structured format:

```json
{
  "question": "Question text",
  "options": {
    "a": "Option A",
    "b": "Option B",
    "c": "Option C",
    "d": "Option D"
  },
  "correct": "a"
}
```

**Why JSON?**

- Human-readable format for easy question management
- Easy to parse and load into Python using the `json` module
- Can be easily modified without changing code
- Scalable: Add or remove questions without touching the application logic

The app loads questions using:

```python
with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
```

## Features

- ✅ User input validation (age must be numeric)
- ✅ Dynamic question loading from JSON
- ✅ Score tracking
- ✅ Object-oriented architecture
- ✅ Multiple-choice quiz format

## License

This project is open source and available for educational purposes.
