from case_root import Case

class ProductItem:
    def __init__(self):
        self.priority: int
        self.name: str
        self.product_type: list[Case]
        self.target: list[str]
        self.benefit: list[str]
        self.related_case: list[str]
        self.related_solution: list[str]
        self.related_company: list[str]
        self.stage: list[str]
        self.note: str
