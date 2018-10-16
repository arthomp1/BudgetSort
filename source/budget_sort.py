import csv
import sys
import category
from tkinter.filedialog import askopenfilename


class BudgetSort:
    def __init__(self):
        self.header, self.all_transactions = self.read_file()
        self.categories = self.get_categories('C:\\Users\\ross7\\Desktop\\VB Testing\\keywords.csv')

    @staticmethod
    def read_file():
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

    # get all categories and their keywords
    @staticmethod
    def get_categories(keywords_file):
        try:
            with open(keywords_file) as csv_f:
                reader = csv.reader(csv_f, delimiter='|')
                cat_dict = {}
                for row in reader:
                    cat_dict[row[0]] = row[1].split(',')
        except Exception as e:
            sys.exit(str(e))
        return cat_dict

    def search_transactions(self):
        remaining_transactions = self.all_transactions[:]
        for key, value in self.categories.items():
            curr_category = category.Category(category_name=key, keywords=value)
            remaining_transactions = curr_category.find_rows(remaining_transactions)
            print("Category:", curr_category.category_name, "\nKeywords:", str(curr_category.keywords),
                  "\nItems:\n" + str(curr_category.items))
        return remaining_transactions

    # Create excel spreadsheet
    def write_file(self):
        pass
        # Format:
        # A-B = bold Category Name C = bold Total: $$     D Empty    E-F = Cat, G = total, etc
        # A, B, C = Date/Description/Cost                   D         E,F,C