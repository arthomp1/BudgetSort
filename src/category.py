class Category:
    def __init__(self, category_name, keywords):
        self.category_name = category_name
        self.keywords = keywords
        self.items = []
        self.total = 0.0

    def find_rows(self, transactions):
        """
        add transactions belonging to the current category instance to category.items
        :param transactions: list of transactions to search
        :return: the transactions that did not belong to the current category
        """
        remaining_transactions = []
        for item in transactions:
            found = False
            for keyword in self.keywords:
                if keyword in item[1]:
                    self.items.append(item)
                    found = True
                    break
            if not found:
                remaining_transactions.append(item)
        return remaining_transactions

    def calculate_total(self):
        """
        get the total cost for this category and set it in the instance variable total
        :return: the total cost for this category
        """
        total = 0.0
        for item in self.items:
            total += item[2]
        self.total = total
        return total
