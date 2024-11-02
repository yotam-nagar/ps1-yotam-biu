

def test_hello():
    # Define the expected content of hello.py
    original_lines = [
        'greeting = "Hello"\n',
        'name = ""\n',
        'greeting = greeting + name\n',
        'print(greeting)\n'
    ]
    
    # Read the current hello.py file
    with open('hello.py', 'r') as file:
        current_lines = file.readlines()
    
    
    assert len(current_lines) >= len(original_lines)
    line_changes = [i for i in range(len(original_lines)) if current_lines[i] != original_lines[i]]
    assert line_changes == [1]  # Only line 2 should differ
