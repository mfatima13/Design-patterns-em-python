from .select import Select

class Repository:

    def __init__(self):
        self.select = Select()

    def select_one(self):
        return self.select.select_single_element()

    def select_many(self):
        return self.select.select_many_elements()