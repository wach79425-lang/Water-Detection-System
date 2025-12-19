# TESTING PROTOCOL

## 1. Pre-Test Preparation

### Equipment Checklist:
- [ ] Assembled leak detection system
- [ ] USB cable and power supply
- [ ] Computer with Arduino IDE
- [ ] Serial monitor software
- [ ] Water for testing
- [ ] Measuring tools
- [ ] Stopwatch/timer

### Initial System Check:
```
1. Connect system to power
2. Verify Green LED illuminates
3. Open Serial Monitor (9600 baud)
4. Confirm "SISTEMA_INICIADO" message
5. Ensure no false alarms
```

## 2. Basic Functionality Tests

### Test 1: Water Leak Detection
```
Procedure:
1. Place water sensor in dry position
2. Add water to sensor detection area
3. Observe system response
4. Remove water and observe recovery

Expected Results:
- LED changes from Green to Red
- Buzzer sounds at 800Hz for 2000ms
- Serial logs "VAZAMENTO_DETECTADO,CRITICO"
- After water removal: LED turns Blue then Green
- Serial logs "VAZAMENTO_NORMALIZADO,INFO"

Acceptance Criteria:
- Response time <200ms
- No false positives during dry periods
- Consistent detection across 10 trials
```

### Test 2: Movement Detection
```
Procedure:
1. Ensure system is stationary
2. Tilt or vibrate the system
3. Observe alert activation
4. Return to normal position

Expected Results:
- LED changes to Orange
- Buzzer sounds at 500Hz for 500ms
- Serial logs "MOVIMENTO_DETECTADO,ATENCAO"
- After stabilization: LED returns to Green
- Serial logs "MOVIMENTO_NORMALIZADO,INFO"

Acceptance Criteria:
- Activation at >15° tilt angle
- No activation during normal handling
- Consistent response across 10 trials
```

### Test 3: Water Level Monitoring (Optional)
```
Procedure:
1. Position ultrasonic sensor above container
2. Add water in 10cm increments
3. Record level measurements
4. Verify accuracy

Expected Results:
- Serial logs "NIVEL_AGUA,[value]" every 5 seconds
- Measurements within ±1cm of actual level
- Consistent readings over time

Acceptance Criteria:
- Accuracy: ±1cm within 2-100cm range
- Update interval: 5000ms ± 500ms
- No measurement errors or timeouts
```

## 3. Performance Tests

### Response Time Measurement:
```
Equipment: High-speed camera or oscilloscope
Procedure:
1. Record system during water exposure
2. Measure time from contact to alert
3. Repeat 20 times
4. Calculate average and standard deviation

Target: <200ms average response time
Acceptable Range: 150-250ms
```

### False Positive Testing:
```
Procedure:
1. Run system for 24 hours in controlled environment
2. Simulate normal conditions (no water, minimal movement)
3. Record any false alerts
4. Calculate false positive rate

Acceptance Criteria:
- False positive rate <3%
- No consecutive false alarms
- System recovers automatically
```

### Debounce Effectiveness:
```
Procedure:
1. Rapidly add/remove water (5 times/second)
2. Observe if system treats as single event
3. Test with sensor bouncing

Expected: System should register single event
Acceptance: No multiple alerts from rapid changes
```

## 4. Environmental Tests

### Temperature Tolerance:
```
Conditions: Test at 10°C, 25°C, 40°C
Procedure:
1. Place system in temperature chamber
2. Allow 30 minutes for stabilization
3. Perform basic functionality tests
4. Record any performance changes

Acceptance Criteria:
- Full functionality across temperature range
- No permanent damage or calibration shift
- Consistent response times
```

### Humidity Testing:
```
Conditions: 30% RH, 60% RH, 90% RH
Procedure:
1. Place in humidity-controlled environment
2. Test water detection accuracy
3. Monitor for false positives
4. Check sensor drying time

Acceptance Criteria:
- No false water detection from humidity alone
- Proper operation in high humidity
- Sensors dry within 5 minutes after water exposure
```

