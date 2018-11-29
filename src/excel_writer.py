import xlsxwriter
from datetime import date


class ExcelWriter:
    """
    Format of excel file:
    A/B = Category Name, C = Total     D Empty    E-F = Category Name, G = Total    ...
    A, B, C = Date/Description/Cost               E,F,C = Date/Description/Cost     ...
    """
    def __init__(self):
        self.date = str(date.today())
        self.file_name = 'budget_summary_' + self.date + '.xlsx'
        self.workbook, self.worksheet = self.create_file()

    def create_file(self):
        """
        Create an excel file with a worksheet and return them
        :param self:
        :return: workbook, worksheet
        """
        workbook = xlsxwriter.Workbook(self.file_name)
        worksheet = workbook.add_worksheet()
        return workbook, worksheet

    def launch_file(self):
        pass

    def write_categories(self, categories):
        """
        Write to the excel sheet
        :param categories: the categories containing the data and groupings
        """
        row = 0
        header_col = 0
        header_cell = self.workbook.add_format({'bold': 1, 'align': 'center'})
        total_cell = self.workbook.add_format({'bold': 1})
        total_cell.set_num_format('$#,##0.00')
        currency_cell = self.workbook.add_format()
        currency_cell.set_num_format('$#,##0.00')
        # Create the headers
        for category in categories:
            # Write category name to two merged columns in bold
            self.worksheet.merge_range(first_row=row, last_row=row, first_col=header_col, last_col=header_col+1, data=category.category_name, cell_format=header_cell)
            # Adjust column width to fit date format
            self.worksheet.set_column(header_col, header_col, width=10)
            # Get the next cell
            header_col += 2
            # Write the total for the category in bold
            self.worksheet.write(row, header_col, category.total, total_cell)
            # Adjust column width to fit total
            cost_width = len('${:,.2f}'.format(category.total)) + 1
            self.worksheet.set_column(header_col, header_col, width=cost_width)
            # Skip a column between each category
            header_col += 2

        # Fill each column with data
        global_col = 0
        for category in categories:
            row = 1
            max_description = 0
            for item in category.items:
                col = global_col
                trans_date = item[0]
                description = item[1]
                cost = item[2]
                self.worksheet.write(row, col, trans_date)
                col += 1
                self.worksheet.write(row, col, description)
                col += 1
                self.worksheet.write(row, col, cost, currency_cell)
                row += 1
                # Keep track of longest description for setting column width
                len_description = len(description)
                if len_description > max_description:
                    max_description = len_description
            self.worksheet.set_column(global_col+1, global_col+1, width=max_description+1)
            global_col += 4





