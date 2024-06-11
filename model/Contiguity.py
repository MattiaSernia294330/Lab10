from dataclasses import dataclass
@dataclass
class Contiguity:
    dyad:str
    state1no:int
    state2no:int
    conttype:int

    def __hash__(self):
        return hash(self.dyad)