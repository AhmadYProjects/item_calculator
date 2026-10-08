from src.calculator.baselines import get_gold_values


def calculate_item_value(item):
    total_value = 0
    for stat_name, gold_per_point in get_gold_values().items():
        item_stat_amount = getattr(item,stat_name,0)
        total_value += item_stat_amount * gold_per_point

    return total_value

def calculate_efficiency(item):
    if item.gold == 0:
        efficiency = 0.0
        return efficiency
    else:
        efficiency = calculate_item_value(item)/item.gold
        return efficiency * 100
