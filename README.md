# Compiler-Design

## LL(1) Grammar
FIRST Set Computation for Context-Free Grammar

This repository contains Python code to compute **FIRST sets** of a given context-free grammar. It is part of **Compiler Design**, aiding in parsing and syntax analysis, particularly for LL(1) parsers.

## 📋 Overview
The code calculates the **FIRST sets** for all non-terminals in the given grammar. It can handle nullable productions represented by epsilon (Ɛ).

## 🚀 Features
- Recursive calculation of FIRST sets.
- Supports epsilon (`Ɛ`) for nullable productions.
- Example grammar for arithmetic expressions.
- Handles terminal formatting with predefined terminal symbols.

🔧 Code Structure
- find_first: Computes the FIRST set recursively.
- compute_first: Calls find_first for all grammar symbols.
- print_first_sets: Prints the computed FIRST sets in a formatted way.

🤖 Example Grammar Execution:
- The predefined grammar models arithmetic expressions with operations like addition and multiplication, as well as parentheses for grouping.

