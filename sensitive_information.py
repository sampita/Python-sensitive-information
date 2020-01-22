# READ ONLY
    # Social security number
    # Date of birth
    # Health insurance account number
# NOT EXPOSED AS PROPERTIES
    # First name
    # Last name
# GETTER AND SETTER
    # Address

class Patient:
    def __init__(self, ssn, dob, hin, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__hin = hin
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__full_name = f"{first_name} {last_name}"
    
    @property #getter
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return "Attribute Error for SSN"
    
    @property #getter
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return "Attribute Error for DOB"
        
    @property #getter
    def hin(self):
        try:
            return self.__hin
        except AttributeError:
            return "Attribute Error for HIN"
    
    @property #getter
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return "Attribute Error for Address"
    
    @address.setter #setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string")
    
    @property #getter
    def full_name(self):
        try:
            return self.__full_name
        except AttributeError:
            return "Attribute Error for Full Name"
    
cashew = Patient("097-23-1003", "08/13/92", "7001294103", "Daniela", "Agnoletti", "500 Infinity Way")

# This should not change the state of the object
# cashew.ssn = "838-31-2256"

# Neither should this
# cashew.dob = "01-30-90"

# But printing either of them should work
print(cashew.ssn)

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
