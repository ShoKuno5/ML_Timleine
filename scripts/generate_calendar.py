#!/usr/bin/env python3
"""
Generate ML Conference Calendar and Timeline
Creates both visual calendar and markdown timeline from YAML data
"""

import yaml
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import seaborn as sns
from pathlib import Path
import numpy as np

def load_conferences(yaml_path):
    """Load conference data from YAML file"""
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    return data['conferences']

def parse_date(date_str):
    """Parse date string, handling estimated dates"""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None

def create_timeline_dataframe(conferences):
    """Convert conference data to DataFrame for visualization"""
    events = []
    
    for conf in conferences:
        conf_name = f"{conf['acronym']} {conf['timeline']['conference_dates']['start'][:4]}"
        
        # Full paper deadlines
        if 'full_paper' in conf['timeline']:
            fp = conf['timeline']['full_paper']
            if fp.get('submission_deadline'):
                events.append({
                    'conference': conf_name,
                    'event_type': 'Full Paper Deadline',
                    'date': parse_date(fp['submission_deadline']),
                    'category': conf['category']
                })
            if fp.get('notification'):
                events.append({
                    'conference': conf_name,
                    'event_type': 'Full Paper Notification',
                    'date': parse_date(fp['notification']),
                    'category': conf['category']
                })
        
        # Workshop/short paper deadlines
        if 'workshop_short_paper' in conf['timeline']:
            ws = conf['timeline']['workshop_short_paper']
            if ws.get('submission_deadline'):
                events.append({
                    'conference': conf_name,
                    'event_type': 'Workshop/Short Paper Deadline',
                    'date': parse_date(ws['submission_deadline']),
                    'category': conf['category']
                })
        
        # Conference dates
        conf_dates = conf['timeline']['conference_dates']
        if conf_dates.get('start'):
            events.append({
                'conference': conf_name,
                'event_type': 'Conference',
                'date': parse_date(conf_dates['start']),
                'category': conf['category']
            })
    
    df = pd.DataFrame(events)
    df = df[df['date'].notna()]
    df = df.sort_values('date')
    return df

