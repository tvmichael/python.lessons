#while

unconfirmed_users = ['Djo', 'Richard', 'Deni', 'Piter']
confirmed_user = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # pop() - бере зі списку останній елемент
    print(current_user)
