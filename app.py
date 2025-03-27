from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
client = Client("hrutikkharjul/Mental-health-chatbot")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    system_message = "You are a psychiatrist and your name is well-being"
    
    result = client.predict(
        message=message,
        system_message=system_message,
        max_tokens=512,
        temperature=0.7,
        top_p=0.95,
        api_name="/chat"
    )
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)