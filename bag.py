class Bag:
    def __init__(self):
        self.size = 4
        self.contents = []

    def add_to_bag(self, name):
        if len(self.contents) < self.size:
            self.contents.append(name)
            return True
        return False

    def clear_bag(self):
        self.contents = []

    def use_item_in_bag(self, name):
        if name in self.contents:
            self.contents.remove(name)
            return name
        return None

    def is_bag_empty(self):
        return len(self.contents) == 0

    def is_bag_full(self):
        return len(self.contents) == self.size
