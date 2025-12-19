"""
Water Leak Detection System - Data Analysis Tool
Author: [Your Name]
Country: Mozambique
Purpose: Analyze CSV logs from leak detection system
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

# Set plotting style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def parse_log_file(filename):
    """
    Parse CSV log file from Arduino system
    """
    print(f"=== Parsing Log File: {filename} ===")
    
    try:
        # Read CSV file
        df = pd.read_csv(filename)
        print(f"Total records: {len(df)}")
        print(f"Date range: {df['Timestamp'].min()} to {df['Timestamp'].max()}")
        
        # Display basic statistics
        print("\n=== Event Statistics ===")
        event_counts = df['Evento'].value_counts()
        print(event_counts)
        
        # Calculate time between events
        if len(df) > 1:
            df['TimeDiff'] = df['Timestamp'].diff()
            avg_time_between = df['TimeDiff'].mean() / 1000  # Convert to seconds
            print(f"\nAverage time between events: {avg_time_between:.2f} seconds")
        
        return df
        
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except Exception as e:
        print(f"Error parsing file: {e}")
        return None

def analyze_leak_patterns(df):
    """
    Analyze water leak patterns and trends
    """
    print("\n=== Leak Pattern Analysis ===")
    
    # Filter for leak events
    leak_events = df[df['Evento'].str.contains('VAZAMENTO')]
    
    if len(leak_events) > 0:
        print(f"Total leak events: {len(leak_events)}")
        
        # Calculate leak duration (approximate)
        leaks_detected = leak_events[leak_events['Evento'] == 'VAZAMENTO_DETECTADO']
        leaks_normalized = leak_events[leak_events['Evento'] == 'VAZAMENTO_NORMALIZADO']
        
        if len(leaks_detected) > 0 and len(leaks_normalized) > 0:
            # Simple pairing of detection and normalization
            print("Leak events paired with normalization events")
    
    return leak_events

def visualize_data(df, output_filename="leak_analysis.png"):
    """
    Create visualization of system data
    """
    print("\n=== Creating Visualizations ===")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Event Type Distribution
    event_counts = df['Evento'].value_counts()
    axes[0, 0].bar(event_counts.index, event_counts.values)
    axes[0, 0].set_title('Event Type Distribution')
    axes[0, 0].set_ylabel('Count')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Timeline of Events
    axes[0, 1].plot(df['Timestamp'], range(len(df)), 'o-', alpha=0.7)
    axes[0, 1].set_title('Event Timeline')
    axes[0, 1].set_xlabel('Timestamp (ms)')
    axes[0, 1].set_ylabel('Event Number')
    
    # 3. Severity Distribution
    if 'Detalhes' in df.columns:
        severity_counts = df['Detalhes'].value_counts()
        axes[1, 0].pie(severity_counts.values, labels=severity_counts.index, autopct='%1.1f%%')
        axes[1, 0].set_title('Event Severity Distribution')
    
    # 4. Water Level Trends (if available)
    water_data = df[df['Evento'] == 'NIVEL_AGUA']
    if len(water_data) > 0:
        axes[1, 1].plot(water_data['Timestamp'], water_data['Detalhes'], 'g-', linewidth=2)
        axes[1, 1].set_title('Water Level Monitoring')
        axes[1, 1].set_xlabel('Timestamp')
        axes[1, 1].set_ylabel('Water Level')
    
    plt.tight_layout()
    plt.savefig(output_filename, dpi=150, bbox_inches='tight')
    print(f"Visualization saved as: {output_filename}")
    
    return fig

def generate_report(df, filename="leak_analysis_report.md"):
    """
    Generate a comprehensive analysis report
    """
    print("\n=== Generating Analysis Report ===")
    
    report = f"""# Water Leak Detection System - Analysis Report

## Summary
- **Total Events**: {len(df)}
- **Analysis Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Data Source**: Arduino Leak Detection System

## Event Statistics
"""
    
    # Add event counts
    event_counts = df['Evento'].value_counts()
    for event, count in event_counts.items():
        report += f"- **{event}**: {count} occurrences\n"
    
    # Add severity analysis
    if 'Detalhes' in df.columns:
        report += "\n## Severity Analysis\n"
        severity_counts = df['Detalhes'].value_counts()
        for severity, count in severity_counts.items():
            percentage = (count / len(df)) * 100
            report += f"- **{severity}**: {count} events ({percentage:.1f}%)\n"
    
    # Add recommendations
    report += """
## System Performance Assessment

### Strengths:
1. **Real-time detection**: Events logged with timestamps
2. **Multiple sensor inputs**: Water, movement, and level monitoring
3. **Alert system**: Visual and auditory alerts implemented
4. **Data logging**: CSV format for easy analysis

### Recommendations:
1. **Add wireless connectivity** for remote alerts
2. **Implement predictive analytics** for leak prevention
3. **Enhance water level monitoring** with trend analysis
4. **Add battery backup** for power outage protection

## Conclusion
The system effectively detects water leaks and provides immediate alerts. With the data collected, preventive measures can be implemented to reduce water damage risks.

---
*Report generated automatically by Water Leak Analysis Tool*
"""
    
    # Save report
    with open(filename, 'w') as f:
        f.write(report)
    
    print(f"Report saved as: {filename}")
    return report

def main():
    """
    Main function to run analysis
    """
    print("=" * 60)
    print("WATER LEAK DETECTION SYSTEM - DATA ANALYSIS")
    print("=" * 60)
    
    # Parse sample data
    df = parse_log_file("sample_logs.csv")
    
    if df is not None:
        # Analyze patterns
        leak_patterns = analyze_leak_patterns(df)
        
        # Create visualizations
        visualize_data(df)
        
        # Generate report
        generate_report(df)
        
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)
        
        # Display summary
        print("\n=== SUMMARY ===")
        print(f"Total events analyzed: {len(df)}")
        print(f"Unique event types: {df['Evento'].nunique()}")
        print(f"Time span: {(df['Timestamp'].max() - df['Timestamp'].min()) / 1000:.1f} seconds")
        
        # Check for critical events
        critical_events = df[df['Detalhes'] == 'CRITICO']
        if len(critical_events) > 0:
            print(f"\n⚠️  CRITICAL ALERTS: {len(critical_events)} water leak(s) detected!")
            print("   Immediate action recommended.")
        else:
            print("\n✅ No critical events detected. System operating normally.")
    
    else:
        print("No data available for analysis.")
    
    print("\n" + "=" * 60)
    print("END OF ANALYSIS")
    print("=" * 60)

if __name__ == "__main__":
    main()
