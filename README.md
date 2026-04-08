# CSREnv – Customer Support Resolution Environment

## 📌 Overview

CSREnv is a real-world OpenEnv-compatible environment that simulates customer service workflows.
An AI agent interacts with the environment to resolve user queries through multi-step reasoning and actions.

---

## 🎯 Motivation

Customer support is a complex real-world task involving:

* Understanding user queries
* Interacting with backend systems
* Taking sequential decisions

This project models that process in a reinforcement-learning-friendly environment.

---

## 🧠 Environment Design

### Observation Space

* `user_query`: Customer request
* `order_status`: Order state
* `payment_status`: Payment state
* `history`: Previous actions

### Action Space

Discrete actions:

* check_order_status
* check_payment
* initiate_refund
* escalate_issue
* respond_user

---

## 🎮 Tasks

### Easy

* Query: "Where is my order?"
* Goal: Check order → Respond

### Medium

* Query: "I want a refund"
* Goal: Multi-step resolution with refund

### Hard

* Query: "Payment failed but money deducted"
* Goal: Complex resolution with escalation

---

## 🎁 Reward Function

* +0.2 for correct step
* -0.1 for wrong step
* +0.5 for successful resolution
* Penalizes inefficient actions

---

## 🤖 Baseline Agent

Uses OpenAI API to decide actions step-by-step.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python inference.py
```

---

## 🐳 Docker

```bash
docker build -t csrenv .
docker run -p 7860:7860 csrenv
```

---

## 🌐 API

```bash
POST /reset
```

Returns initial environment state.

---

## 📊 Sample Output

```text
[START] task=easy env=csrenv model=gpt-4o-mini
[STEP] step=1 action=check_order_status reward=0.20 done=false error=null
[END] success=true steps=2 score=1.00 rewards=0.20,0.70
```

---

## 🚀 Deployment

Deployed on Hugging Face Spaces using Docker.

---

## 🏆 Highlights

* Real-world task simulation
* OpenEnv compliant
* Multi-step reasoning
* Structured evaluation

---
