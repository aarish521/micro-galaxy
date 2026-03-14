from core.orchestrator import run

goal = input("Enter your goal: ")

results = run(goal)

for r in results:
    print(r)
