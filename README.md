# Agentic-Workflow

Description
This project implements an agentic workflow using Langgraph. It allows users to input queries, which are then split into sub-tasks, refined, and solved. The application provides an interactive interface built with Streamlit.

Features
Split user queries into sub-tasks.
Refine tasks using feedback loops.
Solve tasks with a custom ToolAgent.
User-friendly interface.





Project Overview
The Agentic Workflow Implementation is a project designed to demonstrate the use of Langgraph in creating a modular agentic workflow. The application is built using Python and Streamlit, providing an interactive interface for users to input natural language queries.



Here’s a detailed description of the project to include in the README.md file:

Project Overview
The Agentic Workflow Implementation is a project designed to demonstrate the use of Langgraph in creating a modular agentic workflow. The application is built using Python and Streamlit, providing an interactive interface for users to input natural language queries.

Purpose
The primary purpose of this project is to automate and streamline the process of breaking down complex user queries into manageable sub-tasks. This not only enhances task organization but also facilitates effective problem-solving through a structured approach. By utilizing different agents, the workflow ensures that tasks are refined and solved efficiently.

Components
PlanAgent: This component is responsible for interpreting user queries and splitting them into relevant sub-tasks. It analyzes the input and generates a list of tasks based on predefined logic.

ToolAgent: The ToolAgent handles the execution of the generated tasks. It processes each task and provides solutions, showcasing how each component of the workflow contributes to the overall goal.

FeedbackLoop: To ensure that the tasks remain relevant and effective, the FeedbackLoop refines the generated tasks based on specific criteria. It modifies tasks by adding additional complexity or debugging requirements as necessary.

Workflow
The workflow follows these steps:

Query Input: Users enter a natural language query into the Streamlit interface.
Task Generation: The PlanAgent analyzes the query and generates a list of sub-tasks.
Task Refinement: The FeedbackLoop refines these tasks to improve clarity and effectiveness.
Task Execution: The ToolAgent executes the refined tasks, providing users with actionable solutions.
