def get_text(str):
    f = open("config.config.config", "r")
    for x in f:
        if x.startswith(str):
            return x.split("=")[1].strip()
    return output