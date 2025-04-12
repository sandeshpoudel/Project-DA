# FILE I/O + ERROR HANDLING (YOUR FIRST PIPELINE)

# Debugging
# Buggy code (fix 3 errors)  
try:
    with open("data.txt", "r") as file:  
        data = file.read() 
        print("File contents:", data)  
except:
    print("No file found")