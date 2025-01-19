from flask import Flask, render_template
import pandas as pd
import os

# Adjusting the template_folder to point directly to the templates folder
app = Flask(__name__, template_folder=r'C:\\Users\\Ev\\Desktop\\Spending_Patterns\\templates')

CSV_PATH = r'C:\\Users\\Ev\\Desktop\\Spending_Patterns\\spending_patterns_detailed.csv'

@app.route('/')
def display_dataframe():
    # Read the CSV
    df = pd.read_csv(CSV_PATH)
    
    # Filter the DataFrame to keep only the specified columns
    filtered_df = df[['Category', 'Quantity', 'Total Spent']]
    
    # Convert the filtered DataFrame to HTML
    html_table = filtered_df.to_html(classes='table table-striped', index=False)
    
    return render_template('index.html', table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
