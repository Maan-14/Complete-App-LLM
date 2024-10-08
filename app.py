from flask import Flask, render_template, request
from llm import customizable_llm, simple_llm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

chat_history = []

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = simple_llm.simple_llm_chat(user_input)
        chat_history.append({'text': user_input, 'sender': 'user'})
        chat_history.append({'text': bot_response, 'sender': 'bot'})
        return {'bot_response': bot_response}

    return render_template('chatbot.html', chat_history=chat_history)


@app.route('/simple-llm.html', methods=['GET'])
def simple_llm_interface():
        return render_template('simple-llm.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    selected_topic = request.form['topic']
    user_query = request.form['user-query']

    if selected_topic == 'Please select the topic for LLM' or user_query== '':
        return "No selected file or topic or query"

    if selected_topic:
        result = customizable_llm.llm(selected_topic, user_query)
        return render_template('simple-result.html', result=result)
    
if __name__ == '__main__':
    app.run(debug=True)