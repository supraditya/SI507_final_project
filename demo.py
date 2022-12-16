import requests
import helper_functions as helpers
import json as JSON


def branch_data_cleaner(branch_data, branch_commits_dict):
    simplified_data=[]
    for commit in branch_data:
        simplified_commit={}
        simplified_commit["sha"]=commit["sha"]
        simplified_commit["parents"]=commit["parents"]
        simplified_commit["timestamp"]=commit["commit"]["author"]["date"]
        simplified_commit["message"]=commit["commit"]["message"]
        if "branch_name" not in simplified_commit.keys():
            simplified_commit["branches"]=[]
        for key in branch_commits_dict:
            if commit["sha"] in branch_commits_dict[key]:
                simplified_commit["branches"].append(key)
        simplified_data.append(simplified_commit)
    return simplified_data


def main():
    ownername="supraditya"
    repo="test-repo3"
    url=f"https://api.github.com/repos/{ownername}/{repo}/branches"
    headers = {
    'x-rapidapi-host': "api.github.com",
    }
    response=requests.request("GET", url, headers=headers)
    branch_data=JSON.loads(response.text)
    branch_names=[]
    for branch in branch_data:
        branch_names.append(branch["name"])
    
    all_branch_commits_data=[]

    branch_commits_dict={}
    for branch_name in branch_names:
        #Accessing individual branch commit history by inputting branch name as a query parameter into URL
        url=f"https://api.github.com/repos/{ownername}/{repo}/commits?sha={branch_name}"
        headers = {
        'x-rapidapi-host': "api.github.com",
        }
        response=requests.request("GET", url, headers=headers)
        branch_commits=JSON.loads(response.text)
        branch_commits_sha_list=[]
        for commit in branch_commits:
            branch_commits_sha_list.append(commit["sha"])
        branch_commits_dict[branch_name]=branch_commits_sha_list

        cleaned_branch_data=branch_data_cleaner(branch_commits, branch_commits_dict)
        all_branch_commits_data.append(cleaned_branch_data) 
    graph=helpers.adj_matrix_creator(all_branch_commits_data)
    sorted_graph=helpers.graph_sorter(graph)
    node_branch_dict, node_children_dict, node_message_dict=helpers.graph_data_pruner(sorted_graph)
    print("Node Branch Dictionary:")
    print("===============================")
    print(node_branch_dict)
    print()
    print("Node Children Dictionary (Directed Graph):")
    print("===============================")
    print(node_children_dict)
    print()
    print("Node Message Dictionary:")
    print("===============================")
    print(node_message_dict)
    print()
main()