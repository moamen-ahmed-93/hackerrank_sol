

def get_attr_number(node):
    # your code goes here
    num_of_att=0
    num_of_att+=len(node.attrib)
    for c in node:
        #print(c)
        num_of_att+=get_attr_number(c) 
    return num_of_att

