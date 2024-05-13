import numpy as np

def head_to_tail(data, length=50):
    """
    Apply head-to-tail augmentation to EEG data.

    Parameters:
        data (ndarray): EEG data with shape (trials, channels, time_steps).
        length (int): Length for head-to-tail augmentation.

    Returns:
        augmented_data (ndarray): Augmented EEG data with the specified length.
    """
    augmented_data = []
    for trial in data:
        augmented_trial = np.zeros_like(trial)
        for t in range(trial.shape[-1]):  # Loop over the time axis
            augmented_trial[..., t] = np.roll(trial[..., t], -t * length)
        augmented_data.append(augmented_trial)
    augmented_data = np.array(augmented_data)
    return np.concatenate([data, augmented_data], axis=0)

if __name__ == '__main__':
    # Example usage:
    trials = 2592
    channs = 22
    time_points = 257
    input_shape = (trials, channs, time_points)
    example_data = np.random.rand(*input_shape)
    augmented_data = head_to_tail(example_data)
    print("Augmented Dataset's shape:", augmented_data.shape)