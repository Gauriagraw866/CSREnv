from fastapi import FastAPI
from env.environment import CSREnv
from env.tasks import TASKS

app = FastAPI()
env = CSREnv(TASKS[0])

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state.dict()}
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

# 🔥 REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()