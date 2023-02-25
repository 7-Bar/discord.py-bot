import random

swears = ["crap"]    # I will add more later
amongus = ["amongus", "amongi", "crewmate", "imposter"]


def get_response(message: str) -> str:
    p_message = message.lower()

    for x in range(len(swears)):   # loop for swears
        if p_message.__contains__(swears[x]) or p_message.__contains__("{swear}"):
            return "`PLEASE STOP SWEARING`"

    for x in range(len(amongus)):
        if p_message.__contains__(amongus[x]):
            return "did someone mention me?"

    if p_message.__contains__("i will eat you"):
        return "no"

    if p_message == "roll":
        return str(random.randint(0, 10))

    if p_message == "!help":
        return "`MESSAGE IN HERE`"

    return ""
