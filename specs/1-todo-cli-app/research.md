# Research: Evolution of Todo – Phase I: In-Memory Python Console App

## Decision: Task identifier
**Rationale**: Auto-increment integer ID was chosen for simplicity, readability in console output, and ease of user reference (users delete/update by ID). This approach is intuitive for users who will interact with the console application by referencing tasks by their numeric ID.

**Alternatives considered**: 
- UUID: More complex for console users to reference
- String-based IDs: Less efficient and harder to remember for users

## Decision: Data storage
**Rationale**: List of dataclass instances was chosen for strong typing, clarity, and IDE support. Dataclasses provide a clean way to represent the Task entity with type hints while maintaining readability.

**Alternatives considered**:
- List of dictionaries: Less type safety and no IDE support for field names
- Custom Task class: More verbose than necessary for Phase I

## Decision: Project layout
**Rationale**: Standard Python src layout (/src/todo with proper package structure) was chosen to establish good habits for future phases. This follows Python best practices and makes the project more maintainable.

**Alternatives considered**:
- Flat script structure: Would not scale well for future phases
- Single file application: Would become unwieldy as features are added

## Decision: CLI implementation approach
**Rationale**: Interactive REPL loop with numbered menu was chosen for better beginner usability and faster prototyping in Phase I. This provides a clear, simple interface for users to interact with the application.

**Alternatives considered**:
- Argparse with subcommands: More complex for interactive use
- Single command with arguments: Less intuitive for multiple operations

## Decision: Code generation workflow
**Rationale**: Use iterative spec → plan → AI code generation → review cycles with Qwen Code CLI (transitioning to Claude Code) to ensure all code follows the spec-driven development approach and maintains consistency.

**Alternatives considered**:
- Manual coding: Would violate the "No Manual Coding" principle in the constitution
- Direct implementation without specs: Would violate the "Spec-Driven Development" principle

## Technology Research Findings

### Python Dataclasses
- Dataclasses provide automatic generation of special methods (__init__, __repr__, etc.)
- Support for type hints out of the box
- Clean, readable syntax for defining structured data
- Good IDE support for field names and types

### In-Memory Storage Options
- Python lists: Simple to implement and modify
- Python dictionaries: Good for key-based access
- Dataclasses with lists: Best of both worlds - structured data with simple storage

### Console Interface Options
- Raw input() and print(): Simplest approach for Phase I
- Argparse: Better for command-line tools but less interactive
- Rich library: More advanced but violates "no external frameworks" constraint for Phase I