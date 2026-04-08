def grade(history, solution_steps):
    correct = 0
    for i, step in enumerate(solution_steps):
        if i < len(history) and history[i] == step:
            correct += 1
    return round(correct / len(solution_steps), 2)