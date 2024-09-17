# Speckle-Pattern-Flow-Generator
## Description 
The goal of this repo is to generate multi-frame synthetic speckle pattern image sequences and ground-truth flows that represents the deformation field of the sequence. Each sequence has a unique speckle pattern generated by a random process which is then warped by different radomly generated deformation patterns to synthesize the full deforming sequence. This data generation can be used to supervise optical flow estimation and/or strain analysis learning processes.

## Formulation
This data generation process is inspired by [Deep DIC](https://github.com/RuYangNU/Deep-Dic-deep-learning-based-digital-image-correlation) paper.  We implemented the data generation process as described in this paper and further added the flexibility of generating multiple frames per sequence for multi-frame based learning methods.

```math
\begin{bmatrix}
u \\
v
\end{bmatrix}
=
\underbrace{
\begin{bmatrix}
cos\theta & sin\theta \\
-sin\theta & cos\theta
\end{bmatrix}
}_{\text{Rotation}}
\Biggl(
\underbrace{
\begin{bmatrix}
k_x-1 & \gamma_x \\
\gamma_y & k_y-1
\end{bmatrix}
}_{\text{Shear and scale.}}
.
\begin{bmatrix}
x \\
y
\end{bmatrix}
+
\underbrace{
\begin{bmatrix}
d_x^g \\
d_y^g
\end{bmatrix}
\Biggl)
}_{\text{2D gaussian deformation}}
+
\underbrace{
\begin{bmatrix}
t_x \\
t_y
\end{bmatrix}
}_{\text{Translation}}
```
## Run Code
There are four arguments to be specified by the user. `--output_path` specfies the directory where generated image sequences, ground-truth flows and flow vizualizations will be saved.  `--seq_number` and `--seq_length` represent the number of random speckle pattern sequences to generate and the number of frames per each sequence, respectively.
Lastly, the `--dimensions` argument specifies the height and width of the output speckle patterns.
```
python synthetic_data_generator.py
   --output_path=<output_path>
   --seq_number=5
   --seq_length=7
   --dimensions 512 512
```

## Sample demo
Sample sequences can be found in [Sample sequence](https://drive.google.com/file/d/1_3Y8ZrwYb74aBwnhkyuCRy1CM4pd0Zv7/view?usp=sharing). And below is example sequence with corresponding `u`, `v` flow components and `magnitude` of the sequence's underlining deformation.

<p align="center">
   <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence.gif" width="200" height="200" alt="Demo GIF">
   <img src="https://github.com/Fisseha21/Speckle-Pattern-Flow-Generator/blob/main/Samples/Speckle_sequence_flow.gif" width="500" height="250" alt="Demo GIF">
</p>

## Output Format
The output files which includes synthetic speckle pattern image sequences, `.flo` ground truth deformation field which contains the `u` and `v` components of the flow, as well as flow visualizations, heatmap of the `u` and `v` flows.

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

## Acknowledgement 
