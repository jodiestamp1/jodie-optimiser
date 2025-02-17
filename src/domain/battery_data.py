def create_battery_data(battery_capacity_kWh: float, max_charging_rate_kW: float) -> dict:
  
    battery_data = {
        "battery_capacity_kWh": battery_capacity_kWh,
        "max_charging_rate_kW": max_charging_rate_kW
    }

    if battery_data["capacity_kWh"] <= 0:
        raise ValueError("Battery capacity must be great than 0")
    if battery_data["max_charging_rate_kW"] <= 0:
        raise ValueError("Maximum charging rate must be greater than 0.")

    return battery_data
