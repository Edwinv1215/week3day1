class Cart:
    items = []


    def add(self):
       
        print('what type of item would you like to add')
        item = input()
        items.append(item)
        print('you have added item' + item)



mycart = Cart()
is_running = True

while is_running:
    print("Enter add, remove, show or quit")
    selection = input()
    if selection == 'add':
        mycart.add() 
    if selection == 'remove':
        print("You are removing")
    if selection == 'show':
        print("You are showing")
    if selection == 'quit':
        is_running = False