# Saga Pattern Implementation

## Components
1. **Saga Orchestrator**: Coordinates the execution of steps and manages compensation if a step fails.
2. **Steps**: Each step (Payment, Inventory, Shipping) has `execute()` ("do" action) and `compensate()` methods.
   - `execute()`: Performs the step's action.
   - `compensate()`: Reverts the action if any step fails.
3. It can simulate failure if `simulate_failure=True` passed as argument to steps during initialization (see lines 72-74).

## Workflow
1. **Execute Steps in Order**: Payment → Inventory → Shipping.
2. **Compensation on Failure**: If any step fails, the orchestrator triggers compensation for completed steps in reverse order.


## How to Run
```
   python main.py 
```