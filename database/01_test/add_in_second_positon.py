def add_in_second_position(content:str, target_str:str)->str:
    s2 = s.split(target_str)
    # s2 =['d', ' b ', ' c ', ' css']
    s2[2] += 'bat log ...' 
    return target_str.join(s2)


if __name__ == "__main__":
    s = "da b a c a css"
    s2 = add_in_second_position(s,'a')
    print(s2)
    
