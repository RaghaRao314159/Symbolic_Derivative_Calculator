def bracket_count(char, count):
  if char == "(":
    count += 1
  elif char == ")":
    count -= 1
  return count


def strip_useless_brackets(f):
    if f[0] == "(" and f[-1] == ")":
        return f[1:-1]
    else:
        return f





def additive(f):
    """
    this function takes a large linear combination and breaks down into individual expressions
    1 for +, -1 for -
    """
    booli = True
    poslist, neglist = [],[]
    count = 0
    add = []
    polarity = []
    
    for i in range(len(f)):
        
        a = f[i]

        count = bracket_count(a,count)

        if count == 0:
            if a == "+":
                poslist.append(i)
            elif a == "-":
                neglist.append(i)

    alllist = poslist + neglist
    alllist.sort()

    if len(alllist) == 0:
        return [[f],[1]]
    
    alllist.append(len(f))



    if alllist[0] != 0:
        add.append(remove_useless_bracket(f[:alllist[0]]))
        polarity.append(1)


    for i in range(len(alllist)-1):
        add.append(remove_useless_bracket(f[alllist[i]+1 : alllist[i+1]]))
        polarity.append((lambda x: 1 if alllist[x] in poslist else -1)(i))

    
    
    return [add,polarity]




def multiplicative(f):
    """
    this function takes a large multiplicative combination and breaks down into individual expressions
    """
    booli = True
    mullist = [-1]
    divlist = []
    count = 0
    
    for i in range(len(f)):
        
        a = f[i]

        count = bracket_count(a,count)

        if count == 0:
            if a == "*":
                mullist.append(i)
            elif a == "/":
                divlist.append(i)

    allist = mullist + divlist
    allist.sort()
    
    allist.append(len(f))

    return [(lambda x: strip_useless_brackets(x) if allist[i] in mullist else "(" + strip_useless_brackets(x) + ")^(-1)")(f[allist[i]+1 : allist[i+1]])  for i in range(len(allist) - 1)]



def zero_bracket_count(f,initial_count):
  for i in f:
    initial_count = bracket_count(i, initial_count)
    if initial_count == 0:
      return True
  return False


def remove_useless_bracket(f):
  if f[0] == "(" and f[-1] == ")":
    count = 1
    a = f[1:-1]
    if not zero_bracket_count(a,count):
      return a

  return f

"""
def is_power(f):
  if f[0] == "(" and f[-1]==")" and ")^(" in f:
    power_list = f.split(")^(")
    for i in power_list:
      if zero_bracket_count(i[1:-1],1):
        return False
    return True
  return False

"""

    

def is_num_power(f):
  #assumes not addition
    key = -1
    if f[0] == "(" and f[-1] == ")" and ")^(" in f:
        booli = True
        count =  0
        for i in range(len(f)):
            count = bracket_count(f[i],count)
            
            if count != 0:
                booli = False
            else:
                booli = True

            if booli:
                if f[i] == "^":
                    key = i
                    break
        
        if key > 0:
            #power_list = f.split("^")
            base = f[:key]
            power = f[key+1:]
            for i in range(len(power)):
                if power[i] == ")":
                    power = power[:i+1]
                    break
        

        
            if (not zero_bracket_count(base[1:-1],1)) and ("x" not in power):
                actual_power = float(remove_useless_bracket(power))
                return [True, remove_useless_bracket(base), actual_power]
    return [False, f, 0]
  




def is_trigo(f):
    trig_list =  [ "sin(" , "cos(" , "tan(" ] 
    if f[0:4] in trig_list and f[-1] == ")" and (not zero_bracket_count(f[4:-1],1)):
        return [True, trig_list.index(f[0:4])]
    return [False, -2]


def is_exponent_or_ln(f):
    expo_list = ["e^(" , "ln("]
    if (f[0:3] in expo_list)  and f[-1] == ")" and (not zero_bracket_count(f[3:-1],1)):
        return [True, expo_list.index(f[0:3])]
    return [False,-2]



f = "-2*sin(x+2)+5*cos(x-5)-5"

g = "2*3*sin(x)/(cos(2*x)*5+3)"

h = '(x+3)^(x-3)^(3)'

