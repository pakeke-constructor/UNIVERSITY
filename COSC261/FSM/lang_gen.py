


def _gen_strings(alpha, strs, length):
    lis = []
    if length <= 0:
        return strs
    
    if length == 1:
        for each in strs:
            for alp in alpha: 
                lis.append(each + alp)
        return lis
    
    for each in strs:
        for alp in alpha:
            lis.append(each + alp)
    return _gen_strings(alpha, lis, length - 1)


def all_strings(alpha, length):
    '''

    Generates all available strings in a language given
    a certain length of the language.

    '''
    alpha_chars = []
    for char in alpha:
        alpha_chars.append(str(char))
        
    if length == 0:
        return ['']


        
    return _gen_strings(alpha_chars, alpha_chars, length - 1)




