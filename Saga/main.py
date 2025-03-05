class SagaOrchestrator:
    def __init__(self, steps):
        self.steps = steps

    def execute(self):
        executed_steps = []
        try:
            for step in self.steps:
                step.execute()
                executed_steps.append(step)
            return True
        except Exception as e:
            print(f"\nError during saga execution: {e}")
            self.compensate(executed_steps)
            return False

    def compensate(self, executed_steps):
        print("\nStarting compensation...")
        for step in reversed(executed_steps):
            try:
                step.compensate()
            except Exception as e:
                print(f"Error compensating step {step.name}: {e}")


class PaymentStep:
    def __init__(self, simulate_failure=False):
        self.name = "Payment"
        self.simulate_failure = simulate_failure

    def execute(self):
        print("\nProcessing payment...")
        if self.simulate_failure:
            raise Exception("Payment processing failed")
        print("Payment processed successfully")

    def compensate(self):
        print("\nCompensating payment: refunding customer")


class InventoryStep:
    def __init__(self, simulate_failure=False):
        self.name = "Inventory"
        self.simulate_failure = simulate_failure

    def execute(self):
        print("\nUpdating inventory...")
        if self.simulate_failure:
            raise Exception("Inventory update failed")
        print("Inventory updated successfully")

    def compensate(self):
        print("\nCompensating inventory: reverting inventory count")


class ShippingStep:
    def __init__(self, simulate_failure=False):
        self.name = "Shipping"
        self.simulate_failure = simulate_failure

    def execute(self):
        print("\nArranging shipping...")
        if self.simulate_failure:
            raise Exception("Shipping arrangement failed")
        print("Shipping arranged successfully")

    def compensate(self):
        print("\nCompensating shipping: canceling shipping request")


def main():
    payment = PaymentStep(simulate_failure=False)
    inventory = InventoryStep(simulate_failure=False)
    shipping = ShippingStep(simulate_failure=True)

    steps = [payment, inventory, shipping]

    saga = SagaOrchestrator(steps)
    success = saga.execute()

    if success:
        print("\nSuccess!")
    else:
        print("\nSaga failed. Compensation done.")


if __name__ == "__main__":
    main()