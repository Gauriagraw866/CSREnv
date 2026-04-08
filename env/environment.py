from .models import Observation, Action, Reward

class CSREnv:
    def __init__(self, task):
        self.task = task
        self.max_steps = 6

    def reset(self):
        self.steps = 0
        self.done = False

        self.state = Observation(
            user_query=self.task["query"],
            order_status=self.task["order_status"],
            payment_status=self.task["payment_status"],
            history=[]
        )
        return self.state

    def step(self, action: Action):
        if self.done:
            raise Exception("Episode finished")

        self.steps += 1
        reward = 0.0

        self.state.history.append(action.action_type)

        if action.action_type in self.task["solution_steps"]:
            reward += 0.2
        else:
            reward -= 0.1

        if self.task["solution_steps"][-1] in self.state.history:
            reward += 0.5
            self.done = True

        if self.steps >= self.max_steps:
            self.done = True
            reward -= 0.2

        return self.state, Reward(value=max(0.0, min(1.0, reward))), self.done, {}

    def state(self):
        return self.state