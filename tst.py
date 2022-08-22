s = "1edanta"

def is_number(s):
    try:
        i = int(s + "")
        return True
    except:
        return False

print(is_number(s[0]))