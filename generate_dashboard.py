import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr',False)
pd.set_option('max_colwidth',25)


import pandas as pd
import requests
import zipfile
import io

# Cricsheet IPL CSV ZIP
url = "https://cricsheet.org/downloads/ipl_male_csv2.zip"

# Download ZIP into memory
response = requests.get(url)
zip_bytes = io.BytesIO(response.content)

dfs = []

# Open ZIP in memory
with zipfile.ZipFile(zip_bytes) as z:
    for file in z.namelist():
        
        # Only match CSVs (skip _info.csv)
        if file.endswith(".csv") and "_info" not in file:
            
            with z.open(file) as f:
                df = pd.read_csv(f)
                df["match_file"] = file   # optional: track source
                dfs.append(df)

# Merge all matches
all_matches_df = pd.concat(dfs, ignore_index=True)

df = all_matches_df.copy()

if ('2026' in df['season'].unique()) or (2026 in df['season'].unique()):
    df = df[df['season'].isin([2026,'2026'])]
else:
    df = df[df['season'].isin([2025,'2025'])]

#Feeding players to teams

attackers = ['PD Salt','KL Rahul','Mohammed Shami','Ravi Bishnoi','AM Rahane','Mukesh Kumar',
             'AJ Hosein','V Suryavanshi','A Mhatre','Shashank Singh','V Nigam','PP Shaw','PHKD Mendis',
             'L Wood','MP Yadav', ] # 6 player Remaining 

bcc = ['SS Iyer','Rashid Khan','H Klaasen','TA Boult','JR Hazlewood','B Sai Sudharsan',
       'Azmatullah Omarzai','SE Rutherford','Dhruv Jurel','R Sai Kishore','S Gopal','Kartik Tyagi',
       'P Dubey','Harpreet Brar','Yash Thakur','SN Khan','R Powell','J Yadav','MJ Henry','Ashwani Kumar',
       'Musheer Khan','Yash Dayal','Zeeshan Ansari'] # 2 player remaining

blazing_titans = ['Shubman Gill','Ishan Kishan','KK Ahmed','YS Chahal','E Malinga','T Stubbs','N Rana',
                  'SN Thakur','M Prasidh Krishna','DL Chahar','P Simran Singh','Naman Dhir','DS Rathi',
                  'Prince Yadav','D Padikkal','J Overton','Umran Malik','Akash Singh','JA Duffy'] # 7 Players remaining

eleven_stars = ['SA Yadav','Tilak Varma','AR Patel','Arshdeep Singh','Harshit Rana','Kuldeep Yadav',
                'HV Patel','C Bosch','GD Phillips','TL Seifert','A Raghuvanshi','Ashutosh Sharma',
                'Swapnil Singh','XC Bartlett',] # 6 player remaining

kingslayers = ['V Kohli','SP Narine','JC Archer','D Brevis','KH Pandya','MA Starc','K Rabada',
               'Avesh Khan','M Shahrukh Khan','MS Dhoni','KK Nair','RA Tripathi','Shahbaz Ahmed',
               'D Ferreira','SM Curran','I Sharma','Mustafizur Rahman','Akash Deep','Rasikh Salam'] # 4 players reamining

super_kings = ['C Green','R Shepherd','M Jansen','Q de Kock','JM Sharma','M Pathirana','AK Markram',
               'VR Iyer','RD Chahar','AS Roy','Urvil Patel','Anuj Rawat','M Siddharth','Suyash Sharma',
               'Sandeep Sharma','DA Miller','LS Livingstone','A Kamboj'] # 3 players reamaining

knights = ['HH Pandya','S Dube','RA Jadeja','RR Pant','Mohammed Siraj','RK Singh','RM Patidar','TH David',
           'Nithish Kumar Reddy','Ramandeep Singh','MP Breetzke','T Natarajan','TU Deshpande','N Wadhera',
           'Sameer Rizvi','A Badoni','AA Kulkarni','MJ Suthar','Abishek Porel','A Nortje',
           'KT Maphaka','Shivam Mavi'] # 1 player remaining

