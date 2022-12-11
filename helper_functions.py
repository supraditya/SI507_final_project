import cache_functions as cache
import numpy as np

def branch_data_converter(branch_data):
    simplified_data=[]
    for commit in branch_data:
        simplified_commit={}
        simplified_commit["sha"]=commit["sha"]
        simplified_commit["parents"]=commit["parents"]
        # simplified_commit={"sha":commit["sha"], "parents":commit["parents"]}
        simplified_data.append(simplified_commit)
    return simplified_data

# def adj_matrix_generator(simplified_branch_data):

#Create adjacency matrix, directed graphs for all branches. Visualize them in frontend

#Try finding a better algo for this. Currently O(n^4) jeez

# def adj_matrix_creator(APP_CACHE, branch_sha_list):
#     directed_graph_dict={}
#     for branch_sha in branch_sha_list:
#         for commit in APP_CACHE[branch_sha]:
#             directed_graph_dict[branch_sha]=[]
#             for other_commits in APP_CACHE[branch_sha]:
#                 for parent_commit in other_commits["parents"]:
#                     if commit["sha"] in parent_commit.items():
#                         directed_graph_dict[branch_sha].append(other_commits["sha"])
#     return directed_graph_dict

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
                if commit["sha"] == parent_commit["sha"]:
                    directed_graph_dict[commit["sha"]].append(other_commit["sha"])
    return directed_graph_dict    