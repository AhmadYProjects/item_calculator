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

# 2. Put them in a list so we can loop through them
my_items = [ruby_crystal, vamp_scepter, infinity_edge]

# 3. Print out your hard-earned efficiency percentages
print("--- League of Legends Item Efficiency Calculator ---")
for item in my_items:
    eff = engine.calculate_efficiency(item)
    # Nudge: Changed 'Item' to 'item' here:
    print(f"{item.name:<20} | Gold Cost: {item.gold:<5} | Efficiency: {eff:.1f}%")
