# Create a Dictionary with at least 5 key value pairs of the Student ID and Name
dic={"studentId":1,"studentName":"vikash","address":"Bihar","job":"Software eng","qualification":"B.tech"}
print(dic)
dic[0]="ajay"
print(dic)
new_data = {'c': 3, 'd': 4}
dic.update(new_data)
print(dic)
print(dic["studentName"]) 