## Sorting.py

##############################################################
#### Quick sort 
def partition(pivot, st, ed, a):
    '''
    Rearrange items in a , so that all items less then pivot are
    prior to pivot item, and all items great then pivot are 
    '''
    l = st
    r = ed
    while r > l:
        while (a[l] < pivot):
            l += 1
        while (r > st and a[r] >= pivot):
            r -= 1
        a[r], a[l] = a[l], a[r]
    a[r], a[l] = a[l], a[r]
    return l


def quicksort(st, ed, a):
    '''
    The quick sort algorithm.
    '''
    if st >= ed:
        return
    i = partition(a[ed], st, ed-1, a)
    a[ed], a[i] = a[i], a[ed]
    quicksort(st, i-1, a)
    quicksort(i+1, ed, a)

#### end of Quick sort
##################################################################


##################################################################
####  shell sorting
def shellsort(st, ed, a):
    '''
    Shell sort.
    using sequence 1, 3, 7, 15, 31, ..., 
    '''
    n = len(a)
    h = 1
    while h < n:
        h = h*2 + 1
    h /= 2
    while h > 0:
        i = 0
        while i < h:
            j = i
            #inner insertion sort
            while j + h < n:
                k = j
                x = a[k+h]
                while  k >= i and x < a[k]:
                    a[k+h] = a[k]
                    k -= h
                if k < j:
                    a[k+h] = x
                j += h
            i += 1
        h /= 2

### End of Shell sorting
###################################################################
        

###################################################################
###        Heap sorting
def fixDown(i, n, a):
    j = i*2
    while j < n:
        if ( j + 1 < n and a[j + 1] > a[j] ):
            j += 1
        if (a[j] > a[i]):
            a[j], a[i] = a[i], a[j]
            i = j
            j = i*2
        else:
            break
                
    
def makeHeap(n, seq):
    i = n-1
    while i > 0:
        fixDown((i-1)/2, n, a)
        i -= 1

def heapsort(seq):
    makeHeap(len(seq), seq)
    i = len(seq)-1
    while i > 0:
        a[i], a[0] = a[0], a[i]
        fixDown(0, i, seq)
        i -= 1
### End of   Heap sort
####################################################################
        
    
if __name__ == '__main__':

    a = []
    b = []
    c = []
    ind = open('data.txt')

    for line in ind:
        x = int(line.strip())
        a.append(x)
        b.append(x)
        c.append(x)
    ind.close()

    heapsort(a)

    hOut = open('heapout.txt', 'w')
    for x in a:
        print >>hOut, x
    hOut.close()

    quicksort(0, len(b)-1, b)
    qOut = open('quickout.txt', 'w')
    for x in b:
        print >>qOut, x
    qOut.close()

    shellsort(0, len(c)-1, c)
    sOut = open('shellout.txt', 'w')
    for x in c:
        print >>sOut, x
    sOut.close()
    
    
    
    
    
