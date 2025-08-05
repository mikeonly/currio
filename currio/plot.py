import matplotlib.pyplot as plt
import seaborn as sns

from currio.utils import parse_time_range

def plot(obj, neuron, section_name, ax=None, 
         cmap="viridis", backend="inline", t=None,
         **kwargs):
    """Plot voltage or current traces from a neuron section.
    
    Args:
        obj (str): What to plot - "voltage", "v", "currents", or "interp_v"
        neuron (Neuron): Neuron object containing the data
        section_name (str): Name of the section to plot
        ax (matplotlib.axes.Axes, optional): Axes to plot on. If None, creates new figure
        cmap (str, optional): Color map to use. Defaults to "viridis"
        backend (str, optional): Display mode - "inline" or "window"
        t (str, optional): Time range specification:
            - "10..20s"    (10 to 20 seconds)
            - "-1..500ms"  (−1 to 500 milliseconds)
            - "0..1s"      (0 to 1 second)
            - "100..200"   (100 to 200 milliseconds, default unit)
            If None, plots full time range
    
    Returns:
        matplotlib.axes.Axes: The axes containing the plot
        
    Examples:
        # Plot voltage from 10ms to 20ms
        plot("voltage", neuron, "soma[0]", t="10..20ms")
        
        # Plot currents from 0.5s to 1s
        plot("currents", neuron, "dendrite[0]", t="0.5..1s")
        
        # Plot full range in window
        plot("voltage", neuron, "soma[0]", backend="window")
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
    t_slice = parse_time_range(t, times)
    times = times[t_slice]
    
    if obj == "currents":
        values = neuron.record[section_name][obj]
        values = values[:, t_slice] * 1e6  # convert mA → nA
        ylabel = "current, nA"
    elif obj == "voltage" or obj == "v":
        values = neuron.record[section_name]["v"][:, t_slice]
        obj = "voltage"
        ylabel = "voltage, mV"
    elif obj == "interp_v":
        values = neuron.record[section_name]["interp_v"][:, t_slice]
        obj = "interpolated voltage"
        ylabel = "voltage, mV"
    elif obj.startswith("i"):
        values = neuron.record[section_name][obj][:, t_slice]
        ylabel = fr"current, {obj} (mA/cm$^2$)"
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