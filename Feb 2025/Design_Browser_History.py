#you have a browser of one tab where you starton the homepage 
#and you can visit another url, get back or move forward with steps
#Impliment the browser history class

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage:str
        """
        #initialize the object with the homepage 
        #need to keep history in something 
        self.history = [homepage]
        #other functions in the class need to use this value
        #keep track of index
        self.current_index = 0

    def visit(self, url):
        """
        :type url: str
        :rtpye: None
        """
        #visit would append to history
        #clears up all forward history when at new url

        #update current index
        self.current_index += 1

        self.history = self.history[0:self.current_index]
        self.history.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        #move current index back but not beyond 0
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current_index = min(len(self.history)-1, self.current_index+steps)
        return self.history[self.current_index]