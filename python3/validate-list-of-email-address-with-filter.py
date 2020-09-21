def fun(s):
    # return True if s is a valid email, else return False
    try:
        name,temp=s.split('@')
    except:
        return False
    try:
        site,domain=temp.split('.')
    except:
        return False
    if name.replace("-","").replace("_","").isalnum() == False:
        return False
    if site.isalnum() == False:
        return False
    if domain.isalpha() == False or len(domain)>3:
        return False
    #print(name,site,domain)
    return True
