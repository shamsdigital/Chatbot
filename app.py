from flask import Flask, render_template, request
import os
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent

app = Flask(__name__)

# Initialize OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "1553ad660373407f6742ae1f8560c521e2a45179ef173f05480202a28bc8b3e8"

# Initialize LLM
llm = OpenAI(temperature=0.9)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() in ['exit', 'quit']:
        return "Chatbot: Goodbye!"
    response = agent.run(user_input)
    return "Chatbot: " + response

if __name__ == '__main__':
    app.run(debug=True)
