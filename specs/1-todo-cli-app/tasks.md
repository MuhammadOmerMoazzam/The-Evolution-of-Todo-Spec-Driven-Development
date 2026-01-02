---

description: "Task list for todo CLI app implementation"
---

# Tasks: Evolution of Todo – Phase I: In-Memory Python Console App

**Input**: Design documents from `/specs/1-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Constitution Compliance Check

These tasks ensure compliance with the Evolution of Todo Constitution by:
- Following spec-driven development (tasks based on specification)
- Ensuring all code will be AI-generated (no manual coding tasks)
- Maintaining clean architecture (modular, readable code)
- Including type hints, docstrings, and PEP 8 compliance tasks
- Using UV for dependency management

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan with proper Python package layout
- [X] T002 Initialize Python project with UV for dependency management
- [X] T003 [P] Configure linting (Ruff) and formatting (Black) tools as per constitution
- [X] T004 Set up mypy configuration for type checking as per constitution
- [X] T005 Create CLAUDE.md to document AI agent prompts and workflow

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Create Task dataclass with type hints and docstrings in src/todo/core/models.py
- [X] T007 [P] Create InMemoryTodoRepository with type hints and docstrings in src/todo/core/services.py
- [X] T008 [P] Setup CLI interface structure in src/todo/cli/interface.py
- [X] T009 Configure error handling and logging infrastructure
- [X] T010 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks to their todo list and view them so that they can keep track of what they need to do.

**Independent Test**: Can be fully tested by adding a task and then listing all tasks to verify it appears in the list with the correct details.

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement Task dataclass with id, title, description, and completed fields in src/todo/core/models.py
- [X] T012 [P] [US1] Implement add_task method in InMemoryTodoRepository in src/todo/core/services.py
- [X] T013 [US1] Implement get_all_tasks method in InMemoryTodoRepository in src/todo/core/services.py
- [X] T014 [US1] Implement CLI menu display for adding and viewing tasks in src/todo/cli/interface.py
- [X] T015 [US1] Implement CLI command for adding tasks in src/todo/cli/interface.py
- [X] T016 [US1] Implement CLI command for viewing tasks in src/todo/cli/interface.py
- [X] T017 [US1] Add validation to ensure title is not empty in src/todo/core/services.py
- [X] T018 [US1] Add logging for task creation and viewing operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Mark Complete Tasks (Priority: P2)

**Goal**: Enable users to update their tasks and mark them as complete so that they can track their progress and modify task details as needed.

**Independent Test**: Can be fully tested by adding a task, updating its details, and marking it as complete to verify the status changes.

### Implementation for User Story 2

- [X] T019 [P] [US2] Implement update_task method in InMemoryTodoRepository in src/todo/core/services.py
- [X] T020 [P] [US2] Implement toggle_task_completion method in InMemoryTodoRepository in src/todo/core/services.py
- [X] T021 [US2] Implement CLI command for updating tasks in src/todo/cli/interface.py
- [X] T022 [US2] Implement CLI command for marking tasks complete/incomplete in src/todo/cli/interface.py
- [X] T023 [US2] Add validation for task ID existence in src/todo/core/services.py
- [X] T024 [US2] Add logging for task update and completion operations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Enable users to delete tasks from their list so that they can remove items that are no longer relevant.

**Independent Test**: Can be fully tested by adding a task and then deleting it to verify it no longer appears in the task list.

### Implementation for User Story 3

- [X] T025 [P] [US3] Implement delete_task method in InMemoryTodoRepository in src/todo/core/services.py
- [X] T026 [US3] Implement CLI command for deleting tasks in src/todo/cli/interface.py
- [X] T027 [US3] Add validation for task ID existence before deletion in src/todo/core/services.py
- [X] T028 [US3] Add logging for task deletion operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Basic Level Features Completion

**Purpose**: Ensure all Basic Level features are implemented as per constitution

- [X] T029 Implement CLI main loop with menu options in src/todo/cli/interface.py
- [X] T030 Implement CLI entry point in src/todo/__main__.py
- [X] T031 Verify all 5 Basic Level features work: Add, Delete, Update, View, Mark Complete
- [X] T032 Test all Basic Level features interactively as per constitution success criteria

---

## Phase 7: Quality Assurance & Compliance

**Purpose**: Ensure all constitution standards are met

- [X] T033 Verify all functions have type hints as per constitution
- [X] T034 Verify all public functions and classes have docstrings as per constitution
- [X] T035 Run mypy and ensure zero errors as per constitution
- [X] T036 Run Ruff/Black and ensure PEP 8 compliance as per constitution
- [X] T037 Verify all generated code is traceable to its originating specification
- [X] T038 Update README.md with setup and usage instructions as per constitution

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Documentation updates in docs/
- [X] T040 Code cleanup and refactoring
- [X] T041 Performance optimization across all stories
- [X] T042 [P] Additional unit tests (if requested) in tests/unit/
- [X] T043 Security hardening
- [X] T044 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Basic Level Features (Phase 6)**: Depends on all desired user stories being complete
- **Quality Assurance (Phase 7)**: Can run in parallel with other phases but final verification at end
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Implement Task dataclass with id, title, description, and completed fields in src/todo/core/models.py"
Task: "Implement add_task method in InMemoryTodoRepository in src/todo/core/services.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Team completes Setup + Foundational together
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Complete Basic Level Features → Test all 5 features → Deploy/Demo
6. Complete Quality Assurance → Verify constitution compliance → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- All code must be AI-generated as per constitution principle
- All code must follow type hints, docstrings, and PEP 8 as per constitution