# Contributing to te-kyle-pandas

We welcome contributions to the te-kyle-pandas project! This document provides guidelines for contributing to the project.

## Table of Contents
1. [Getting Started](#getting-started)
2. [How to Contribute](#how-to-contribute)
3. [Pull Request Process](#pull-request-process)
4. [Coding Standards](#coding-standards)
5. [Testing](#testing)
6. [Documentation](#documentation)

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/te-kyle-pandas.git
   cd te-kyle-pandas
   ```
3. Set up the development environment as described in the README.md.
4. Create a new branch for your feature or bugfix:
   ```
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

1. Check the issue tracker for open issues that interest you.
2. If you have a new feature idea or notice a bug, open a new issue to discuss it before starting work.
3. Once you've identified an issue to work on, assign it to yourself and start working on your branch.

## Pull Request Process

1. Ensure your code adheres to the [Coding Standards](#coding-standards).
2. Update the documentation with details of changes to the interface, if applicable.
3. Add or update tests as necessary.
4. Ensure the test suite passes:
   ```
   pytest tests
   ```
5. Update the README.md as needed.
6. Commit your changes:
   ```
   git add .
   git commit -m "Your detailed commit message"
   ```
7. Push to your fork:
   ```
   git push origin feature/your-feature-name
   ```
8. Submit a pull request through the GitHub interface.

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style.
- Use meaningful variable and function names.
- Write docstrings for all functions, classes, and modules.
- Keep functions small and focused on a single task.
- Use type hints where possible.

## Testing

- Write unit tests for new functionality.
- Ensure all tests pass before submitting a pull request.
- Aim for high test coverage, especially for critical components.
- Run tests using:
  ```
  pytest tests
  ```

## Documentation

- Keep the README.md up to date.
- Document any new features or significant changes.
- Use inline comments to explain complex logic.
- Update docstrings for any modified functions or classes.

Thank you for contributing to the te-kyle-pandas project!
