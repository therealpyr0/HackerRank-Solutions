# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertion_sort(l):
    counter=0
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j+1] = l[j]
            j -= 1
            counter=counter+1
        l[j+1] = key
    print counter


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
