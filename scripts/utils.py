import plotly.graph_objects as go
from IPython.display import Audio


# Função para plotar o sinal utilizando Plotly
def plot_signal(
    time_vector,
    *audio_data_list,
    t_inicial=None,
    t_final=None,
    labels=None,
    title=None,
    subtitle=None,
    x_title=None,
    y_title=None,
    show_legend=True,
):
    """
    Plot a line chart for one or more audio signals using Plotly.
        time_vector (iterable): An array or list of time points for the x-axis.
        *audio_data_list (iterable): One or more arrays/lists of amplitude values corresponding to the time points.
        t_inicial (float, optional): The starting time for the x-axis range. Defaults to the first element in time_vector.
        t_final (float, optional): The ending time for the x-axis range. Defaults to the last element in time_vector.
        labels (list of str, optional): A list of labels for the audio signals. If not provided or if there are fewer labels
                                        than signals, default labels ("Sinal 1", "Sinal 2", etc.) will be used.
        title (str, optional): The title of the plot.
        subtitle (str, optional): The subtitle of the plot.
        x_title (str, optional): The label for the x-axis.
        y_title (str, optional): The label for the y-axis.
        show_legend (bool, optional): Whether to display the legend. Defaults to True.
        The function displays the generated plot automatically using Plotly's display mechanism.
    """
    fig = go.Figure()
    for i, audio_data in enumerate(audio_data_list):
        if labels is not None and i < len(labels):
            label = labels[i]
        else:
            # Default label if none provided
            label = f"Sinal {i + 1}"
        fig.add_trace(go.Scatter(x=time_vector, y=audio_data, mode="lines", name=label))

    if t_inicial is None:
        t_inicial = time_vector[0]

    if t_final is None:
        t_final = time_vector[-1]

    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        showlegend=show_legend,
        hovermode="x",
        template="plotly_white",
        xaxis=dict(
            showline=True,
            showgrid=True,
            zeroline=True,
            linewidth=2,
            linecolor="black",
            gridcolor="lightgray",
            range=[t_inicial, t_final]
        ),
        yaxis=dict(
            showline=True,
            showgrid=True,
            zeroline=True,
            linewidth=2,
            linecolor="black",
            gridcolor="lightgray",
        ),
    )

    # Add subtitle as an annotation if provided
    if subtitle:
        fig.add_annotation(
            x=0.5,
            y=0.95,
            xref="paper",
            yref="paper",
            text=subtitle,
            showarrow=False,
            font=dict(size=12),
            xanchor="center",
        )

    fig.show()


# Função para tocar a nota com um determinado volume
def play_sound(audio_data, sample_rate, volume=0.5, autoplay=True):
    """
    Plays a sound by scaling its amplitude and initializing an Audio object for playback.
    Parameters:
        audio_data (array-like): The input sound data to be played.
        sample_rate (int): The sample rate for the audio playback.
        volume (float, optional): The factor by which to scale the sound's amplitude. Defaults to 0.5.
        autoplay (bool, optional): Whether to start playback automatically. Defaults to True.
    Returns:
        Audio: An Audio object instantiated with the scaled sound, configured to autoplay and normalized.
    """

    # Escala a nota pelo volume
    scaled_note = audio_data * volume
    return Audio(scaled_note, rate=sample_rate, autoplay=autoplay, normalize=True)
