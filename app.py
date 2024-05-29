from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = [
        {'name': 'Margherita', 'ingredients': 'Tomato, Mozzarella, Basil', 'price': 8.99},
        {'name': 'Pepperoni', 'ingredients': 'Tomato, Mozzarella, Pepperoni', 'price': 9.99},
        {'name': 'Hawaiian', 'ingredients': 'Tomato, Mozzarella, Ham, Pineapple', 'price': 10.99},
    ]

    sort_by = request.args.get('sort', 'asc')
    if sort_by == 'asc':
        pizzas = sorted(pizzas, key=lambda x: x['price'])
    elif sort_by == 'desc':
        pizzas = sorted(pizzas, key=lambda x: x['price'], reverse=True)

    return render_template('menu.html', pizzas=pizzas, sort_by=sort_by)

if __name__ == '__main__':
    app.run(debug=True)