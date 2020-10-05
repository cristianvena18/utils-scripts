import bluetooth

print("Performing inquiry...")

nearby_devices = bluetooth.discover_devices(lookup_names=True)

print("Found {} devices".format(len(nearby_devices)))

for addr, name in nearby_devices:
    try:
        print("   {} - {}".format(addr, name))
    except UnicodeEncodeError:
        print("   {} - {}".format(addr, name.encode("utf-8", "replace")))
