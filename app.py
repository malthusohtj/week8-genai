from flask import Flask, request, render_template
import textblob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def default():
    return render_template("index.html")


@app.route("/sentiment_analysis", methods=["GET", "POST"])
def sentiment():
    return render_template("sentiment_analysis.html")


@app.route("/sentiment_analysis_result", methods=["GET", "POST"])
def sentiment_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return render_template("sentiment_analysis_result.html", r=r)


@app.route("/interest", methods=["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        return render_template("interest_rates.html", result=90.2 - (50.6 * num))
    else:
        return render_template("interest_rates.html", result="Waiting……….")


if __name__ == "__main__":
    app.run()
