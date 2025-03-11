import string
##my soln: in c++ theres this thing i think called isal or isalnum; so i think we can use this here; get a string s; make a new string a; which we will actually care about, so you do for int i in range(0,len(s)): if (isal(s[i])) a+=s[i];
#then we willl get a as the string we care about... then you just do for check=true;  for int i=0 i<=len(a)/2 i++: if a[i]!=a[len(a)-i]: check=false; break;
#MOif(check) print(True) else print(False)
def is_palindrome(s: str) -> bool:
    
    a = "".join(c.lower() for c in s if c.isalnum())
    
    
    for i in range(len(a) // 2):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True


s = input().strip()
print(is_palindrome(s))