def create_gantt_chart(conferences, output_path):
    """Create Gantt chart showing conference timelines"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Color map for different event types
    colors = {
        'Full Paper Deadline': '#FF6B6B',
        'Full Paper Notification': '#4ECDC4',
        'Workshop/Short Paper Deadline': '#45B7D1',
        'Conference': '#96CEB4'
    }
    
    y_positions = {}
    y_counter = 0
    
    for i, conf in enumerate(conferences):
        conf_name = conf['acronym']
        if conf_name not in y_positions:
            y_positions[conf_name] = y_counter
            y_counter += 1
        
        y_pos = y_positions[conf_name]
        
        # Plot full paper timeline
        if 'full_paper' in conf['timeline']:
            fp = conf['timeline']['full_paper']
            
            # Submission to notification
            if fp.get('submission_deadline') and fp.get('notification'):
                start = parse_date(fp['submission_deadline'])
                end = parse_date(fp['notification'])
                if start and end:
                    ax.barh(y_pos, (end - start).days, left=start, height=0.3,
                           color=colors['Full Paper Deadline'], alpha=0.8,
                           label='Full Paper Review' if i == 0 else "")
        
        # Conference dates
        conf_dates = conf['timeline']['conference_dates']
        if conf_dates.get('start') and conf_dates.get('end'):
            start = parse_date(conf_dates['start'])
            end = parse_date(conf_dates['end'])
            if start and end:
                ax.barh(y_pos, (end - start).days, left=start, height=0.3,
                       color=colors['Conference'], alpha=0.8,
                       label='Conference' if i == 0 else "")
    
    # Format plot
    ax.set_yticks(list(y_positions.values()))
    ax.set_yticklabels(list(y_positions.keys()))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45, ha='right')
    
    ax.set_xlabel('Timeline')
    ax.set_title('ML Conference Timeline: August 2026 - July 2027', fontsize=16, pad=20)
    ax.grid(True, axis='x', alpha=0.3)
    
    # Add legend
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper right')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def create_calendar_view(df, output_path):
    """Create monthly calendar view with deadlines"""
    fig, axes = plt.subplots(4, 3, figsize=(18, 16))
    axes = axes.flatten()
    
    # Define months from Aug 2026 to Jul 2027
    months = []
    current = datetime(2026, 8, 1)
    for _ in range(12):
        months.append(current)
        if current.month == 12:
            current = datetime(current.year + 1, 1, 1)
        else:
            current = datetime(current.year, current.month + 1, 1)
    
    for idx, month_start in enumerate(months):
        ax = axes[idx]
        
        # Get month data
        if month_start.month == 12:
            month_end = datetime(month_start.year + 1, 1, 1)
        else:
            month_end = datetime(month_start.year, month_start.month + 1, 1)
        
        month_events = df[(df['date'] >= month_start) & (df['date'] < month_end)]
        
        # Create calendar grid
        ax.set_xlim(0, 7)
        ax.set_ylim(0, 6)
        ax.set_aspect('equal')
        
        # Draw month name
        month_name = month_start.strftime('%B %Y')
        ax.text(3.5, 5.5, month_name, ha='center', va='center', fontsize=14, fontweight='bold')
        
        # Draw day headers
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            ax.text(i + 0.5, 4.8, day, ha='center', va='center', fontsize=10)
        
        # Draw calendar days
        first_day = month_start.weekday()
        days_in_month = (month_end - month_start).days
        
        for day in range(1, days_in_month + 1):
            row = (first_day + day - 1) // 7
            col = (first_day + day - 1) % 7
            y_pos = 4 - row
            
            # Check for events on this day
            day_date = datetime(month_start.year, month_start.month, day)
            day_events = month_events[month_events['date'].dt.date == day_date.date()]
            
            # Color based on event type
            if len(day_events) > 0:
                if 'Conference' in day_events['event_type'].values:
                    color = '#96CEB4'
                elif 'Full Paper Deadline' in day_events['event_type'].values:
                    color = '#FF6B6B'
                elif 'Workshop/Short Paper Deadline' in day_events['event_type'].values:
                    color = '#45B7D1'
                else:
                    color = '#4ECDC4'
                
                ax.add_patch(plt.Rectangle((col, y_pos - 0.4), 0.8, 0.8, 
                                         facecolor=color, alpha=0.6))
            
            ax.text(col + 0.5, y_pos, str(day), ha='center', va='center', fontsize=9)
        
        # Remove axes
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
    
    plt.suptitle('ML Conference Calendar 2026-2027', fontsize=18)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_markdown_timeline(conferences, output_path):
    """Generate markdown file with conference timeline"""
    with open(output_path, 'w') as f:
        f.write("# ML Conference Timeline: August 2026 - July 2027\n\n")
        f.write("*Note: All dates are estimates based on historical patterns from previous years.*\n\n")
        
        # Create summary table
        f.write("## Quick Reference Table\n\n")
        f.write("| Conference | Full Paper Deadline | Workshop/Short Deadline | Conference Dates | Links |\n")
        f.write("|------------|-------------------|------------------------|------------------|-------|\n")
        
        for conf in conferences:
            fp_deadline = conf['timeline']['full_paper'].get('submission_deadline', 'TBD')
            ws_deadline = conf['timeline'].get('workshop_short_paper', {}).get('submission_deadline', 'TBD')
            conf_start = conf['timeline']['conference_dates'].get('start', 'TBD')
            conf_end = conf['timeline']['conference_dates'].get('end', 'TBD')
            
            links = []
            for source in conf.get('sources', []):
                links.append(f"[{source['year']}]({source['url']})")
            
            f.write(f"| **{conf['acronym']}** | {fp_deadline} | {ws_deadline} | {conf_start} to {conf_end} | {', '.join(links)} |\n")
        
        # Detailed timeline by month
        f.write("\n## Detailed Timeline by Month\n\n")
        
        current_month = None
        for conf in sorted(conferences, key=lambda x: x['timeline']['conference_dates']['start']):
            conf_date = parse_date(conf['timeline']['conference_dates']['start'])
            if conf_date:
                month_year = conf_date.strftime("%B %Y")
                if month_year != current_month:
                    current_month = month_year
                    f.write(f"\n### {month_year}\n\n")
                
                f.write(f"#### {conf['name']} ({conf['acronym']})\n")
                f.write(f"- **Category**: {conf['category']}\n")
                f.write(f"- **Website**: {conf['website']}\n")
                f.write(f"- **Conference Dates**: {conf['timeline']['conference_dates']['start']} to {conf['timeline']['conference_dates']['end']}\n")
                
                if 'full_paper' in conf['timeline']:
                    f.write(f"- **Full Paper**:\n")
                    f.write(f"  - Submission: {conf['timeline']['full_paper'].get('submission_deadline', 'TBD')}\n")
                    f.write(f"  - Notification: {conf['timeline']['full_paper'].get('notification', 'TBD')}\n")
                
                if 'workshop_short_paper' in conf['timeline']:
                    f.write(f"- **Workshop/Short Paper**:\n")
                    f.write(f"  - Submission: {conf['timeline']['workshop_short_paper'].get('submission_deadline', 'TBD')}\n")
                    f.write(f"  - Notification: {conf['timeline']['workshop_short_paper'].get('notification', 'TBD')}\n")
                
                if conf.get('notes'):
                    f.write(f"- **Notes**: {conf['notes']}\n")
                
                f.write("\n")

def main():
    # Set up paths
    base_dir = Path(__file__).parent.parent
    data_file = base_dir / "data" / "conferences_2026_2027.yaml"
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Load conference data
    print("Loading conference data...")
    conferences = load_conferences(data_file)
    
    # Create timeline dataframe
    print("Creating timeline dataframe...")
    df = create_timeline_dataframe(conferences)
    
    # Generate visualizations
    print("Generating Gantt chart...")
    create_gantt_chart(conferences, output_dir / "conference_gantt_chart.png")
    
    print("Generating calendar view...")
    create_calendar_view(df, output_dir / "conference_calendar.png")
    
    # Generate markdown timeline
    print("Generating markdown timeline...")
    generate_markdown_timeline(conferences, output_dir / "conference_timeline.md")
    
    # Save processed data as CSV
    print("Saving processed data as CSV...")
    df.to_csv(output_dir / "conference_events.csv", index=False)
    
    print(f"\nAll outputs generated in {output_dir}")
    print("- conference_gantt_chart.png: Timeline visualization")
    print("- conference_calendar.png: Monthly calendar view")
    print("- conference_timeline.md: Detailed markdown timeline")
    print("- conference_events.csv: Processed event data")

if __name__ == "__main__":
    main()