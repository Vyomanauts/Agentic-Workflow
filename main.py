import streamlit as st

# Custom PlanAgent: Responsible for splitting user queries into sub-tasks
class PlanAgent:
    def __init__(self, query):
        self.query = query
        self.sub_tasks = []

    def split_query(self):
        # Example task splitting logic
        if "build" in self.query:
            self.sub_tasks = ["Define Requirements", "Design Architecture", "Write Code", "Test Application"]
        elif "analyze" in self.query:
            self.sub_tasks = ["Collect Data", "Clean Data", "Perform Analysis", "Generate Report"]
        else:
            self.sub_tasks = ["Understand Query", "Research Problem", "Gather Resources"]
        return self.sub_tasks

    def execute(self):
        return self.split_query()


# Custom ToolAgent: Handles solving tasks
class ToolAgent:
    def __init__(self, tasks):
        self.tasks = tasks
        self.solved_tasks = []

    def solve_task(self, task):
        # Example task-solving logic
        solution = f"Solving Task: {task}"
        return solution

    def execute(self):
        for task in self.tasks:
            solution = self.solve_task(task)
            self.solved_tasks.append(solution)
        return self.solved_tasks


# Custom FeedbackLoop: Refines and modifies tasks based on feedback
class FeedbackLoop:
    def __init__(self, tasks):
        self.tasks = tasks
        self.refined_tasks = []

    def refine_task(self, task):
        # Refinement logic: Example of adding further complexity
        if "Test" in task:
            task += " & Debug"
        elif "Design" in task:
            task += " & Create Detailed Plan"
        return task

    def execute(self):
        for task in self.tasks:
            refined_task = self.refine_task(task)
            self.refined_tasks.append(refined_task)
        return self.refined_tasks


# Main Pipeline: Orchestrates the agentic workflow
def agentic_workflow(query):
    # Step 1: Split the query into tasks using PlanAgent
    plan_agent = PlanAgent(query)
    sub_tasks = plan_agent.execute()

    # Step 2: Refine tasks using FeedbackLoop
    feedback_loop = FeedbackLoop(sub_tasks)
    refined_tasks = feedback_loop.execute()

    # Step 3: Solve tasks using ToolAgent
    tool_agent = ToolAgent(refined_tasks)
    final_solutions = tool_agent.execute()

    return final_solutions


# Streamlit App Interface for testing the workflow
st.title("Agentic Workflow Testing")

user_query = st.text_input("Enter your query", "build a recommendation system")
if st.button("Run Workflow"):
    results = agentic_workflow(user_query)
    st.write("Results:")
    for idx, solution in enumerate(results):
        st.write(f"Solution {idx + 1}: {solution}")
