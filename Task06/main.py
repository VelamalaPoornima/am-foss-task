import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import csv
import os
import datetime

# Define your bot's command prefix
bot = commands.Bot(command_prefix="/")

# Define the CSV file name
CSV_FILE = "live_scores.csv"

# Function to scrape live cricket scores
def scrape_live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores" 
    headers = {"User-Agent": "Your User Agent"}  # Set your user agent
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract relevant information from the website
        team1 = soup.find("div", class_="team1-score").get_text()
        team2 = soup.find("div", class_="team2-score").get_text()
        summary = soup.find("div", class_="match-summary").get_text()

        return team1, team2, summary
    else:
        return None

# Function to append live score data to the CSV file
def append_to_csv(data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp] + list(data))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name="livescore")
async def live_score(ctx):
    live_data = scrape_live_scores()
    if live_data:
        append_to_csv(live_data)
        team1, team2, summary = live_data
        response = f"**Team 1**: {team1}\n**Team 2**: {team2}\n**Summary**: {summary}"
    else:
        response = "Failed to fetch live scores."
    await ctx.send(response)

@bot.command(name="generate")
async def generate_csv(ctx):
    # Check if the CSV file exists
    if os.path.exists(CSV_FILE):
        await ctx.send(file=discord.File(CSV_FILE))
    else:
        await ctx.send("No live score data available.")

@bot.command(name="help")
async def help_command(ctx):
    response = (
        "Commands:\n"
        "/livescore - Get live cricket score updates.\n"
        "/generate - Get the CSV file containing live score data.\n"
        "/help - Show this help message."
    )
    await ctx.send(response)

# Run the bot with your token
bot.run("MTE1NTM5NzIwMjkzMjQwODMyMA.GRQR0A.v21Tcc0dVgkjczdAefaa8WHWBt9NHVuu0-MYZc")
