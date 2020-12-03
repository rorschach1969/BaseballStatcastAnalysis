from pybaseball import statcast
from battingStats import *
from matplotlib.axes import Axes



def pitch_velocity(player, data, date):
    frequency = df.pitch_type.value_counts(normalize=True) * 100
    for pitch in df.pitch_type.unique():
        if (pitch != 'nan'):
            line = df.loc[(df['pitch_type'] == pitch), "release_speed"]
            if not line.empty:
                line.plot.line(label=pitch +' (' + str(round(frequency[pitch], 1)) +'%)' , style='.-')
    size = len(df) + 2
    if (size<30):
        plt.xticks(np.arange(0, size , step=2))
    else:
        plt.xticks(np.arange(0, size, step=5), rotation=45)
    plt.title(player + " Pitch Velocity " + date)
    plt.xlabel('Pitch Count')
    plt.ylabel('Velocity (MPH)')
    plt.legend(loc='upper left', bbox_to_anchor=(1.01, 1), ncol=1)
    plt.show()

def pitch_velo_scatter(player, df, day):
    frequency = df.pitch_type.value_counts(normalize=True)*100
    #print_full(data.loc[(data['player_name'] == player), ["des", 'pitch_name', 'release_speed']])
    for pitch in df.pitch_type.unique():
        if (pitch != 'nan'):
            line = df.loc[(df['pitch_type'] == pitch), "release_speed"]
            if not line.empty:
                line.plot.line(label=pitch + ' (' + str(round(frequency[pitch], 1)) + '%)', style='.')
            line = df.loc[(df['pitch_type'] == pitch) & (df['events'] == 'strikeout'), "release_speed"]
            if not line.empty:
                line.plot.line(label=pitch + 'K', style='X')


    count =1
    batter = 0
    for event in df.events:
        if str(event) != 'nan':
            batter +=1
            plt.axvline(x=count, linestyle=':', color = 'grey', alpha = .3)
        count +=1
    plt.axvline(x=count-1, linestyle=':', color='grey', alpha=.3, label='Batters ' + str(batter))
    size = len(df) +2

    if (size<30):
        plt.xticks(np.arange(0, size + 2, step=2))
    else:
        plt.xticks(np.arange(0, size + 10, step=10), rotation=45)
    plt.title(player + " Pitch Velocity " + day)
    plt.xlabel('Pitch Count')
    plt.ylabel('Velocity (MPH)')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, -0.1), ncol=2, prop={'size' : 8})
    plt.show()



def spin_rate_scatter(player, df, day):
    for pitch in df.pitch_type.unique():
        if (str(pitch) != 'nan'):
            y = df.loc[(df['pitch_type'] == pitch), ['release_speed']]
            x = df.loc[(df['pitch_type'] == pitch), ['release_spin_rate']]
            plt.scatter(x,y, label=pitch)
    plt.title(player + " Spin Rate " + day)
    plt.xlabel('Spin Rate (RPM)')
    plt.ylabel('Velocity (MPH)')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, -0.1), ncol=2, prop={'size': 8})
    plt.show()



def dataFormatPlayer(player, data):
    df = data[['pitch_type', 'release_speed', 'player_name', 'events', 'release_spin_rate', 'release_pos_x', 'release_pos_y']]
    df = df[::-1]
    df = df.loc[(data['player_name'] == player),['pitch_type', 'release_speed', 'player_name', 'events', 'release_spin_rate', 'release_pos_x', 'release_pos_y']]
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    return df


if __name__ == '__main__':

    day = '2019-07-03'
    data = statcast(start_dt= day, team ='CHC')
    for player in data.player_name.unique():
        spin_rate_scatter(player, dataFormatPlayer(player, data), day)
    print_full(data.events.unique())
        # spin_rate_scatter(player, dataFormatPlayer(player, data), day)
    # spin_rate_scatter(player, dataFormatPlayer(player, data), day)
    #date = ['2019-05-01', '2019-04-29', '2019-04-27', '2019-04-23', '2019-04-22', '2019-03-20']




