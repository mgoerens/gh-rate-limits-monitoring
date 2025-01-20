import argparse

import matplotlib.pyplot as plt
import numpy as np


def extract_points(file, compensate_remaining_offset = False):
    xarray = []
    yarray_limit = []
    yarray_remaining = []

    with open(file, "r") as f:
        lines = f.readlines()

    initial_timestamp = None
    remaining_offset = None

    for line in lines:
        timestamp, limit, remaining = line.split(" ")

        if not initial_timestamp:
            initial_timestamp = float(timestamp)

        if not remaining_offset:
            remaining_offset = float(5000 - float(remaining))

        # import pdb; pdb.set_trace()

        xarray.append(float(timestamp)-initial_timestamp)
        yarray_limit.append(float(limit))
        if compensate_remaining_offset:
            yarray_remaining.append(float(remaining) + remaining_offset)
        else:
            yarray_remaining.append(float(remaining))

    return xarray, yarray_limit, yarray_remaining


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        dest="input_file",
        type=str,
        required=True,
        help="File containing rate limit monitoring",
        action="append",
    )
    parser.add_argument(
        "-c",
        "--compensate_offset",
        dest="compensate_remaining_offset",
        help="Set to true if some API calls are already consumed at the start of the capture to compensate",
        action="store_true",
    )

    args = parser.parse_args()

    for file in args.input_file:
        xarray, yarray_limit, yarray_remaining = extract_points(file, args.compensate_remaining_offset)

        xpoints = np.array(xarray)
        ypoints_limit = np.array(yarray_limit)
        ypoints_remaining = np.array(yarray_remaining)

        plt.plot(xpoints, ypoints_remaining)
    plt.show()


if __name__ == "__main__":
    main()
