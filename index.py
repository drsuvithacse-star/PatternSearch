from flask import Flask, render_template, request
import os

template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')

app = Flask(__name__, template_folder=template_dir)

# Naive Pattern Search
def naive_search(text, pattern):
    positions = []

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True

        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.append(i)

    return positions


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    positions = []
    count = 0

    if request.method == "POST":

        text = request.form["text"]
        pattern = request.form["pattern"]

        positions = naive_search(text, pattern)
        count = len(positions)

        if count > 0:
            result = "Pattern Found"
        else:
            result = "Pattern Not Found"

    return render_template(
        "index1.html",
        result=result,
        positions=positions,
        count=count
    )


# Required by Vercel
app = app