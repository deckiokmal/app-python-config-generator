my_list = [
    "10.79.2.244",
    "10.79.2.230",
    "10.79.2.224",
    "10.79.2.250",
    "10.79.2.233",
    "10.79.2.208",
]


print("config firewall address")
for i in my_list:
    print(f"edit {i}")
    print("set allow-routing enable")
    print(f"set subnet {i} 255.255.255.255")
    print("next")

print("end")
