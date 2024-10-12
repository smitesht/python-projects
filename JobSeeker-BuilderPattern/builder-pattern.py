
class Address:
    
    def __init__(self, address=None, city=None, pincode=None):
        self.address = address
        self.city = city
        self.pincode = pincode
        
    def __str__(self):
        return (f'{self.address}, {self.city}, {self.pincode}')
        
    def getAddress(self):
        return self
    
class Education:
    
    def __init__(self, certiName=None, instituteName=None, startYear=None, endYear=None):
        self.certName = certiName
        self.instituteName = instituteName
        self.startYear = startYear
        self.endYear = endYear
        
    def __str__(self):        
        return (f"(Title: {self.certName}, Institute: {self.instituteName}, StartYear:{self.startYear}, EndYear:{self.endYear})")

class Experience:
    
    def __init__(self,companyName=None,designation=None,startDate=None,endDate=None):
        self.companyName = companyName
        self.designation = designation
        self.startDate = startDate
        self.endDate = endDate
    
    def __str__(self):
        return (f"(Company Name: {self.companyName}, Designation: {self.designation}, StartYear:{self.startDate}, EndYear:{self.endDate})")
    
    def getExperience(self):
        return self   

class JobSeeker:
    
    def __init__(self):
        self.firstName = None
        self.middleName = ""
        self.lastName = None
        self.dob = None
        self.gender = None
        self.permanentAddress = None
        self.currentAddress = None
        self.mobile = None
        self.email = None
        self.education = []
        self.workExperience = []
        self.skills = []
        
    def __str__(self):
                    
        educations_str = [ str(e) for e in self.education]
            
        work_experience_str = [str(w) for w in self.workExperience]           
              
        return (f'Name: {self.firstName} {self.middleName} {self.lastName}\n'
                f'DoB: {self.dob} - Gender: {self.gender}\n'
                f'Current Address: {str(self.currentAddress)}\n'
                f'Permanent Address: {str(self.permanentAddress)}\n'
                f'Mobile: {self.mobile}, Email: {self.email}\n'
                f"Education: {educations_str}\n"               
                f"Work Experience:{work_experience_str}, \n"
                f"Skills: {self.skills}"
                )
    

class JobSeekerBuilder:
    
    def __init__(self, firstName, lastName):
        self.jobSeeker = JobSeeker()
        self.jobSeeker.firstName = firstName        
        self.jobSeeker.lastName = lastName
    
    def setMiddleName(self, middleName=""):
        self.jobSeeker.middleName = middleName
        return self
    
    def setDateOfBirth(self, dob):
        self.jobSeeker.dob = dob
        return self
    
    def setGender(self, gender):
        self.jobSeeker.gender = gender
        return self
    
    def setMobile(self, mobile):
        self.jobSeeker.mobile = mobile
        return self
        
    def setEmail(self, email):
        self.jobSeeker.email = email
        return self
    
    def setPermenantAddress(self, address, city, pincode):
        self.jobSeeker.permanentAddress = Address(address, city, pincode)        
        return self
        
    def setCurrentAddress(self, address, city, pincode):
        self.jobSeeker.currentAddress = Address(address, city, pincode)
        return self
        
    def addEducation(self, certiName, instituteName, startYear, endYear ): 
        self.jobSeeker.education.append(Education(certiName, instituteName, startYear, endYear))
        return self
        
    def addExperience(self,companyName,designation,startDate,endDate ):
        self.jobSeeker.workExperience.append(Experience(companyName, designation, startDate, endDate))
        return self
        
    def addSkill(self, skill):
        self.jobSeeker.skills.append(skill)
        return self
    
    def build(self):
        return self.jobSeeker
        
    
        
if __name__ == "__main__":   
    
    
    jhon = JobSeekerBuilder("Jhon","Peter")\
            .setDateOfBirth('05-10-2000')\
            .setGender("Male")\
            .setMobile("+1-1234567890") \
            .setEmail("jhone@gmail.com") \
            .setPermenantAddress("1023, Oak St, Albert Avenue","Calgary","ADC234") \
            .setCurrentAddress("112, Munroe Park","Regina","DCE324") \
            .addEducation("10th","Govt. Institute","2014","2015") \
            .addEducation("12th","Govt. Institute","2016","2017") \
            .addEducation("B.Sc.(Computer Science)","Royal University","2017","2021") \
            .addExperience("ABCL Software","Trainee Engineer","2021","2023") \
            .addExperience("Craft Solution","Software Engineer","2023","Present") \
            .addSkill("Javascript") \
            .addSkill("SQL") \
            .addSkill("HTML/CSS") \
            .build()
        
        
    print(str(jhon))