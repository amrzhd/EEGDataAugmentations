import numpy as np

def jittering(data, std_values=(0.03, 0.07, 0.1), mean=0):
    """
    Apply jittering augmentation to EEG data.

    Parameters:
        data (ndarray): EEG data with shape (samples, channels).
        std_values (tuple): Standard deviation values for Gaussian noise.
        mean (float): Mean value for Gaussian noise.

    Returns:
        augmented_data (ndarray): Augmented EEG data with shape (samples, channels).
    """
    augmented_data = []
    for std in std_values:
        # Generate Gaussian noise
        noise = np.random.normal(mean, std, size=data.shape)
        # Add noise to the original data
        augmented_data.append(data + noise)
    augmented_data = np.concatenate(augmented_data, axis=0)
    return augmented_data

if __name__ == '__main__':
    # Example usage:
    trials = 2592
    channs = 22
    time_points = 257
    input_shape = (trials, channs, time_points)
    example_data = np.random.rand(*input_shape)
    augmented_data = jittering(example_data)
    print("Augmented Dataset's shape:", augmented_data.shape)