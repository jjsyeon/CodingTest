def solution(s, skip, index):
    answer = ""
    skip_set = [ord(_) for _ in skip]
    alphabets = [word for word in range(ord("a"), ord("z")+1) if word not in skip_set]
    
    for word in s: 
        print((alphabets.index(ord(word)) + index) % 26 + 97)
        answer += chr(alphabets[(alphabets.index(ord(word)) + index) % len(alphabets)])
        
    return answer