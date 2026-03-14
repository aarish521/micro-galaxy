from agents.planner import plan
from agents.worker import work

def run(goal):
    tasks = plan(goal)  

    results = []
    for task in tasks:
        result = work(task)  
        results.append(result)

    return results




