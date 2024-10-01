import os
import pandas as pd
import plotly.graph_objects as go

Circles_df = pd.read_csv(os.path.join('user-inputs','Circles.csv'), delimiter=';')
Sim_df = pd.read_csv(os.path.join('user-inputs',
                                          'simulation-outputs',
                                          Circles_df['SIMULATION'][0]),
                                          delimiter=';')

# removing leading and trailing whitespace in column names
keys_clean = [key.strip() for key in Sim_df.keys()]
keys_update_dict = dict(zip(Sim_df.keys(), keys_clean))
Sim_df.rename(columns=keys_update_dict, inplace=True)

labels = ['total', 'in', 'out', 'storage change', 'balance']
parents = ['', 'total', 'total', 'total', 'total']
values = [0, 0, 0, 0, 0]

for flow_n in range(len(Circles_df['VARIABLES'])):

    flow_name = Circles_df['VARIABLES'][flow_n]
    parent_name = Circles_df['TYPE'][flow_n]
    # unify units to m3
    if Circles_df['UNITS'][flow_n] == 'm3s':
        multiplier = 60*60*24
    elif Circles_df['UNITS'][flow_n] == 'm3':
        multiplier = 1

    Sim_df[flow_name] *= multiplier
    
    # create storage change variables
    if Circles_df['TYPE'][flow_n] == 'storage':

        storage_component = Circles_df['VARIABLES'][flow_n]
        new_storage_change_key = storage_component + ' change'
        Sim_df[new_storage_change_key] = Sim_df[storage_component] - Sim_df[storage_component].shift(1)

        flow_name = new_storage_change_key
        parent_name = 'storage change'

    # sum the variables and add to circle
    total_sum = Sim_df[flow_name][1:].sum()

    if parent_name == 'in':
        values[1] += total_sum
    if parent_name == 'out':
        values[2] += total_sum
    if parent_name == 'storage change':
        values[3] += abs(total_sum)

    labels.append(flow_name)
    parents.append(parent_name)
    values.append(total_sum)

values[4] = abs(values[3] - values[1] + values[2])
values[0] = values[1]+values[2]+values[3]+values[4]

fig =go.Figure(go.Sunburst(labels = labels, parents = parents, values = values,
                           branchvalues="total"))

fig.update_layout(template = 'plotly_dark')
fig.update_layout(plot_bgcolor='rgb(0,0,0)', 
                      paper_bgcolor ='rgb(0,0,0)')

fig.show()


