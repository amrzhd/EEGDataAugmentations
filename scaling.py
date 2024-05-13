import numpy as np

def scaling(data, std_values=(0.03, 0.07, 0.1), mean=1):
    """
    Apply scaling augmentation to EEG data.

    Parameters:
        data (ndarray): EEG data with shape (samples, channels, time_steps).
        std_values (tuple): Standard deviation values for Gaussian distribution.
        mean (float): Mean value for Gaussian distribution.

    Returns:
        augmented_data (ndarray): Augmented EEG data with shape (samples, channels, time_steps).
    """
    augmented_data = []
    for std in std_values:
        # Generating random scalars from Gaussian distribution
        scalars = np.random.normal(mean, std, size=data.shape[:-1])
        scalars = scalars[..., np.newaxis]  # Add a new axis for broadcasting
        # Multiplying with random scalars
        scaled_data = data * scalars
        augmented_data.append(scaled_data)
    augmented_data = np.concatenate(augmented_data, axis=0)
    return augmented_data

if __name__ == '__main__':
    # Example usage:
    trials = 2592
    channs = 22
    time_points = 257
    input_shape = (trials, channs, time_points)
    example_data = np.random.rand(*input_shape)
    augmented_data = scaling(example_data)
    print("Augmented Dataset's shape:", augmented_data.shape)