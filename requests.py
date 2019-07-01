import requests
import json

def course_name():
	var = requests.get("http://saral.navgurukul.org/api/courses")
	data = var.json()
	# print(data)
	number = 1
	for i in data:
		for j in data[i]:
			print(number,j["name"])
			number+=1
course_name()

def id_find():
	var = requests.get("http://saral.navgurukul.org/api/courses")
	data = var.json()
	id_list = []
	for i in data:
		for j in data[i]:
			id_list.append(j["id"])
	return id_list
print(id_find())
		
print('')
user_1 = int(input("any number you want chek course "))

def menu_list(user):
	a=id_find()
	# print(len(a))
	number_list = []
	b=len(a)
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i == user:
			# print(i)
			y=a[i-1]
			# print(y)
			link_id = requests.get(" http://saral.navgurukul.org/api/courses/"+str(y)+"/exercises")
			sec_data = link_id.json()
			# print(sec_data)

			for i in sec_data:
				number=1
				for j in sec_data[i]:
					print(number,j["name"])
					number+=1
					a=j["childExercises"]
					for k in a:
						print('	',number,k["name"])
						number+=1
menu_list(user_1)


def slug_menu_list(user):
	list_slug = []
	a=id_find()
	# print(len(a))
	number_list = []
	b=len(a)
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i == user:
			# print(i)
			y=a[i-1]
			# print(y)
			link_id = requests.get(" http://saral.navgurukul.org/api/courses/"+str(y)+"/exercises")
			sec_data = link_id.json()
			# print(sec_data)

			for i in sec_data:
				number=1
				for j in sec_data[i]:
					list_slug.append(number)
					list_slug.append(j["slug"])
					number+=1
					a=j["childExercises"]
					for k in a:
						list_slug.append(number)
						list_slug.append(k["slug"])
						number+=1
	return(list_slug)
print(slug_menu_list(user_1))

def content_find(user,choice):
	list_slug = []
	a=id_find()
	# print(len(a))
	number_list = []
	b=len(a)
	for i in range(1,b+1):
		number_list.append(i)
	# print(number_list)

	for i in number_list:
		if i == user:
			y=a[i-1]
			# print(y)

	find_slug = slug_menu_list(user_1)
	# print(find_slug)
	print('')
	# chouse = int(input("input any number you want open content "))
	print('')
	for i in range(len(find_slug)):
		if choice == find_slug[i]:
			# print(find_slug[i+1])
			new_var= requests.get("http://saral.navgurukul.org/api/courses/"+str(y)+"/exercise/getBySlug?slug="+find_slug[i+1])
			third_data = new_var.json()
			# print(third_data)
			print(third_data["content"])
content_find(user_1,int(input("input any number you want open content ")))



course_name()
print('')
user_1 = int(input("any number you want chek course "))
m=user_1
menu_list(user_1)
print('')
user_5=int(input("input any number you want open content "))
content_find(user_1,user_5)

Next=user_5
while True:
	print('')
	user_3 = input("input/ up=agen_corse/ n=Next/ p=previous/ b=break ")
	if user_3 == "up" or user_3 == "UP":
		course_name()
		print('')
		user_1 = int(input("any number you want chek course "))
		print('')
		menu_list(user_1)
		print('')
		user_5=int(input("input any number you want open content "))
		content_find(user_1,user_5)
	
	elif user_3 == "n" or user_3 == "N":
		content_find(m,Next+1)
		Next+=1

	elif user_3 == "p" or user_3 == "P":
		content_find(m,Next-1)
		Next-=1
	else:
		break
