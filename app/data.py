from flask import Flask, render_template
import pandas as pd
import os

# Adjusting the template_folder to point directly to the templates folder
app = Flask(__name__, template_folder=r'C:\\Users\\Ev\\Desktop\\Spending_Patterns\\templates')

CSV_PATH = r'C:\\Users\\Ev\\Desktop\\Spending_Patterns\\spending_patterns_detailed.csv'

@app.route('/')
def display_dataframe():
    df = pd.read_csv(CSV_PATH)

    html_table = df.to_html(classes='table table-striped', index=False)

    return render_template('index.html', table=html_table)

@app.route('/average-spent')
def average_spent_per_category():
    # Read the CSV
    df = pd.read_csv(CSV_PATH)
    
    # Calculate the average total spent per category
    average_spent = df.groupby('Category')['Total Spent'].mean().reset_index()
    average_spent.rename(columns={'Total Spent': 'Average Total Spent'}, inplace=True)
    
    # Convert the result to an HTML table
    html_table = average_spent.to_html(classes='table table-striped', index=False)
    
    return render_template('average_spent.html', table=html_table)

@app.route('/average-quantity')
def average_quantity_per_category():
    # Read the CSV
    df = pd.read_csv(CSV_PATH)
    
    # Calculate the average quantity per category
    average_quantity = df.groupby('Category')['Quantity'].mean().reset_index()
    average_quantity.rename(columns={'Quantity': 'Average Quantity'}, inplace=True)
    
    # Convert the result to an HTML table
    html_table = average_quantity.to_html(classes='table table-striped', index=False)
    
    return render_template('average_quantity.html', table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
