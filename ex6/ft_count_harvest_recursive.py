def helper(total_days: int, current_day: int = 1) -> None:
    if current_day <= total_days:
        print(f"Day: {current_day}")
        helper(total_days, current_day + 1)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive() -> None:
    days_until_harvest = int(input("Days until harvest: "))
    helper(days_until_harvest)
