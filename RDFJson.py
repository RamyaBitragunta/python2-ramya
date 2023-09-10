import json

# we need to read a file - for that we need to  first open the file , to open that file we have to know the pAth of the file.
# so right click on the file and copy relative path
#here we have to use a method called open and we have to take 2 parameters, one is path(location of file )and other one is
# r- means which open the file in reading mode
# myjsonfile is a variable which refers to open the file
# for reading the file we have to write one command called myjsonfile.read() and have to save in a varible- called jsondata

myjsonfile = open('json project/employee.json','r')
jsondata = myjsonfile.read()

#now this command myjsonfile.read() wil read the data from this file  and we save the data in a variable called json data
# from this jsondata we have to parse it; jsondata will normally in the string format so we need to parse the data in json format
# to parse the json data we need to use a method called loads(this particular method wil parse the data)
# after parsing the data - we need to save them into an object variable.
# and now from this obj we can abstract the data from employee.json
# to abstract the data we have to specify the key
# after abstraction we have to convert that into string and we have to print that one.

obj = json.loads(jsondata)
print(str(obj['firstName']))
print(str(obj['lastName']))
print(str(obj['address']))

# so the address contains 2 elements again these 2 elements are the json objects, so if we want to extract individual elements
# or if we want to get specific values , so in order to get it we need to write loop statement.
# before that we have to save multiple elements in lists
# so we create a variable called lists
# so from the json object which contain address will be saved in lists


list = obj['address']
print(list)
print(list[0])
print(list[1])
print(len(list)) # to count how many elements in json ( here it has 2 elements)
# to read each and individual data from the json array we have to write a loop statement
# i represents the index(element), we use range function
# now we have to extract the data

for i in range(len(list)):
    print("Address of ",i,"is....")
    print(list[i].get("streetAddress"))
    print(list[i].get("city"))
    print(list[i].get("state"))
    print(list[i].get("postalcode"))

