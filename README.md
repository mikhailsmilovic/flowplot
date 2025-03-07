# FlowPlot: flow diagrams and assessment tools

pip install flowplot

Usage demonstrated in the Notebook **Cycle**:
```
from flowplot import cycle
cycle(r".\user-inputs\cycles\Overall.csv", delimiter=';')
```
_user-inputs_ folder includes user-input examples of: 
- flow time series: this is the simplest when each line represents m3d or m3s, already scaled by cell area
- cycles: associates the cycle flows as in, out, storage, and sub-flows

Creates the following three diagrams for a user-determined cycle:
1. **Water circles**, showing the partitioned inputs, outputs, net storage changes, and balance, aggregated spatiotemporal;
2. **Line graphs, overall**, showing the inputs, outputs, net storage changes, and balance through time, aggregated spatially;
3. **Line graphs, partitioned**, showing the partitioned flows through time, aggregated spatially.
![image](https://github.com/user-attachments/assets/c3d8cae7-bf6b-4cdd-aad2-508964d65ed9)
