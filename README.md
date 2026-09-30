# AUTOCRASH TEST

## Overview

AutoCrash Test is a beginner-level Python project that checks whether a vehicle can stop before an obstacle. If the vehicle cannot stop in time, the program estimates the speed at impact and provides a simple person-impact analysis.

## Main Functional Modules

1. **Vehicle & Brake Module** - collects vehicle speed, reaction time, obstacle distance and brake type.
2. **Stopping & Crash Analysis Module** - converts speed, calculates reaction/braking distance, stopping time and determines SAFE or CRASH.
3. **Person Impact Module** - collects person details and estimates kinetic energy and average impact force for a crash case.

Supporting modules provide validation and basic test cases.

## Python Concepts Used

- Variables and data types
- Input and output
- Type conversion
- Arithmetic operators
- `if`, `elif`, and `else`
- Nested decision-making
- `while` loops for basic validation
- Functions
- Modules and imports
- `math.sqrt()`
- `round()`

## Files

- `main.py` - controls the complete program workflow.
- `vehicle.py` - collects vehicle and brake information.
- `calculations.py` - contains stopping-distance and time calculations.
- `crash_analysis.py` - determines crash status and impact speed/category.
- `person_impact.py` - contains person input and impact calculations.
- `validation.py` - contains small validation helpers.
- `test_cases.py` - runs simple calculation/validation tests.
- `statement.md` - problem statement, scope, users and high-level features.

## How to Run

### 1. Open the project folder in VS Code

Open the `AutoCrash_Test` folder.

### 2. Open the VS Code terminal

Use **Terminal → New Terminal**.

### 3. Run the main project

```bash
python main.py
```

On some Windows setups, use:

```bash
py main.py
```

### 4. Run the automatic tests

```bash
python test_cases.py
```

Or on Windows:

```bash
py test_cases.py
```
