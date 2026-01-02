---
id: 2
title: todo-cli-app-plan
stage: plan
date_iso: 2026-01-02
surface: agent
model: Qwen Code
feature: todo-cli-app
branch: 1-todo-cli-app
user: user
command: /sp.plan
labels:
  - planning
  - todo
  - cli
  - python
links:
  spec: specs/1-todo-cli-app/spec.md
  plan: specs/1-todo-cli-app/plan.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - specs/1-todo-cli-app/plan.md
  - specs/1-todo-cli-app/research.md
  - specs/1-todo-cli-app/data-model.md
  - specs/1-todo-cli-app/contracts/todo-cli-contract.md
  - specs/1-todo-cli-app/quickstart.md
tests_yaml: []
prompt_text: |
  /sp.plan Create: Project structure, module architecture, data model, CLI interface flow, and implementation workflow for Phase I Todo Console App.

  Decisions needing documentation:
  - Task identifier: Options (auto-increment integer vs UUID). Chosen: auto-increment integer ID for simplicity, readability in console output, and ease of user reference (users delete/update by ID).
  - Data storage: In-memory structure. Options (list of dicts vs list of dataclass objects vs custom Task class). Chosen: list of dataclass instances for strong typing, clarity, and IDE support.
  - Project layout: Options (flat scripts vs proper package). Chosen: standard Python src layout (/src/evolution_of_todo with __main__.py or console entrypoint) to establish good habits for future phases.
  - CLI implementation approach: Options (argparse with subcommands vs simple loop with input parsing). Chosen: interactive REPL loop with numbered menu for better beginner usability and faster prototyping in Phase I.
  - Code generation workflow: Use iterative spec → plan → AI code generation → review cycles with Qwen Code CLI (transitioning to Claude Code).

  Testing strategy: Manual validation based on /sp.specify success criteria.
  - Run the application interactively and verify each Basic Level feature works end-to-end.
  - Checklist:
    - Add multiple tasks → visible in list with unique IDs, titles, descriptions, and status [ ]
    - Mark as complete → status changes to [x] and persists in same session
    - Update task → title/description changes reflected in list
    - Delete task → removed from list and ID no longer accessible
    - Empty state handling → graceful message when no tasks
    - Invalid input handling → helpful error messages without crashing
  - Static analysis: Run mypy --strict and ruff check to ensure zero type errors and clean code.

  Technical details:
  - Use Python dataclasses for Task model (fields: id: int, title: str, description: str, completed: bool)
  - Core modules under /src/evolution_of_todo/:
    - models.py → Task dataclass
    - repository.py → InMemoryTodoRepository with methods: add, get_all, get_by_id, update, delete, toggle_complete
    - cli.py → Main interactive loop, menu display, input handling, and orchestration of repository calls
    - __main__.py or separate entrypoint script for `python -m evolution_of_todo`
  - Organize implementation by incremental specifications in /specs/history/:
    1. Data model and repository interface
    2. Basic repository implementation (add, list, toggle)
    3. Update and delete operations
    4. CLI menu and user interaction loop
    5. Polish: input validation, user-friendly messages, status indicators
  - Use UV for project setup: uv init, uv add for any future dependencies (none required in Phase I)
  - All code must include type hints, Google-style docstrings, and pass formatting/linting
  - Commit plan: constitution → specify → plan → individual feature specs → generated code → README and supporting files
response_text: |
  Created a comprehensive implementation plan for the Evolution of Todo CLI application, including:
  - Technical context with language, dependencies, and constraints
  - Constitution compliance check
  - Project structure with source code organization
  - Research document with key decisions (task identifier, data storage, project layout, CLI approach)
  - Data model defining the Task entity and repository interface
  - API contracts for the CLI operations
  - Quickstart guide for using the application
  All artifacts are stored in the specs/1-todo-cli-app directory and align with the project constitution.
outcome: |
  Successfully created all required planning artifacts for the todo CLI application. The plan includes technical context, research findings, data model, contracts, and quickstart guide. All artifacts comply with the project constitution and are ready for the task breakdown phase.
evaluation: |
  The implementation plan comprehensively covers all required aspects for the Phase I todo CLI application. It follows the constitution principles with proper technical context, research, data modeling, and documentation. The plan is ready for the next phase of task breakdown.
---

# Todo CLI App Implementation Plan

This PHR documents the creation of the implementation plan for the Evolution of Todo Phase I: In-Memory Python Console App.