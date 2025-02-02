#you are given the array paths where paths[i] = [cityAi, city Bi]
#means that there is a direct path going from citya to city B
#return the destinatino city, that is the city without any path outgoing to 
#another city 
#it is guaranteed that the graph of the paths 
#will form a line iwhtout a loop thereofre theere will be one dest
from typing import List

class Solution(object):
    def destination(self, paths: List[List[str]]) -> str :
        """
        :type paths: List[List[str]]
        :rtype:str
        """

    #ides: linked lsit? hash table store values?
    #think about counting: final city has 0 outgoing
    #use a dictionary

    #initialize a dict to hold the cities and the counts 
        outgoing_count = {}
        for path in paths:
            #unpack the tuple
            city_a, city_b = path
            #increase a count for each city 
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)

        #iterate over the dictionaries 
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city
            
