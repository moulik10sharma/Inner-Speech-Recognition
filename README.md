# Inner-Speech-Recognition

## Abstract

This repository contains a novel dataset for inner speech recognition, collected using surface electroencephalography (EEG). The dataset comprises over 9 hours of continuous EEG recordings from ten participants who performed mental tasks under three conditions: inner speech, pronounced speech, and visualized actions.

## Summary

The dataset is a valuable resource for researchers interested in developing new techniques for inner speech recognition and understanding the brain mechanisms underlying inner speech. It includes 5640 trials and is the first dataset with native Spanish speakers and a high-density acquisition system (128+8 channels).

## Methods

- **Participants:** The study involved ten participants.
- **Procedures:** EEG recordings were conducted using visual cues and speech conditions.
- **Data Acquisition:** EEG, EOG, and EMG data were recorded using a BioSemi ActiveTwo system.
- **Interaction Conditions:** The dataset includes inner speech, pronounced speech, and visualized conditions.
- **Data Processing:** Data was processed using Python and the MNE library.

## Data Records

The dataset is organized into ten subfolders, one for each participant's session. It includes raw data files, processed EEG data, external electrodes data, events data, and a report file.

## Limitations & Final Remarks

While the dataset is a significant contribution to the field, limitations include potential variations in participants' mental activity interpretation and the unclear distinction between imagined and inner speech processes.

## Usage Notes

The processing script was developed in Python 3.7, using the MNE-python package v0.21.051, NumPy v1.19.267, Scipy v.1.5.268, Pandas v1.1.269, and Pickle v4.070. The main script, `InnerSpeech_processing.py`, contains all the processing steps and can be modified for different results.

## Tutorial

The tutorial provided in the repository guides users on loading and running the Inner Speech Database, including installing dependencies, importing libraries, loading data, processing, and creating classifier groups.

## Credits

- **Presentation Template:** Slidesgo
- **Icons:** Flaticon
- **Infographics & Images:** Freepik

## License

The dataset is available under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

## Citation

If you use this dataset in your research, please cite the following publication:

Nieto, N., Peterson, V., Ruﬁner, H., Kamienkowski, J., & Spies, R. (2022). Thinking out loud, an open-access EEG-based BCI dataset for inner speech recognition. *Scientific Data*.

## Contact

For any questions or feedback, please contact the authors at [211210039@nitdelhi.ac.in](mailto:211210039@nitdelhi.ac.in) or [jaiswalshubham502@gmail.com](mailto:jaiswalshubham502@gmail.com).


---

This repository is maintained by [Moulik Sharma](https://github.com/moulik10sharma) and [Shubham Anand Jaiswal](https://github.com/Shubham-Jaiswal-31).
