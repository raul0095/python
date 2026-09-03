def someFunction(settings):
    if not settings:
        return "No settings available"
    else:
        for key, value in settings.items():
            return f"\n{key.capitalize()}: {value}"


# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high