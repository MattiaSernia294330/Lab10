from dataclasses import dataclass
@dataclass
class Nazione():
    CCode:int
    StateAbb:str
    StateNme:str
    def __hash__(self):
        return hash(self.CCode)