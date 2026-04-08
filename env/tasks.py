TASKS = [
    {
        "id": "easy",
        "query": "Where is my order?",
        "order_status": "shipped",
        "payment_status": "paid",
        "solution_steps": ["check_order_status", "respond_user"]
    },
    {
        "id": "medium",
        "query": "I want a refund",
        "order_status": "delivered",
        "payment_status": "paid",
        "solution_steps": [
            "check_order_status",
            "check_payment",
            "initiate_refund",
            "respond_user"
        ]
    },
    {
        "id": "hard",
        "query": "Payment failed but money deducted",
        "order_status": "pending",
        "payment_status": "failed",
        "solution_steps": [
            "check_payment",
            "escalate_issue",
            "initiate_refund",
            "respond_user"
        ]
    }
]