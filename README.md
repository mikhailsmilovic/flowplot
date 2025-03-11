# FlowPlot: flow diagrams and assessment tools

pip install flowplot

Usage demonstrated in the Notebook **Cycle**:
```
from flowplot import cycle
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';')
```
### Creates the following diagrams for a user-determined cycle:
1. **Water circles**, showing the partitioned inputs, outputs, net storage changes, and balance, aggregated spatiotemporal;
2. **Line graphs, overall**, showing the inputs, outputs, net storage changes, and balance through time, aggregated spatially;
3. **Line graphs, partitioned**, showing the partitioned flows through time, aggregated spatially.
![image](https://github.com/user-attachments/assets/c3d8cae7-bf6b-4cdd-aad2-508964d65ed9)

### user-inputs folder includes: 
#### cycles: 
- associates the cycle flows as in, out, storage, and sub-flows
  
#### flow time series:
- Contains three columns for the date: YYYY, MM,  DD
- Column names match those indicated in the cycles csv above
- There can be several csv files holding flow time series
- Columns hold daily values of flows, with name and unit indicated in cycle csv


### Units
- standard
  - m3   (meaning m3/day)
  - m3s  (meaning m3/second)
- with option num_cells_domain:
  - mmcell (meaning mm/day/averaged across all cells)
  - m3cell (meaning m3/day averaged across all cells)
  - m3scell (meaning m3/second averaged across all cells)
- with option cellsize_m2, assuming all cells are the same size in square metres
  - mm     (meaning mm/day)
```
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';', cellsize_m2=1000*1000, num_cells_domain=153451)
```

