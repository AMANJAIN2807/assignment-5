a = {"Alice":85, "isha":75, "tisha":100, "eti":100 ,"rupal": 80}
b=input("enter a name: ")
if b in a:
	print(f"{b}'s marks: {a[b]} ")
else:
	print("student is not found")