# Active Learning Evaluation
Fraunhofer IPA Project

Evaluation of active learning pipeline:

The project aims to evaluate a process to reduce manual labelling effort by active learning.

Process involves:
  1. Label a small set of train data.
  2. Train the model on the labelled data.
  3. Use the model to make predictions on some more data.
  4. Use manual labelling, if the model misses finding some labels.
  5. continue from step 2, gradually increasing the model accuracy.

To start with Synthetic Data was produced using Blender. It was partitioned into train, test sets.

![alt test](synthdata/Screenshot.png)
  The data consists of images with randomly positioned screw holes, with varying light conditions, controlled in the blender environment.
  A sample:
  
  ![alt test](synthdata/nex.png)
