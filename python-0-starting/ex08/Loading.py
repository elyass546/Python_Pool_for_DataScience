import sys
import time


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
        Custom tqdm-like progress bar function using yield.
        :param lst: The range object to iterate over.
    """
    total = len(lst)  # Get the total number of items in the range
    bar_length = 50  # Length of the progress bar

    for i, item in enumerate(lst):
        # Calculate percentage completion
        percent_complete = (i + 1) / total * 100

        # Calculate the number of '=' symbols in the progress bar
        filled_length = int(bar_length * (i + 1) / total)

        # Create the progress bar string
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)

        # Display the progress bar with percentage and item count
        sys.stdout.write(f'\r{percent_complete:3.0f}\
                    %|[{bar}]| {i + 1}/{total}')
        sys.stdout.flush()

        # Yield the current item
        # (this mimics the behavior of tqdm with yield)
        yield item

    sys.stdout.write('\n')  # Add a newline after completion


# Example usage:
if __name__ == "__main__":
    for item in ft_tqdm(range(33)):
        time.sleep(0.09)  # Simulate some work
