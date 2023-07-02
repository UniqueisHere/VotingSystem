from datetime import date, datetime
from getpass import getpass
import os

admin_name = 'admin'
admin_password = 'password'

def main():
    
    print("1. Admin")
    print("2. Voter Registration")
    print("3. Cast Vote")
    print("4. Exit")

    userInput = int(input('Enter the number to proceed further: '))
    
    if userInput == 1:
        admin_login_attempt = 0
        
        
        for i in range(1,4):
            input_admin_name = input("Enter username of the admin: ")
            print()
            input_admin_password = getpass('Enter the password of the admin: ')
            print('--------------------------------------')
            
            if admin_login_attempt < 3:
                if input_admin_name == admin_name and input_admin_password == admin_password:
                    admin_actions()  
                else:
                    admin_login_attempt += 1
                    print(f"Sorry the entered user name didn't match the admin credentials. You have attempted {admin_login_attempt} out of 3 times.")
            else:
                exit
                
    elif userInput == 2: 
        voter_registration()
    
    elif userInput == 3: 
        cast_vote()
    
    elif userInput == 4: 
        exit
    
    else:
        print('Only select the number in between 1 - 4')


def admin_actions():
    print('Election Management System: ')
    print('--------------------------------------')
    print('1. Election Schedule')
    print('2. Candidate Registration')
    print('3. Candidate Update')
    print('4. Delete Candidate')
    print('5. List of Candidates')
    print('6. Update Voter')
    print('7. Delete Voter')
    print('8. Voter Search')
    print('9. Voter Results')
    print('10. Logout')
    print('--------------------------------------')
    admin_options = int(input('Enter your choice: '))
    
    if admin_options == 1:
        voting_schedule()
        
    elif admin_options == 2:
        candidate_registration()
        
    elif admin_options == 3:
        update_candidate()
    
    elif admin_options == 4:
        delete_candidate()
    
    elif admin_options == 5:
        list_of_candidate()
    
    elif admin_options == 6:
        update_voter()
    
    elif admin_options == 7:
        delete_voter()
    
    elif admin_options == 8:
        search_voter()
    
    elif admin_options == 9:
        pass
    
    elif admin_options == 10:
        print('--------------------------------------')
        print('Loggin admin out of the system.')
        main()
    
    else:
        print('Please enter the valid option')
        admin_actions()
    
