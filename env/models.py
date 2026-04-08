from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    user_query: str
    order_status: Optional[str]
    payment_status: Optional[str]
    history: List[str]

class Action(BaseModel):
    action_type: str
    payload: Optional[dict] = None

class Reward(BaseModel):
    value: float