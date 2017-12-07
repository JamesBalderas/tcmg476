from flask import Flask, request, jsonify 
import os
from hashlib import md5
import json 
import math
import requests



app = Flask(__name__)

@app.route("/")
def hello():
	html = "<h3>Hello {name}!</h3>" \
		   "<b>Hostname:</b> {hostname}<br/>" \
		   "<b>Visits:</b> {visits}"
	#return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
	return html.format(name='world', hostname='localhost', visits='who knows')

#md5hash
@app.route("/md5/<user_input>")
def md5_resp(user_input):
#def md5_resp():

	#user_input = request.args.get('q', 'foobar')
	resp = md5(user_input).hexdigest()
	json_object = {
		'input': user_input, 
		'output': resp
	}
	return json.dumps(json_object)
 
#factorial 
def fact(n):
	if n > 0:
		return n * fact(n-1)
	else: 
		return 1

@app.route("/factorial/<int:user_input>")
def factorial_resp(user_input):
	return jsonify(
		input = user_input,
		output = fact(user_input)
			)


#fibonacci
def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

@app.route("/fibonacci/<int:user_input>")
def fibonacci_resp(user_input):
	 if int(user_input) <= 0:
	 	return "Error: input integer is negative "
   	 else:
		return jsonify(
            input = int(user_input),
            output = fib2(int(user_input))
        )

#is_prime
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True	



@app.route("/is-prime/<int:user_input>")
def i_prime(user_input):
	return jsonify(
		input = user_input,
		output = is_prime(user_input)
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
	




#@app.route("/kv-retrieve/<string:user_input>")





#@app.route("/kv-")





        

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)