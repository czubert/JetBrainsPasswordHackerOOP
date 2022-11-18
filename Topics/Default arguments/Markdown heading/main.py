def heading(msg, level=1):
    if level <= 1:
        multiply = 1
    elif level <= 6:
        multiply = level
    else:
        multiply = 6
    
    return f"{multiply * '#'} {msg}"
    
