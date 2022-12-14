import cache_functions as cache
import numpy as np

def branch_data_cleaner(branch_data):
    simplified_data=[]
    for commit in branch_data:
        simplified_commit={}
        simplified_commit["sha"]=commit["sha"]
        simplified_commit["parents"]=commit["parents"]
        simplified_commit["timestamp"]=commit["commit"]["author"]["date"]
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

        #Adding commit timestamp as first element in the array (for ordering)
        directed_graph_dict[commit["sha"]].append(commit["timestamp"])

        for other_commit in flattened_list:
            parents_list=other_commit["parents"]
            for parent_commit in parents_list:
                if commit["sha"] == parent_commit["sha"] and other_commit["sha"] not in directed_graph_dict[commit["sha"]]:
                    directed_graph_dict[commit["sha"]].append(other_commit["sha"])
    return directed_graph_dict    

# def first_commit_finder(directed_graph):
#     for key in directed_graph:
#         flag=0
#         for value in directed_graph.values():
#             if key in value:
#                flag=1
#                break
#         if flag==0:
#             return key 

def adj_matrix_sorter(directed_graph):
    #sorting directed_graph keys by their timestamps, which is the first element within the value of each key (values are lists)
    sorted_directed_graph = {key: val for key, val in sorted(directed_graph.items(), key = lambda ele: ele[1][0])}

    #Now, we remove the timestamps from the directed graph structure as it has served its purpose
    for key in sorted_directed_graph:
        sorted_directed_graph[key]=sorted_directed_graph[key][1:]

    return sorted_directed_graph