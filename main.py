from fastapi import FastAPI, HTTPException, Query, Path
from typing import List, Dict, Optional

app = FastAPI()

# Data storage simulation
data_storage = {
    "sales": [],
    "expenses": [],
}

# Route to add sales data
@app.post("/sales/")
def add_sale(sale: Dict[str, float]):
    data_storage["sales"].append(sale)
    return {"message": "Sale added successfully!"}

# Route to add expenses data
@app.post("/expenses/")
def add_expense(expense: Dict[str, float]):
    data_storage["expenses"].append(expense)
    return {"message": "Expense added successfully!"}

# Route to generate reports and analysis
@app.get("/reports/")
def generate_report():
    if not data_storage["sales"] or not data_storage["expenses"]:
        raise HTTPException(status_code=404, detail="Not enough data to generate a report")

    total_sales = sum(sale["amount"] for sale in data_storage["sales"])
    total_expenses = sum(expense["amount"] for expense in data_storage["expenses"])
    profits = total_sales - total_expenses

    report = {
        "total_sales": total_sales,
        "total_expenses": total_expenses,
        "profits": profits,
    }

    return report

# Route to get details of a specific sale by ID
@app.get("/sales/{sale_id}")
def get_sale(sale_id: int = Path(..., title="Sale ID", ge=1)):
    try:
        sale = data_storage["sales"][sale_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

# Route to get details of a specific expense by ID
@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int = Path(..., title="Expense ID", ge=1)):
    try:
        expense = data_storage["expenses"][expense_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

# Route to filter sales by date range
@app.get("/sales/range/")
def filter_sales_by_date(start_date: str = Query(..., title="Start Date", description="Format: YYYY-MM-DD"),
                         end_date: str = Query(..., title="End Date", description="Format: YYYY-MM-DD")):
    filtered_sales = [sale for sale in data_storage["sales"] if start_date <= sale["date"] <= end_date]
    return filtered_sales

# Route to filter expenses by date range
@app.get("/expenses/range/")
def filter_expenses_by_date(start_date: str = Query(..., title="Start Date", description="Format: YYYY-MM-DD"),
                            end_date: str = Query(..., title="End Date", description="Format: YYYY-MM-DD")):
    filtered_expenses = [expense for expense in data_storage["expenses"] if start_date <= expense["date"] <= end_date]
    return filtered_expenses
