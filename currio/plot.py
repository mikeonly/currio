import matplotlib.pyplot as plt
import seaborn as sns


def plot(obj, neuron, section_name, ax=None, 
         cmap="viridis", backend="inline",
         **kwargs):
    """Plot voltage or current traces from a neuron section.
    
    Args:
        obj (str): What to plot - "voltage", "v", "currents", or "interp_v"
        neuron (Neuron): Neuron object containing the data
        section_name (str): Name of the section to plot
        ax (matplotlib.axes.Axes, optional): Axes to plot on. If None, creates new figure
        cmap (str, optional): Color map to use. Defaults to "viridis". 
            Possible values: "rocket", "mako", "crest", "magma", "YlOrBr", etc.
        backend (str, optional): How to display the plot:
            - "inline": Plot in current notebook/console (default)
            - "window": Open in new window (closes when window is closed)
    
    Returns:
        matplotlib.axes.Axes: The axes containing the plot
        
    Usage examples:
    - plot("voltage", neuron, section_name="apical_dendrite[1]")
    - plot("currents", neuron, "soma[0]", backend="window")
    """
    if backend == "window":
        # Use TkAgg backend for window display
        import matplotlib
        matplotlib.use('TkAgg')
        
    with sns.axes_style("darkgrid"):
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 4))
        else:
            fig = ax.figure
    
    times = neuron.record["t"]
    if obj == "currents":
        values = neuron.record[section_name][obj]
        values = values * 1e6  # convert mA → nA
        ylabel = "current, nA"
    elif obj == "voltage" or obj == "v":
        values = neuron.record[section_name]["v"]  # to conform to the record key name
        obj = "voltage"
        ylabel = "voltage, mV"
    elif obj == "interp_v":
        values = neuron.record[section_name]["interp_v"]
        obj = "interpolated voltage"
        ylabel = "voltage, mV"
    else:
        raise ValueError(f"Invalid object type: {obj}")
    
    # Get number of segments
    n_segments = values.shape[0]

    # Create color palette that varies sequentially
    colors = sns.color_palette(cmap, n_segments)

    # Plot each segment with different color
    for j in range(n_segments):        
        sns.lineplot(x=times, 
                    y=values[j, :],
                    color=colors[j],
                    ax=ax)

    # Customize plot
    ax.set_xlabel('time, ms')
    ax.set_ylabel(ylabel)
    ax.set_title(f'{obj} along {section_name} segments vs. time')

    # Remove legend
    ax.legend([])

    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    if backend == "window":
        # Show the plot in a window
        plt.show(block=True)  # block=True ensures window stays open
        # Clean up after window is closed
        plt.close(fig)
    
    return ax