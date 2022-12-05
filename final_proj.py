
import requests
import json as JSON
from requests.auth import HTTPBasicAuth

def yesNoValidator(prompt):
    #TODO: Add docstring
    yes_prompts=['yes', 'y', 'sure', 'yep']
    no_prompts=['no', 'n', 'nah', 'nope']
    if prompt.lower() in yes_prompts:
        return True
    elif prompt.lower() in no_prompts:
        return False
    else:
        print("Please enter either yes or no!")
        return None

#This is the driver function
def repo_search(username, repo_name, is_private):
    #TODO: Add docstring
    # print("Welcome to repository visualizer!")
    # print("=================================")
    # username=input("Please enter the repository owner's Github Username: ")
    # repo_name=input("Please enter the repository's name: ")
    url=f"https://api.github.com/repos/{username}/{repo_name}/commits"
    token=""
    while True:
        # is_private=input("Is the repository private? (Y/N): ")
        user_response=yesNoValidator(is_private.lower())
        if user_response==True:
            token=input("Enter the personal access token for this owner: ")
            token="Bearer "+token
            break
        elif user_response==False:
            break
    headers = {
        'x-rapidapi-host': "api.github.com",
        'Authorization': token
        }
    response=requests.request("GET", url, headers=headers)
    fetched_data=JSON.loads(response.text)
    print(f"Fetched data: {fetched_data}")
# main()



