import ollama

def plan(goal):

    print("\n[AI Planner] Thinking...\n")

    prompt = f"""
    Break this goal into 4 simple tasks.

    Goal: {goal}

    Tasks:
    """

    response = ollama.chat(
        model="phi",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response["message"]["content"]

    tasks = text.split("\n")

    tasks = [t.strip() for t in tasks if t.strip() != ""]

    return tasks
