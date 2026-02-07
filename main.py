import subprocess, time

def get_sensors():
    out = subprocess.run(["sensors"], capture_output=True, text=True).stdout
    return out.splitlines()

def get_core_temps(lines):
    temps = []  
    for line in lines:
        if "Core" in line:
            try:
                temp = line.split()[2].replace("+","").replace("°C","")
                temps.append(float(temp))
            except:
                pass
    return temps

def get_mem():
    out = subprocess.run(["free", "-m"], capture_output=True, text=True).stdout.splitlines()
    parts = out[1].split()
    return {
        "used": int(parts[2]),
        "free": int(parts[3]),
        "available": int(parts[6])
    }

with open("syslog.txt", "a") as f:
    while True:
        sensors = get_sensors()
        temps = get_core_temps(sensors)
        mem = get_mem()

        line = f"temps={temps} | mem={mem}\n"
        f.write(line)
        f.flush()
        print(line.strip())

        time.sleep(1)
