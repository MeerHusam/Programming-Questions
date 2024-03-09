def main():
    m, n = map(int, input().split())
    
    minutes = int(input())        
    
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
        
    # Create a queue which has the infected values
    infected = []    
    
    # Find the num of infected vals initially and add to queue
    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 2:
                infected.append((a, b))                
    
    # Num of people infected
    num_infected = 0
        
    while(minutes > 0):
        
        # Current number of people infected
        current_infected = len(infected)
        
        while(current_infected):
            
            # Dequeue
            current = infected.pop(0)
            
            # Indices of the infected person
            i, j = current[0], current[1]

            # Check if the infected person can also infect it's neighbours
            if i - 1 >= 0 and matrix[i-1][j] == 1:  # Up
                matrix[i-1][j] = 2
                infected.append((i - 1, j))
                num_infected += 1
            if i + 1 < m and matrix[i+1][j] == 1:  # Down
                matrix[i+1][j] = 2
                infected.append((i + 1, j))
                num_infected += 1
            if j - 1 >= 0 and matrix[i][j-1] == 1:  # Left
                matrix[i][j-1] = 2
                infected.append((i, j - 1))
                num_infected += 1
            if j + 1 < n and matrix[i][j+1] == 1:  # Right
                matrix[i][j+1] = 2
                infected.append((i, j + 1))
                num_infected += 1
            
            # The infected person is removed from the list
            current_infected -= 1
            
        minutes -= 10
        
    print(num_infected)
        
main()