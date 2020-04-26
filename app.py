# using flask_restful 
from flask import Flask, jsonify, request, send_file
from flask_restful import Resource, Api 
import glob, io
import random

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 


class Hello(Resource): 

	def get(self): 
		return jsonify({'message': '“But it’s in the nature of progress that it erases its tracks, and its champions fixate on the remaining injustices and forget how far we have come.” ― Steven Pinker, Enlightenment Now: The Case for Reason, Science, Humanism, and Progress'}) 


	def post(self): 		
		data = request.get_json()	 # status code 
		return jsonify({'data': data}), 201

class GetEnlightmentCharts(Resource): 

	def get(self): 
		images = glob.glob("./charts/*.jpg")
		chart = random.choice(images)
		return send_file(chart, 
                     attachment_filename=chart,
                     mimetype='image/jpg')



# defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(GetEnlightmentCharts, '/chart') 


if __name__ == '__main__': 

	app.run(debug = True) 
