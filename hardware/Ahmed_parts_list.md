# Hardware Parts List

## Computing Platform

### Raspberry Pi 4 Model B

**Specifications:**
- **Model:** Raspberry Pi 4 Model B
- **Processor:** Broadcom BCM2711, Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
- **RAM:** 4GB 
- **GPIO Pins:** 40-pin GPIO header (compatible with previous models)
- **Operating System:** Raspberry Pi OS
-  **Power Requirements:** 5V DC via USB-C, minimum 3A power supply recommended
- **Connectivity:**
  - 2 × USB 3.0 ports
  - 2 × USB 2.0 ports
  - Gigabit Ethernet
  - 2.4 GHz and 5.0 GHz IEEE 802.11ac wireless
  - Bluetooth 5.0, BLE

**Why Raspberry Pi 4:**
- Plenty of processing power for data analysis
- Built-in WiFi for remote notifications
- GPIO pins for sensor connections
- Python support out of the box
- Large community and educational resources

**Purchase Link:** [raspberrypi.com](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

---

## Moisture Sensor

### Capacitive Soil Moisture Sensor

**Specifications:**
- **Model:** Songhe
- **Type:** Capacitive (corrosion-resistant)
- **Operating Voltage:** 3.3V - 5V DC
- **Output:** Analog voltage (0-3.3V)
- **Measurement Range:** Soil moisture percentage
- **Probe Length:** ~98mm
- **Probe Width:** ~23mm
- **Interface:** 3-pin (VCC, GND, AOUT/Signal)

**Features:**
- Corrosion-resistant capacitive design
- Suitable for long-term soil monitoring
- Analog output for precise readings

**Calibration Values:**
- **Air (dry):** [Your measured value]
- **Water (wet):** [Your measured value]
- **Optimal watering threshold:** [Your decision point]

**Purchase Link:** Amazon

---

## Additional Components

### MicroSD Card
- **Capacity:** 32GB recommended
- **Class:** Class 10 or UHS-I for better performance
- **Purpose:** Operating system and data storage

### Power Supply
- **Type:** USB-C Power Adapter
- **Output:** 5V DC, 3A (15W)
- **Note:** Official Raspberry Pi power supply recommended

### Jumper Wires
- **Quantity:** 3-4 wires minimum
- **Type:** Female-to-Female (or Male-to-Female depending on sensor)
- **Purpose:** Connect sensor to GPIO pins

### Optional Components
- **Breadboard:** For prototyping and testing
- **Case:** Protective case for Raspberry Pi
- **Heat Sinks:** For Raspberry Pi processor (optional but recommended)
- **Micro HDMI Cable:** For setup and debugging
- **USB Keyboard/Mouse:** For initial setup

---

## GPIO Pin Connections

### Sensor Wiring to Raspberry Pi 4

| Sensor Pin | GPIO Pin | Physical Pin | Description |
|------------|----------|--------------|-------------|
| VCC | 3.3V or 5V | Pin 1 or Pin 2 | Power supply |
| GND | Ground | Pin 6 (or any GND) | Ground connection |
| AOUT | GPIO [X] | Pin [Y] | Analog signal output |

**Note:** Raspberry Pi doesn't have built-in ADC (Analog-to-Digital Converter). You'll need either:
- **Option 1:** MCP3008 ADC chip (recommended for analog sensors)
- **Option 2:** Digital output sensor
- **Option 3:** Arduino as intermediary

---

## Total Cost Estimate

| Component | Quantity | Unit Price | Total |
|-----------|----------|------------|-------|
| Raspberry Pi 4 (4GB) | 1 | $55 | $55 |
| MicroSD Card (32GB) | 1 | $10 | $10 |
| USB-C Power Supply | 1 | $8 | $8 |
| Capacitive Moisture Sensor | 1 | $5-10 | $8 |
| MCP3008 ADC (if needed) | 1 | $4 | $4 |
| Jumper Wires (set) | 1 | $5 | $5 |
| **Total** | | | **~$90** |

*Prices are approximate and may vary*

---

## Setup Requirements

### Software Prerequisites
- Raspberry Pi OS (formerly Raspbian)
- Python 3.7+
- Required Python libraries: (see requirements.txt)
  - RPi.GPIO or gpiozero
  - spidev (for ADC communication)
  - smtplib (for email notifications)

### Initial Setup Steps
1. Flash Raspberry Pi OS to microSD card
2. Complete initial Raspberry Pi setup
3. Enable SPI interface (for ADC)
4. Install required Python packages
5. Connect and test moisture sensor
6. Calibrate sensor readings

See [docs/SETUP.md](../docs/SETUP.md) for detailed instructions.

---

## Notes for High School Students

**Why Raspberry Pi 4?**
- Perfect balance of power and affordability
- Easy to learn Python programming
- Great for STEM education
- Can run Jupyter notebooks locally
- Built-in networking for IoT projects

**Safety Notes:**
- Always power off before connecting/disconnecting components
- Double-check wiring before powering on
- Use proper 3A power supply to avoid issues
- Keep electronics away from water (except the sensor probe!)

**Learning Resources:**
- [Official Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [GPIO Pinout Reference](https://pinout.xyz/)
- [Python GPIO Tutorial](https://gpiozero.readthedocs.io/)
