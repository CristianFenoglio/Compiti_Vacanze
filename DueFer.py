def es(name="you"):
    if name=="error":
        raise Exception("you cant hava a friend named 'error'")
        
    return "One for "+name+", one for me."
