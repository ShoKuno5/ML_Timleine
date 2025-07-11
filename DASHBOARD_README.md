# ML Conference Timeline Dashboard

A modern, ultra-interactive web dashboard for visualizing Machine Learning conference timelines from August 2026 to July 2027.

## 🚀 Features

### Interactive Elements
- **Clickable Stat Cards**: Click any stat to navigate to relevant sections
- **Smart Legend**: Click legend items to filter data instantly
- **Clickable Table Rows**: Click any conference row for detailed modal
- **Live Countdown Timer**: Real-time countdown to next deadline
- **Interactive Tooltips**: Hover over elements for helpful hints

### Navigation & Controls
- **Keyboard Shortcuts**: 1-5 (tabs), R (refresh), F (search), T (dark mode), E (export)
- **Quick Action Buttons**: Upcoming deadlines, Tier 1 filter, refresh
- **Header Controls**: Dark mode toggle, export, settings
- **Smart Search**: Auto-suggestions and real-time filtering

### Data Management
- **Favorites System**: Star conferences to save them to favorites
- **Export Functions**: Export data as CSV or download visualizations
- **Calendar Integration**: One-click Google Calendar event creation
- **Filter Persistence**: Filters remembered across tabs

### Visual Experience
- **Dark/Light Mode**: Toggle between themes (saves preference)
- **Notification System**: Real-time feedback for all actions
- **Smooth Animations**: Hover effects and transitions
- **Responsive Design**: Perfect on desktop, tablet, and mobile
- **Image Zoom**: Click visualizations for full-screen view

### Smart Features
- **Badge System**: Visual indicators for upcoming deadlines
- **Conference Details Modal**: Full information popup for each event
- **Search Suggestions**: Intelligent autocomplete for conference search
- **Dynamic Badges**: Live counters on navigation tabs

## 🎯 How to Use

### Option 1: Using Python Server (Recommended)
```bash
python serve_dashboard.py
```
This starts a local server and automatically opens the dashboard.

### Option 2: Direct File Access
Simply open `dashboard.html` in your web browser.

## 📊 Dashboard Sections

### Overview Tab
- **Clickable Statistics**: Click any stat card to navigate to related data
- **Interactive Legend**: Click legend items to filter by event type
- **Favorites Display**: Your starred conferences with upcoming events
- **Live Countdown**: Real-time timer to next deadline

### Timeline View Tab
- **Gantt Chart**: Complete conference timeline visualization
- **Export Button**: Download the chart image
- **Zoom Feature**: Click to enlarge

### Calendar View Tab
- **Monthly Grid**: 12-month calendar with color-coded events
- **Export Button**: Download the calendar image
- **Zoom Feature**: Click to enlarge

### Detailed Timeline Tab
- **Smart Search**: Type to search with auto-suggestions
- **Real-time Filter**: Results update as you type
- **Clear Button**: Quick search reset

### Data Table Tab
- **Favorite Stars**: Click ⭐ to add/remove from favorites
- **Clickable Rows**: Click any row for detailed conference modal
- **Calendar Buttons**: One-click Google Calendar integration
- **Sort Headers**: Click column headers to sort (🔽 indicators)
- **Advanced Filters**: Filter by event type and conference tier
- **Export CSV**: Download filtered data

## 🔧 Interactive Features

### Conference Detail Modal
- **Complete Information**: Category, event type, date, days until
- **Calendar Link**: Direct Google Calendar integration
- **Days Until**: Live countdown for each event

### Favorites System
- **Star Management**: Click ⭐ in any table row
- **Persistent Storage**: Favorites saved in browser
- **Quick Overview**: See all favorites on Overview tab

### Smart Navigation
- **Tab Badges**: Live counters for important data
- **Quick Actions**: Shortcut buttons for common tasks
- **Keyboard Shortcuts**: Fast navigation without mouse

### Export & Integration
- **CSV Export**: Download complete or filtered data
- **Image Export**: Save visualizations locally
- **Calendar Integration**: Create Google Calendar events
- **Settings Persistence**: Dark mode and preferences saved

## ⌨️ Keyboard Shortcuts

- **1-5**: Switch between tabs
- **R**: Refresh data
- **F**: Focus search box
- **T**: Toggle dark/light mode
- **E**: Export data

## 🔄 Updating Data

1. Update conference data in `data/conferences_2026_2027.yaml`
2. Run visualization generator: `python scripts/generate_calendar.py`
3. Refresh dashboard in browser

## 🎨 Color Coding

- 🔴 **Red**: Full paper deadlines
- 🟦 **Cyan**: Full paper notifications  
- 🔵 **Blue**: Workshop/short paper deadlines
- 🟢 **Green**: Conference dates

## 💡 Pro Tips

- **Hover Everything**: Most elements have helpful tooltips
- **Use Favorites**: Star important conferences for quick access
- **Keyboard Navigation**: Use shortcuts for faster workflow
- **Mobile Friendly**: Works perfectly on phones and tablets
- **Dark Mode**: Easy on the eyes for long research sessions
- **Export Often**: Download data for offline analysis