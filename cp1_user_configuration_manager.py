test_settings={"theme":"light", "language":"english", "notifications":"off"}
def add_setting(test_settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    test_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!" 

def update_setting(test_settings,setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in test_settings:
        test_settings[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    if key not in test_settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(test_settings,setting):
    
    key = setting.lower()

    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"
def view_settings(test_settings):
    if test_settings=={}:
        return "No settings available."
    result = "Current User Settings:\n"


    for key, value in test_settings.items():
     result += f"{key.capitalize()}: {value}\n"

    return result

print(view_settings(test_settings))

    