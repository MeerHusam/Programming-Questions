# Test case 6 is -1
def main():
    name = input()
    if ' ' in name:
        names = name.split(' ')
        # Take the first name and the lastname
        if len(names[0]) <= len(names[-1]):
            # Test Case 1,5
            encrypted = "".join(sorted(name)).replace(" ", "")
            encrypted += "#"
        else:
            # Test Case 2
            encrypted = "#"
            encrypted += "".join(sorted(name)).replace(" ", "")
    else:
        encrypted = "".join(sorted(name))
    
    if name == encrypted:
        print(-1)
    else:
        print(encrypted)
   
main()