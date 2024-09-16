# Speckle-Pattern-Flow-Generator

## Run Code
There four arguments to be specified by the user. `--output_path` specfies the directory where generated image sequences, ground-truth flows and flow vizualizations will be saved.  `--seq_number`and  `--seq_length` represent the number of random speckle pattern sequences to generate and the number of frames per each sequences, respectively.
Lastly, the `--dimensions` argument specifies the height and width of the output speckle patterns.
```
python synthetic_data_generator.py
   --output_path=<output_path>
   --seq_number=5
   --seq_length=7
   --dimensions 512 512
```

## Sample demo

<p align="center">
   <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif" width="200" height="200" alt="Demo GIF">
   <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence_flow.gif" width="500" height="250" alt="Demo GIF">
</p>


<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <!-- First GIF and caption -->
  <div style="display: flex; flex-direction: column; align-items: center;">
    <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif" style="height: 200px; width="200" alt="Demo GIF">
    <p>Caption for GIF 1</p>
  </div>

  <!-- Second GIF and caption -->
  <div style="display: flex; flex-direction: column; align-items: center;">
    <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence_flow.gif" style="height: 500px; width="250" alt="Demo GIF">
    <p>Caption for GIF 2</p>
  </div>
</div>

## Output Format
The output files which includes synthetic speckle pattern sequences, .flo ground truth deformation field as well as flow vizualisations

```
├── <output_path>/
│   ├── Sequences├──Seq1├──frame0001.png
│   │            │              .
│   │            │      ├──frame000n.png     
│   │            │ 
│   ├── Flow     ├──Seq1├──flow0001.flo
│   │            │              .
│   │            │      ├──frame000n-1.flo
│   │            │     
│   ├── Flow_vis ├──Seq1├──flow0001.png
│   │            │              .
│   │            │      ├──frame000n-1.png
```
