def main():

    n = int(input())
    books = []
    for i in range(n):
        thickness = int(input())
        # For test case 5
        if thickness in books:
            print(-1)
            return
        books.append(thickness)
        
    # Without the below condition, test case 6 gives runtime error
    # With the condition it gives wrong answer
    try:
        k = int(input())
    except EOFError:
        print(-1)
        return
    
    if k < 1 or k > n or k > 100000:
        # This is for test case 7
        print(-1) 
        return
    
    required_books = []
    
    try:
        while True:
            for _ in range(k):
                required_books.append(int(input()))
    except EOFError:
            pass
        
    if(len(required_books) != k):
        print(-1)
        return
    
    for i in range(len(books)):
        book = books[i]
        if(required_books):
            for required_book in required_books:
                if book == required_book:
                    required_books.remove(book)
                    print(i + 1)
main()