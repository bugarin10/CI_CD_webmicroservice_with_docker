from flask import Flask, request, jsonify
from utils import text_split, embedding

app = Flask(__name__)

app.config["SECRET_KEY"] = "123"


@app.route("/process_text", methods=["POST"])
def process_text():
    if request.method == "POST":
        data = request.get_json()
        text = data["text"]

        # Split text into chunks
        chunks = text_split(text)

        # Get embeddings for each chunk
        embeddings = embedding(chunks)

        response_data = {
            "chunks": chunks,
            "embeddings": embeddings.tolist(),  # Convert numpy array to list for JSON serialization
        }

        return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
