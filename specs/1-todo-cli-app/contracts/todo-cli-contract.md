# API Contract: Todo CLI Application

## Overview
This document defines the interface contracts for the Todo CLI application. Since this is a console application, the "API" refers to the user interaction patterns and data flow between the CLI interface and the core business logic.

## Task Operations

### Add Task
- **User Action**: Select "Add Task" option from main menu or enter corresponding command
- **Input**: Title (required), Description (optional)
- **Output**: Success message with assigned task ID, or error message
- **Data Format**: 
  - Request: `{"title": "string", "description": "string"}`
  - Response: `{"success": true, "task_id": int}` or `{"success": false, "error": "string"}`

### List Tasks
- **User Action**: Select "View Tasks" option from main menu
- **Input**: None
- **Output**: Formatted list of all tasks with ID, title, description, and completion status
- **Data Format**: 
  - Response: `{"tasks": [{"id": int, "title": "string", "description": "string", "completed": bool}]}`

### Update Task
- **User Action**: Select "Update Task" option and provide task ID
- **Input**: Task ID, new title (optional), new description (optional)
- **Output**: Success confirmation or error message
- **Data Format**: 
  - Request: `{"task_id": int, "title": "string", "description": "string"}`
  - Response: `{"success": true}` or `{"success": false, "error": "string"}`

### Delete Task
- **User Action**: Select "Delete Task" option and provide task ID
- **Input**: Task ID
- **Output**: Success confirmation or error message
- **Data Format**: 
  - Request: `{"task_id": int}`
  - Response: `{"success": true}` or `{"success": false, "error": "string"}`

### Toggle Task Completion
- **User Action**: Select "Mark Complete/Incomplete" option and provide task ID
- **Input**: Task ID
- **Output**: Success confirmation or error message
- **Data Format**: 
  - Request: `{"task_id": int}`
  - Response: `{"success": true}` or `{"success": false, "error": "string"}`

## Error Handling
- All operations should provide user-friendly error messages
- Invalid task IDs should result in appropriate error messages
- Empty titles should be rejected with a clear message
- The application should not crash on invalid input