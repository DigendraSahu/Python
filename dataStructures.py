# In a given list of elements, all elements are equal except the one.Write a code to find the odd man out (Stray number)
def odd_man_out(l1):
    for i in range(len(l1)):
        for j in range(len(l1)):
            if l1[i]!=l1[j]:
                return l1[j]

# n a given list of elements, find the elements which is close to its mean
def close_to_mean(l1):
    mean_val = sum(l1)/len(l1)
    
