from enum import Enum

class Faction(Enum):
    All = 0
    Arborec = 1
    BaronyOfLetnev = 2
    ClanOfSarr = 3
    EmbersOfMuaat = 4
    EmiratesOfHacan = 5
    FederationOfSol = 6
    GhostsOfCeruss = 7
    L1Z1XMindnet = 8
    MentakCoalition = 9
    NaaluCollective = 10
    NekroVirus = 11
    SardakkNorr = 12
    UniversitiesOfJolNar = 13
    Winnu = 14
    XxchaKingdom = 15
    YinBrotherhood = 16
    YssarilTribes = 17

class Ship():
    def __init__(self, hitValue:int, attackTimes:int, sustainDamage:bool, capacity:int, antiFighterHitValue:int, antiFighterAttackTimes:int, factions:list):
        self.hitValue = hitValue
        self.attackTimes = attackTimes
        self.sustainDamage = sustainDamage
        self.antiFighterHitValue = antiFighterHitValue
        self.antiFighterAttackTimes = antiFighterAttackTimes
        self.capacity = capacity
        if (factions[0] == Faction.All):
            availableFactions = list(Faction)
            for faction in factions:
                availableFactions.remove(faction)
        else:
            availableFactions = factions
        self.factions = availableFactions

fighter1 = Ship(9, 1, False, 0, None, 0, [Faction.All, Faction.NaaluCollective])
fighter2 = Ship(8, 1, False, 0, None, 0, [Faction.All, Faction.NaaluCollective])

naaluFighter1 = Ship(8, 1, False, 0, None, 0, [Faction.All, Faction.NaaluCollective])
naaluFighter1 = Ship(7, 1, False, 0, None, 0, [Faction.All, Faction.NaaluCollective])

destroyer1 = Ship(9, 1, False, 0, 9, 2, [Faction.All])
destroyer2 = Ship(8, 1, False, 0, 6, 3, [Faction.All])


cruiser1 = Ship(7, 1, False, 0, None, 0, [Faction.All])
cruiser2 = Ship(6, 1, False, 1, None, 0, [Faction.All])


dreadnought1 = Ship(5, 1, True, 1, None, 0, [Faction.All, Faction.L1Z1XMindnet, Faction.SardakkNorr])
mindsetDreadnought1 = Ship(5, 1, True, 2, None, 0, [Faction.L1Z1XMindnet])
mindsetDreadnought2 = Ship(4, 1, True, 2, None, 0, [Faction.L1Z1XMindnet])


carrier1 = Ship(9, 1, False, 4, None, 0, [Faction.All, Faction.FederationOfSol])
carrier2 = Ship(9, 1, False, 6, None, 0, [Faction.All, Faction.FederationOfSol])
solCarrier1 = Ship(9, 1, False, 6, None, 0, [Faction.FederationOfSol])
solCarrier2 = Ship(9, 1, True, 8, None, 0, [Faction.FederationOfSol])

floatingFactory1 = Ship(None, None, False, 4, None, 0, [Faction.ClanOfSarr])
floatingFactory2 = Ship(None, None, False, 5, None, 0, [Faction.ClanOfSarr])

warSun2 = Ship(3, 3, True, 6, None, 0, [Faction.All])
