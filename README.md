# Speckle-Pattern-Flow-Generator

## Sample demo
![A sample 2 seconds moment.](https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif)

<img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif" width="100" height="100" alt="Demo GIF">
## Output Format
The output files which includes synthetic speckle pattern sequences, .flo ground truth deformation field as well as flow vizualisations

```
├── <output_path>/
│   ├── Sequences├──Seq1├──frame0001.png
│   │            │              .
│   │            │      ├──frame000n.png
│   │            │      
│   │            │ 
│   ├── Flow     ├──Seq1├──flow0001.flo
│   │            │              .
│   │            │      ├──frame000n-1.flo
│   │            │     
│   │ 
│   │ 
│   ├── Flow_vis ├──Seq1├──flow0001.png
│   │            │              .
│   │            │      ├──frame000n-1.png
```
