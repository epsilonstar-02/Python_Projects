with open("names.txt","r") as names:
    name = names.read().splitlines()

with open("letter.txt") as letter:
    template = letter.read().strip()
    for i in name:
        with open(f"letter for {i}", "w") as l:
            l.write(template.replace("[Name]", i).replace("[Your Name]", "Abdul"))