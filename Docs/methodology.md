# SCIENTIFIC METHODOLOGY

## 1. System Design Philosophy

### Core Principles:
- **Simplicity**: Easy to understand, install, and maintain
- **Reliability**: Consistent performance in diverse conditions
- **Affordability**: Accessible to all socioeconomic levels
- **Scalability**: Adaptable to various deployment scenarios

### Sensor Selection Criteria:
```
Sensor Type       | Primary Use                | Selection Rationale
------------------|----------------------------|-----------------------
Water Level       | Direct leak detection      | Low cost, high reliability
Tilt Switch       | Movement/vibration         | Simple, durable, low power
Ultrasonic        | Water level monitoring     | Non-contact, accurate
```

## 2. Technical Implementation

### Hardware Architecture:
```
┌─────────────────────────────────────────┐
│           SENSOR ARRAY                  │
│  • Water Detection (Digital)            │
│  • Movement Sensing (Digital)           │
│  • Level Monitoring (Analog/Digital)    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│        PROCESSING UNIT                   │
│  • Arduino Uno (ATmega328P)              │
│  • Real-time sensor reading              │
│  • State machine logic                   │
│  • Alert system management               │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           OUTPUT SYSTEMS                 │
│  • Visual Indicators (RGB LED)           │
│  • Auditory Alerts (Buzzer)              │
│  • Data Logging (Serial Output)          │
└─────────────────────────────────────────┘
```

### Software Architecture:

#### Main Control Loop:
```cpp
void loop() {
    // 1. Read all sensors with debounce
    // 2. Process state changes
    // 3. Execute appropriate actions
    // 4. Log events to serial
    // 5. Manage alert timing
}
```

#### Key Algorithms:
1. **Debounce Algorithm**: 200ms filtering prevents false positives
2. **State Machine**: Manages system states (Normal, Alert, Recovery)
3. **Color Mapping**: RGB values correspond to specific conditions
4. **Data Logging**: CSV format for easy analysis

## 3. Detection Methodology

### Water Leak Detection:
- **Method**: Conductivity-based sensing
- **Threshold**: Digital HIGH/LOW based on water presence
- **Response Time**: <200ms
- **False Positive Prevention**: Debounce + confirmation sampling

### Movement Detection:
- **Method**: Tilt switch with internal pull-up
- **Activation**: LOW signal when tilted >15 degrees
- **Purpose**: Detects pipe movement or equipment vibration
- **Applications**: Earthquake detection, tamper alert

### Water Level Monitoring (Optional):
- **Method**: Ultrasonic time-of-flight measurement
- **Accuracy**: ±1cm within 2-100cm range
- **Update Rate**: Every 5 seconds
- **Data Use**: Trend analysis, preventive alerts

## 4. Alert System Design

### Visual Alert System (RGB LED):
```
Condition           | Color     | RGB Values    | Meaning
--------------------|-----------|---------------|-------------------
Normal Operation    | Green     | (0, 255, 0)   | System OK
Water Leak Detected | Red       | (255, 0, 0)   | Immediate Action
Movement Detected   | Orange    | (255, 165, 0) | Investigation
Recovery State      | Blue      | (0, 0, 255)   | System Recovering
```

### Auditory Alert System (Buzzer):
```
Event Type          | Frequency | Duration      | Pattern
--------------------|-----------|---------------|-------------------
Water Leak          | 800 Hz    | 2000 ms       | Continuous
Movement            | 500 Hz    | 500 ms        | Single pulse
System Status       | 300 Hz    | 100 ms        | Confirmation beep
```

## 5. Data Collection Protocol

### Logging Format (CSV):
```
Timestamp (ms), EventType, Severity, AdditionalData
```

### Event Types:
- `SISTEMA_INICIADO`: System startup
- `VAZAMENTO_DETECTADO`: Water leak detected
- `VAZAMENTO_NORMALIZADO`: Water leak cleared
- `MOVIMENTO_DETECTADO`: Movement/vibration detected
- `MOVIMENTO_NORMALIZADO`: Movement stopped
- `NIVEL_AGUA`: Water level measurement
- `SISTEMA_OPERACIONAL`: System status check

### Severity Levels:
- `CRITICO`: Immediate action required
- `ATENCAO`: Investigation recommended
- `INFO`: Informational only

## 6. Testing and Validation

### Laboratory Testing:
- **Controlled water exposure** tests
- **Angle sensitivity** measurements
- **Response time** verification
- **False positive** rate calculation

### Field Testing:
- **Residential installation** monitoring
- **Environmental condition** testing
- **Long-term reliability** assessment
- **User interface** evaluation

### Performance Metrics:
```
Metric              | Target     | Measurement Method
--------------------|------------|---------------------
Detection Accuracy  | >95%       | Controlled tests
Response Time       | <200ms     | High-speed recording
False Positive Rate | <3%        | 30-day continuous test
System Uptime       | >99%       | Automated monitoring
```

## 7. Calibration Procedures

### Water Sensor Calibration:
1. Ensure sensor is clean and dry
2. Verify HIGH signal when dry
3. Test LOW signal when wet
4. Adjust placement if needed

### Tilt Sensor Calibration:
1. Mount sensor in desired orientation
2. Verify HIGH signal in normal position
3. Test LOW signal when tilted >15°
4. Adjust sensitivity if required

### Ultrasonic Sensor Calibration:
1. Measure known distances (10cm, 50cm, 100cm)
2. Calculate correction factor if needed
3. Verify accuracy within ±1cm
4. Update code constants if necessary

## 8. Maintenance Protocol

### Daily Checks:
- Visual inspection of LED status
- Serial monitor connection verification
- Power supply confirmation

### Weekly Maintenance:
- Sensor cleaning (water sensors)
- Physical inspection of all connections
- Data log review and backup

### Monthly Procedures:
- Full system functional test
- Battery check/replacement (if used)
- Firmware update check
- Performance report generation

### Annual Maintenance:
- Complete system recalibration
- Component replacement if worn
- Software updates as available
- Deployment location reassessment

## 9. Safety Considerations

### Electrical Safety:
- All circuits operate at <12V DC
- Proper grounding of all components
- Water-resistant enclosure for electronics
- Circuit protection against shorts

### Installation Safety:
- Avoid placement near high-voltage equipment
- Secure mounting to prevent falls
- Clear labeling of all components
- Emergency shutdown procedures

### Environmental Safety:
- Use lead-free, RoHS compliant components
- Proper disposal procedures
- Minimal environmental impact
- Energy-efficient operation

## 10. Quality Assurance

### Manufacturing Standards:
- Consistent component sourcing
- Assembly procedure documentation
- Quality control checkpoints
- Batch testing protocols

### Deployment Standards:
- Installation guidelines
- User training materials
- Troubleshooting documentation
- Support contact information

### Continuous Improvement:
- User feedback collection
- Performance data analysis
- Regular system updates
- Feature enhancement planning
