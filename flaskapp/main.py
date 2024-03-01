from flask import render_template, render_template_string, request, Flask

app = Flask(__name__)

# Sample store data (replace this with your actual store data)
store_data = [
    {"id": 1, "name": "Horlicks", "price": 35.0, "description": "Lorem ipsum dolor sit amet.", "image": "product1.jpg"},
    {"id": 2, "name": "Dairy Milk", "price": 30.0, "description": "Consectetur adipiscing elit.", "image": "product2.jpg"},
    {"id": 3, "name": "Maggi", "price": 25.0, "description": "Pellentesque habitant morbi tristique senectus.", "image": "product3.jpg"},
    {"id": 4, "name": "Rooh Afza", "price": 45.0, "description": "Et netus et malesuada fames ac turpis egestas.", "image": "product4.jpg"},
    {"id": 5, "name": "Parle-G", "price": 15.0, "description": "Ut enim ad minim veniam, quis nostrud exercitation ullamco.", "image": "product5.jpg"},
    {"id": 6, "name": "Lays", "price": 20.0, "description": "Laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in.", "image": "product6.jpg"},
    {"id": 7, "name": "Crax", "price": 20.0, "description": "Reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla.", "image": "product7.jpg"},
    {"id": 8, "name": "Rasna", "price": 25.0, "description": "Excepteur sint occaecat cupidatat non proident.", "image": "product8.jpg"}
]

@app.route('/')
def home():
    return render_template('index.html', products=store_data)

@app.route('/auth.txt')
def auth():
    return render_template('auth.txt')

@app.route('/robots.txt')
def robot():
    return render_template('robots.txt')





@app.route('/api/users', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        user = request.form['username']         # replace with actual url for abgtest background
        html_code = """                             
        <body style="background-color: #0000; background-image: url('/static/abgtest1.png'); background-position: center; background-repeat: no-repeat; background-size: 1500px 650px; color: #39FF14; display: flex; justify-content: center; align-items: center; margin: 0; height: 100vh; position: relative;">
            <div style="text-align: center; font-size: 50px; position: absolute; top: 510px;">Welcome, {}!!!</div>
        </body>
        """.format(user)

        return render_template_string(html_code)
    return '''
        <body style="background-color: black; color: #39FF14; font-family: 'Courier New', Courier, monospace; display: flex; justify-content: center; align-items: center; height: 100vh;">
            <form method="post" action="/api/users" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                <label for="username" style="font-size: 20px;">Enter your username:</label><br>
                <input type="text" id="username" name="username" style="font-size: 20px; width: 300px; height: 40px; margin-bottom: 10px;"><br>
                <input type="submit" value="Submit" style="font-size: 20px;">
            </form>
        </body>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
