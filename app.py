from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def calculate_risk_stage(risk):

    if risk < 30:
        stage = "Normal Stage"
        message = "No major cardiovascular risk detected."
        category = "normal"

    elif 30 <= risk < 60:
        stage = "Starting Stage"
        message = "Early cardiovascular indicators detected. Lifestyle monitoring recommended."
        category = "risk"

    else:
        stage = "Danger Stage"
        message = "High cardiovascular risk detected. Please consult a cardiologist immediately."
        category = "risk"

    return stage, message, category


def generate_risk_values(base_risk):

    heart_attack = base_risk + random.randint(-5, 5)
    hypertension = base_risk + random.randint(-8, 3)
    stroke = base_risk + random.randint(-7, 4)
    cholesterol = base_risk + random.randint(-10, 2)

    heart_attack = max(0, min(100, heart_attack))
    hypertension = max(0, min(100, hypertension))
    stroke = max(0, min(100, stroke))
    cholesterol = max(0, min(100, cholesterol))

    return heart_attack, hypertension, stroke, cholesterol


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["file"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        retina_conditions = [
            "normal",
            "diabetic_retinopathy",
            "glaucoma",
            "cataract",
            "hypertensive_retinopathy"
        ]

        prediction = random.choice(retina_conditions)

        if prediction == "normal":
            risk_score = random.randint(5, 29)
        else:
            risk_score = random.randint(30, 95)

        heart_attack, hypertension, stroke, cholesterol = generate_risk_values(risk_score)

        stage, message, category = calculate_risk_stage(risk_score)

        return render_template(
            "index.html",
            prediction=prediction,
            image=filepath,
            risk_score=risk_score,
            heart_attack=heart_attack,
            hypertension=hypertension,
            stroke=stroke,
            cholesterol=cholesterol,
            stage=stage,
            message=message,
            category=category
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)