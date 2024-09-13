# Speckle-Pattern-Flow-Generator


## Output Format
The output files which includes synthetic speckle pattern sequences, .flo ground truth deformation field as well as flow vizualisations

```
<output_path>/
├── film_net/
│   ├── Sequences├──Seq1├──frame0001.png
│   │            │      ├──frame0002.png
│   │            │              .
│   │            │      ├──frame000n.png
│   │            │      
│   │            ├──Seq1├──frame0001.png
│   │            │      ├──frame0002.png
│   │            │              .
│   │            │      ├──frame000n.png
│   │            │ 
│   ├── Flow     ├──Seq1├──flow0001.flo
│   │            │      ├──frame0002.flo
│   │            │              .
│   │            │      ├──frame000n-1.png
│   │            │   .   
│   │            ├──Seq1├──frame0001.png
│   │            │      ├──frame0002.png
│   │            │              .
│   │            │      ├──frame000n.png
│   │ 
│   │ 
│   ├── Flow_vis ├──Seq1├──flow0001.flo
│   │            │      ├──frame0002.flo
│   │            │              .
│   │            │      ├──frame000n-1.png
│   │            │   .   
│   │            ├──Seq1├──frame0001.png
│   │            │      ├──frame0002.png
│   │            │              .
│   │            │      ├──frame000n.png
```
