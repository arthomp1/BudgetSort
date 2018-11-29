import src.budget_sort as budget_sort
import src.excel_writer as excel_writer

def main():
    budget = budget_sort.BudgetSort()
    uncategorized = budget.sort_transactions()

    if uncategorized:
        print("The following rows are un-categorized:")
        print(uncategorized)
    else:
        print("All items are categorized!")

    # Write to excel sheet
    try:
        excel = excel_writer.ExcelWriter()
        excel.write_categories(budget.categories)
    finally:
        excel.workbook.close()


if __name__ == "__main__":
    main()
