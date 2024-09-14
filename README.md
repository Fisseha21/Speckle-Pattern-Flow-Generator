# Speckle-Pattern-Flow-Generator

## Run Code
There `--output_path`, which controls
the number of times the frame interpolator is invoked. When the number of frames
in a directory is `num_frames`, the number of output frames will be
`(2^times_to_interpolate+1)*(num_frames-1)`.
```
python synthetic_data_generator.py
   --output_path=<output_path>
   --seq_number=5
   --seq_length=7
   --dimensions 512 512
```

## Sample demo
<img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif" width="200" height="200" alt="Demo GIF">

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
