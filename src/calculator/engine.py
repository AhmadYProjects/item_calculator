from src.calculator.baselines import get_gold_values


def calculate_item_value(item):
    total_value = 0
    for stat_name, gold_per_point in get_gold_values().items():
        item_stat_amount = getattr(item,stat_name,0)
        total_value += item_stat_amount * gold_per_point

    return total_value

def calculate_secondary_effect_value(item):
    total_value = 0
    for stat_name, gold_per_point in get_gold_values().items():
        secondary_stat_name = f"secondary_effect_{stat_name}"

        item_stat_amount = getattr(item,secondary_stat_name,0)
        total_value += item_stat_amount * gold_per_point

    return total_value

def calculate_efficiency(item):
    if item.gold == 0:
        return 0
    else:
        efficiency = calculate_item_value(item)/item.gold
        return efficiency * 100

def calculate_secondary_effect_efficiency(item):
    if item.gold == 0:
        efficiency = 0.0
        return efficiency
    else:
        efficiency = calculate_secondary_effect_value(item)/item.gold
        return efficiency * 100

def adjust_stats(self,**kwargs):
    for stat_name, stat_value in kwargs.items():
        if hasattr(self, stat_name):
            setattr(self,stat_name,stat_value)
        else:
            print(f"Warning: '{stat_name}' is not a valid stat for this item.")
