class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()
        
    # don't understand how this function works 
    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) < self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{}, {}, admitted to bed #{}".format(patient.id, patient.name, patient.bed_num)
            return self
        else:
            print "Hospital is at full capacity"
            return self 

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break
                self.patients.remove(patient)
                print "Patient #{}, {}, sucessfully discharged.  Bed #{} now available".format(patient.id, patient.name, patient.bed_num)
                return self
        return "Patient not found"


Greg=Patient("Greg", "Seafood")
Andrea=Patient("Andrea", "Flour")


Eddie=Patient("Eddie", "Bread")
Michael=Patient("Michael", "Grain")
Marissa=Patient("Marissa", "Fruit")

# hosp = Hospital("LA CITY HOSPITAL", 4)

# hosp.initialize_beds().admit(Greg)

Hospital("LA CITY HOSPITAL", 4).admit(Greg).admit(Andrea).admit(Michael).admit(Marissa).admit(Eddie).discharge(1)