thalasons = ['RD Gaikwad','JC Buttler','SV Samson','JJ Bumrah','CV Varun','Washington Sundar','R Parag',
             'JO Holder','N Burger','PVD Chameera','JD Unadkat','Suryansh Shedge',
             'JG Bethell','MK Pandey'] # 8 players remaining

troublemaker_kings = ['MR Marsh','N Pooran','B Kumar','Noor Ahmad','PJ Cummins','JP Inglis','FA Allen',
                      'LH Ferguson','Priyansh Arya','Aniket Verma','Harsh Dubey','Kumar Kushagra',
                      'VG Arora','V Puthur','R Tewatia','WG Jacks','KR Sen','Yudhvir Singh'] #6 players remaining

vsk = ['YBK Jaiswal','RG Sharma','TM Head','Abhishek Sharma','NT Ellis','SO Hetmyer','MP Stoinis',
       'MJ Santner','Abdul Samad','Arjun Tendulkar','R Minz','Vishnu Vinod','Mukesh Choudhary',
       'Arshad Khan','Mohsin Khan','M Markande','Vijaykumar Vyshak','MJ Owen','MW Short','R Ravindra',
       'SB Dubey','PH Solanki'] # 3 Playersr reamining

#Tour_02 Teams

xi_strikers = ['RD Gaikwad','HH Pandya','Ishan Kishan','H Klaasen','T Stubbs','Ramandeep Singh',
               'Dhruv Jurel','A Mhatre','Vishnu Vinod','V Puthur','PP Shaw','MJ Owen','Akash Singh',] #6players missing

rebels = ['YBK Jaiswal','C Green','TM Head','JC Buttler','N Rana','Sameer Rizvi',
          'V Suryavanshi','V Nigam','Prince Yadav','WG Jacks','Zeeshan Ansari'] #12 players remaining

rcb_xii = ['Shubman Gill','SA Yadav','PD Salt','JM Sharma','RM Patidar','PJ Cummins',
           'JO Holder','Azmatullah Omarzai','R Minz','S Gopal','DS Rathi','M Siddharth',
           'J Overton','R Ravindra','LS Livingstone','MJ Henry','Yash Dayal'] # 3 players missing

defending_champions = ['SS Iyer','V Kohli','SP Narine','RR Pant','Noor Ahmad','TH David','M Prasidh Krishna',
                       'MS Dhoni','Mohsin Khan','R Powell','J Yadav','PHKD Mendis','I Sharma',
                       'Umran Malik','Shivam Mavi','MK Pandey','Ashwani Kumar','Musheer Khan','JA Duffy']  #7 palyer missing

bloodline = ['S Dube', 'RA Jadeja', 'M Jansen', 'SV Samson', 'JC Archer', 'NT Ellis', 'D Brevis',
              'VR Iyer', 'JP Inglis', 'T Natarajan', 'K Rabada', 'R Sai Kishore', 'Naman Dhir', 
              'Vijaykumar Vyshak', 'Sandeep Sharma', 'KK Nair', 'A Nortje', 'SB Dubey'] # 4 players missing

team_r_d = ['MR Marsh', 'Abhishek Sharma', 'N Pooran', 'JJ Bumrah', 'JR Hazlewood', 'B Sai Sudharsan', 'MJ Santner', 
            'RD Chahar', 'P Simran Singh', 'Aniket Verma', 'Harsh Dubey', 'Kartik Tyagi', 'Yash Thakur', 
            'DA Miller', 'SN Khan'] #9 players missing

