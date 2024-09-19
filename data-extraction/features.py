import re

def extract_features(text, touchscreen=True, threeg=True, talk_time=True, four_g=True, price_range=None):
    features = {
        "battery_power": None,
        "dual_sim": True,  # Marking dual_sim as True
        "fc": None,
        "four_g": four_g,
        "int_memory": None,
        "m_dep": None,
        "mobile_wt": None,
        "pc": None,
        "px_height": None,
        "px_width": None,
        "ram": None,
        "sc_h": None,
        "sc_w": None,
        "talk_time": talk_time,
        "three_g": threeg,
        "touch_screen": touchscreen,
        "wifi": None,
        "n_cores": None,
        "price_range": price_range,
        "processor": None  # Add the processor key
    }

    # Extract RAM
    ram_match = re.search(r'(\d+)\s*GB\s*RAM', text)
    if ram_match:
        features["ram"] = int(ram_match.group(1)) * 1024  # Convert GB to MB

    # Extract ROM
    rom_match = re.search(r'(\d+)\s*GB\s*ROM', text)
    if rom_match:
        features["int_memory"] = int(rom_match.group(1))

    # Extract Display size
    display_match = re.search(r'(\d+\.\d+)\s*cm', text)
    if display_match:
        features["sc_h"] = features["sc_w"] = float(display_match.group(1))

    # Extract Front Camera
    fc_match = re.search(r'(\d+)MP\s*\+\s*(\d+)MP\s*\|\s*(\d+)MP\s*Front\s*Camera', text)
    if fc_match:
        features["fc"] = int(fc_match.group(1))

    # Extract Battery
    battery_match = re.search(r'(\d+)\s*mAh\s*Battery', text)
    if battery_match:
        features["battery_power"] = int(battery_match.group(1))

    # Extract Processor
    processor_match = re.search(r'Snapdragon\s*(\d+)\s*(\w+)\s*Processor', text)
    if processor_match:
        features["n_cores"] = int(processor_match.group(1))
        features["processor"] = processor_match.group(0)

    return features
