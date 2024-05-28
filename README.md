UPDATE: This repository is being revamped, as this will now be a general page of my BCI projects.

Recent Update: I collected 400 observations for notes C4, D4, E4, and also doing nothing. The random forest model fitted (just to test predictability) is able to achieve 73% accuracy! Notes D4 and E4 seem to be hard to distinguish, this could be because recording it was also difficult.

# ExploringBCI
This repository is used for my personal brain computer interface (BCI) projects. As of now, I am working on MusicGENBCI, developing a model to make predictions as to which musical note the user is thinking of. the project is still on-going. This README file will be updated as relevant information comes in.

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

Note: Step 2 has a 2 second timer before starting to record, this is used as "rest time" for the user to prevent mental fatigue and also allow for blinking.

Now that the data collection is handled, I have also worked on developing a workflow for the data. After receiving the data recording, a copy is made, which gets denoised. After that, the power spectral density for each wave category (alpha, beta, gamma, etc.) gets extracted into features. Since we have 4 useful EEG channels, we will have a total of 20 features! By simply fitting a random forest model, we were able to achieve 73% accuracy! Looking at the errors, this is most likely caused by the lack of clarity when recording notes D4 and E4 (I may have switched the two around / couldn't think of the note clearly so it might've sounded like the other).



## Hardware Used
1. Muse2