_7th_gear = ['Q de Kock', 'B Kumar', 'KK Ahmed', 'CV Varun', 'AM Rahane', 'Washington Sundar', 
             'MP Stoinis', 'R Parag', 'KH Pandya', 'Nithish Kumar Reddy', 'N Burger', 'DL Chahar', 
             'LH Ferguson', 'Avesh Khan', 'AS Roy', 'M Shahrukh Khan', 'Abishek Porel', 'VG Arora', 'Harpreet Brar', 
             'Suyash Sharma', 'MP Yadav',] #4 plpayer missing

attackers_xii = ['KL Rahul', 'SO Hetmyer', 'SN Thakur', 'Mukesh Kumar', 'TU Deshpande', 'AJ Hosein', 
                 'JD Unadkat', 'N Wadhera', 'Priyansh Arya', 'Abdul Samad', 'A Badoni', 'Arjun Tendulkar', 
                 'Shashank Singh', 'Urvil Patel', 'Mukesh Choudhary', 'SM Curran'] #8 players missing

sonu_48 = ['Rashid Khan', 'YS Chahal', 'Ravi Bishnoi', 'AK Markram', 'RK Singh', 'SE Rutherford', 'MA Starc', 
           'Anuj Rawat', 'Arshad Khan', 'M Markande', 'D Padikkal', 'RA Tripathi', 'R Tewatia', 'D Ferreira', 'Akash Deep', 'A Kamboj', 'Rasikh Salam']

################
### Bidstrom Auction Teams ####

roar_26 = ['SA Yadav','HH Pandya', 'MA Starc', 'Mohammed Siraj', 'Harpreet Brar', 'M Siddharth', 'D Brevis', 'R Powell', 'MJ Santner',
            'Shahbaz Ahmed', 'R Ravindra', 'J Overton', 'KK Ahmed', 'Mukesh Kumar', 'V Puthur'] #3 Players missing

defending_champions_bs = ['V Kohli', 'JC Buttler', 'RA Jadeja', 'TM Head', 'KH Pandya', 'MP Stoinis', 'S Dube', 'K Rabada',
                           'MK Pandey', 'Abdul Samad', 'AM Rahane', 'MW Short', 'JP Inglis', 'T Natarajan', 'Rasikh Salam','JA Duffy'] # 2 players remaining

bsmj = ['JM Sharma', 'PD Salt', 'Ishan Kishan', 'N Pooran', 'Abhishek Sharma', 'JJ Bumrah', 'YS Chahal', 'Mohsin Khan', 'PP Shaw', 
        'FA Allen', 'D Ferreira', 'E Malinga', 'SB Dubey', 'Kartik Tyagi'] #3 player missing

msk = ['B Sai Sudharsan', 'Shubman Gill', 'TA Boult', 'Noor Ahmad', 'N Wadhera', 'A Mhatre', 'P Simran Singh', 'V Nigam',
       'SN Khan', 'PHKD Mendis', 'Avesh Khan', 'N Burger', 'RD Chahar', 'A Badoni'] #3 players remaining

arsenal = ['PJ Cummins', 'SP Narine', 'MS Dhoni', 'YBK Jaiswal', 'H Klaasen', 'Urvil Patel', 'LH Ferguson', 'Rashid Khan', 
           'Sameer Rizvi', 'A Kamboj', 'Azmatullah Omarzai', 'WG Jacks', 'MP Yadav', 'Zeeshan Ansari', 'AR Patel','Tilak Varma'] #1 plYER MISSING

rebels_bs = ['MR Marsh', 'RD Gaikwad', 'TH David', 'R Parag', 'SV Samson', 'C Green', 'M Prasidh Krishna', 'R Sai Kishore', 
             'Aniket Verma', 'N Rana', 'JG Bethell', 'Ramandeep Singh', 'PVD Chameera', 'Kumar Kushagra'] # 3 players missing

wildwolves = ['RG Sharma', 'JC Archer', 'CV Varun', 'Naman Dhir', 'M Markande', 'DS Rathi', 'DA Miller', 'Dhruv Jurel',
               'VR Iyer', 'MJ Owen', 'MJ Henry','L Ngidi','Ashutosh Sharma', 'HV Patel'] #3 players missing

