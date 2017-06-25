import requests
import pprint

reminder = {
    'description': 'Shit I gotta take the gf out tonight!',
    'when': 'today at 9 pm'
}

print("Paul! First, check out http://localhost:7878/tasks")
print("It's hooked to your db and pulls the next task coming up.")
print("I filled it with some stuff for this example.")
print()

print("Here a new reminder we want to set for ourselves.")
pprint.pprint(reminder)
go = input("Press enter to POST this new reminder to your API. (Type n then enter to cancel)")
if go == 'n':
    print("Canceled")
    exit()

requests.post('http://localhost:7878/tasks', params=reminder)
print()
print("Request posted, check out http://localhost:7878/tasks now..")