from flask import Flask, render_template, request, redirect, url_for
from ml.recommendation_model import generate_skincare_routine
from models.model import db, UserInput

app = Flask(__name__)

# Configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/skincare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Routes for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect user input from the form
        user_data = UserInput(
            age=request.form['age'],
            skin_type=request.form['skin_type'],
            concerns=request.form['concerns'],
            lifestyle=request.form['lifestyle'],
            allergies=request.form['allergies']
        )
        db.session.add(user_data)
        db.session.commit()

        # Generate skincare routine using the AI model
        recommended_routine = generate_skincare_routine(user_data)
        return render_template('result.html', routine=recommended_routine)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
