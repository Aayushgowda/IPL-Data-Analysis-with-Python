
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load all your datasets
deliveries = pd.read_csv('data/deliveries.csv')
matches = pd.read_csv('data/matches.csv')
batsmen_stats = pd.read_csv('data/most_run_average_strike.csv')
home_away = pd.read_csv('data/team_wise_home_and_away.csv')
teams = pd.read_csv('data/teams.csv', header=None, names=['Team'])

# Basic checks
print("✅ Matches:", matches.shape[0])
print("✅ Deliveries:", deliveries.shape[0])
print("✅ Batsman stats:", batsmen_stats.shape[0])
print("✅ Teams:", teams.shape[0])

# 1. 🔥 Top 10 Batsmen by Runs
top_batsmen = batsmen_stats.sort_values(by='total_runs', ascending=False).head(10)
fig1 = px.bar(top_batsmen, x='batsman', y='total_runs', title='🏏 Top 10 Batsmen (Total Runs)')
fig1.show()

# 2. ⚔️ Average vs Strike Rate
fig2 = px.scatter(batsmen_stats, x='strikerate', y='average', size='total_runs',
                  color='batsman', hover_name='batsman',
                  title='⚡ Strike Rate vs Batting Average')
fig2.show()

# 3. 🏠 Team Home vs Away Wins
fig3 = px.bar(home_away, x='team', y=['home_wins', 'away_wins'],
              barmode='group', title="🏠 Home vs Away Wins")
fig3.show()

# 4. 📊 Batting First vs Chasing Wins
batting_first = matches[matches['win_by_runs'] > 0].shape[0]
chasing = matches[matches['win_by_wickets'] > 0].shape[0]
plt.pie([batting_first, chasing], labels=['Bat First', 'Chase'], autopct='%1.1f%%')
plt.title("Batting 1st vs Chasing Wins")
plt.show()

# 5. 🏟️ Most Popular Venues
venue_counts = matches['venue'].value_counts().head(10)
fig5 = px.bar(venue_counts, title="Top 10 IPL Venues", labels={'index': 'Venue', 'value': 'Matches'})
fig5.show()

# 6. 💀 Most Dismissed Batsmen
dismissed = deliveries['player_dismissed'].value_counts().head(10)
fig6 = px.bar(dismissed, title='💀 Most Dismissed Players', labels={'index': 'Player', 'value': 'Dismissals'})
fig6.show()
