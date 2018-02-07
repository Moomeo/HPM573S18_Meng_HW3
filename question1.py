#question 1

class Patient:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def discharge(self):
        raise NotImplementedError("This is an abstract method and need to be implemented in subclass.")

class EmergencyPatient(Patient):
    def __init__(self, name, type):
        Patient.__init__(self, name, type)

    def discharge(self):
        print(self.name)
        print(self.type)

        return self.name, self.type

class HospitalizedPatient(Patient):
    def __init__(self, name, type):
        Patient.__init__(self, name, type)

    def discharge(self):
        print(self.name)
        print(self.type)

        return self.name,self.type



class Hospital():
    def __init__(self, patients):
        self.patients = patients

    def admit(self):
        admitpatients = dict()
        for thispatient in self.patients:
            admitpatients[thispatient.name] = thispatient.discharge()

        return admitpatients

    def discharge_all(self):
        for thispatient in self.patients:
            print(thispatient.discharge())

    def get_total_cost(self):
        cost = 0
        for thispatient in self.patients:
            if type(thispatient) == HospitalizedPatient:
                cost += 2000
            elif type(thispatient) == EmergencyPatient:
                cost += 1000
        return cost

H1 = HospitalizedPatient("one", type = "hospitalized")
H2 = HospitalizedPatient("two", type = "hospitalized")
H3 = HospitalizedPatient("three", type = "hospitalized")
E1 = EmergencyPatient("four", type = "emergency")
E2 = EmergencyPatient("five", type = "emergency")

Hosp1 = Hospital(patients=[H1, H2, H3, E1, E2])

print(Hosp1.get_total_cost())
print(Hosp1.discharge_all())



