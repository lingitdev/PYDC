from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import json
from rich.console import Console
from rich.table import Table

console = Console()

with open("data/distros.json", "r", encoding="utf-8") as f:
    data = json.load(f)

distros = data["distros"]


exp = inquirer.select(
    message="What is your Linux experience level?",
    choices=[
        Choice(value="beginner", name="Beginner / Keep it easy to use"),
        Choice(value="intermediate", name="Intermediate / Somewhat comfortable with terminal"),
        Choice(value="advanced", name="Advanced / Want to build the system myself")
    ]
).execute()

purpose = inquirer.select(
    message="What will be the primary use for this computer?",
    choices=[
        Choice(value="daily", name="Daily Home / Office Work & Movies"),
        Choice(value="gaming", name="Gaming (Steam, Lutris, etc.)"),
        Choice(value="dev", name="Software Development / System Administration"),
        Choice(value="server", name="Server Setup")
    ]
).execute()

has_nvidia = inquirer.confirm(
    message="Does your system have an NVIDIA graphics card?",
    default=False
).execute()

release_type = inquirer.select(
    message="What update release philosophy do you prefer?",
    choices=[
        Choice(value="stable", name="Fixed & Stable (Major updates every 6 months, rock solid)"),
        Choice(value="rolling", name="Rolling Release (Latest packages and kernel at all times)")
    ]
).execute()

features = inquirer.checkbox(
    message="What extra features do you care about? (Select with Space):",
    choices=[
        Choice(value="privacy", name="Maximum Privacy & Anonymity"),
        Choice(value="out_of_box", name="Everything works out of the box (Drivers, Codecs)"),
        Choice(value="large_community", name="Huge Community & Abundant Documentation"),
        Choice(value="aur", name="Vast Package Repository (Like AUR)")
    ]
).execute()

ui_pref = inquirer.select(
    message="What desktop appearance do you prefer?",
    choices=[
        Choice(value="windows_like", name="Windows-like (Classic Start menu layout)"),
        Choice(value="mac_like", name="macOS / Modern sleek look"),
        Choice(value="minimal", name="Very simple, lightweight, and minimalist"),
        Choice(value="dont_care", name="Don't care / Open to trying something different")
    ]
).execute()

wants_gui_store = inquirer.confirm(
    message="Would you like to install apps via a Graphical Store (like App Store) instead of command line?",
    default=True
).execute()

user_tags = [
    exp,
    purpose,
    release_type,
    ui_pref
]

if has_nvidia:
    user_tags.append("nvidia")

if wants_gui_store:
    user_tags.append("gui_store")

user_tags.extend(features)

results = []

for distro in distros:
    score = len(set(user_tags) & set(distro["tags"]))

    results.append({
        "name": distro["name"],
        "score": score,
        "description": distro["description"],
        "url": distro["download_url"]
    })

results.sort(key=lambda x: x["score"], reverse=True)

# Table
table = Table(
    title="🐧 Top 3 Linux Distributions for You",
    header_style="bold cyan",
    show_lines=True
)

table.add_column("Rank", justify="center", style="yellow", width=6)
table.add_column("Distribution", style="bold green")
table.add_column("Match", justify="center", style="magenta", width=8)
table.add_column("Description")

for i, distro in enumerate(results[:3], start=1):
    percent = round((distro["score"] / len(user_tags)) * 100)

    table.add_row(
        str(i),
        distro["name"],
        f"{percent}%",
        distro["description"]
    )

console.print()
console.print(table)

console.print("\n[bold cyan]📥 Download Links[/bold cyan]\n")

for distro in results[:3]:
    console.print(
        f"[bold green]{distro['name']}[/bold green] Download = [blue underline]{distro['url']}[/blue underline]"
    )
