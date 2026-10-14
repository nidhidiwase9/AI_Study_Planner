from flask import Flask, request, render_template
from gemini_client import gemini_ai_call

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def generate_ai_study_plan():
    if request.method == "GET":
        return render_template("user_input.html")
    elif request.method == "POST":
        l = request.form.get("level")
        t = request.form.get("topic")
        d = request.form.get("days")
        prompt = f"I am a {l} learner, I want to learn {t} in {d} days, Can you generate a day wise roadmap for me. \
                    Give me response in HTML format, which I can embed in <body> tag. Do not generate any extra info/text apart from HTML response."
        resp = gemini_ai_call(prompt)
        return render_template("ai_study_plan.html", resp = resp)

if __name__ == "__main__":
    app.run(debug=True)
