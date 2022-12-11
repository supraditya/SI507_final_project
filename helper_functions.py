import cache_functions as cache
import numpy as np

def branch_data_cleaner(branch_data):
    simplified_data=[]
    for commit in branch_data:
        simplified_commit={}
        simplified_commit["sha"]=commit["sha"]
        simplified_commit["parents"]=commit["parents"]
        # simplified_commit={"sha":commit["sha"], "parents":commit["parents"]}
        simplified_data.append(simplified_commit)
    return simplified_data


#Creates directed graph out of consolidated commit history of all branches
def adj_matrix_creator(all_branches_list):
    directed_graph_dict={}
    flattened_list=[]
    for branch in all_branches_list:
        for commit in branch:
            flattened_list.append(commit)
    for commit in flattened_list:
        directed_graph_dict[commit["sha"]]=[]
        for other_commit in flattened_list:
            parents_list=other_commit["parents"]
            for parent_commit in parents_list:
                if commit["sha"] == parent_commit["sha"] and other_commit["sha"] not in directed_graph_dict[commit["sha"]]:
                    directed_graph_dict[commit["sha"]].append(other_commit["sha"])
    return directed_graph_dict    
