from flask import Flask, render_template, request
import os
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent

app = Flask(__name__)

# Initialize OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "58e8fec7ef2550920e610f044a933a58a834fc4ea1713773ffcb59a3d101bbef"

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
