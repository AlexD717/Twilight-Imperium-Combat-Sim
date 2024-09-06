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
    def __init__(self, hitValue:int, attackTimes:int, sustainDamage:bool, antiFighterHitValue:int, antiFighterAttackTimes:int, factions:list):
        self.hitValue = hitValue
        self.attackTimes = attackTimes
        self.sustainDamage = sustainDamage
        self.antiFighterHitValue = antiFighterHitValue
        self.antiFighterAttackTimes = antiFighterAttackTimes
        if (factions[0] == Faction.All):
            aviableFactions = list(Faction)
            for faction in factions:
                aviableFactions.remove(faction)
        else:
            aviableFactions = factions
        self.factions = aviableFactions

fighter = Ship(9, 1, False, None, 0, [Faction.All])