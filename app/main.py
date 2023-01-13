from flask import Flask
import machinelearning as ml

app = Flask(__name__)
    
@app.route('/')
def hello_world():
    questions = "What is copyleft?"
    context = "copyleft org"
    text = ml.MachineLearning.run_machine_learning(context, questions)
    return text




if __name__ == '__main__':
    app.run(threaded=True, port=5000)