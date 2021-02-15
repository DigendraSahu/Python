from decision_Making import is_leap
import ipaddress
# Correct the malformed time string , for e.g "5:70:65" to "6:11:05"
def malformed_time(a):
    l = a.split(":")
    for i in range(0,len(l)):
        l[i] = int(l[i])
    h = l[0]
    m = l[1]
    s = l[2]
    m = m + s//60
    s = s%60
    h = h + m//60
    m = m%60
    ans = f"{h}:{m}:{s}"
    return ans

# Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018"
def malformed_date(a):
    l = a.split("/")
    for i in range(0,len(l)):
        l[i] = int(l[i])
    d = l[0]
    m = l[1]
    y = l[2]
    if(m == 2):
        if is_leap(y):
            m += d//29
            d %= 29
            y += m//12
            m %= 12
        else:
            m += d//28
            d %= 28
            y += m//12
            m %= 12
    if(m in [4,6,9,11]):
        m += d//30
        d %= 30
        y += m//12
        m %= 12    
    else:
        m += d//31
        d %= 31
        y += m//12
        m %= 12  
    ans = (f"{d}/{m}/{y}")
    return ans
# Convert ip address from "a.b.c.d" format into integer and vice versa
def ip_address(ip):
    try:
        ip=int(ip)
        z=ipaddress.ip_address(ip)
    except:
        ans = ipaddress.ip_address(ip)  
        return(int(ans))

# Given a string, find the mexican wave
def maxican_wave(s):
    ans = []
    for i in range(len(s)):
        ans.append(s[:i]+s[i].upper()+s[i+1:])
    return ans
# Given a number, find the largest number by deleting single digit (order of digits will remain same)
def largest_num_by_del(n):
    i = 1
    max = 0
    while n//i>0:
        temp = (n//(i*10))*i + (n%i)
        if(max<temp):
            max = temp
        i=i*10
    return max
# Given a number, find the largest number by shuffling the digits
def largest_num_shuffle(n):
    li = []
    ans = ""
    while n>0:
        li.append(str(n%10))
        n//=10
    li = sorted(li)
    li = li[::-1]
    ans = ans.join(li)
    return int(ans)
# Compute the word frequency in given message
def char_in_word(word):
    l1 = []
    for letter in word:
        if letter not in l1:
            l1.append(letter)
    return l1
def num_of_occurance(word,character):
    count = 0
    for letter in word:
        if letter == character:
            count+=1
    return count
def word_frequency(message):
    ans = {}
    char_list = char_in_word(message)
    for i in range(0,len(char_list)):
        ans[char_list[i]] = num_of_occurance(message,char_list[i])
    return ans
                    
# Check whether given string is isogram or not
def isIsogram(word):
    for i in range(0,len(word)):
        temp = num_of_occurance(word,word[i])
        if temp>1:
            return False
    return True
# RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF
def RGB_hexa(a):
    ans = "0x"
    for i in a:
        if(i>255 or i<0):
            return None
        else:
            h = hex(i)
            h = h[2:]
            ans = ans + h
    return ans
# Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd
def accumulated(s):
    for i in range(0,len(s)):
        print(s[i].capitalize(),end="")
        for j in range(0,i):
            print(s[i],end="")
        if(i!=len(s)-1):
         print("-",end=" ")
