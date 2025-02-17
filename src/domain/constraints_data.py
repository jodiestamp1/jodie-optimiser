def create_constraints_data(min_soc, max_soc, ready_by_time):
   
    constraints_data = {
        "min_soc": min_soc,
        "max_soc": max_soc,
        "ready_by_time": ready_by_time
    }

    if constraints_data["min_soc"] < 0 :
        raise ValueError("Minimum SOC cannot be less than 0.")
    if constraints_data["max_soc"] > 1:
        raise ValueError("Maximum SOC cannot be greater than 1.")
    if constraints_data["min_soc"] >= constraints_data["max_soc"]:
        raise ValueError("Minimum SOC must be less than maximum SOC.")

    return constraints_data

