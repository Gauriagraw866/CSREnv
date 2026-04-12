def grade(history, solution_steps):
    
    correct_steps = 0

    for step in history:
        if step in solution_steps:
            correct_steps += 1

    raw_score = correct_steps / len(solution_steps)

    
    score = max(0.01, min(raw_score, 0.99))

    return score