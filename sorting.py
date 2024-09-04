# Imports for inf and math.floor
from cmath import inf
import math

# File array for quick accessing of file name
fileName = ["pokemonRandomSmall.csv", "pokemonRandomMedium.csv", "pokemonRandomLarge.csv", 
            "pokemonReverseSortedSmall.csv", "pokemonReverseSortedMedium.csv", "pokemonReverseSortedLarge.csv",
            "pokemonSortedSmall.csv", "pokemonSortedMedium.csv", "pokemonSortedLarge.csv"]

# Runtime arrays for storing the counters and file used for the trial
insertRun = []
quickRun = []
mergeRun = []

# Counter variables to count comparisons made during a trial 
insertCount = 0
quickCount = 0
mergeCount = 0

# Array to be passed into the sorts
pokeStat = []

# Insertion sort module definition - COMPLETE
def insertion(statArr):

    global insertCount

    for i in range (1, len(statArr)):

        currStat = statArr[i]
        j = i-1

        while (j >= 0 and currStat[1] < statArr[j][1]) or (currStat[1] == statArr[j][1] and currStat[0] < statArr[j][0]): # Tie breaker after the or
                statArr[j+1] = statArr[j]
                j -= 1
                insertCount += 1

        statArr[j+1] = currStat

    return statArr

# Quick sort paritition module definition - COMPLETE
def partition(statArr, p, r):

    global quickCount

    x = statArr[r]
    i = p

    for j in range(p, r):
        if x[1] == statArr[j][1] and x[0] < statArr[j][0]: # Also handles the tie breaker by placing incrementally
            quickCount += 1
        elif statArr[j][1] <= x[1]:
            statArr[j], statArr[i] = statArr[i], statArr[j]
            i += 1
            quickCount += 1

    statArr[i], statArr[r] = statArr[r], statArr[i]
    return i

# Quick sort primary module definition - COMPLETE
def quick(statArr, p, r):

    if p < r:
        q = partition(statArr, p, r)
        quick(statArr, p, q-1)  # Left values
        quick(statArr, q+1, r)  # Right values

    return statArr

# Merge for merge sort module definition - COMPLETE
def merge(statArr, p, q, r):

    global mergeCount # for tracking num of comparisons

    n1 = int(q - p + 1)
    n2 = int(r - q)
    
    L = [0] * n1
    R = [0] * n2

    for i in range (n1):
        L[i] = statArr[p + i]

    for j in range (n2):
        R[j] = statArr[q + j + 1]

    L.append([inf,inf])
    R.append([inf,inf])
    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i][1] < R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]): # Also includes a section of code to handle tie breaker after the or
            statArr[k] = L[i]                                               # by comparing the actual IDs and ensuring they are placed incrementally
            i = i + 1
            mergeCount += 1
        else: 
            statArr[k] = R[j]
            j = j + 1
            mergeCount += 1

# Merge sort module definition - COMPLETE
def merge_sort(statArr, p, r):
    if p < r:
        q = int(math.floor(((p+r)/2))) # define q as point in statArr that is divided
        merge_sort(statArr, p, q)
        merge_sort(statArr, q+1, r)
        merge(statArr, p, q, r)

    return statArr

# Create and return an array holding the values of the designated spreadsheet
def sortMaker(list):
    file = open(list, "r") 
    text = file.readlines()
    text.pop(0)

    for i in range(len(text)):
        text[i] = text[i].rstrip("\n")
        text[i] = text[i].split(",")
        text[i][1] = int(text[i][1])
        text[i][0] = float(text[i][0])

    return text

# Driver Code

# Run insertion sort for each of the 9 files
for i in range (0, len(fileName)):
    pokeStat = sortMaker(fileName[i]) # Create array to be sorted
    print("\n", insertion(pokeStat))
    print("\nTotal sort count is:", insertCount)
    insertRun.append([fileName[i], insertCount]) # Store the results
    insertCount = 0
    pokeStat.clear()
    ++i

# Run quick sort for each of the 9 files
for i in range (0, len(fileName)):
    pokeStat = sortMaker(fileName[i]) # Create array to be sorted
    print("\n", quick(pokeStat, 0, len(pokeStat)-1))
    print("\nTotal sort count is:", quickCount)
    quickRun.append([fileName[i], quickCount]) # Store the results
    quickCount = 0
    pokeStat.clear()
    ++i

# Run merge sort for each of the 9 files
for i in range (0, len(fileName)):
    pokeStat = sortMaker(fileName[i]) # Create array to be sorted
    print("\n", merge_sort(pokeStat, 0, len(pokeStat)-1))
    print("\nTotal sort count is:", mergeCount)
    mergeRun.append([fileName[i], mergeCount]) # Store the results
    mergeCount = 0
    pokeStat.clear()
    ++i

print("\nInsertion sort: Sorted file with their respective runtimes:")
print("\n", insertRun)

print("\n\nQuick sort: Sorted file with their respective runtimes:")
print("\n", quickRun)

print("\n\nMerge sort: Sorted file with their respective runtimes:")
print("\n", mergeRun)

print("\n\nFinished all executions! Have a good day :-)")
