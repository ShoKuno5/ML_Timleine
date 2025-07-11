# ML Conference Timeline 2026-2027

A comprehensive calendar tracking Machine Learning conferences from August 2026 to July 2027, including estimated submission deadlines based on historical patterns.

## Features

- **20+ Major ML Conferences**: Covers top-tier conferences including NeurIPS, ICML, ICLR, CVPR, ACL, and more
- **Deadline Tracking**: Both full paper and workshop/short paper submission deadlines
- **Historical Sources**: Links to previous years' conference pages for verification
- **Multiple Visualizations**: 
  - Gantt chart timeline
  - Monthly calendar view
  - Detailed markdown timeline
  - CSV export for custom analysis

## Repository Structure

```
ML_Timeline/
├── data/
│   ├── conference_schema.yaml      # Data format specification
│   └── conferences_2026_2027.yaml  # Conference data
├── scripts/
│   └── generate_calendar.py        # Visualization generator
├── output/                         # Generated files (created on run)
├── docs/                           # Additional documentation
└── requirements.txt                # Python dependencies
```

## Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ML_Timeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Generate Visualizations

Run the calendar generation script:
```bash
python scripts/generate_calendar.py
```

This will create the following files in the `output/` directory:
- `conference_gantt_chart.png` - Timeline visualization showing submission and conference periods
- `conference_calendar.png` - Monthly calendar view with color-coded deadlines
- `conference_timeline.md` - Detailed markdown timeline with all conference information
- `conference_events.csv` - Processed event data for custom analysis

## Data Format

Conference data is stored in YAML format. Each conference entry includes:

```yaml
- name: "Conference Full Name"
  acronym: "CONF"
  category: "tier1"  # tier1, tier2, or workshop
  timeline:
    full_paper:
      submission_deadline: "2026-MM-DD"
      notification: "2026-MM-DD"
    workshop_short_paper:
      submission_deadline: "2026-MM-DD"
      notification: "2026-MM-DD"
    conference_dates:
      start: "2026-MM-DD"
      end: "2026-MM-DD"
  sources:
    - year: 2025
      url: "https://conference2025.org/timeline"
```

## Adding/Updating Conferences

1. Edit `data/conferences_2026_2027.yaml`
2. Follow the schema defined in `data/conference_schema.yaml`
3. Include source URLs from previous years for verification
4. Run the generation script to update visualizations

## Important Notes

- **Estimated Dates**: All dates for 2026-2027 are estimates based on historical patterns
- **Verification**: Always check official conference websites for confirmed dates
- **Updates**: Conference organizers may change dates; this calendar provides planning estimates

## Conference Categories

- **Tier 1**: Top-tier conferences (NeurIPS, ICML, ICLR, CVPR, etc.)
- **Tier 2**: Strong regional or specialized conferences
- **Workshop**: Workshop-focused events

## Contributing

To add or update conference information:
1. Verify dates from official sources
2. Update the YAML data file
3. Include source URLs for transparency
4. Test visualization generation

## Output Examples

### Gantt Chart
Shows conference timelines with submission periods, review periods, and conference dates.

### Calendar View
Monthly grid showing:
- 🔴 Full paper deadlines
- 🔵 Workshop/short paper deadlines
- 🟢 Conference dates

### Markdown Timeline
Detailed text-based timeline organized by month with all deadline information and source links.

## License

This project is open source. Conference information is collected from publicly available sources.