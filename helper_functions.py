import cache_functions as cache
import numpy as np


def branch_data_cleaner(branch_data, APP_CACHE):
    '''
    Function accepts the fetched API data for a given github branch, and removes the unnecessary information
    out of it

    PARAMETERS
    ===============
    branch_data: JSON Object
    Contains the fetched API data for a given branch within the repository

    APP_CACHE: JSON Object
    Contains the application cache, passed in by the calling function

    RETURNS
    ===============
    simplified_data: list
    A list containing only the data deemed necessary for the application's functionality
    These include the commit SHA, the commit's list of parents, its creation timestamp, and the commit message

    '''
    simplified_data=[]
    for commit in branch_data:
        simplified_commit={}
        simplified_commit["sha"]=commit["sha"]
        simplified_commit["parents"]=commit["parents"]
        simplified_commit["timestamp"]=commit["commit"]["author"]["date"]
        simplified_commit["message"]=commit["commit"]["message"]
        if "branch_name" not in simplified_commit.keys():
            simplified_commit["branches"]=[]
        for key in APP_CACHE["branch_commits_dict"]:
            if commit["sha"] in APP_CACHE["branch_commits_dict"][key]:
                simplified_commit["branches"].append(key)
        simplified_data.append(simplified_commit)
    return simplified_data


#Creates directed graph out of consolidated commit history of all branches
def adj_matrix_creator(all_branches_list):
    '''
    This function creates a directed graph-like dictionary out of the commit from ALL the branches
    within a given github repository. Note that its not a perfect directed-graph as it contains extra
    list items, as mentioned in branch_data_cleaner

    PARAMETERS
    ====================
    all_branches_list: list
    A list containing (along with the extra information) dictionaries for every commit in EVERY branch within the
    github repository

    RETURNS
    ====================
    directed_graph_dict: dict
    A dictionary in which the key is the parent node, and the value is a list containing the extra information,
    and all of the nodes' children commit SHAs
    
    '''
    directed_graph_dict={}
    flattened_list=[]
    for branch in all_branches_list:
        for commit in branch:
            flattened_list.append(commit)
    for commit in flattened_list:
        directed_graph_dict[commit["sha"]]=[]

        #Adding commit timestamp as first element in the array (for ordering)
        directed_graph_dict[commit["sha"]].append(commit["timestamp"])
        directed_graph_dict[commit["sha"]].append(commit["branches"])
        directed_graph_dict[commit["sha"]].append(commit["message"])

        for other_commit in flattened_list:
            parents_list=other_commit["parents"]
            for parent_commit in parents_list:
                if commit["sha"] == parent_commit["sha"] and other_commit["sha"] not in directed_graph_dict[commit["sha"]]:
                    directed_graph_dict[commit["sha"]].append(other_commit["sha"])
    return directed_graph_dict    

def graph_sorter(directed_graph):
    '''
    This function essentially 'sorts' the directed_graph dictionary using the commit timestamps.
    A direct string comparison between each commit's timestamp is sufficient for this

    PARAMETERS
    ===============================
    directed_graph: dict
    A dictionary containing the output returned by adj_matrix_creator()

    RETURNS
    ===============================
    sorted_directed_graph: dict
    The sorted directed_graph (in order of timestamps)

    '''

    #sorting directed_graph keys by their timestamps, which is the first element within the value of each key (values are lists)
    sorted_directed_graph = {key: val for key, val in sorted(directed_graph.items(), key = lambda ele: ele[1][0])}
    return sorted_directed_graph

def graph_data_pruner(directed_graph):
    '''
    This function removes the extra information from the directed_graph variable (introduced in the adj_matrix_creator() function)
    and returns several separate dictionaries for application usage.

    PARAMETERS
    ==================================
    directed_graph: dict
    The output returned by the function graph_sorter(). Is a dictionary containing the directed graph sorted in order of
    the commit timestamps.

    RETURNS
    ==================================
    
    branches_graph: dict
    A dictionary whose keys are the parent commit node SHAs, and values are lists containing all the branches within
    the repo it belongs to
    
    children_graph: dict
    A dictionary whose keys are the parent commit node SHAs, and values are lists containing all the children commit SHAs
    for that commit

    message_graph: dict
    A dictionary whose keys are the parent commit node SHAs, and values are lists containing the commit messages for those nodes
    
    '''
    branches_graph={}
    children_graph={}
    message_graph={}
    for key in directed_graph:
        branches_graph[key]=directed_graph[key][1:2]
        children_graph[key]=directed_graph[key][3:]
        message_graph[key]=directed_graph[key][2:3]
    return branches_graph, children_graph, message_graph