special_ones = ['KL Rahul', 'Q de Kock', 'M Jansen', 'Mohammed Shami', 'B Kumar', 'Harsh Dubey', 'VG Arora', 'D Padikkal', 
                'JO Holder', 'SN Thakur', 'AJ Hosein', 'Prince Yadav', 'V Suryavanshi','Kuldeep Yadav','SH Johnson'] # 2 player missing

attackers_bs =  ['RM Patidar', 'RM Patidar', 'Nithish Kumar Reddy', 'Washington Sundar', 'DL Chahar', 'Priyansh Arya', 'Shashank Singh',
                  'M Shahrukh Khan', 'AS Roy', 'Sandeep Sharma', 'T Stubbs', 'SO Hetmyer', 'SE Rutherford', 'JD Unadkat','RD Rickelton', 'PWH de Silva','GD Phillips'] #

sonu_48_bs = ['SS Iyer', 'RR Pant', 'AK Markram', 'RK Singh', 'JR Hazlewood', 'R Tewatia', 'Abishek Porel',
               'Suyash Sharma', 'TU Deshpande', 'LS Livingstone', 'R Shepherd', 'Umran Malik', 'Arshdeep Singh', 'R Bishnoi', 'A Raghuvanshi'] # 2 players remaining

#################
### TOURNAMENT 01 TEAMS ###

tour_01 = {'attackers':attackers,
             'bcc':bcc,
             'blazing_titans':blazing_titans,
             'eleven_stars':eleven_stars,
             'kingslayers':kingslayers,
             'super_kings':super_kings,
             'knights':knights,
             'thalasons':thalasons,
             'troublemaker_kings':troublemaker_kings,
             'vsk':vsk
}

#captain and Vice-Captain Boost
tour_01_boost_df = pd.DataFrame({'player':['C Green','V Kohli','HH Pandya','SV Samson','V Suryavanshi',
                                           'SS Iyer','N Pooran','YBK Jaiswal','Ishan Kishan','AR Patel',
                                           'AK Markram','D Brevis','RR Pant','CV Varun','SA Yadav',
                                           'KL Rahul','B Sai Sudharsan','Noor Ahmad','SO Hetmyer','Shubman Gill'
                                           ],
                            'BOOST':[2,2,2,2,2,2,2,2,2,2,
                                     1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,]})

###################
###################

###################
### TOURNAMENT 02 TEAMS ###

tour_02 = {'attackers_xii':attackers_xii,
           'rebels':rebels,
           'rcb_xii':rcb_xii,
           'defending_champions':defending_champions,
           'team_r_d':team_r_d,
           'bloodline':bloodline,
           '7th_gear':_7th_gear,
           'xi_strikers':xi_strikers,
           'sonu_48':sonu_48}

tour_02_boost_df = pd.DataFrame({'player':['KL Rahul','SV Samson','MR Marsh','YBK Jaiswal','HH Pandya',
                                           'CV Varun','AK Markram','V Kohli','Shubman Gill',
                                           'Priyansh Arya','M Jansen','Abhishek Sharma','TM Head','RD Gaikwad',
                                           'Q de Kock','D Padikkal','SS Iyer','SA Yadav'],
                            'BOOST':[2,2,2,2,2,2,2,2,2,
                                     1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]})

#####################
#####################

#####################
###### BIDSTROM AUCTION 2.0 #######

bidstrom_auction_2_0 = {'sonu_48_bs':sonu_48_bs,
                        'bsmj':bsmj,
                        'wildwolves':wildwolves,
                        'rebels_bs':rebels_bs,
                        'msk':msk,
                        'roar_26':roar_26,
                        'attackers_bs':attackers_bs,
                        'special_ones':special_ones,
                        'defending_champions_bs':defending_champions_bs,
                        'arsenal':arsenal}

