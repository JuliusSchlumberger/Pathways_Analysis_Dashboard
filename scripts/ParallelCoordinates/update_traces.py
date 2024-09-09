from scripts.ParallelCoordinates.generate_ticks import generate_ticks

# Helper function to determine the tick step
def calculate_tick_step(d, roh_dict, range_upper):
    """Calculate the appropriate step for tick generation."""
    label = d['label'].replace('<br>', ' ')
    label = label.rstrip()
    # print(label)
    # print(label)
    if label in roh_dict.keys():
        return 1
    elif range_upper > 1000:
        return int(range_upper / 1000)
    elif range_upper <= 100:
        return 1
    # elif range_upper <= 1000:
    #     return 25
    else:
        return 10


# Helper function to calculate the number of ticks
def calculate_num_ticks(d, roh_dict, range_upper):
    """Calculate the number of ticks based on the range and label."""
    label = d['label'].replace('<br>', ' ')
    label = label.rstrip()

    if label in roh_dict.keys():
        return range_upper + 1
    elif range_upper <= 1000:
        return int(range_upper / 10) + 1
    # elif range_upper <= 1000:
    #     return int(range_upper / 25) + 1
    else:
        return int(range_upper / 100) + 1


# Main function to update traces
def update_traces_with_ticks(fig, roh_dict, range_dict):
    """Update trace dimensions with tick values and tick text."""
    fig.update_traces(
        dimensions=[
            {
                **d,
                # Calculate tick values
                "tickvals": generate_ticks(
                    d['range'][0],
                    d['range'][1],
                    calculate_num_ticks(d, roh_dict, d['range'][1]),
                    calculate_tick_step(d, roh_dict, d['range'][1])
                )[0],
                # Calculate tick text
                "ticktext": generate_ticks(
                    0 if d['label'].replace('<br>', '') in roh_dict else d['range'][0],
                    range_dict[d['label'].replace('<br>', '')][1] if d['label'].replace('<br>', '') in roh_dict else
                    d['range'][1],
                    calculate_num_ticks(d, roh_dict, d['range'][1]),
                    calculate_tick_step(d, roh_dict, d['range'][1])
                )[1]
            }
            for d in fig.to_dict()["data"][0]["dimensions"]
        ]
    )