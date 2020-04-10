def build_profile(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile