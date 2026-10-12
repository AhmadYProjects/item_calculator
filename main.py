from src.calculator.item import Item
from src.calculator import engine
# 1. Instantiate the items
ruby_crystal = Item(
    name="Ruby Crystal",
    gold=400,
    health=150
)
vamp_scepter = Item(
    name="Vampiric Scepter",
    gold=900,
    attack_damage=15,
    life_steal=7
)

# Let's test a massive Legendary item!
infinity_edge = Item(
    name="Infinity Edge",
    gold=3500,
    attack_damage=75,
    critical_strike_chance=25,
    critical_strike_damage= 30

)

ardent_censer = Item(
    name = "Ardent Censer",
    gold = 2200,
    ability_power=45,
    heal_and_shield_power=10,
    percent_movement_speed=4,
    mana_regeneration=125,
    secondary_effect = True,
    secondary_effect_attack_speed=25,
    secondary_effect_on_hit_damage=20,
    secondary_effect_base_benefactors=2,
)

staff_of_flowing_water = Item(
    name="Staff of Flowing Water",
    gold=2250,
    ability_power=35,
    heal_and_shield_power=10,
    mana_regeneration=125,
    ability_haste=15,
    secondary_effect = True,
    secondary_effect_ability_haste= 15,
    secondary_effect_ability_power=40,
    secondary_effect_base_benefactors=2,

)



my_items = [ruby_crystal, vamp_scepter, infinity_edge, ardent_censer, staff_of_flowing_water]

#output


print("--- League of Legends Item Efficiency Calculator ---")

for item in my_items:
    eff = engine.calculate_efficiency(item)

    if item.secondary_effect:
        secondary_eff = (
            engine.calculate_secondary_effect_efficiency(item)
        )

        base_benefactor_eff = (
            secondary_eff * item.secondary_effect_base_benefactors
        )

        active_efficiency = eff + base_benefactor_eff

        print(
            f"{item.name:<24} | "
            f"Base Stat Efficiency: {eff:6.1f}% | "
            f"Minimum Efficiency During Effect: "
            f"{active_efficiency:6.1f}% | "
            f"Extra Efficiency / Extra Benefactor: "
            f"{secondary_eff:6.1f}%"
        )
    else:
        print(
            f"{item.name:<24} | "
            f"Base Stat Efficiency: {eff:6.1f}%"
        )

