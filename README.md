# FlowPlot: flow diagrams and assessment tools

pip install flowplot

Usage demonstrated in the Notebook **Cycle**:
```
from flowplot import cycle
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';')
```
_user-inputs_ folder includes user-input examples of: 
### flow time series:
- Contains three columns for the date: YYYY, MM,  DD
- Column names match those indicated in the cycles csv below
- Columns hold daily values of flows, simplest when the unit is m3 or m3s (meaning m3/day or m3/second)

### cycles: 
- associates the cycle flows as in, out, storage, and sub-flows

### Creates the following diagrams for a user-determined cycle:
1. **Water circles**, showing the partitioned inputs, outputs, net storage changes, and balance, aggregated spatiotemporal;
2. **Line graphs, overall**, showing the inputs, outputs, net storage changes, and balance through time, aggregated spatially;
3. **Line graphs, partitioned**, showing the partitioned flows through time, aggregated spatially.
![image](https://github.com/user-attachments/assets/c3d8cae7-bf6b-4cdd-aad2-508964d65ed9)
