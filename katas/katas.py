## Count the number of divisors of a positive integer n.

def divisors(n):
    list_of_divs = [div for div in range(1, n+1) if n % div == 0]
    return len(list_of_divs)

# Learnings: sum is fast so sum(1 for div in range(1, n+1) if n % div == 0) is better
# # also could have used lambda


#####################################################
## 
