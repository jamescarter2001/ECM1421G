class OperationResult:
    def __init__(self, success=True, id=0, error=""):
        self.success = success
        self.id = id
        self.error = error