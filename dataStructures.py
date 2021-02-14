# In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)
def odd_man_out(l1):
    if l1[0]!=l1[1] and l1[2]==l1[2]:
        return l1[0]
    else:
        for i in range(len(l1)):
            for j in range(len(l1)):
                if l1[i]!=l1[j]:
                    return l1[j]
# In a given list of elements, find the elements which is close to its mean
def close_to_mean(l1):
    minimum = 10000
    mean_val = sum(l1)/len(l1)
    for i in range(0,len(l1)):
        if minimum>abs(mean_val-l1[i]):
            minimum = mean_val-l1[i]
            ans = l1[i]
    return ans

# Find the average speed of vehicle, given the distance travelled for fixed time intervals, e.g. [0, 0.1, 0.25, 0.45, 0.55, 0.7, 0.9, 1.0]
def avg_speed(l):
    l1 = []
    for i in range(0,len(l)-1):
        l1.append(l[i+1]-l[i])
    return sum(l1)/len(l1)

# Find the no.of people in a bus, given the data of people onboarding & alighting at each station
def no_of_people(onboarding,alighting):
    return sum(onboarding)-sum(alighting)

#Find the missing number, given the original list and modified one
def missing(l1,mod_l1):
    ans = []
    for i in range(0,len(l1)):
            if l1[i] not in mod_l1:
                ans.append(l1[i])
    return ans

#Find the difference between two lowest numbers in the list
def difference_of_lowest_two(l1):
    a = min(l1)
    l1.remove(a)
    b = min(l1)
    return abs(a-b)

#In a given list, count no.of elements smaller than their mean
def smaller_than_mean(l1):
    count = 0
    mean = sum(l1)/len(l1)
    for i in range(0,len(l1)):
        if(l1[i]<mean):
            count+=1
    return count
