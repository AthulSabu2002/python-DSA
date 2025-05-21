def areAnagrams(x, y):
    
    x = x.upper()
    y = y.upper()
    
    if len(x) != len(y):
        return False
    
    
    freqx = {}
    
    for ch in x:
        if ch in freqx:
            freqx[ch] += 1
        else:
            freqx[ch] = 1
    
    
    freqy = {}
    for ch in y:
        if ch in freqy:
            freqy[ch] += 1
        else:
            freqy[ch] = 1
            
    for key in freqx:
        if key not in freqy or freqx[key] != freqy[key]:
            return False
    
    return True

print(areAnagrams("lisTen", "silent"))