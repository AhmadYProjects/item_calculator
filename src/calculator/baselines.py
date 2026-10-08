from src.calculator.item import Item


def get_gold_values():
    # Component items
    ruby_crystal = Item(gold=400, health=150)
    long_sword = Item(gold=350, attack_damage=10)
    amplifying_tome = Item(gold=400, ability_power=20)
    glowing_mote = Item(gold=250, ability_haste=5)
    cloth_armor = Item(gold=300, armor=15)
    null_magic_mantle = Item(gold=400, magic_resistance=20)
    sapphire_crystal = Item(gold=300, mana=300)
    rejuvenation_bead = Item(gold=300, health_regeneration=100)
    faerie_charm = Item(gold=200, mana_regeneration=50)
    cloak_of_agility = Item(gold=600, critical_strike_chance=15)
    dagger = Item(gold=250, attack_speed=10)
    boots = Item(gold=300, flat_movement_speed=25)

    # Advanced Items
    last_whisper = Item(gold=1450, attack_damage=20, armor_penetration=18)
    forbidden_idol = Item(gold=600, mana_regeneration=50, heal_and_shield_power=8)
    serrated_dirk = Item(gold=1000, attack_damage=20, lethality=10)
    vampiric_scepter = Item(gold=900, attack_damage=15, life_steal=7)
    sorcerer_shoes = Item(gold=1100, flat_movement_speed=45, flat_magic_penetration=12)
    recurve_bow = Item(gold=700, attack_speed=15, on_hit_damage=15)
    winged_moonplate = Item(gold=800, health=200, percent_movement_speed=5)
    blighting_jewel = Item(gold=1100, ability_power=25, percent_magic_penetration=13)
    infinity_edge = Item(gold = 3500, critical_strike_chance = 25, attack_damage = 75, critical_strike_damage = 30)

    GOLD_VALUES = {
        "attack_damage": long_sword.gold / long_sword.attack_damage,
        "ability_haste": glowing_mote.gold / glowing_mote.ability_haste,
        "ability_power": amplifying_tome.gold / amplifying_tome.ability_power,
        "armor": cloth_armor.gold / cloth_armor.armor,
        "magic_resistance": null_magic_mantle.gold / null_magic_mantle.magic_resistance,
        "health": ruby_crystal.gold / ruby_crystal.health,
        "mana": sapphire_crystal.gold / sapphire_crystal.mana,
        "health_regeneration": rejuvenation_bead.gold / rejuvenation_bead.health_regeneration,
        "mana_regeneration": faerie_charm.gold / faerie_charm.mana_regeneration,
        "critical_strike_chance": cloak_of_agility.gold / cloak_of_agility.critical_strike_chance,
        "attack_speed": dagger.gold / dagger.attack_speed,
        "flat_movement_speed": boots.gold / boots.flat_movement_speed,


        "armor_penetration": (last_whisper.gold - (
                    long_sword.gold / long_sword.attack_damage) * last_whisper.attack_damage) / last_whisper.armor_penetration,
        "heal_and_shield_power": (forbidden_idol.gold - (
                    faerie_charm.gold / faerie_charm.mana_regeneration) * forbidden_idol.mana_regeneration) / forbidden_idol.heal_and_shield_power,
        "lethality": (serrated_dirk.gold - (
                    long_sword.gold / long_sword.attack_damage) * serrated_dirk.attack_damage) / serrated_dirk.lethality,
        "life_steal": (vampiric_scepter.gold - (
                    long_sword.gold / long_sword.attack_damage) * vampiric_scepter.attack_damage) / vampiric_scepter.life_steal,
        "flat_magic_penetration": (sorcerer_shoes.gold - (
                    boots.gold / boots.flat_movement_speed) * sorcerer_shoes.flat_movement_speed) / sorcerer_shoes.flat_magic_penetration,
        "percent_magic_penetration": (blighting_jewel.gold - (
                    amplifying_tome.gold / amplifying_tome.ability_power) * blighting_jewel.ability_power) / blighting_jewel.percent_magic_penetration,
        "on_hit_damage": (recurve_bow.gold - (
                    dagger.gold / dagger.attack_speed) * recurve_bow.attack_speed) / recurve_bow.on_hit_damage,
        "percent_movement_speed": (winged_moonplate.gold - (
                    ruby_crystal.gold / ruby_crystal.health) * winged_moonplate.health) / winged_moonplate.percent_movement_speed,
        #"critical_strike_damage" : (infinity_edge.gold -
        #                           (long_sword.gold/long_sword.attack_damage*infinity_edge.attack_damage))/ infinity_edge.critical_strike_damage,
    }

    return GOLD_VALUES