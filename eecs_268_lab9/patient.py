'''
Author: Michael Stang
KUID: 3073983
Date: 04-23-2023
Lab: lab09
Last modified: 04-23-2023
Purpose: A class for Patients
'''

class Patient:
    def __init__(self, first_name, last_name, age, illness, severity, arrival=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival = arrival
    
    def __str__(self):
        return f"     Name: {self.last_name}, {self.first_name}\n     Age: {self.age}\n     Suffers from: {self.illness}\n     Illness severity: {self.severity}\n"
    
    def __repr__(self):
        return f"Patient({self.first_name}, {self.last_name}, {self.age}, {self.illness}, {self.severity})"

    def __lt__(self, other):
        if isinstance(other, int):
            return self.severity < other
        elif isinstance(other, Patient):
            return self.severity < other.severity
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.severity > other
        elif isinstance(other, Patient):
            return self.severity > other.severity

    def __eq__(self, other):
        if isinstance(other, int):
            return self.severity == other
        elif isinstance(other, Patient):
            return self.severity == other.severity

    def __le__(self, other):
        if isinstance(other, int):
            return self.severity <= other
        elif isinstance(other, Patient):
            return self.severity <= other.severity
    
    def __ge__(self, other):
        if isinstance(other, int):
            return self.severity >= other
        elif isinstance(other, Patient):
            return self.severity >= other.severity