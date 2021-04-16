employee = {"id":1001,"name":"ani","designation":"software engineer","salary":20000}

print(employee["name"])
print("company" in employee)
employee["company"] = "luminar"
employee["salary"] += 15000
for i in employee :
    print(i , employee[i])


