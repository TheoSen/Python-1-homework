# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:49:44 2023

@author: TheoS
"""
import os
import datetime
import pickle

def create_user(name: str, data: str, password: str, log_file: str = 'logs.txt'):
    
    # get the current path
    path = os.getcwd()
    path = os.path.join(path, name + ".pkl")
    # check name.pkl already exists
    if os.path.exists(path):
        # write attempt in log_file
        with open(log_file,"a") as f:
            f.write(f"Attempted creation of existing user {name} at {datetime.datetime.now()}\n")
            
    else:
        # creat .pkl
        dict = {'name': name, 'data': data, 'password': password, 'last_changed': datetime.datetime.now()}
        
        # why the file must be opened with binary mode???
        with open(name+'.pkl', "wb") as f:
            pickle.dump(dict, f)
            
        # write log_file
        with open(log_file,"a") as f:
            f.write(f'Created user {name} at {datetime.datetime.now()}\n')
            
def login(name: str, password: str, log_file: str = 'logs.txt'):
    
    # get the current path
    path = os.getcwd()
    path = os.path.join(path, name + ".pkl")
    
    #  an attempted login for a given user and the current time should be added to the log file. 
    with open(log_file,"a") as f:
        f.write(f'Attempted login for user {name} at {datetime.datetime.now()}\n')
    # name.pkl does not exist
    if not os.path.exists(path): 
        with open(log_file,"a") as f:
            f.write(f'Attempted login for non-existing user {name} at {datetime.datetime.now()}\n')
            return None
    else:
        # compare password
        with open(path, "rb") as x:
            # save pkl into content
            content = pickle.load(x)
            if password == content['password']:
                # log in sucessfully
                # write in log_file
                with open(log_file,"a") as f:
                    f.write(f'Login successful for user {name} at {datetime.datetime.now()}\n')
                return content['data']
                # print(content['data'])
            else:
                # log in not sucessfully
                with open(log_file,"a") as f:
                    f.write(f'Login failed for user {name} at {datetime.datetime.now()}\n')
                    return None
            

def change_password(name: str, old_password: str, new_password: str, log_file : str = 'logs.txt'):
    # get the current path
    path = os.getcwd()
    path = os.path.join(path, name + ".pkl")
    
    #  an attempted login for a given user and the current time should be added to the log file. 
    with open(log_file,"a") as f:
        f.write(f'Attempted password change for user {name} at {datetime.datetime.now()}\n')
    # name.pkl does not exist
    if not os.path.exists(path): 
        with open(log_file,"a") as f:
            f.write(f'Attempted password change for non-existing user {name} at {datetime.datetime.now()}\n')
    else:
        # compare password
        with open(path, "rb") as x:
            
            # save pkl into content
            content = pickle.load(x)
            if old_password == content['password']:
                
                # log in sucessfully
                # update password and last_changed
                content['password'] = new_password
                content['last_changed'] = datetime.datetime.now()
                # update the pkl file with new content
                with open(path, "wb") as z:
                    pickle.dump(content, z)
                    
                # write in log_file
                with open(log_file,"a") as f:
                    f.write(f'Password change successful for user {name} at {datetime.datetime.now()}\n')
            else:
                # log in not sucessfully
                with open(log_file,"a") as f:
                    f.write(f'Password change failed for user {name} at {datetime.datetime.now()}\n')

                    
create_user('Franz Kafka', 'Die Verwandlung', 'fkafka') 
create_user('H. P. Lovecraft', 'The Call of Cthulhu', 'lcrft') 
create_user('William Golding', 'Lord of the Flies', 'password')
create_user('George Orwell', '1984', 'orwell1948')
login('Franz Kafka', 'fkafks') 
login('Franz Kafka', 'fkafka') 
login('H. P. Lovecraft', 'lcrft')
login('William Golding', 'password')
change_password('William Golding', 'password', 'wigold') 
login('George Orwell', 'orwell1984') 
login('George Orwell', 'orwell1948') 
change_password('George Orwell', 'orwell1984', 'orwell1984') 
change_password('George Orwell', 'orwell1948', 'orwell1984') 
login('George Orwel', 'orwell1984')
create_user('George Orwell', '1984', 'orwell1984')
# with open('F:/Uni/Python/6/William Golding.pkl', "rb") as f:
#     content = pickle.load(f)