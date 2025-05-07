from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loan', methods=['GET', 'POST'])
def loan():
    monthly_payment = None
    if request.method == 'POST':
        loan_amount = float(request.form['loan_amount'])
        interest_rate = float(request.form['interest_rate']) / 100 / 12
        loan_term = int(request.form['loan_term']) * 12

        if interest_rate > 0:
            monthly_payment = loan_amount * (interest_rate * (1 + interest_rate) ** loan_term) / ((1 + interest_rate) ** loan_term - 1)
        else:
            monthly_payment = loan_amount / loan_term

        monthly_payment = round(monthly_payment, 2)

    return render_template('loan.html', monthly_payment=monthly_payment)

@app.route('/mortgage')
def mortgage():
    return render_template('mortgage.html')

@app.route('/savings', methods=['GET', 'POST'])
def savings():
    future_value = None
    if request.method == 'POST':
        try:
            initial = float(request.form['initial_amount'])
            monthly = float(request.form['monthly_contribution'])
            annual_rate = float(request.form['annual_interest']) / 100
            years = int(request.form['years'])

            months = years * 12
            monthly_rate = annual_rate / 12

            future_value = initial * ((1 + monthly_rate) ** months)
            for i in range(1, months + 1):
                future_value += monthly * ((1 + monthly_rate) ** (months - i))

            future_value = round(future_value, 2)
        except Exception as e:
            future_value = "Invalid input."

    return render_template('savings.html', future_value=future_value)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)