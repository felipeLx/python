""" 
You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class
'analysedText' with the following methods -

<ul>
    <li> Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"      
    <li> freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
    <li> freqOf - returns the frequency of the word passed in argument.
</ul>
 """
class analysedText(object):
    def __init__(self, text):
         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
         formattedText = formattedText.lower()
         self.fmtText = formattedText

    def freqAll(self):
        wordList = self.fmtText.split(' ')

        freqMap = {}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)
        
        print(freqMap)
        return freqMap
    
    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            print(freqDict[word])
            return freqDict[word]
        else:
            return 0

text = analysedText('Hello, what the point?! If you know that hello have to be a start. That why.')
print(text)