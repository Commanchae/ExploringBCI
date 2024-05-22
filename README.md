# MusicGen_BCI
This repository is used for my personal brain computer interface (BCI) mini-project. As of now, the project is still on-going. This README file will be updated as relevant information comes in.

## Project's Goal
The project's goal is to develop a traditional machine learning or deep learning model that's able to make predictions on a user's brainwaves as to which musical note they're thinking of. 

Now, that sounds like a very vague goal that does not seem actionable. So, I've decided to start off small, by having three different notes for the model to predict: C4, D4, E4 (based off the notation in https://virtualpiano.net/). 

The flow of the prediction loop will be as follows:
1. The user records a 2 second snap-shot of their brain waves as they are thinking of a specific note.
2. The script extracts relevant features from this 2 second snapshot and passes it to a model.
3. The model then predicts which note the user was thinking of in the snapshot.

## Project's Current State
As of now, I have created the Data Collection script, which will allow you to record 2 second snapshots. The current data collection loop is as follows:

1. The script prompts the user to think about a specific note.
2. After 2 seconds (which acts as rest time for subsequent iterations), the script starts recording the user's brainwaves through a Muse2 stream created via the BrainFlow library.
3. The script records for 2 seconds, then goes to the next iteration.
4. This is repeated for the number of iterations set. 

Note: Step 2 has a 2 second timer before startnig to record, this is used as "rest time" for the user to prevent mental fatigue and also allow for blinking.

Now that the data collection is handled, I will have to work on creating a function/workflow to process the collected data into useful features. After that, it will be time to start some deep learning!

## Hardware Used
1. Muse2