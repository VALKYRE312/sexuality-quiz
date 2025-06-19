from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Landing page (age form)
@app.route("/")
def index():
    return render_template("index.html")

# Age verification
@app.route("/verify", methods=["POST"])
def verify():
    birth_year = request.form.get("birth_year")
    try:
        birth_year = int(birth_year)
        age = datetime.now().year - birth_year
        if age >= 18:
            return redirect(url_for("quiz"))
        else:
            error = "You must be 18+ to access the quiz."
            return render_template("index.html", error=error)
    except:
        return render_template("index.html", error="Invalid input. Please enter a valid year.")

# Quiz page and result handling
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        answers = {
            "q1": request.form.get("q1"),
            "q2": request.form.get("q2"),
            "q3": request.form.get("q3"),
            "q4": request.form.get("q4"),
            "q5": request.form.get("q5"),
            "q6": request.form.get("q6"),
            "q7": request.form.get("q7"),
            "q8": request.form.get("q8")
        }

        # Simple rules-based logic
        result = ""

        if answers["q1"] == "both" or answers["q6"] == "open_all":
            result = "You may identify as **Bisexual** or **Pansexual** — someone who is open to multiple genders."
        elif answers["q1"] == "same" and answers["q6"] == "gender_specific":
            result = "You may identify as **Homosexual** — someone who is attracted to the same gender."
        elif answers["q1"] == "opposite" and answers["q6"] == "gender_specific":
            result = "You may identify as **Heterosexual** — someone attracted to the opposite gender."
        elif answers["q1"] == "none" and answers["q3"] in ["repulsed", "neutral"]:
            result = "You may identify as **Asexual** — someone who experiences little to no sexual attraction."
        elif answers["q2"] == "rarely" or answers["q3"] == "neutral":
            result = "You may be on the **Graysexual** or **Demisexual** spectrum — attraction may come in specific contexts."
        elif answers["q8"] == "exploring":
            result = "You might be **Questioning** or **Sexually Fluid**, and that’s completely valid. Keep exploring!"
        else:
            result = "Sexuality is a spectrum, and yours might be beautifully unique! 💜"

        return render_template("result.html", result_message=result)

    return render_template("quiz.html")


# Optional result route
@app.route("/result")
def result():
    return render_template("result.html", result_message="Your result will appear here.")

if __name__ == "__main__":
    app.run(debug=True)