### Vibration Resistance:
```
Procedure:
1. Mount system on vibrating platform
2. Apply vibrations simulating:
   - Foot traffic (1-10Hz)
   - Machinery (10-100Hz)
   - Transportation (100-500Hz)
3. Monitor for false movement alerts

Acceptance Criteria:
- <5% false movement alerts
- No system resets or failures
- Water detection unaffected
```

## 5. Endurance Testing

### Continuous Operation:
```
Duration: 30 days uninterrupted
Procedure:
1. Set up automatic water exposure every 6 hours
2. Record all events and system states
3. Monitor power consumption
4. Check for memory leaks or performance degradation

Metrics to Track:
- System uptime percentage
- Event detection consistency
- Alert accuracy over time
- Power stability
```

### Component Lifespan:
```
Test: Accelerated lifecycle testing
Procedure:
1. Simulate 1 year of operation in 1 month
2. Perform 100,000 detection cycles
3. Check component wear and tear
4. Measure performance degradation

Acceptance Criteria:
- >90% of original performance after testing
- No catastrophic failures
- Gradual, predictable degradation
```

## 6. User Acceptance Testing

### Installation Test:
```
Participants: 5 non-technical users
Procedure:
1. Provide components and instructions
2. Time installation process
3. Record difficulties encountered
4. Survey satisfaction

Success Criteria:
- Average installation time <30 minutes
- >80% success rate without assistance
- Satisfaction score >4/5
```

### Usability Test:
```
Procedure:
1. Demonstrate system to users
2. Have users interpret LED colors
3. Test alert recognition
4. Survey clarity and effectiveness

Success Criteria:
- >90% correct color interpretation
- Alert recognition within 10 seconds
- Overall usability score >4.5/5
```

### Maintenance Test:
```
Procedure:
1. Train users on basic maintenance
2. Have them perform weekly checks
3. Record time and accuracy
4. Survey maintenance difficulty

Success Criteria:
- Maintenance time <10 minutes/week
- >95% task completion accuracy
- Willingness to continue maintenance >80%
```

## 7. Data Analysis Tests

### Log File Verification:
```
Procedure:
1. Generate 24 hours of test data
2. Export to CSV file
3. Verify format consistency
4. Check for missing or corrupted entries

Acceptance Criteria:
- 100% of events logged
- No format errors in CSV
- Timestamps sequential and consistent
- All required fields populated
```

### Data Parsing Test:
```
Procedure:
1. Use provided Python analysis tool
2. Process sample log files
3. Verify calculation accuracy
4. Check visualization generation

Acceptance Criteria:
- All data correctly parsed
- Statistical calculations accurate
- Visualizations generated without errors
- Report contains all required information
```

## 8. Safety Tests

### Electrical Safety:
```
Tests:
1. Insulation resistance (>10MΩ)
2. Leakage current (<0.5mA)
3. Short circuit protection
4. Overvoltage protection

Acceptance: Meets basic electrical safety standards
```

### Water Exposure Safety:
```
Procedure:
1. Expose electronics to water spray
2. Verify no electrical hazards
3. Check enclosure effectiveness
4. Test recovery after exposure

Acceptance: No electrical hazards, system recovers after drying
```

## 9. Documentation Verification

### Manual Accuracy:
```
Procedure:
1. Follow installation guide step-by-step
2. Note any discrepancies or omissions
3. Test troubleshooting procedures
4. Verify all diagrams and references

Acceptance: 100% accurate, no missing steps
```

### Code Documentation:
```
Procedure:
1. Review inline code comments
2. Verify function documentation
3. Check variable naming consistency
4. Test code examples

Acceptance: Code is well-documented and understandable
```

## 10. Final Certification

### Pass/Fail Criteria:
```
Required for Certification:
- [ ] All basic functionality tests PASS
- [ ] Performance within specifications
- [ ] Environmental tests successful
- [ ] Endurance testing completed
- [ ] User acceptance positive
- [ ] Safety requirements met
- [ ] Documentation verified
- [ ] Data analysis functional
```

### Test Report Generation:
Upon completion, generate comprehensive report including:
1. Executive summary
2. Test methodology
3. Detailed results
4. Issues encountered
5. Recommendations
6. Certification decision
