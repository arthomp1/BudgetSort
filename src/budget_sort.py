import csv
import sys
import src.category as category
from tkinter.filedialog import askopenfilename


class BudgetSort:
    def __init__(self):
        self.header, self.all_transactions = self.read_file()
        self.category_dict = self.get_categories('C:\\Users\\ross7\\Desktop\\VB Testing\\keywords.csv')
        self.categories = []

    @staticmethod
    def read_file():
        """
        prompt for file with expenses and read it
        :return:
            header_row - the header of the file ('Trans Date', 'Description', 'Amount')
            csv_lst - list of transactions; each transaction is a list of the values labeled in header_row
        """
        filename = askopenfilename()
        try:
            with open(filename) as csv_f:
                reader = csv.reader(csv_f)
                csv_lst = [row for row in reader if not row[0] == 'Payment']
        except Exception as e:
            sys.exit(str(e))
        header_row = [csv_lst[0][1], csv_lst[0][3], csv_lst[0][4]]
        del csv_lst[0]
        for index, item in enumerate(csv_lst):
            csv_lst[index] = [item[1], item[3], float(item[4]) * -1]
        return header_row, csv_lst

    @staticmethod
    def get_categories(keywords_file):
        """
        get all the categories from the keyword file
        :return: cat_dict - dictionary with key = category name, value = list of category's keywords
        """
        try:
            with open(keywords_file) as csv_f:
                reader = csv.reader(csv_f, delimiter='|')
                cat_dict = {}
                for row in reader:
                    cat_dict[row[0]] = row[1].split(',')
        except Exception as e:
            sys.exit(str(e))
        return cat_dict

    def sort_transactions(self):
        """
        sort all transactions into their intended category by keyword
        :return: the transactions that did not belong to any category
        """
        remaining_transactions = self.all_transactions[:]
        for key, value in self.category_dict.items():
            curr_category = category.Category(category_name=key, keywords=value)
            # Add matching items to the current category object and remove them from remaining_transactions
            remaining_transactions = curr_category.find_rows(remaining_transactions)
            # Calculate the total for the category
            curr_category.calculate_total()
            # Add the current category to list of all categories
            self.categories.append(curr_category)
        return remaining_transactions
