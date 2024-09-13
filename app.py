from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from src.components.data_transformation import ingestion
from src.components.model_trainer import generation

app = Flask(__name__)

load_dotenv()

vectorstore = ingestion("Done")
model = generation(vectorstore)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get",methods=["GET","POST"])
def get_bot_response():
    msg = request.form['msg']

    results=model.invoke(msg)

    print(f"Result: {results}")
    return jsonify(results)


if  __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8000)  # run with debug mode