k = "e^((x+2)^(x+3))+58(3*x+5)"







"""
___RULES___

DO NOT LEAVE SPACES

Functions must have initial and final brackets:
sin( expression ), cos( expression ), tan( expression ),  e^( expression ), ln( expression )

Multiplication must have brackets unless numbers or single letters
( expression )*( expression )*( expression )

e.g. 3*((x)^(4))


Powers, including the base, must all have brackets:
( expression )^( expression )^( expression )


Multiplication: MUST USE *


Division: MUST USE / or ^(-1)


"""


def derivative(f):

    if 'x' not in f:
        return "0"
    
    elif f == "x":
        return "1"

    elif is_trigo(f)[0]:
        angle = f[4:-1]
        diff_angle = derivative(f[4:-1])

        if "x" in diff_angle:
            diff_angle = "(" + diff_angle + ")"
            
        c = is_trigo(f)[1]

        if c == 0:
            if  diff_angle == "1":
                return "cos({})".format(angle)
            else:
                return "{}*cos({})".format(diff_angle,angle)

        elif c == 1:
            if  diff_angle == "1":
                return "-sin({})".format(angle)
            else:
                return "-{}*sin({})".format(diff_angle,angle)
            
        else:
            if  diff_angle == "1":
                return "(sec({}))^(2)".format(angle)
            else:
                return "{}*((sec({}))^(2))".format(diff_angle,angle)


    elif is_exponent_or_ln(f)[0]:
        inside_bracket = f[3:-1]
        diff_inside_bracket = derivative(f[3:-1])

        if "x" in diff_inside_bracket:
            diff_inside_bracket = "(" + diff_inside_bracket + ")"

        c = is_exponent_or_ln(f)[1]

        if c == 0:
            if diff_inside_bracket == "1":
                return "e^({})".format(inside_bracket)
            else:
                return "{}*e^({})".format(diff_inside_bracket,inside_bracket)

        elif c == 1:
            if diff_inside_bracket == "1":
                return "({})^(-1)".format(inside_bracket)
            else:
                return "{}*(({})^(-1))".format(diff_inside_bracket,inside_bracket)
        
        
      
    elif len(additive(f)[0]) == 1 and is_num_power(f)[0]:
        diff_base = derivative(is_num_power(f)[1])
        old_power = is_num_power(f)[2]
        base = is_num_power(f)[1]

        
        if diff_base == "1":
            return "{}*(({})^({}))".format(old_power, base, old_power-1)
        elif "x" not in diff_base:
            return "{}*{}*(({})^({}))".format(old_power,diff_base, base, old_power-1)
        else:
            return "{}*({})*(({})^({}))".format(old_power,diff_base, base, old_power-1)


    elif len(additive(f)[0])== 1:
        ans = ""
        prod = multiplicative(f)
        for i in range(len(prod)):
            partial_ans = ""
            booli2 = True
            for j in range(len(prod)):
                booli1 = True
                if j == i:
                    d = derivative(prod[i])
                    if d != "1" and d!= "0":
                        partial_ans += "({})".format(d)
                    elif d == "1":
                        booli1 = False
                    else:
                        booli2 = False
                        break
    
                else:
                    partial_ans += "({})".format(prod[j])

                if booli1:
                    partial_ans += (lambda x:"*" if x != len(prod)-1 else "")(j)
                    
                

            if booli2:
                if partial_ans[-1] == "*":
                    partial_ans = partial_ans[0:-1]
                ans += remove_useless_bracket(partial_ans)
                ans += (lambda x:"+" if x != len(prod)-1 else "")(i)
            
        return ans

    else:
        add_list, polarity_list = additive(f)[0], additive(f)[1]
        ans = ""
        for i in range(len(add_list)):
            a = derivative(add_list[i])
            if a != "0":
                ans += (lambda x: "+" if polarity_list[x] == 1 else "-")(i)  
                ans += a
            
        if ans[0] == "+":
            return ans[1:]
        
        return ans





stri = "(3*((x)^(4))+(sin(2*x+3))^(-2))/(9*x+4*((x)^(2)))"

stre = "ln((x)^(2))+(x)^(2)"


print(derivative(stre))






            
    
