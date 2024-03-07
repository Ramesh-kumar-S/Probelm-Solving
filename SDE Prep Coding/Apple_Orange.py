def countApplesAndOranges(s, t, a, b, apples, oranges):
    Collectable_Apple=[apple+a for apple in apples]
    Collectable_Orange=[orange+b for orange in oranges]
    print(Collectable_Apple,Collectable_Orange)
    Apples_Count=0
    Orange_Count=0
    No_of_Apple_inRange = [ Apples_Count+1 for N in Collectable_Apple if N >= s and N <= t]
    No_of_Orange_inRange = [ Orange_Count+1 for N in Collectable_Orange if N >= s and N <= t]
    print(sum(No_of_Apple_inRange))
    print(sum(No_of_Orange_inRange))
    # print(Orange_Count)
    # No_of_Oranges_inRange=[N for N in Collectable_Orange if N >= s and N <= t N+=1]


countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])



