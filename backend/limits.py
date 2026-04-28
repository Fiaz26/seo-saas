PLAN_LIMITS = {
    "free": 20,
    "pro": 500,
    "enterprise": 5000
}

def check_limit(user_plan, usage):
    limit = PLAN_LIMITS.get(user_plan, 20)
    return usage < limit
