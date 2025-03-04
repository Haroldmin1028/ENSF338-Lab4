""" 4/2: 1) The worst case time complexity would be O(n^2). Worst case scenario occurs 
when every element in "li" is greater than 5 which would mean that the inner loop always runs
and the multiplication within the inner loop will also always occur. both "for loops" have a O(n) time complexity
while the if statement and the multiplication within the inner loop have an 0(1) time complexity. We can see that O(n) * O(n) = 0(n^2)
which means that the worst case scenario would be O(n^2)

The average case time complexity would also be O(n^2). If we were to look at the scenario where only some elements are large enough
for the inner loop to run, we can make an assumption. Assume half of the elements are large enough for the inner loop to run, and we know that
the outer loop already runs at O(n), then O(n) * O(n/2) = O(n^2/2) which simplifies to O(n^2) in big-O.

The best case scenario would occur if the list ln had small enough elements so that the inner loop never has to run. Thus leaving us with
an O(n) time complexity. The only cost of time complexity occurs with the for loop which is O(n) and the if statement which is
O(1) as it checks the condition, which by the way will never meet requirments to run the inner loop for best case scenario.

2) No, the average, best, and worst case complexity are not the same. Average and worst case are the same, but not best.

"""

# original version of the code
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *=2


# modified version of the code where all cases are O(n^2) due to it always being in the inner loop. Simply just switched the order of the if statement and for loop

def modifiedprocessdata(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] > 5:
                li[i] *=2

newlist = [4, 2, 3, 5, 8, 3, 6]

newlist2 = [4, 2, 3, 5, 8, 3, 6]

processdata(newlist)
print(newlist)

modifiedprocessdata(newlist2)


print(newlist2)