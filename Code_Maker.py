
import numpy as np


##TODO: research methods and finalize  this class to meet scope and aim of project
##Coerce logical and operation to byte_array for comparisons
##Feel free to edit style/functionality of any of the class, add changes up here
##Ensure compatability with Scrambler class, as these two interface with each other often



class code_Manager:
        def __init__(self,code_size):
            ## CONSTRUCTOR PARAMETER: code_size, bounds the size of our codes and how many colluders our codes can resist
            ## Unless we decide to do collusion resistance, treat this as size of codes
            self.identities = {}
            self.num_identities=0
            self.codes_to_identication = {}
            self.identification_to_codes = {}
            self.code_size=code_size
            self.collusion_matrix = np.ndarray([code_size,code_size])
            self.collusion_matrix.fill(1)
            for i in range(code_size):
                    self.collusion_matrix[i][i] = 0
            self.code_match()
        def code_match(self):
            ##Current Code construction is basic collusion detection, possibly could be implemented as error correcting code, gaussian vectors,
            # or entropy based codes.  Returns a dictionary that maps each code to an identification pair
            # Not used for current example, but could be used later 
            
            for i in range(1,self.code_size):
                 for j in range(1,self.code_size):
                        self.identification_to_codes[tuple([i,j])] = np.logical_and(self.collusion_matrix[i-1:i],self.collusion_matrix[j-1:j]) 
        def fingerprint_code(self,id):
            ##Takes a user ID (string, abstract format for now), 
            # assigns it to self.identities.  Returns a code vector, throws error if none available
            if(self.num_identities==self.code_size):
                raise Exception("All codes currently in use")
            else:
                self.identities[id]=self.num_identities
                self.num_identities+=1


        def identify_leaker(self,leaked_code):
            ##Identifies Leaker using self.identification_to_codes given an extracted code vector (leaked_code).
            if len(self.identities) == 0 or len(self.collusion_matrix) ==0:
                raise Exception("Array of size zero")
            leaker = ""
            
            for i in range(len(self.collusion_matrix[1])):
                if (leaked_code == self.collusion_matrix[i]).all() :
                    leaker =list(self.identities.keys())[list(self.identities.values()).index(i)] ## Finds key(id) given value(index) 
            return leaker


        def find_colluders(self,leaked_code):
            colluders ="leakers: "
            for i in range(len(leaked_code)):
                
                if leaked_code[i] == False:
                    colluders +=  list(self.identities.keys())[list(self.identities.values()).index(i)] +" "

                    
            return colluders 
        def get_code_from_Id(self,id):
            ## PARAM string id (identification), returns the code associated with the given user
            return self.collusion_matrix[self.identities[id]]

                








def main():
    c=code_Manager(10)
    c.fingerprint_code("jay")
    print(c.get_code_from_Id("jay"))
    print(c.identify_leaker(c.get_code_from_Id("jay")))
    c.fingerprint_code("nurain")
    print(c.identify_leaker(c.get_code_from_Id("nurain")))
    c.fingerprint_code("brady")
    print(c.find_colluders([False,True,False,True,True,True,True,True,True,True]))
    print(c.find_colluders([True,False,True,True,True,True,True,True,True,True]))

    

    

if __name__ == "__main__":
    main()