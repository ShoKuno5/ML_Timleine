#!/usr/bin/env python3
"""
Simple HTTP server for the ML Conference Timeline Dashboard
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuration
PORT = 8081
DIRECTORY = Path(__file__).parent

class DashboardHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    """Start the dashboard server"""
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), DashboardHTTPRequestHandler) as httpd:
        print(f"🚀 ML Conference Timeline Dashboard")
        print(f"📊 Server running at http://localhost:{PORT}")
        print(f"🌐 Open http://localhost:{PORT}/dashboard.html in your browser")
        print(f"⌨️  Press Ctrl+C to stop the server\n")
        
        # Optionally open browser automatically
        try:
            webbrowser.open(f'http://localhost:{PORT}/dashboard.html')
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == "__main__":
    main()