def list_of_candidate():
    try:
        file = open('candidatelist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of candidates are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        # print(contents)
        print('--------------------------------------')
        admin_actions()
        
    except:
        print('No candidate has been registerd till now.')
        print('Please register some candidate to view')
        
        
        
def candidate_registration():
    
    candiate_name = input('Enter the name of the candiadate: ')
    candidate_party = input('Enter the party of the candidate: ')
    candidate_city = input("Enter the location of the candadate: ")
    
    
    candidate_details = f'{candiate_name}|{candidate_city}|{candidate_party}'
    
    

    file = open('candidatelist.txt', 'a+')
    file.writelines(f'{candidate_details}\n')
    file.close()

    
    print('--------------------------------------')
    print('Candidate Successfully Registerd')
    print('--------------------------------------')
    
    admin_actions()



def delete_candidate():
    try:
        file = open('candidatelist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of candidates are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        # print(contents)
        print('--------------------------------------')
        
        line_number = int(input('Enter the candidate to delete: '))
        
        with open('candidatelist.txt') as file:
            lines = file.readlines()
            print(lines)
        
        if line_number <= len(lines):
            del lines[line_number - 1]
            
            with open('candidatelist.txt', 'w') as file:
                for line in lines:
                    file.write(line)
                
        else:
            print(f'No candidate available at number {line_number}')
            print('--------------------------------------')
            
        
    except:
        print('Error!!! No candidate has been registerd till now.')
        print('--------------------------------------')
        


def update_candidate():
    try:
        file = open('candidatelist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of candidates are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        print('--------------------------------------')
        
        line_number = int(input('Enter the candidate to update: '))
        
        
        with open('candidatelist.txt') as file:
            lines = file.readlines()
        
        if line_number <= len(lines):
            candiate_name = input('Enter the name of the candiadate: ')
            candidate_party = input('Enter the party of the candidate: ')
            candidate_city = input("Enter the location of the candadate: ")
            
            
            candidate_details = f'{candiate_name}|{candidate_city}|{candidate_party}'
            
            lines[line_number - 1] = candidate_details + '\n'
            
            with open('candidatelist.txt', 'w') as file:
                for line in lines:
                    file.write(line)
                
        else:
            print(f'No candidate available at number {line_number}')
            print('--------------------------------------')
            
        
    except:
        print('Error!!! No candidate has been registerd till now.')
        print('--------------------------------------')
 
 
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
        
def list_of_voters():
    try:
        file = open('voterlist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of voters are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        # print(contents)
        print('--------------------------------------')
        admin_actions()
        
    except:
        print('No voters has been registerd till now.')
        print('Please register some voters to view')
        
        
        
def voter_registration():
    voter_name = input('Enter the voter name: ')
    voter_dob = input('Enter the voter DOB in yyyymmdd: ')
    voter_address = input('Enter the address of the voter: ')
    voter_password = getpass('Enter the password of the voter: ')
    
    if len(voter_dob) != 8:
        print('Please enter a valid date of birth in the format yyyymmdd.')
    else:
        try:
            voter_dob_datetime = datetime.strptime(voter_dob, '%Y%m%d')
            voter_age = calculate_age(voter_dob_datetime)
            
            if voter_age < 18:
                print('Voter is under 18 years of age. Registration not allowed.')
            else:
                voter_dob_formatted = voter_dob_datetime.strftime('%Y-%m-%d')
                
                final_voter_details = f'{voter_name}|{voter_dob_formatted}|{voter_address}|{voter_password}'
                
                file = open('voterlist.txt', 'a+')
                file.writelines(f'{final_voter_details}\n')
                file.close()

                print('--------------------------------------')
                print('Voter Registered Successfully')
                print('--------------------------------------')
                
        except ValueError:
            print('Invalid date of birth.')
            



def delete_voter():
    try:
        file = open('voterlist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of voters are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        # print(contents)
        print('--------------------------------------')
        
        line_number = int(input('Enter the voter to delete: '))
        
        with open('voterlist.txt') as file:
            lines = file.readlines()
            print(lines)
        
        if line_number <= len(lines):
            del lines[line_number - 1]
            
            with open('voterlist.txt', 'w') as file:
                for line in lines:
                    file.write(line)
                
        else:
            print(f'No voter available at number {line_number} ')
            print('--------------------------------------')
            
        
    except:
        print('Error!!! No voter has been registerd till now.')
        print('--------------------------------------')



def update_voter():
    try:
        file = open('voterlist.txt', 'r')
        contents = file.read().rsplit('\n')
        file.close()
        
        print('The list of voters are: ')
        print('--------------------------------------')
        for i in contents:
            print(i)
        print('--------------------------------------')
        
        line_number = int(input('Enter the voter to update: '))
        
        
        with open('voterlist.txt') as file:
            lines = file.readlines()
        
        if line_number <= len(lines):
            voter_name = input('Enter the voter name: ')
            voter_dob = input('Enter the voter DOB in yyyymmdd: ')
            voter_address = input('Enter the address of the voter: ')
            voter_password = getpass('Enter the password of the voter: ')
            
            try:
                voter_dob_datetime = datetime.strptime(voter_dob, '%Y%m%d')
                voter_age = calculate_age(voter_dob_datetime)
                
                if voter_age < 18:
                    print('Voter is under 18 years of age. Registration not allowed.')
                else:
                    voter_dob_formatted = voter_dob_datetime.strftime('%Y-%m-%d')
                    
                    final_voter_details = f'{voter_name}|{voter_dob_formatted}|{voter_address}|{voter_password}'
                    
                    
                    lines[line_number - 1] = final_voter_details + '\n'
                    

                    with open('voterlist.txt', 'w') as file:
                        for line in lines:
                            file.write(line)
                            
                    print('--------------------------------------')
                    print('Voter Updated Successfully')
                    print('--------------------------------------')
                    
                    
            except ValueError:
                print('Invalid date of birth.')
            
            
                
        else:
            print(f'No candidate available at number {line_number}')
            print('--------------------------------------')
            
        
    except:
        print('Error!!! No voters has been registerd till now.')
        print('--------------------------------------')


def search_voter():
    word = input('Enter the voter name to search: ')
    is_found = False
    try:
        with open('voterlist.txt', "r") as file:
            for line_num, line in enumerate(file, start=1):
                if word in line:
                    is_found = True
                    print(f"{line_num}: {line.strip()}")
                    print(line)
                    
            if not is_found:             
                print(f"The searched voter doesn't exixts")

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("An error occurred:", str(e))

def cast_vote():
    
    name_to_check = input('Please enter your username: ')
    password_to_check = getpass('Please enter your password: ')
    
    try:
        with open('voterlist.txt', "r") as file:
            for line in file:
                data = line.strip().split("|")
                name = data[0]
                password = data[3]
                
            if name == name_to_check and password == password_to_check:
                print("Name and password match!")
                    
            else:
                print("Name and password do not match.")
                print('--------------------------------------')
                main()

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("An error occurred:", str(e))


def check_candidate(candidate_name: str, candidate_party: str):
    try:
        with open('candidate.txt', "r") as file:
            for line in file:
                data = line.strip().split("|")
                name = data[0]
                party = data[3]
                
                if name == candidate_name and party == candidate_party:
                    print("Name and password match!")
                    
            else:
                print("Candidate name or party didn't match")
                print('--------------------------------------')
                main()

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("An error occurred:", str(e))


def voting_schedule():
    voting_location = input('Enter the location of the Election: ')
    voting_date = input('Enter the date for the Election in yyyymmdd: ')
    
    matched = False
    
    if os.path.exists('votingschedule.txt'):
        try:
            date = datetime.strptime(voting_date, "%Y%m%d")
            dates = f'{date.year}-{date.month}-{date.day}'
            print(dates)     
            with open('votingschedule.txt', 'r') as file:
                candidate_details = f'{voting_location}|{dates}'
                for line in file:
                    data = line.strip().split("|")
                    location = data[0]
                    v_date = data[1]
                    
                    if location == voting_location and v_date == dates:
                        matched = True
                if matched:
                    print('Cannot held Election on the same date at the same time.')
                    admin_actions()
                else:
                    with open('votingschedule.txt', 'a') as file:
                        file.write(candidate_details + '\n')
        except ValueError:
            print("Invalid date.")
    
    else:
        with open('votingschedule.txt', 'w') as file:
            pass
    



def cast_vote():
    user_matched = False
    user_name = input('Enter your name: ')
    user_password = getpass('Enter your password: ')
    today = date.today()
    
    with open('voterlist.txt', 'r') as file:
        for line in file:
            data = line.strip().split("|")
            name = data[0]
            password = data[3]
            
            if name == user_name and password == user_password:
                user_matched = True
        else:
            print("User name or password didn't match.")
            
        if user_matched:
            vote_for_candidate = input('Enter the name of candidate to vote: ')
            if os.path.exists('candidatelist.txt'):
                pass
            else:
                print('--------------------------------------')
                print('No candidates are registered till now. Register some candidate.')
                print('--------------------------------------')
                with open('votingrecord.txt', 'w') as file:
                    pass
                
            
    
    # matched = False
    
    # if os.path.exists('votingschedule.txt'):
    #     try:
    #         date = datetime.strptime(voting_date, "%Y%m%d")
    #         dates = f'{date.year}-{date.month}-{date.day}'
    #         print(dates)     
    #         with open('votingschedule.txt', 'r') as file:
    #             candidate_details = f'{voting_location}|{dates}'
    #             for line in file:
    #                 data = line.strip().split("|")
    #                 location = data[0]
    #                 v_date = data[1]
                    
    #                 if location == voting_location and v_date == dates:
    #                     matched = True
    #             if matched:
    #                 print('Cannot hold Election on the same date at the same time.')
    #                 admin_actions()
    #             else:
    #                 with open('votingschedule.txt', 'a') as file:
    #                     file.write(candidate_details + '\n')
    #     except ValueError:
    #         print("Invalid date.")
    
    # else:
    #     with open('votingschedule.txt', 'w') as file:
    #         pass


# main()
cast_vote()




# voting_schedule()