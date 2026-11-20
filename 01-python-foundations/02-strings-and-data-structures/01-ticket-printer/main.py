# 01 - Ticket Printer
event = input()
guest = input()
seat = input()
l1 = f'Event: "{event}"'
l2 = f'Guest: {guest}'
l3 = f'Seat: {seat}'
l4 = f"File: C:\\tickets\\{guest.lower().replace(" ", "_")}.txt"
m = max(len(l1), len(l2), len(l3), len(l4)) + 4
print(f"""╔{"═" * m}╗
║{l1:^{m}}║
║{l2:^{m}}║
║{l3:^{m}}║
║{l4:^{m}}║
╚{"═" * m}╝""")
