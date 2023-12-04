import numpy as np
import heapq
import statistics
from copy import deepcopy
from pprint import pprint


def save_input():
    with open("input") as f:
        input_string = f.read()
    lines = input_string.strip().splitlines()
    matrix = []
    for line in lines:
        matrix.append(line.split("-"))

    return matrix


def get_marked_dict(graph):
    mark_dict = {}
    for item in graph:
        for point in item:
            if point not in mark_dict:
                mark_dict[point] = False
    mark_dict["start"] = True
    return mark_dict


def update_graph(graph):
    graph_dict = {}
    for line in graph:
        if "start"  in line:
            line.remove("start")
            try:
                graph_dict["start"].append(line[0])
            except KeyError:
                graph_dict["start"] = [line[0]]
        elif "end" in line:
            line.remove("end")
            try:
                graph_dict[line[0]].append("end")
            except KeyError:
                graph_dict[line[0]] = ["end"]
        else:
            try:
                graph_dict[line[0]].append(line[1])
            except KeyError:
                graph_dict[line[0]] = [line[1]]
            try:
                graph_dict[line[1]].append(line[0])
            except KeyError:
                graph_dict[line[1]] = [line[0]]

    return graph_dict


def part1(input_data):
    ans = []
    stk = []
    # mark_dict = get_marked_dict(input_data)
    graph = update_graph(input_data)
    pprint(graph)
    visit = []

    def dfs(x):
        if x.lower() == x and x != "end":
            visit.append(x)
        if x == 'end':
            ans.append(stk[:])
            return
        for y in graph[x]:
            if y not in visit:
                if y.lower() == y and y != "end":
                    visit.append(y)
                stk.append(y)
                dfs(y)
                stk.pop()
            elif y in visit:
                visit.remove(y)

    stk.append('start')
    dfs('start')
    print(ans)
    return ans


def part1_2(input_data):
    ans = []
    stk = []
    graph = update_graph(input_data)
    pprint(graph)
    visit = []
    ans, stk, visit, graph = dfs2("start", ans, stk, visit, graph)
    return ans


def dfs2(x, ans, stk, visit, graph):
    stk.append(x)
    if x.lower() == x and x != "end":
        visit.append(x)
    if x == 'end':
        ans.append(stk[:])
    else:
        for y in graph[x]:
            if y not in visit:
                ans, stk, visit, graph = dfs2(y, ans, stk, visit, graph)
    stk.pop()
    if x in visit:
        visit.remove(x)
    return ans, stk, visit, graph


def initialize_visit(input_data):
    visit = {}
    for line in input_data:
        for item in line:
            if item == "start":
                visit[item] = 3
            else:
                visit[item] = 0
    return visit


def part1_3(input_data):
    ans = []
    stk = []
    graph = update_graph(input_data)
    visit = initialize_visit(save_input())
    ans, stk, visit, graph = dfs3("start", ans, stk, visit, graph)
    return ans


def check_visit(visit, y):
    if visit[y] < 1:
        return True
    if visit[y] > 1:
        return False

    for item in visit:
        if item in ["start", y]:
            continue
        if visit[item] > 1:
            return False

    return True


def dfs3(x, ans, stk, visit, graph):
    stk.append(x)
    if x.lower() == x and x != "end":
        visit[x] += 1
    if x == 'end':
        ans.append(stk[:])
    else:
        for y in graph[x]:
            # print(visit, y, check_visit(visit, y))
            if check_visit(visit, y):
                ans, stk, visit, graph = dfs3(y, ans, stk, visit, graph)
    stk.pop()
    if visit[x] > 0:
        visit[x] -= 1
    return ans, stk, visit, graph


def main():
    input_data = save_input()
    print(len(part1_3(input_data)))
    #visit = {"a": 0, "b": 1, "c": 1}
    #print(check_visit(visit, "a"))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
