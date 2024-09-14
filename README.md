# Speckle-Pattern-Flow-Generator

## Run Code
```
python synthetic_data_generator.py
   --output_path=C:\Users\Fisseha\Downloads\results
   --seq_number=5
   --seq_length=7
   --dimensions 512 512
```

python synthetic_data_generator.py --output_path=C:\Users\Fisseha\Downloads\results --number=5 --length=7 --dimensions 512 512

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