bidstrom_auction_2_0_boost_df = pd.DataFrame({'player':['B Sai Sudharsan','KL Rahul','RD Gaikwad','RR Pant','Abhishek Sharma',
                                                        'Priyansh Arya','YBK Jaiswal','RG Sharma','HH Pandya','V Kohli',
                                                       'TM Head','SA Yadav','CV Varun','AR Patel','RM Patidar',
                                                       'PD Salt','SS Iyer','MR Marsh', 'V Suryavanshi','Shubman Gill'],
                            'BOOST':[2,2,2,2,2,2,2,2,2,2,
                                     1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]})

#####################
#####################

def total_points_df_return(df): #returns total_points_df

    #Match Info
    match_info = df.groupby(['match_id']).agg({'batting_team':'first','bowling_team':'first'}).reset_index()

    match_info.rename(columns={'batting_team':'team_1','bowling_team':'team_2'}, inplace=True)

    #captain and Vice-Captain Boost

    #Featue Engineering

    # Dot,1s ,2s, 3s, 4s, 6s
    df['isdot'] = ( (df['runs_off_bat']==0) & (df['wides'].isna()) & (df['noballs'].isna()) ).astype(int)
    df['is_batter_dot'] = ((df['runs_off_bat']==0) & (df['wides'].isna()) ).astype(int)
    df['isone'] = df['runs_off_bat'].apply(lambda x: 1 if x == 1 else 0)
    df['istwo'] = df['runs_off_bat'].apply(lambda x: 1 if x == 2 else 0)
    df['isthree'] = df['runs_off_bat'].apply(lambda x: 1 if x == 3 else 0)
    df['isfour'] = df['runs_off_bat'].apply(lambda x: 1 if x == 4 else 0)
    df['issix'] = df['runs_off_bat'].apply(lambda x: 1 if x == 6 else 0)

    # Bowler Runs, Over No
    df['is_bowler_runs'] = df['runs_off_bat'].fillna(0) + df['wides'].fillna(0) +df['noballs'].fillna(0) 
    df['over_no'] = df['ball'].apply(np.ceil)

    # Is Ball?
    df['is_ball'] = (df['wides'].isna() & df['noballs'].isna()).astype(int)
    df['is_batter_ball'] = (1 & df['wides'].isna()).astype(int)

    # Is bowler Wicket
    df['is_bowl_out'] = np.where(df['wicket_type'].isin(['caught', 'bowled',  'lbw', 'caught and bowled',
       'stumped', 'hit wicket']),1,0)

    #Batting Points

    #Groupby Batting df
    batting_df = df.groupby(['match_id','striker']).agg({'runs_off_bat':'sum','is_batter_ball':'sum','is_batter_dot':'sum','isfour':'sum','issix':'sum'}).reset_index()

    # Bat SR, bat points, boundary points, run Bonus
    batting_df['sr'] = round(batting_df['runs_off_bat']/batting_df['is_batter_ball'] * 100,2)
    batting_df['batting_points'] = batting_df['runs_off_bat']
    batting_df['batting_boundary_points'] = batting_df['isfour']*4 + batting_df['issix']*6
    batting_df['batting_run_bonus'] = batting_df['runs_off_bat'].apply(lambda x: 16 if x>=100 else(
                                                                                    12 if x>=75 else(
                                                                                        8 if x>=50 else(
                                                                                            4 if x>=25 else
                                                                                                -2 if x==0 else 0))   
                                                                    ))
    batting_df['batting_sr_points'] = batting_df.apply(lambda x : 0 if x['is_batter_ball']<=10 else
                                                    6 if x['sr'] > 170 else 
                                                    4 if x['sr'] > 150 else
                                                    2 if x['sr'] > 130 else
                                                    -6 if x['sr'] < 50 else
                                                    -4 if x['sr'] < 60 else
                                                    -2 if x['sr'] < 70 else 0, axis=1)
    batting_df.rename(columns={'striker':'player'}, inplace=True)
    batting_df['total_batting_points'] = batting_df['batting_points'] + batting_df['batting_boundary_points'] + batting_df['batting_run_bonus'] + batting_df['batting_sr_points']

    #Bowler Points
    
    # Groupby Bowler df for Maiden
    bowling_df = df.groupby(['match_id','bowler','over_no']).agg({'is_bowler_runs':'sum','is_ball':'sum','is_bowl_out':'sum','isdot':'sum'}).reset_index()

    # Is maiden
    bowling_df['is_maiden'] = bowling_df.apply(lambda x: 1 if ((x['is_bowler_runs']==0) & (x['isdot']==6)) else 0, axis=1)

    # # Groupby Bowler df
    bowling_df = bowling_df.groupby(['match_id','bowler']).agg({'is_bowler_runs':'sum','is_ball':'sum','is_bowl_out':'sum','isdot':'sum','is_maiden':'sum'}).reset_index()

    # Economy, Wkt points, dot points, economy points
    bowling_df['economy'] = round(bowling_df['is_bowler_runs']/bowling_df['is_ball'] *6, 2)
    bowling_df['bowling_wkt_points'] = bowling_df['is_bowl_out'] * 35
    bowling_df['bowling_dot_points'] = bowling_df['isdot']
    bowling_df['bowling_economy_points'] = bowling_df.apply(lambda x: 0 if x['is_ball']<12 else
                                                            6 if x['economy'] < 5 else
                                                            4 if x['economy'] < 6 else
                                                            2 if x['economy'] < 7 else
                                                            -6 if x['economy'] > 12 else
                                                            -4 if x['economy'] > 11 else
                                                            -2 if x['economy'] > 10 else 0, axis=1)
    bowling_df['bowling_wkt_bonus'] = bowling_df['is_bowl_out'].apply(lambda x: 12 if x >= 5 else
                                                                    8 if x >= 4 else
                                                                    4 if x >= 3 else 0)
    bowling_df['bowling_maiden_points'] = bowling_df['is_maiden'] * 12

    bowling_df.rename(columns={'bowler':'player'}, inplace=True)

    bowling_df['total_bowling_points'] = bowling_df['bowling_wkt_points'] + bowling_df['bowling_economy_points'] + bowling_df['bowling_dot_points'] + bowling_df['bowling_wkt_bonus'] +bowling_df['bowling_maiden_points'] 

    #Merging Bat_df , bowl_df , boost_df
    total_points_df = pd.merge(batting_df,bowling_df, on=['match_id','player'], how='outer')
    total_points_df = total_points_df.merge(match_info, on=['match_id'],how='outer')

    # Add Total_points clmn
    total_points_df['total_batting_points'].fillna(0, inplace=True)
    total_points_df['total_bowling_points'].fillna(0, inplace=True)

    total_points_df['total_points'] = total_points_df['total_batting_points'] + total_points_df['total_bowling_points']

    total_points_df['auction_tour_01'] = total_points_df['player'].apply(lambda x: 'attackers' if x in attackers else
                                                                      'bcc' if x in bcc else
                                                                      'blazing titans' if x in blazing_titans else
                                                                      'eleven_stars' if x in eleven_stars else
                                                                      'kingslayers' if x in kingslayers else
                                                                      'super kings' if x in super_kings else
                                                                      'super knights' if x in knights else
                                                                      'troublemaker_kings' if x in troublemaker_kings else
                                                                      'thalasons' if x in thalasons else
                                                                      'vsk' if x in vsk else 
                                                                      np.nan)
    
    total_points_df['auction_tour_02'] = total_points_df['player'].apply(lambda x: 'attackers_xii' if x in attackers_xii else
                                                                         'bloodline' if x in bloodline else
                                                                         '_7th_gear' if x in _7th_gear else
                                                                         'defending_champions' if x in defending_champions else
                                                                         'team_r_d' if x in team_r_d else
                                                                         'rebels' if x in rebels else
                                                                         'rcb_xii' if x in rcb_xii else
                                                                         'xi_strikers' if x in xi_strikers else
                                                                         'sonu_48' if x in sonu_48 else 
                                                                         np.nan)
    
    total_points_df['bidstrom_auction_2.0_team'] = total_points_df['player'].apply(lambda x: 'attackers_bs' if x in attackers_bs else
                                                                         'bsmj' if x in bsmj else
                                                                         'special_ones' if x in special_ones else
                                                                         'defending_champions_bs' if x in defending_champions_bs else
                                                                         'wildwolves' if x in wildwolves else
                                                                         'rebels_bs' if x in rebels_bs else
                                                                         'roar_26' if x in roar_26 else
                                                                         'arsenal' if x in arsenal else
                                                                         'sonu_48_bs' if x in sonu_48_bs else 
                                                                         'msk' if x in msk else
                                                                         np.nan)

    ###########################
    # Download total_points_df to get match by match player points
    ############################
    
    #total_points_df df Total points for Players
    final_df = total_points_df.groupby(['player']).agg({'total_points':'sum', 'auction_tour_01':'first','auction_tour_02':'first'}).reset_index().sort_values(by='total_points',ascending=False)
    final_df.rename(columns={'total_points':'points'},inplace=True)

    return total_points_df,final_df

