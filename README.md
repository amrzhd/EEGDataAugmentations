# EEG Data Augmentation Methods

Data augmentation plays a crucial role in enhancing the performance and robustness of machine learning models, particularly in domains with limited data availability like EEG (Electroencephalography) signal processing. This repository provides implementations of various data augmentation methods tailored for EEG data.

## Why Data Augmentation?

Data augmentation is essential for enriching the training dataset by creating diverse variations of the existing data. In EEG analysis, this is particularly important due to the limited availability of labeled data and the high variability of EEG signals across individuals and conditions. By applying augmentation techniques, we can effectively enhance the generalization capability of EEG classifiers and improve their performance on unseen data.

## Methods

- **Jittering**: Jittering involves introducing small random shifts in the temporal domain of EEG signals. This helps in simulating slight variations in the timing of neural events, making the model more robust to temporal variations in the data.

- **Scaling**: Scaling alters the amplitude of EEG signals by multiplying them with a scaling factor. This mimics changes in signal intensity, which can occur due to differences in electrode placement, contact quality, or individual differences in neural activity strength.

- **Head-to-Tail**: Head-to-Tail augmentation involves concatenating EEG segments in both forward and reverse directions. This technique helps in simulating variations in the spatial distribution of neural activity, which can arise from changes in electrode montages or head orientations.

## Files

- **Module Folder**: This folder contains the implementation of all augmentation methods as Python modules. Each module provides functions to apply the corresponding augmentation technique to EEG data.

- **Colab Notebook**: The provided Colab notebook demonstrates the application of each augmentation method using a sample EEG dataset. It includes code snippets and visualizations to illustrate the effects of augmentation on EEG signals.

## Papers Using These Methods

- Jittering and Scaling:
  [E. Arı and E. Taçgın, "NF-EEG: A generalized CNN model for multi-class EEG motor imagery classification without signal preprocessing for brain-computer interfaces," Biomedical Signal Processing and Control, vol. 92, p. 106081, 2024.](https://doi.org/10.1016/j.bspc.2024.106081)

- Head-to-Tail:
  [R. Wu, J. Jin, I. Daly, X. Wang, and A. Cichocki, "Classification of motor imagery based on multi-scale feature extraction and the channel-temporal attention module," IEEE Transactions on Neural Systems and Rehabilitation Engineering, 2023.](http://dx.doi.org/10.1109/TNSRE.2023.3294815)

---

Feel free to explore the provided modules and notebook to incorporate these augmentation methods into your EEG analysis pipeline! If you find this repository useful, don't forget to star it and cite the relevant papers in your work. For any questions or suggestions, please open an issue or reach out via email.
