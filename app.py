
try:
    from pathlib import Path
    import os
    import requests
    from requests.auth import HTTPBasicAuth
    import cache_functions as cache
    import helper_functions as helpers

    #Following line is for development purposes ONLY, will be needed to execute OAuth in http localhost servers
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    from dotenv import load_dotenv
    load_dotenv()
    env_path=Path('.','.env')
    load_dotenv(dotenv_path=env_path)
    from flask import Flask,render_template,url_for,request,redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
except Exception as e:
    print("Some Modules are Missing {}".format(e))


app = Flask(__name__)
app.config["SECRET_KEY"]=os.getenv('SECRET_KEY')

github_blueprint = make_github_blueprint(client_id=os.getenv('CLIENT_ID'),
                                         client_secret=os.getenv('CLIENT_SECRET'), scope='repo')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

APP_CACHE=cache.open_cache()


@app.route('/', methods=['POST', 'GET'])
def github_login():
    '''
    Function handles the OAuth logic for github's API
    '''
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            if cache.is_entry_in_cache(APP_CACHE, account_info_json)==False:
                APP_CACHE['account_info']=account_info_json
                cache.save_cache(APP_CACHE)
            return render_template("credentials.html", account_name=account_info_json['login'])

    return '<h1>Request failed!</h1>'

@app.route('/result', methods=['POST', 'GET'])
def result():
    '''
    Function renders the result page with fetched and processed data
    '''
    if request.method=='POST':
        ownername=APP_CACHE['account_info']['login']
        repo_name=request.form['reponame']
        if cache.is_entry_in_cache(APP_CACHE, repo_name)==False:
            APP_CACHE['repo_name']=repo_name
            cache.save_cache(APP_CACHE)  

        #Fetching information on all branches within the given repo
        branch_url=f"/repos/{ownername}/{APP_CACHE['repo_name']}/branches"
        branch_data=github.get(branch_url)

        #If fetch worked
        if branch_data.ok:
            branch_data_json=branch_data.json()
            if cache.is_entry_in_cache(APP_CACHE, branch_data_json)==False:
                APP_CACHE['branch_data']=branch_data_json
                cache.save_cache(APP_CACHE)          
            branch_names=[]
            for branch in APP_CACHE['branch_data']:
                branch_names.append(branch["name"])
            if cache.is_entry_in_cache(APP_CACHE, branch_names)==False:
                #Making a list of just the names of every branch in the repo
                APP_CACHE['branch_names']=branch_names
                cache.save_cache(APP_CACHE)
        else:
            #If fetch failed
            return render_template('result.html')  
        all_branch_commits_data=[]

        branch_commits_dict={}


        for branch_name in APP_CACHE['branch_names']:
            #Accessing individual branch commit history by inputting branch name as a query parameter into URL
            url=f"/repos/{ownername}/{repo_name}/commits?sha={branch_name}"
            branch_commits=github.get(url)

            if branch_commits.ok:
                branch_commits_json=branch_commits.json()
                branch_commits_sha_list=[]
                #Making a list of commit SHAs present with the fetched branch data
                for commit in branch_commits_json:
                    branch_commits_sha_list.append(commit["sha"])
                #Added the list of branch commit SHAs into a dictionary, and then caching it
                branch_commits_dict[branch_name]=branch_commits_sha_list
                if cache.is_entry_in_cache(APP_CACHE, branch_commits_dict)==False:
                    APP_CACHE['branch_commits_dict']=branch_commits_dict
                    cache.save_cache(APP_CACHE) 

                #Cleaning the fetched API data from the branch to only keep the required data
                cleaned_branch_data=helpers.branch_data_cleaner(branch_commits_json, APP_CACHE)

                #Appending the list to a list that will eventually contain the cleaned branch data for EVERY branch in
                #the repository
                all_branch_commits_data.append(cleaned_branch_data)

        #Creating a directed-graph like structure (with additional data) out of the recently made list
        graph=helpers.adj_matrix_creator(all_branch_commits_data)

        #Sorting the directed graph dictionary according to commit timestamps
        sorted_graph=helpers.graph_sorter(graph)

        #Separating the additional information into separate dictionaries, creating a pure directed-graph
        node_branch_dict, node_children_dict, node_message_dict=helpers.graph_data_pruner(sorted_graph)

        #Rendering data within result.html
        return render_template('result.html', graph=graph, node_message_data=node_message_dict, node_children_data=node_children_dict, node_branch_data=node_branch_dict, first_commit=list(node_branch_dict.keys())[0], branch_names=APP_CACHE["branch_names"])

if __name__ == "__main__":
    app.run(debug=True)

