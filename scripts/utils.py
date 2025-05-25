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
    Plota um gráfico de linha para um ou mais sinais de áudio usando Plotly.
        time_vector (iterável): Um array ou lista de pontos de tempo para o eixo x.
        *audio_data_list (iterável): Um ou mais arrays/listas de valores de amplitude correspondentes aos pontos de tempo.
        t_inicial (float, opcional): O tempo inicial para o intervalo do eixo x. O padrão é o primeiro elemento em time_vector.
        t_final (float, opcional): O tempo final para o intervalo do eixo x. O padrão é o último elemento em time_vector.
        labels (list de str, opcional): Uma lista de rótulos para os sinais de áudio. Se não fornecido ou se houver menos rótulos
                                        do que sinais, rótulos padrão ("Sinal 1", "Sinal 2", etc.) serão usados.
        title (str, opcional): O título do gráfico.
        subtitle (str, opcional): O subtítulo do gráfico.
        x_title (str, opcional): O rótulo para o eixo x.
        y_title (str, opcional): O rótulo para o eixo y.
        show_legend (bool, opcional): Se deve exibir a legenda. O padrão é True.
        A função exibe o gráfico gerado automaticamente usando o mecanismo de exibição do Plotly.
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
            range=[t_inicial, t_final],
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
    Reproduz um som escalonando sua amplitude e inicializando um objeto Audio para reprodução.
    Parâmetros:
        audio_data (array-like): Os dados de som de entrada a serem reproduzidos.
        sample_rate (int): A taxa de amostragem para a reprodução do áudio.
        volume (float, opcional): O fator pelo qual a amplitude do som será escalonada. O padrão é 0.5.
        autoplay (bool, opcional): Se a reprodução deve iniciar automaticamente. O padrão é True.
    Retorna:
        Audio: Um objeto Audio instanciado com o som escalonado, configurado para reprodução automática e normalizado.
    """

    # Escala a nota pelo volume
    scaled_note = audio_data * volume
    return Audio(scaled_note, rate=sample_rate, autoplay=autoplay, normalize=True)
