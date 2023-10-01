# Purpose: To calculate mean, median, mode, variance, standard deviation, covariance and corelation
def sort_list(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = []
    right = []
    for x in nums[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_list(left) + [pivot] + sort_list(right)

def mean_mode_median(a):
    a=sort_list(a)
    print(a)
    mean=sum(a)/len(a)
    b=mean
    print("Mean is"+ str(b))
    if len(a)%2==0:
        median=(a[int(len(a)/2)]+a[int(len(a)/2)-1])/2
    else:
        median=a[int(len(a)/2)]
    d=median
    print("Median is"+ str(d))
    mode=max(a,key=a.count)
    e=mode
    print("Mode is"+ str(e))
def variance_and_standard_deviation(a):
    a=sort_list(a)
    mean= sum(a)/len(a)
    variance=sum([(x-mean)**2 for x in a])/len(a)
    v=variance
    print("Variance is"+ str(v))
    standard_deviation=variance**0.5
    sd=standard_deviation
    print("Standard deviation is"+ str(sd))
def covariance_and_corelation(a,b):
    a=sort_list(a)
    mean_a= sum(a)/len(a)
    variance=sum([(x-mean_a)**2 for x in a])/len(a)
    v=variance
    standard_deviation=variance**0.5
    sd=standard_deviation
    b=sort_list(b)
    mean_b= sum(b)/len(b)
    covariance=sum([(x-mean_a)*(y-mean_b) for x,y in zip(a,b)])/len(a)
    cv=covariance
    print("Covariance is "+str(cv))
    corelation=covariance/(v*sd)
    cr=corelation
    print("Corelation is "+str(cr))

a=[]
n= int(input("Enter the number of elements in list:"))
print("Enter the elements")
for i in range(0,n):
    j=int(input(""))
    a.append(j)
print(a)
print("what operation do you want to perform?")
print("Enter 1 for calculating Mean, Median and Mode\nEnter 2 for calculating Variance and Standard Deviation\nEnter 3 for adding one more list and calculating Mean, Median and Mode of both lists\nEnter 4 for adding one more list and calculating Variance and Standard Deviation of both lists \nEnter 5 for adding one more list and calculating covariance and corelation between the two\n")
z=int(input("Enter your choice:"))
if z==1:
    mean_mode_median(a)
elif z==2:
    variance_and_standard_deviation(a)
elif z==3:
    l2=[]
    n= int(input("Enter the number of elements in list:"))
    print("Enter the elements")
    for k in range(0,n):
        m=int(input(""))
        l2.append(m)
    mean_mode_median(a)
    mean_mode_median(l2)
elif z==4:
    l2=[]
    n= int(input("Enter the number of elements in list:"))
    print("Enter the elements")
    for k in range(0,n):
        m=int(input(""))
        l2.append(m)
    variance_and_standard_deviation(a)
    variance_and_standard_deviation(l2)
elif z==5:
    l2=[]
    n= int(input("Enter the number of elements in list:"))
    print("Enter the elements")
    for k in range(0,n):
        m=int(input(""))
        l2.append(m)
    covariance_and_corelation(a,l2)
    