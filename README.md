# FastAPI Report and Analysis Backend

This is a backend developed with FastAPI that allows for data collection and processing to generate reports, statistics, and analysis to aid in making informed business decisions.

## Features

- **Add Sales and Expenses**: You can add sales and expenses data to the system.
- **Generate Reports**: Get detailed reports on total sales, total expenses, and profits.
- **Get Sales and Expenses Details**: Access specific details of sales and expenses using their IDs.
- **Filter by Date Range**: Filter sales and expenses by a specific date range.

## Requirements to Run the Program

- Python 3.x
- FastAPI
- Uvicorn

## Usage

1. **Add Sales and Expenses**: Use the `/ventas/` and `/gastos/` routes to add sales and expenses data respectively. Data should be provided in JSON format.
2. **Generate Reports**: Access the `/informes/` route to get a detailed report on finances.
3. **Get Details**: Use the `/ventas/{venta_id}` and `/gastos/{gasto_id}` routes to get specific details of sales and expenses respectively, replacing `{venta_id}` and `{gasto_id}` with the corresponding IDs.
4. **Filter by Date**: Access the `/ventas/rango/` and `/gastos/rango/` routes to filter sales and expenses by a specific date range. Specify the start and end dates as query parameters in the format `YYYY-MM-DD`.

## Execution

1. Install dependencies using `pip install -r requirements.txt`.
2. Run the server using `uvicorn main:app --reload`.
3. Access `http://localhost:8000` in your browser or API client tool to interact with the routes.

## Contributions

Contributions are welcome! If you have suggestions for new features, code improvements, or bug reports, feel free to open an issue or submit a pull request.