total_points_df,final_df = total_points_df_return(df)



def rank_df_return(final_df,all_teams,boost_df): #returns rank_df

    # Adding Captaincy boost for player
    final_df = final_df.merge(boost_df, on='player',how='outer')
    final_df['BOOST'] = final_df['BOOST'].fillna(1)
    final_df['total_points'] = final_df['points'] * final_df['BOOST']

    #Adding Team and Team Points in Dictionary
    final_team_points_dict = {}

    for team_name, players in all_teams.items():
        final_team_points_dict[f'{team_name}'] = final_df[final_df['player'].isin(players)]['total_points'].sum()

    final_team_names = list(final_team_points_dict.keys()) # Storing Team names in a list
    final_team_points = list(final_team_points_dict.values()) # Storing Team Points In a List

    #ranking the points 
    rank_df = pd.DataFrame({'teams': final_team_names[:10],
                        'points': final_team_points[:10]})

    rank_df['rank'] = rank_df['points'].rank(ascending=False,method='min')


    ########################
    # Final Points Table for Auction
    rank_df = rank_df.sort_values(by='rank')
    ########################

    # print(total_points_df)
    print(rank_df)
    print('No. of Matches completed ', df['match_id'].nunique())

    return rank_df

rank_tour_01 = rank_df_return(final_df,
                              all_teams=tour_01,
                              boost_df=tour_01_boost_df)

rank_tour_02 = rank_df_return(final_df,
                              all_teams=tour_02,
                              boost_df=tour_02_boost_df)

bidstrom_auction_2_0_rank_df = rank_df_return(final_df,
                                              all_teams=bidstrom_auction_2_0,
                                              boost_df=bidstrom_auction_2_0_boost_df)

matches_completed = df['match_id'].nunique()


###################################
###################################
###################################

import json

rank_json_01 = json.dumps(rank_tour_01.to_dict(orient='records'))
rank_json_02 = json.dumps(rank_tour_02.to_dict(orient='records'))
bidstrom_auction_2_0_json = json.dumps(bidstrom_auction_2_0_rank_df.to_dict(orient='records'))
points_json = json.dumps(total_points_df.to_dict(orient='records'))

with open("template.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("{{RANK_DATA_01}}", rank_json_01)
html = html.replace("{{RANK_DATA_02}}", rank_json_02)
html = html.replace("{{BIDSTROM_RANK_DATA}}", bidstrom_auction_2_0_json)
html = html.replace("{{POINTS_DATA}}", points_json)
html = html.replace("{{MATCHES_COMPLETED}}", str(df['match_id'].nunique()))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)