from flask import Flask, jsonify
import hashlib
import math
import json
import requests

app = Flask(__name__)

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
def prime(z):
    if int(z) > 1:
        for i in range(2,int(z)):
            if (int(z) % i) == 0:
                return False
        else:
            return True
    else:
        return False      

@app.route('/')
def hi():
    return "Hello world"


@app.route('/md5/<input_string>')
def md5(input_string):
    return jsonify(
        input = input_string, 
        output = hashlib.md5(input_string.encode("utf-8")).hexdigest()
    )
    
@app.route('/factorial/<input_integer>')
def factorial(input_integer):
    if int(input_integer) < 0:
        return "Error: input integer is negative."
    else:
        return jsonify(
            input = int(input_integer),
            output = math.factorial(int(input_integer))
        )

@app.route('/fibonacci/<input_integer>')
def fibonacci(input_integer):
    if int(input_integer) <= 0:
        return "Error: input integer is negative."
    else:
        return jsonify(
            input = int(input_integer),
            output = fib2(int(input_integer))
        )

@app.route('/prime/<input_integer>')
def is_prime(input_integer):
    return jsonify(
        input = int(input_integer),
        output = bool(prime(input_integer))
    )

url = "https://hooks.slack.com/services/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"
@app.route('/slack_alert/<input_string>')
def slack_alert(input_string):
    payload = {"text": str(input_string)}
    resp = requests.post(url, json=payload)
    if resp.status_code == 200:
        result = "Message posted"
    else:
        result = "Message failed to post"
    return jsonify(
        input = input_string,
        output = result
    )

if __name__ == '__main__':
    app.run(ip=0.0.0.0, port=5000)