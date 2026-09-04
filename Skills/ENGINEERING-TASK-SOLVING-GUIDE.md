# Engineering Task Solving Guide

## Purpose

This guide defines a general method for solving engineering tasks that must
comply with construction codes, standards, specifications, or other regulatory
documents.

## Method

### 1. Extract the task objects

Identify all objects, systems, subsystems, operating conditions, environmental
conditions, controlled parameters, and constraints explicitly or implicitly
present in the engineering task.

### 2. Map objects to regulatory requirements

For every identified object, search the applicable construction rules,
standards, and specifications for all sections and requirements related to
that object.

The goal is to establish a traceable mapping:

`Task Object -> Applicable Regulation Section -> Requirement`

### 3. Build the engineering specification

Convert the discovered regulatory requirements into explicit engineering
requirements and acceptance criteria.

Requirements originating from the task itself must remain distinguishable from
requirements originating from regulations.

### 4. Define compliance tests

For every regulatory requirement and acceptance criterion, create a test that
can verify whether a proposed engineering object or solution satisfies that
requirement.

Tests must be defined independently of any particular implementation.

The resulting traceability should be:

`Task Object -> Regulation Requirement -> Acceptance Criterion -> Compliance Test`

### 5. Propose engineering objects and solutions

Only after the requirements and tests are established, propose concrete
engineering objects, equipment, subsystems, parameters, or design decisions.

### 6. Test proposed objects against the regulations

Every proposed object or design decision must be evaluated using the previously
defined compliance tests.

A proposed object is acceptable only if it satisfies all regulatory
requirements applicable to it.

The final traceability must therefore be:

`Proposed Object -> Compliance Test -> Regulatory Requirement -> Result`

## Core Principle

The solution must not define the tests.

The regulations define the requirements.
The requirements define the tests.
The tests evaluate the proposed solution.

In other words:

First identify what exists in the task.
Then determine what the regulations require from it.
Then define how compliance will be tested.
Only then propose a solution and verify it against those tests.

