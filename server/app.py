from fastapi import FastAPI
from env.environment import CSREnv
from env.tasks import TASKS

app = FastAPI()
env = CSREnv(TASKS[0])

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state.dict()}