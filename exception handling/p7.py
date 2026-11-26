# to create your own exception
#class MYCustomException(Exception):
   # pass

class InvalidAge(Exception):
    pass

    age=15
    try:
        if age< 18 :
            raise InvalidAge("You must be 18 or older")
    #except InvalidAge as e:
        #print("error:", e)
        
    finally:
        print("Access granted")