def reverse_my_word(word):
    
    reversed_word = ""
    
    
    position = len(word) - 1  # This points to the very last letter ('n')
    
    
    while position >= 0:
        
        reversed_word = reversed_word + word[position]
        
        
        position = position - 1
        
    
    return reversed_word