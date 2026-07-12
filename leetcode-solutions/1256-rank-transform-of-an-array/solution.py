class Solution(object):
    def arrayRankTransform(self, arr):
        unique_set=set(arr)
        #sort the arr
        sorted_arr=sorted(unique_set)
        #create a rank dictionary and store ther
        rank_dictionary={}
        current_rank=1
        for i in sorted_arr:
            rank_dictionary[i]=current_rank
            current_rank+=1
        #map the original array elements to their ranks 
        result=[]
        for i in arr:
            rank_of_number=rank_dictionary[i]
            result.append(rank_of_number)
        return result








       
