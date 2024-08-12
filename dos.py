import matplotlib.pyplot as plt

# Load DOS data from Quantum ESPRESSO output file
def load_dos(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            if not line.startswith('#') and line.strip() != '':
                data.append([float(x) for x in line.split()])
        return data

# Plot the density of states (DOS)
def plot_dos(dos_data):
    energies = [x[0] for x in dos_data]
    total_dos = [x[1] for x in dos_data]
    partial_dos = [x[2:] for x in dos_data]
    num_orbitals = len(partial_dos[0])

    fig, ax = plt.subplots()
    ax.plot(energies, total_dos, label='Total DOS')
    for i in range(num_orbitals):
        orbital_dos = [x[i] for x in partial_dos]
        ax.plot(energies, orbital_dos, label=f'Orbital {i+1} DOS')
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('DOS')
    ax.legend()
    plt.show()

# Specify the filename of the Quantum ESPRESSO output file
filename = 'YCO.dat'

# Load and plot the DOS data
dos_data = load_dos(filename)
plot_dos(dos_data)

