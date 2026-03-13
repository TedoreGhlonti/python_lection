def main():
   names = ["Mario", "Luigi", "Daisy", "Yoshi"]
   for name in names:
       print(write_letter(name, "Princess Peach"))

def write_letter(reciever, sender):
    return f"""
    +----------------------+
    Dear {reciever}

    You are cordially invited to a ball at 
    Peache's Clastle this evening, at 7:00 PM
    Sincerely
    {sender}
    +----------------------+
    """

main()