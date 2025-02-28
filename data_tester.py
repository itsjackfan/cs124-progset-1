import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import io

data_string = """
0.23776580814631765 16
0.17827532764839749 16
0.13055272898952797 16
0.20336951985393836 16
0.2172557738416072 16
0.1546426771236028 16
0.17148084443780998 16
0.15094951397793588 16
0.22997190232786113 16
0.20579628609445855 16
0.2191669877360488 16
0.1493059276532832 16
0.2379140316755417 16
0.22816672103018953 16
0.1714021281853607 16
0.15217743698839092 16
0.2085199828809976 16
0.16842440185240326 16
0.16190699351314985 16
0.25395669099358875 16
0.1156191044448337 32
0.09576792476799978 32
0.23888457058833135 32
0.13030902442392445 32
0.11856986367136424 32
0.12620869438179472 32
0.10733789849416897 32
0.09359321913253427 32
0.13779972099128612 32
0.1066093602619711 32
0.10688110430341591 32
0.13220076453260265 32
0.10461656679260878 32
0.10810231285427108 32
0.1453270072167765 32
0.13280139863666252 32
0.11001846346505861 32
0.11004186464704568 32
0.15720062073706031 32
0.14899470426704986 32
0.06814190689381994 64
0.0831516524559105 64
0.054808912106703134 64
0.05143039527558935 64
0.07467504143390225 64
0.07240310435923247 64
0.1193613902437648 64
0.06341606312520609 64
0.08018665076639442 64
0.06451798673026043 64
0.07242183666891266 64
0.07079727877641051 64
0.08190332088439334 64
0.07198592798020143 64
0.08078556118983282 64
0.0516304158463744 64
0.05389106904358831 64
0.05325740001305135 64
0.08331257309328499 64
0.06828140775933189 64
0.042445073394629995 128
0.03582776980141589 128
0.04052774829979133 128
0.05287183145766783 128
0.05153908300325816 128
0.046206406515411524 128
0.03724796729942581 128
0.043885041779896494 128
0.04300199584205455 128
0.04922194581215067 128
0.040938516704596584 128
0.039630492622020896 128
0.03466039209859151 128
0.03887227738753629 128
0.04332839265102284 128
0.05130742167185354 128
0.036911362827178884 128
0.041355366628641255 128
0.03805050108606589 128
0.0434370479357411 128
0.018794340969467305 256
0.03166956000429488 256
0.03008606816043702 256
0.025526706369069396 256
0.019411016969399286 256
0.023213211342036466 256
0.026009706770548258 256
0.02221101133501746 256
0.020851972352994186 256
0.023723995088721472 256
0.023532903306647812 256
0.02549220876123537 256
0.016705555413613404 256
0.02348100211147064 256
0.02209460185538248 256
0.019966900219573258 256
0.02601990573113211 256
0.021324085651679647 256
0.02793345091834598 256
0.020206450263703712 256
"""

def analyze_data_from_string(data_string):
    """Analyzes max edge weight data from a string, fits functions, and plots."""

    data_dict = {}
    try:
        with open("max_edge_weights.txt", "r") as f:
            data_io = f.readlines()
    except FileNotFoundError:
        print("Error: range_results.txt not found.")
        return

    for line in data_io:
        parts = line.strip().split()
        if len(parts) == 2:
            weight = float(parts[0])
            n_val = int(parts[1])
            if n_val not in data_dict:
                data_dict[n_val] = []
            data_dict[n_val].append(weight)

    mean_max_edge_weight = {n: np.mean(weights) for n, weights in data_dict.items()}
    N_values = np.array(list(mean_max_edge_weight.keys()))
    mean_weights = np.array(list(mean_max_edge_weight.values()))

    # Function definitions
    def linear(x, a, b):
        return a * x + b

    def logarithmic(x, a, b):
        return a * np.log(x) + b

    def exponential_decay(x, a, b):
        return a * np.exp(-b * x)

    def inverse_sqrt(x, a):
        return a / np.sqrt(x)

    # Curve fitting
    popt_linear, pcov_linear = curve_fit(linear, N_values, mean_weights)
    popt_log, pcov_log = curve_fit(logarithmic, N_values, mean_weights, p0=[0.1, 0.1])
    popt_exp, pcov_exp = curve_fit(exponential_decay, N_values, mean_weights, p0=[0.1, 0.001])
    popt_inv_sqrt, pcov_inv_sqrt = curve_fit(inverse_sqrt, N_values, mean_weights)

    # Evaluate fitted functions
    N_fit = np.linspace(min(N_values), max(N_values), 500) # Increased points for smoother curves
    fit_linear = linear(N_fit, *popt_linear)
    fit_log = logarithmic(N_fit, *popt_log)
    fit_exp = exponential_decay(N_fit, *popt_exp)
    fit_inv_sqrt = inverse_sqrt(N_fit, *popt_inv_sqrt)

    # Plotting
    plt.figure(figsize=(12, 8))
    plt.scatter(N_values, mean_weights, label='Mean Max Edge Weights', color='blue')
    plt.plot(N_fit, fit_linear, label=f'Linear Fit: y = {popt_linear[0]:.3e}*x + {popt_linear[1]:.3f}', color='red')
    plt.plot(N_fit, fit_log, label=f'Logarithmic Fit: y = {popt_log[0]:.3f}*ln(x) + {popt_log[1]:.3f}', color='green')
    plt.plot(N_fit, fit_exp, label=f'Exponential Decay Fit: y = {popt_exp[0]:.3f}*exp(-{popt_exp[1]:.3e}*x)', color='purple')
    plt.plot(N_fit, fit_inv_sqrt, label=f'Inverse Sqrt Fit: y = {popt_inv_sqrt[0]:.3f} / sqrt(x)', color='orange')

    plt.xlabel('N (Number of Vertices)')
    plt.ylabel('Mean Max Edge Weight')
    plt.title('Mean Max Edge Weights vs. N with Lines of Best Fit')
    plt.legend()
    plt.grid(True)
    plt.xscale('log') # Use log scale for x-axis to see trends better
    plt.yscale('log') # Use log scale for y-axis to see trends better
    plt.show()

    # Print function parameters (optional)
    print("Fitted Function Parameters:")
    print(f"Linear Fit: a = {popt_linear[0]:.3e}, b = {popt_linear[1]:.3f}")
    print(f"Logarithmic Fit: a = {popt_log[0]:.3f}, b = {popt_log[1]:.3f}")
    print(f"Exponential Decay Fit: a = {popt_exp[0]:.3f}, b = {popt_exp[1]:.3e}")
    print(f"Inverse Square Root Fit: a = {popt_inv_sqrt[0]:.3f}")


analyze_data_from_string(data_string)