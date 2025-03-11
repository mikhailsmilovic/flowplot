# flowplot: circle, bar, and line flow diagrams

pip install flowplot

Usage demonstrated in the Notebook **Cycle**:
```
from flowplot import cycle
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';')
```
![circle](https://github.com/user-attachments/assets/b8e8d3da-c002-4039-b5cd-cd8a98bf604c)

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
  - m3s  
(meaning m3/second)
- with option num_cells_domain:
  - mmcell (meaning mm/day/averaged across all cells)
  - m3cell (meaning m3/day averaged across all cells)
 

  - m3scell (meaning m3/second averaged across all cells)
- with option cellsize_m2, assuming all cells are the same size in square metres
  - mm     (meaning mm/day)
```
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';', cellsize_m2=1000*1000, num_cells_domain=153451)
```
### Creates the following diagrams for a user-determined cycle:
  1. **Circles**, showing the partitioned inputs, outputs, net storage changes, and balance, aggregated spatiotemporally;
  2. **Bar graphs**, showing the partitioned inputs, outputs, net storage changes, and balance, aggregated spatiotemporal;
  3. **Line graphs, overall**, showing the inputs, outputs, net storage changes, and balance through time, aggregated spatially;
  4. **Line graphs, partitioned**, showing the partitioned flows through time, aggregated spatially.
![flowplot](https://github.com/user-attachments/assets/defcf9c5-6750-4270-b0a6-a74806361582)
