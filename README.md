# Quick-Calc: A Simple Calculator with Comprehensive Testing

## Project Description

Quick-Calc is a simple calculator application that performs basic arithmetic operations including addition, subtraction, multiplication, and division. The application is designed with a focus on code quality and comprehensive testing, demonstrating professional software testing practices including unit tests, integration tests, and edge case handling. The calculator gracefully handles error conditions such as division by zero and provides a user-friendly interaction model with support for decimal inputs and chained operations.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/swe-testing-assignment.git
cd swe-testing-assignment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run the Application

To use the calculator programmatically:

```python
from src.calculator import Calculator

calc = Calculator()
calc.input_digit("5")
calc.set_operation("+")
calc.input_digit("3")
result = calc.calculate()
print(calc.get_display())  # Output: 8
```

## How to Run Tests

### Run all tests:
```bash
python3 -m pytest tests/ -v
```

### Run only unit tests:
```bash
python3 -m pytest tests/test_unit.py -v
```

### Run only integration tests:
```bash
python3 -m pytest tests/test_integration.py -v
```

### Run tests with coverage report:
```bash
python3 -m pytest tests/ --cov=src --cov-report=html
```

### Test Summary

The test suite includes:
- **Unit Tests**: 19 tests covering all four arithmetic operations, edge cases, and clear functionality
- **Integration Tests**: 5 tests verifying end-to-end calculator workflows
- **Total**: 24 tests, all passing

## Testing Framework Research

### Pytest vs Unittest: A Comparative Analysis

#### Pytest

**Pros:**
- **Simpler syntax**: Tests are written as simple functions with assertions, reducing boilerplate code
- **Fixtures**: Built-in fixture system provides powerful setup and teardown mechanisms for test data and state management
- **Plugins**: Extensive plugin ecosystem (pytest-cov, pytest-xdist, pytest-mock) extends functionality
- **Output quality**: Detailed, readable test output with colored diff displays and assertion introspection
- **Parametrization**: @pytest.mark.parametrize allows testing multiple scenarios with minimal code duplication
- **Better assertion messages**: Pytest rewrites assertions at runtime to provide more informative failure messages

**Cons:**
- Less familiar to developers coming from Java/C# backgrounds
- Documentation is less centralized than xUnit frameworks
- Smaller corporate backing compared to some alternatives

#### Unittest

**Pros:**
- **Standard library**: Part of Python stdlib, no external dependencies required
- **Familiarity**: Follows xUnit pattern, familiar to many developers from other languages
- **Enterprise adoption**: Common in larger organizations with existing test infrastructure
- **Mature**: Well-established with stable API

**Cons:**
- **Verbose**: Requires test classes inheriting from TestCase, more boilerplate code
- **Limited introspection**: Less detailed failure messages compared to pytest
- **Setup/teardown**: Less elegant than pytest's fixture system
- **No parametrization**: Running tests with multiple datasets requires nested loops or helper functions
- **Slower feedback**: Less powerful output and debugging capabilities

### Framework Choice Justification

**We chose Pytest** for this project because:

1. **Development velocity**: The simpler syntax and less boilerplate code allows faster test development and modification
2. **Test maintenance**: Clear, readable test code is easier to maintain and understand for team members
3. **Fixture system**: Better suited for managing test state and dependencies in a calculator application
4. **Professional output**: Pytest's detailed failure messages aid in debugging when tests fail
5. **Industry adoption**: Increasingly preferred in modern Python projects and data science communities
6. **Extensibility**: Easy to add coverage reporting and other advanced testing features through plugins

For this assignment, pytest's clean syntax and powerful features provide better test organization and clarity while maintaining ease of use.

## Project Structure

```
swe-testing-assignment/
├── src/
│   ├── __init__.py
│   └── calculator.py          # Core calculator logic
├── tests/
│   ├── __init__.py
│   ├── test_unit.py           # Unit tests (19 tests)
│   └── test_integration.py    # Integration tests (5 tests)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── TESTING.md                  # Testing strategy documentation
└── .gitignore                  # Git ignore patterns
```

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply two numbers
- **Division**: Divide two numbers with zero-division protection
- **Clear (C)**: Reset calculator to initial state
- **Decimal Support**: Handle decimal number inputs
- **Chained Operations**: Support multiple operations in sequence (e.g., 2 * 3 + 4 = 10)
- **Error Handling**: Graceful handling of invalid operations

## Version

- **Current Version**: 1.0.0
- **Release Date**: March 5, 2026

## License

This project is provided for educational purposes.