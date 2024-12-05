---
title: Installing PyFly
description: Learn how to install and set up PyFly on your system
---

# Installation Guide

PyFly is a Python-based interpreter, so you'll need Python installed on your system to use it. Follow these steps to get started with PyFly.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pyfly.git
cd pyfly
```

### 2. Set Up a Virtual Environment (Recommended)

It's recommended to use a virtual environment to avoid conflicts with other Python packages:

```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

PyFly has minimal dependencies, all of which are included in the Python standard library. No additional packages are required.

### 4. Verify Installation

To verify that PyFly is working correctly, you can run the test suite:

```bash
python -m unittest lexer_test.py
```

If all tests pass, you're ready to start using PyFly!

## Project Structure

After installation, you'll find the following key files in your project directory:

```
pyfly/
├── lexer.py         # Lexical analyzer
├── parser.py        # Parser implementation
├── ast1.py          # Abstract Syntax Tree definitions
└── lexer_test.py    # Test suite
```

## Next Steps

Now that you have PyFly installed, you can:

1. Follow the [Quick Start](/getting-started/quick-start/) guide to write your first PyFly program
2. Read the [Language Guide](/language-guide/syntax-overview/) to learn about PyFly's syntax
3. Explore the [API Reference](/api-reference/lexer/) for detailed documentation

## Troubleshooting

If you encounter any issues during installation:

1. Make sure you have the correct Python version installed
2. Check that your virtual environment is activated
3. Verify that all files are in the correct directory structure

For more help, please check the project's GitHub repository or open an issue. 