#takes a big task or goal and breaks it down into steps
#to be used by a a computer 

#goal parser can interpret a string command
#The command consists of an alphasbet "G", "()" and/or (al) in some oirder
#the goal parser will interpret "G" as the string "G"
#the "()" as the string "o"
#"(al) as the string "al"
#the interpreted strings are then concatenated in original order

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        "rtype: str
        """
#replacements in python - string replacement method 
#replace method: replaces a specific phrase with another specified phrase
#only do replacements that are necessary
        return command.replace("()", "o").replace("(al)", "al")