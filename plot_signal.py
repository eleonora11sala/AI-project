import matplotlib.pyplot as plt
def plot_signal(t, signal, color, title):
    fig, axs = plt.subplots()
    axs.plot(t, signal, color=color)
    axs.set_title(title)
    axs.set_xlabel("Time [s]")
    axs.set_ylabel("Amplitude")
    plt.show()