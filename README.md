# 🧮 Python Calculator Web App

A beautiful, responsive calculator built with Python and deployed automatically using GitHub Actions and GitHub Pages.

## 🌐 Live Demo

**Try it now:** [https://jyotidabass.github.io/calculator/]


## ✨ Features

- 🖱️ **Click or Type** - Use mouse clicks or keyboard input
- 🎯 **Basic Operations** - Addition, subtraction, multiplication, division
- 🔢 **Decimal Support** - Handle decimal numbers with precision
- ⌨️ **Keyboard Shortcuts** - Full keyboard support for faster calculations
- 🎨 **Modern Design** - Clean, responsive interface that works on all devices
- ❌ **Error Handling** - Smart error detection and user-friendly messages
- 🚀 **Auto-Deploy** - Automatically updates when code changes

## 🎮 How to Use

### Mouse/Touch:
- Click number buttons to enter values
- Click operation buttons (+, -, ×, /) for calculations
- Click **=** to get results
- Click **C** to clear everything
- Click **⌫** to delete last entry

### Keyboard:
- `0-9` → Enter numbers
- `+`, `-`, `*`, `/` → Operations
- `Enter` or `=` → Calculate result
- `Escape` or `C` → Clear display
- `Backspace` → Delete last character

## 🛠️ Technology Stack

- **Python 3.11** - Generates the HTML calculator interface
- **HTML5/CSS3** - Modern, responsive design
- **JavaScript** - Interactive calculator functionality
- **GitHub Actions** - Automated deployment pipeline
- **GitHub Pages** - Free web hosting

## 📁 Project Structure

```
calculator/
├── calculator.py          # Python script that generates the web app
├── requirements.txt       # Python dependencies (none needed)
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions deployment workflow
└── README.md             # This file
```

## 🚀 Deployment Process

This project uses a modern CI/CD pipeline:

1. **Code Push** → GitHub detects changes
2. **GitHub Actions** → Runs Python script automatically
3. **Generate HTML** → Python creates the calculator webpage
4. **Deploy** → GitHub Pages hosts the live website
5. **Live Update** → Website updates automatically (2-3 minutes)

## 🔧 Local Development

Want to test locally before deploying?

```bash
# Clone the repository
git clone https://github.com/yourusername/calculator.git
cd calculator

# Run the Python script
python calculator.py

# Open index.html in your browser to test
```

## 📝 Customization Guide

### Change Colors:
Edit the CSS in `calculator.py`:
```python
.number { background: #e3f2fd; color: #1976d2; }  # Number buttons
.operator { background: #fff3e0; color: #f57c00; } # Operator buttons
.equals { background: #4caf50; color: white; }     # Equals button
```

### Add New Features:
1. Edit `calculator.py`
2. Commit and push changes
3. GitHub Actions will automatically deploy updates

### Popular Customizations:
- Change calculator title and emoji
- Add scientific functions (sin, cos, log)
- Implement memory functions (M+, M-, MR, MC)
- Add calculation history
- Create dark/light theme toggle

## 🤝 Contributing

Want to improve this calculator? Here's how:

1. **Fork** this repository
2. **Create** a new branch: `git checkout -b feature-name`
3. **Make** your changes
4. **Test** locally: `python calculator.py`
5. **Commit** changes: `git commit -m "Add new feature"`
6. **Push** to branch: `git push origin feature-name`
7. **Create** a Pull Request

## 🐛 Common Issues & Solutions

### Calculator Not Loading?
- Check if GitHub Pages is enabled in repository Settings → Pages
- Ensure "GitHub Actions" is selected as the source
- Wait 5-10 minutes for first deployment

### Buttons Not Working?
- Open browser developer tools (F12)
- Check Console tab for JavaScript errors
- Verify all code was copied correctly

### Deployment Failed?
- Go to Actions tab in your repository
- Click on the failed workflow to see error details
- Common fix: Check file names and paths are exact

## 📖 Learning Resources

This project demonstrates several important concepts:

- **Static Site Generation** with Python
- **Continuous Integration/Continuous Deployment (CI/CD)**
- **GitHub Actions** for automation
- **Responsive Web Design**
- **JavaScript Event Handling**
- **Git Version Control**

### Helpful Links:
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [MDN Web Docs](https://developer.mozilla.org/en-US/) - HTML/CSS/JavaScript reference

## 📊 Project Stats

- **Setup Time:** 15 minutes
- **Files:** 3 core files
- **Dependencies:** Zero external packages
- **Hosting Cost:** $0 (GitHub Pages is free)
- **Maintenance:** Automatic updates via GitHub Actions

## 🎯 What You'll Learn

By working with this project, you'll gain experience with:

- Modern web development workflow
- Python automation scripting
- Git/GitHub version control
- CI/CD pipeline setup
- Static site deployment
- Responsive web design principles

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Questions?

If you run into any issues or have questions:

1. Check the [Issues](../../issues) tab for common problems
2. Create a new issue if your problem isn't listed
3. Include error messages and steps you tried

## 🌟 Show Your Support

If this project helped you learn something new:

- ⭐ **Star** this repository
- 🍴 **Fork** it to customize for yourself
- 📢 **Share** it with friends learning to code
- 🐛 **Report** any bugs you find

---

**Built with ❤️ using Python and GitHub Actions**

*Happy calculating! 🧮*
