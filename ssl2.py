import random
import array


#acct no + random1 + account type + random2
acct_no = str(input())
account_type = ["admin","contibutor", "support" ,"viwer"]
random1 = str(random.randint(10000,99999))
random2 = str(random.randint(10000,99999))
print("1-#admin 2-#contibutor 3-#support 4-#viwer")
opp = int(input())
def sslop(op):
    match op:
        case 1:
            return "admin"
        case 2:
            return "contributor"
        case 3:
            return "support"
        case 4:
            return "viewer"    
        case default:
            return "something"

y = sslop(opp)
print(acct_no+random1+y+random2)
