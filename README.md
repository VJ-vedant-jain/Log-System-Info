# Log-System-Info
This project will log CPU temps and memory details saving them into a txt file. 

## Dependencies

This project requires:

### System (Linux only for now)

This script depends on Linux system tools:

-   `lm-sensors` → provides the `sensors` command\
-   `procps` / `procps-ng` → provides the `free` command

These tools are **not cross-platform** and will not work on Windows or
macOS.

### Installation

#### Ubuntu / Debian

``` bash
sudo apt install lm-sensors procps
sudo sensors-detect
```

#### Arch Linux

``` bash
sudo pacman -S lm_sensors procps-ng
sudo sensors-detect
```

#### Fedora

``` bash
sudo dnf install lm_sensors procps-ng
sudo sensors-detect
```

### Notes

-   The script assumes CPU temperature labels contain `"Core"`.
-   Output is expected in °C.