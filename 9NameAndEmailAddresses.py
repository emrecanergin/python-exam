

email_name = {'em' : 'emre'}

print('For look up 1')
print('For add new 2')
print('For delete a address 3')
print('For change existing address 4')
print('for exit 0')

while True:
    chooise = int(input())
    if chooise == 1:
       print(email_name)
    
    elif chooise == 2:
       name = input('enter name')
       mail = input('enter mail')
       email_name[name] = mail
    
    elif chooise == 3:
        key = input('name you want to delete')
        email_name.pop(key)
        print(email_name)
    
    elif chooise == 4:
        change = input('name you want change')
        new = input('new value')
        email_name[change] = new
   
    elif chooise == 0:
        file = open('mail_book.txt','r+')
        for key,value in email_name.items():
            file.write('%s:%s\n' % (key, value))
        break

    


    





