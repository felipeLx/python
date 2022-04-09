import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

result = pd.read_csv('data/data_processed.csv', sep=';')
fixtures = pd.read_csv('data/fixtures.csv', sep=',')
ranking = pd.read_csv('data/fifa_ranking.csv')

"""
print(fixtures.head())
print(bra.head())
print(result.head())
"""

# recreate ranking by history ranking from first in the ranking to the last
ranking = ranking.groupby('country_full', as_index=False)['rank'].mean().round(0).sort_values(by='rank', ascending=True)
#print(ranking.head(10))

# list of the teams that will participate in the next WorldCup
team1 = fixtures['Team_1']
team2 = fixtures['Team_2']
teams = pd.concat([team1, team2], axis=0).drop_duplicates()
# clean the world cup history to have just the teams that will participate in the next WorldCup
result = result[(result['Home Team Name'].isin(teams)) | (result['Away Team Name'].isin(teams))]
team_result = result.drop(['Year', 'Stage', 'Home Team Goals', 'Away Team Goals', 'Points'], axis=1)
# print(team_result.head())

# teams best ranker: Brazil, Spain, Germany, Argentina, France, Netherlands, England and Portugal
bra = result[(result['Home Team Name'] == 'Brazil') | (result['Away Team Name'] == 'Brazil')]
esp = result[(result['Home Team Name'] == 'Spain') | (result['Away Team Name'] == 'Spain')]
ger = result[(result['Home Team Name'] == 'Germany') | (result['Away Team Name'] == 'Germany')]
arg = result[(result['Home Team Name'] == 'Argentina') | (result['Away Team Name'] == 'Argentina')]
fra = result[(result['Home Team Name'] == 'France') | (result['Away Team Name'] == 'France')]
net = result[(result['Home Team Name'] == 'Netherlands') | (result['Away Team Name'] == 'Netherlands')]
eng = result[(result['Home Team Name'] == 'England') | (result['Away Team Name'] == 'England')]
por = result[(result['Home Team Name'] == 'Portugal') | (result['Away Team Name'] == 'Portugal')]

# transforming data
final_result = pd.get_dummies(team_result, prefix=['T1', 'T2'], columns=['Home Team Name', 'Away Team Name'])
# print(final_result.head())

# building model
x = final_result.drop(['Winner'], axis=1)
y = final_result['Winner']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# initialize model and fitting data
model = LogisticRegression()
model.fit(x_train, y_train)
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)
print('Trainning accurary: ', train_score)
print('Test accuracy: ', test_score)

# predicting the winner
fixtures.insert(1, 'T1_position', fixtures['Team_1'].map(ranking.set_index('country_full')['rank']))
fixtures.insert(2, 'T2_position', fixtures['Team_2'].map(ranking.set_index('country_full')['rank']))
fixture = fixtures.iloc[:45,:]
# print(fixture.head())

# transforming the fixture
final_set = fixture[['Team_1', 'Team_2']]
final_set = pd.get_dummies(final_set, prefix=['T1', 'T2'], columns=['Team_1', 'Team_2'])

for col in (set(final_result.columns) - set(final_set.columns)):
    final_set[col] = 0
final_set = final_set.sort_index(axis=1)
final_set = final_set.drop(['Winner'], axis=1)
# print(final_set.head())

# predicting the winner
prediction = model.predict(final_set)

# display and store the prediction
for index, tuples in fixture.iterrows():
    print('Teams: ' + tuples['Team_1'] + ' vs ' + tuples['Team_2'])
    print('Winner: ' + prediction[index] + '\n')

# prepare the data to plot
for i in range(len(prediction)):
    fixture['Result'].iloc[i] = prediction[i]
fixture['Result'].value_counts().plot(kind='bar')

# combine parts to create a function
"""
def predict_result(matches,final_result,ranking,model,match_type):
    #obtaining team position 
    team_position=[]
    for match in matches:
        team_position.append([ranking.loc[ranking['Team'] == match[0],'Position'].iloc[0],ranking.loc[ranking['Team'] == match[1],'Position'].iloc[0]])
    
    #transforming data into useful information
    final=pd.DataFrame()
    final[['Team_1','Team_2']]=pd.DataFrame(matches)
    final_set=final
    final_set = pd.get_dummies(final_set, prefix=['Team_1', 'Team_2'], columns=['Team_1', 'Team_2'])
    
    for col in (set(final_result.columns)-set(final_set.columns)):
        final_set[col]=0
    final_set=final_set.sort_index(axis=1)
    final_set=final_set.drop(['Winner'],axis=1)
    
    #predict winner
    prediction=model.predict(final_set)          
    
    #Results from League mathes 
    if match_type == 'League':
        print("League Matches")
        
        final_fixture=fixtures[0:45]
        for index,tuples in final_fixture.iterrows():
            print("Teams: " + tuples['Team_1']+ " and " + tuples['Team_2'])
            print("Winner: "+ prediction[index])
            fixtures['Result'].iloc[index]=prediction[index]
    
        Semi_final_teams=[]
        for i in range(4):
            Semi_final_teams.append(fixture['Result'].value_counts().index[i])   
        matches=[(Semi_final_teams[0],Semi_final_teams[3]),(Semi_final_teams[1],Semi_final_teams[2])]
        match_type="Semi-Final"
        predict_result(matches,final_result,ranking,model,match_type)
    #Result from semi-final
    elif match_type == 'Semi-Final':
        print("\nSemi-Final Matches")
        final_fixture=fixtures[45:47]
        for index,tuples in final_fixture.iterrows():
            fixtures['Team_1'].iloc[index]=final['Team_1'].iloc[index-45]
            fixtures['Team_2'].iloc[index]=final['Team_2'].iloc[index-45]
            fixtures['Team_1_position'].iloc[index]=team_position[index-45][0]
            fixtures['Team_2_position'].iloc[index]=team_position[index-45][1]
        final_fixture=fixtures[45:47]
        for index,tuples in final_fixture.iterrows():
            print("Teams: " + tuples['Team_1']+ " and " + tuples['Team_2'])
            print("Winner: "+ prediction[index-45])
            fixtures['Result'].iloc[index]=prediction[index-45]    
        matches=[(prediction[0],prediction[1])]
        match_type="Final"
        predict_result(matches,final_result,ranking,model,match_type)
    #Result of Final        
    elif match_type == 'Final':
        print("\nFinal Match")
        final_fixture=fixtures[47:48]
        for index,tuples in final_fixture.iterrows():
            fixtures['Team_1'].iloc[index]=final['Team_1'].iloc[index-47]
            fixtures['Team_2'].iloc[index]=final['Team_2'].iloc[index-47]
            fixtures['Team_1_position'].iloc[index]=team_position[index-47][0]
            fixtures['Team_2_position'].iloc[index]=team_position[index-47][1]
        final_fixture=fixtures[47:48]
        for index,tuples in final_fixture.iterrows():
            print("Teams: " + tuples['Team_1']+ " and " + tuples['Team_2'])
            print("Winner: "+ prediction[0]+"\n")
            fixtures['Result'].iloc[index]=prediction[index-47]
        print("Winner Of the tournament is: " + fixtures['Result'].iloc[47])
"""