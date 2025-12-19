# CIRCUIT SCHEMATIC

## Arduino Pin Connections

### Input Sensors:
1. **Water Level Sensor** → Pin 2
   ```
   Sensor Signal → Pin 2
   Sensor VCC → 5V
   Sensor GND → GND
   ```

2. **Tilt Switch** → Pin 3 (with internal pull-up)
   ```
   Pin 3 → Tilt Switch → GND
   ```

3. **Ultrasonic Sensor (HC-SR04)**:
   ```
   VCC → 5V
   Trig → Pin 9
   Echo → Pin 10
   GND → GND
   ```

### Output Devices:
4. **Buzzer** → Pin 8
   ```
   Pin 8 → Buzzer (+) → Buzzer (-) → GND
   ```

5. **RGB LED**:
   ```
   Pin 5 (Red) → 220Ω → R LED → GND
   Pin 6 (Green) → 220Ω → G LED → GND
   Pin 7 (Blue) → 220Ω → B LED → GND
   ```

## Color Coding System

### LED Status Indicators:
- **GREEN (0,255,0)**: System normal, no leaks
- **RED (255,0,0)**: Water leak detected (CRITICAL)
- **ORANGE (255,165,0)**: Movement/vibration detected (ATTENTION)
- **BLUE (0,0,255)**: System recovering after leak

### Alert Patterns:
- **Water Leak**: Red LED + 800Hz buzzer (2 seconds)
- **Movement**: Orange LED + 500Hz buzzer (0.5 seconds)
- **Water Level Monitoring**: Continuous ultrasonic measurement

## Power Requirements
- **Primary**: USB 5V (500mA)
- **Optional**: 9V battery backup
- **Consumption**: <100mA average
- **24/7 Operation**: Suitable for continuous monitoring
