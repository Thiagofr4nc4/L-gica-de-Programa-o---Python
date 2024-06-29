while True:
    HF, HDF, HA = input().split()
    if HF == "FIM" and HDF == "FIM" and HA == "FIM":
        break
    if HF == "NAO" and HDF == "SIM" and HA == "SIM":
        print("VITÓRIA")
    else:
        print("DERROTA")