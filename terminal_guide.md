# Terminal Menu Options & Guide

## 🚀 How to Access Terminal

### In Cursor/VS Code:
- **Ctrl+`** (backtick) - Toggle terminal
- **Ctrl+Shift+`** - New terminal  
- **View → Terminal** - Menu option

## 📋 Basic Terminal Commands

### Navigation:
- `pwd` - Show current directory
- `ls` - List files (`ls -la` for detailed view)
- `cd` - Change directory

### File Operations:
- `cat filename` - View file contents
- `nano filename` - Edit files
- `touch filename` - Create empty files
- `mkdir dirname` - Create directories

## 🐍 Python/Flask Project Commands

### Setup:
```bash
pip3 install -r requirements.txt  # Install dependencies
pip3 list                         # Show installed packages
```

### Run Application:
```bash
python3 app.py                   # Start Flask server
python3 app.py &                 # Run in background
```

### Development & Testing:
```bash
python3 -c "import flask; print('Flask version:', flask.__version__)"
curl http://localhost:5000        # Test the app (if running)
curl http://localhost:5000/about  # Test about page
```

### Virtual Environment:
```bash
python3 -m venv venv              # Create virtual environment
source venv/bin/activate          # Activate virtual environment
deactivate                        # Deactivate virtual environment
```

## 📁 Git Commands

```bash
git status                        # Check repository status
git add .                         # Stage all changes
git commit -m "message"          # Commit changes
git log                          # View commit history
git branch                       # List branches
```

## ⌨️ Terminal Shortcuts

- **Ctrl+C** - Stop running command
- **Ctrl+L** - Clear screen  
- **Ctrl+R** - Search command history
- **Tab** - Auto-complete
- **↑/↓ arrows** - Navigate command history

## 🔧 Utility Commands

```bash
clear                          # Clear terminal screen
history                        # Show command history
which python3                 # Find Python location
ps aux | grep python           # Find running Python processes
whoami                         # Current user
uname -a                       # System information
```

## 🎯 Current Environment

- **OS**: Linux 6.12.8+
- **User**: ubuntu
- **Shell**: /bin/bash
- **Python**: Python 3.13.3
- **Working Directory**: /workspace
- **Project**: Flask Web Application

## 📦 Project Structure

```
/workspace/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .git/              # Git repository
```

---

**Quick Start**: Run `python3 app.py` to start your Flask server, then visit `http://localhost:5000` in your browser!