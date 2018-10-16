class Category:
    def __init__(self, category_name, keywords):
        self.category_name = category_name
        self.keywords = keywords
        self.items = []

    # get all transactions in the category and return the remaining ones
    def find_rows(self, transactions):
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
