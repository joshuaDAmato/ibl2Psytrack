import datetime

def toDatetime(dateString):
    """
    Converts a date string to a datetime object. 
    """
    return datetime.strptime(dateString, '%Y-%m-%d')

class Mouse:
    def __init__(self, name, dob = None, deprivationStart = None, headplateDate = None, color = None, siblings = None):
        """
        Mouse class to store all of the information about a subject, in a pre-indexed format, and to be able to easily access all of a mouse's data with a single file. 
        Dates must be entered as YYYY-MM-DD, including the dashes.
        Enter color as a string. 
        """
        self.name = str(name)
        self.cageid = self.name.split('_')[0]
        self.uniqueid = int(self.name.split('_')[1])

        # variables filled optionally during class instantiation
        self.dob = toDatetime(dob)
        self.deprivationDateRanges = [(toDatetime(deprivationStart), None)] # initialize with a single range, which is open-ended
        self.headplateDate = toDatetime(headplateDate)
        self.color = color
        self.siblings = [siblings] # siblings are entered as a list of mouse objects
        
        # variables not filled during class instantiation 
        self.notes = [] # notes should be entered as tuples, where a given element of the notes list is a tuple of (date, session, note) -- date should be a datetime object, session should be an integer, and note should be a string

        # mice should be a list of mouse objects
        mice = []
        mice.append(self)

    def save(self):


    