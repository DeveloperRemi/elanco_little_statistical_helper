import requests
import json
from collections import Counter
import operator
import itertools

class methodsss:

	def __init__():
		pass


	# publicly accessible list of top tens options
	top_tens = ["Highest cost resources", "Lowest cost resources", "Most used resources", "Least used resources", "Highest cost apps", "Lowest cost apps", "Most used apps", "Least used apps"]

	#send request of RESOURCES, process and sort alphabetically
	def send_request_res():
		url = "https://engineering-task.elancoapps.com/api/resources"
		response_url = requests.get(url)
		convert_to_text = response_url.text
		convert_to_list = json.loads(convert_to_text)
		sorted_list = sorted(convert_to_list, key=str.lower)
		return sorted_list

	#send request of APPLICATIONS, process and sort alphabetically
	def send_request_apps():
		url = "https://engineering-task.elancoapps.com/api/applications"
		response_url = requests.get(url)
		convert_to_text = response_url.text
		convert_to_list = json.loads(convert_to_text)
		sorted_list = sorted(convert_to_list, key=str.lower)
		return sorted_list

	#compute total cost of a list entity
	def total_cost(some_list):
		new_list = [i["Cost"] for i in some_list]
		converted_to_f = [float(j) for j in new_list]
		result = sum(converted_to_f)
		return result
	
	#computer total consumed quantity
	def consumed_quantity(some_list):
		new_list = [i["ConsumedQuantity"] for i in some_list]
		converted_to_f = [float(j) for j in new_list]
		result = sum(converted_to_f)
		return result

	#compute average cost of a list entity
	def average_cost(some_list):
		lst_size = len(some_list)
		result = methodsss.total_cost(some_list) / lst_size
		return result

	#compute total cost of a list entity
	def time_frame(some_list):
		result = []
		new_list = [i["Date"] for i in some_list]
		result.append(min(new_list))
		result.append(max(new_list))
		return result

	#compute most popular location of a list entity
	def location_counter(some_list):
		new_list = [i["Location"] for i in some_list]
		words = str([word for word, word_count in Counter(new_list).most_common(1)])
		result = words.replace('[','').replace("'",'').replace("]",'')
		return result

	#compute top or bottom APPLICATIONS
	def top_applications(some_list, var):
		complete = ""
		top_ten_cost = {}
		dictlist = []
		for i in some_list:
			url = "https://engineering-task.elancoapps.com/api/applications/" + i
			response_url = requests.get(url)
			convert_to_text = response_url.text
			convert_to_list = json.loads(convert_to_text)

			if var == methodsss.top_tens[6] or var == methodsss.top_tens[7]:

				new_list = [i["ConsumedQuantity"] for i in convert_to_list]
				converted_to_f = [float(j) for j in new_list]
				result = sum(converted_to_f)

				top_ten_cost[i] = result

			else:
				new_list = [i["Cost"] for i in convert_to_list]
				converted_to_f = [float(j) for j in new_list]
				result = sum(converted_to_f)

				top_ten_cost[i] = result

		if var == methodsss.top_tens[4] or var == methodsss.top_tens[6]:

			sorted_d = dict( sorted(top_ten_cost.items(), key=operator.itemgetter(1),reverse=True))
			
			temp = []
			for key, value in sorted_d.items():
				temp = [key, value]
				dictlist.append(temp)
				

		elif var == methodsss.top_tens[5] or var == methodsss.top_tens[7]:
			sorted_d = dict( sorted(top_ten_cost.items(), key=operator.itemgetter(1)))
			#dictlist = []
			temp = []
			for key, value in sorted_d.items():
				temp = [key, value]
				dictlist.append(temp)
				

		

		result = methodsss.convert_dict_to_list(dictlist, var)

		return result

	# convert a dictionary to list
	def convert_dict_to_list(some_dict, var):
		complete = ""
		x=0
		while x < 10:
			temp = str(some_dict[x])
			
			temp2 = temp.replace('[',"").replace(']',"").replace("'","")
			temp3 = temp2.split(", ")
			if var == methodsss.top_tens[0] or  var == methodsss.top_tens[1] or var == methodsss.top_tens[4] or  var == methodsss.top_tens[5]:
				complete = complete + str(x+1) + ": " + temp3[0] + " - Cost: " + temp3[1] +"\n"
				x+=1
			else:
				complete = complete + str(x+1) + ": " + temp3[0] + " - Consumed quantity: " + temp3[1] +"\n"
				x+=1

		return complete

	#compute top or bottom RESOURCES
	def top_resources(some_list, var):
		complete = ""
		top_ten_cost = {}
		dictlist = []
		for i in some_list:
			url = "https://engineering-task.elancoapps.com/api/resources/" + i
			response_url = requests.get(url)
			convert_to_text = response_url.text
			convert_to_list = json.loads(convert_to_text)

			if var == methodsss.top_tens[2] or var == methodsss.top_tens[3]:

				new_list = [i["ConsumedQuantity"] for i in convert_to_list]
				converted_to_f = [float(j) for j in new_list]
				result = sum(converted_to_f)

				top_ten_cost[i] = result

			else:
				new_list = [i["Cost"] for i in convert_to_list]
				converted_to_f = [float(j) for j in new_list]
				result = sum(converted_to_f)

				top_ten_cost[i] = result

		if var == methodsss.top_tens[0] or var == methodsss.top_tens[2]:

			sorted_d = dict( sorted(top_ten_cost.items(), key=operator.itemgetter(1),reverse=True))
			
			temp = []
			for key, value in sorted_d.items():
				temp = [key, value]
				dictlist.append(temp)
				

		elif var == methodsss.top_tens[1] or var == methodsss.top_tens[3]:
			sorted_d = dict( sorted(top_ten_cost.items(), key=operator.itemgetter(1)))
			#dictlist = []
			temp = []
			for key, value in sorted_d.items():
				temp = [key, value]
				dictlist.append(temp)
				

		

		result = methodsss.convert_dict_to_list(dictlist, var)

		return result

		

		

		#RENAME

	#determine which top tens option was selected
	def which_top_selection(var):


		if var == methodsss.top_tens[0] or var == methodsss.top_tens[1] or var == methodsss.top_tens[2] or var == methodsss.top_tens[3]:

			convert_to_list = methodsss.send_request_res()

			if var == methodsss.top_tens[0]:
				result = methodsss.top_resources(convert_to_list, var)
			elif var == methodsss.top_tens[1]:
				result = methodsss.top_resources(convert_to_list,var)
			elif var == methodsss.top_tens[2]:
				result = methodsss.top_resources(convert_to_list,var)
			elif var == methodsss.top_tens[3]:
				result = methodsss.top_resources(convert_to_list,var)

		else:
			convert_to_list = methodsss.send_request_apps()
			if var == methodsss.top_tens[4]:
				result = methodsss.top_applications(convert_to_list, var)
			elif var == methodsss.top_tens[5]:
				result = methodsss.top_applications(convert_to_list,var)
			elif var == methodsss.top_tens[6]:
				result = methodsss.top_applications(convert_to_list,var)
			elif var == methodsss.top_tens[7]:
				result = methodsss.top_applications(convert_to_list,var)


		return result
			
	

	
