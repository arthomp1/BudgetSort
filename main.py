import budget_sort


def main():
    budget = budget_sort.BudgetSort()
    for row in budget.all_transactions:
        print(row)
    print("*" * 100)
    uncategorized = budget.search_transactions()

    if uncategorized:
        print("The following rows are un-categorized:")
        print(uncategorized)
    else:
        print("*" * 100)
        print("All items are categorized!")


if __name__ == "__main__":
    main()
