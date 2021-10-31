#   T(°R) = (T(°C) + 273.15) × 9/5
#   T(°C) = (5/9) * T(°C) - 273.15
#   T(°C) = (5/9) * T(°C) - 273.15
#   T(°C) = (5/9) * T(°C) - 273.15

class CUnit:
	
    def __init__(this, fact=1.0, cnst=0.0):
        this.fact = fact     
        this.cnst = cnst     # F=9/5 C + 32 or C = (F-32) /(9/5)  
    
    # add this function
    def inv_convert (self, myVal):
        return (myVal - self.cnst) / self.fact; # Fixed
    
    def convert (self, myVal):
        return myVal * self.fact + self.cnst; # fixed
    
    def get_fact(self):
        return self.fact
        
    def get_cnst(self):
        return self.cnst

#------------------------ 
class CTemp:  
    # Set main properties for Fahrenheit, Celsius and Kelvin    
    objUnit_C2F = CUnit() # 'Assigin variable  for object to convert from Celsius to Fahrenheit 
    objUnit_C2K = CUnit() # 'Assigin variable  for object to convert from Celsius to Kelvin
    m_freh = m_cels = m_kelin = 0.0
    
    def __init__(self):  
        self.objUnit_C2F = CUnit(9.0/5.0, 32.0)  # Create object to convert from Celsius to Fahrenheit 
        self.objUnit_C2K = CUnit(1.0, 273.0)  # Create object to convert from Celsius to Kelvin
    
    # Creating setter and getter for each property  
    def get_freh(self):
    	return self.m_freh 

    def set_freh(self, val):
        self.m_freh = val;
        self.m_cels = self.objUnit_C2F.inv_convert(self.m_freh)  # Convert from F to C
        self.m_kelin = self.objUnit_C2K.convert(self.m_cels)       # Convert from C to K            
 
    def get_cels(self):
    	return self.m_cels 
        
    def set_cels(self, val):
        self.m_cels = val;
        self.m_freh = self.objUnit_C2K.convert(self.m_cels)        # Convert from C to F
        self.m_kelin = self.objUnit_C2F.inv_convert(self.m_cels)   # Convert from C to K             
        
    def get_kelin(self):
    	return self.m_kelin 
        
    def set_kelin(self, val):
        m_kelin = val;
        m_cels = self.objUnit_C2K.inv_convert(self.m_kelin)   # Convert from K to C
        m_freh = self.objUnit_C2F.convert(self.m_cels)        # Convert from C to F            
    
# -----------------------------------------------  
  
# test CUnit
objUnit_C2F = CUnit(9.0/5.0, 32.0);

print("objUnit inv_convert = ", objUnit_C2F.inv_convert(200.0));

print("objUnit convert = ", objUnit_C2F.convert(200.0));
    
print("======================" );
objTemp = CTemp();  
objTemp.set_freh(300.0);

print("objTemp.freh = ", objTemp.get_freh())
print("objTemp.cels = ", objTemp.get_cels())
print("objTemp.kelin = ", objTemp.get_kelin())
    
  
