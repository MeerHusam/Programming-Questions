# Dolved by myself. Uses graphs and adjacency list
# https://codeforces.com/problemset/problem/129/B

def compute(n, m, adj_list):
    groups = 0
    queue = []

    while adj_list:

        # Check if any students is linked to just one student.
        # In that case, append a tuple of both the numbers
        for val in adj_list:
            length = len(adj_list[val])
            if(length == 1):
                queue.append((val, adj_list[val][0]))

        if not queue:  # If the queue is empty, no more students to reprimand, break the loop
            break
                
        groups += 1

        while len(queue) > 0:
            link = queue.pop()

            # Remove the 2 students from the adjacency list
            if link[0] in adj_list:
                adj_list[link[0]].remove(link[1])
            if link[1] in adj_list:
                adj_list[link[1]].remove(link[0])

            # If a student is no longer linked to anothe student, remove him
            if link[0] in adj_list:
                if len(adj_list[link[0]]) == 0:
                    del adj_list[link[0]]
            
            if link[1] in adj_list:
                if len(adj_list[link[1]]) == 0:
                    del adj_list[link[1]]

    print(groups)

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = {}  

    for _ in range(m):
        a, b = map(int, input().split())

        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []

        adj_list[a].append(b)
        adj_list[b].append(a)

    compute(n, m, adj_list)
