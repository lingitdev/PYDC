# 🐧 PYDC - Python Distribution Chooser

A lightweight terminal-based Linux distribution recommendation tool built with Python.

PYDC asks a series of interactive questions about your experience, hardware, and preferences, then compares your answers against a JSON-based Linux distribution database to recommend the **three most suitable Linux distributions**.

---

## ✨ Features

- Interactive terminal questionnaire
- Recommends the top 3 Linux distributions
- JSON-powered distribution database
- Rich terminal table output
- Direct download links for recommended distributions
- Easily extendable by adding new distributions to `distros.json`

---

## 📦 Requirements

- Python 3.10+
- pip

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/PYDC.git
cd PYDC
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Answer the interactive questions, and PYDC will recommend the three Linux distributions that best match your preferences.

---

## 📁 Project Structure

```
PYDC/
│
├── data/
│   └── distros.json
│
├── src/
│   └── main.py
|
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠️ Built With

- **Python**
- **InquirerPy** – Interactive terminal prompts
- **Rich** – Beautiful terminal formatting
- **JSON** – Distribution database

---

## 📈 Future Improvements

- Weighted recommendation algorithm
- More Linux distributions
- Distribution comparison mode
- Export recommendations to a text file
- Optional command-line arguments
- Multi-language support

---

## 📄 License

This project is licensed under the GNU GNU General Public License v3.0.

---

## 🤝 Contributing

Contributions are welcome!
If you'd like to improve the recommendation algorithm, add new Linux distributions, or fix bugs, feel free to open an issue or submit a pull request.
