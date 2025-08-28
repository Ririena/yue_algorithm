import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom, binom, poisson
from matplotlib.widgets import Slider, Button
import matplotlib.animation as animation

# Set up the figure and axes
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
plt.subplots_adjust(left=0.1, bottom=0.4, top=0.9)

# Initial parameters
init_p = 0.3
init_n = 20
init_lambda = 6

# Create slider axes
ax_slider_p = plt.axes([0.25, 0.30, 0.65, 0.03])
ax_slider_n = plt.axes([0.25, 0.25, 0.65, 0.03])
ax_slider_lambda = plt.axes([0.25, 0.20, 0.65, 0.03])
ax_button = plt.axes([0.25, 0.10, 0.2, 0.04])
ax_reset_zoom = plt.axes([0.50, 0.10, 0.2, 0.04])
ax_zoom_all = plt.axes([0.75, 0.10, 0.2, 0.04])

# Create sliders and buttons
slider_p = Slider(ax_slider_p, 'Probability (p)', 0.05, 0.95, valinit=init_p, valstep=0.05)
slider_n = Slider(ax_slider_n, 'Trials (n)', 5, 50, valinit=init_n, valstep=1)
slider_lambda = Slider(ax_slider_lambda, 'Lambda (λ)', 1, 20, valinit=init_lambda, valstep=1)
animate_button = Button(ax_button, 'Animate Parameters')
reset_zoom_button = Button(ax_reset_zoom, 'Reset Zoom')
zoom_all_button = Button(ax_zoom_all, 'Zoom to Data')

# Store original limits for zoom reset
original_limits = {}

# Initialize plot data
x_geom = np.arange(1, 51)
x_binom = np.arange(0, 51)
x_poisson = np.arange(0, 51)
x_comparison = np.arange(0, 51)

# Initial plots
geom_bars = ax1.bar(x_geom, geom.pmf(x_geom, init_p), alpha=0.7, color='skyblue', edgecolor='navy', linewidth=0.5)
binom_bars = ax2.bar(x_binom[:init_n + 1], binom.pmf(x_binom[:init_n + 1], init_n, init_p),
                     alpha=0.7, color='lightgreen', edgecolor='darkgreen', linewidth=0.5)
poisson_bars = ax3.bar(x_poisson, poisson.pmf(x_poisson, init_lambda),
                       alpha=0.7, color='lightcoral', edgecolor='darkred', linewidth=0.5)

# Comparison plot
comparison_line1, = ax4.plot(x_comparison, np.zeros_like(x_comparison), 'o-',
                             label='Geometric', color='blue', markersize=4, linewidth=2)
comparison_line2, = ax4.plot(x_comparison, np.zeros_like(x_comparison), 's-',
                             label='Binomial', color='green', markersize=4, linewidth=2)
comparison_line3, = ax4.plot(x_comparison, np.zeros_like(x_comparison), '^-',
                             label='Poisson', color='red', markersize=4, linewidth=2)


# Set up plot properties
def setup_plot(ax, title, xlabel, ylabel='Probability'):
    ax.set_title(title, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1)
    # Store original limits
    original_limits[ax] = (ax.get_xlim(), ax.get_ylim())


setup_plot(ax1, 'Geometric Distribution', 'Trials until first success')
setup_plot(ax2, 'Binomial Distribution', 'Number of successes')
setup_plot(ax3, 'Poisson Distribution', 'Number of events')
setup_plot(ax4, 'Distribution Comparison', 'Number of events/trials')
ax4.legend()


# Simple zoom functionality using button clicks
def zoom_in_x(event):
    """Zoom in horizontally on all plots"""
    for ax in [ax1, ax2, ax3, ax4]:
        xlim = ax.get_xlim()
        x_range = xlim[1] - xlim[0]
        new_xlim = (xlim[0] + x_range * 0.1, xlim[1] - x_range * 0.1)
        ax.set_xlim(new_xlim)
    fig.canvas.draw_idle()


def zoom_out_x(event):
    """Zoom out horizontally on all plots"""
    for ax in [ax1, ax2, ax3, ax4]:
        xlim = ax.get_xlim()
        x_range = xlim[1] - xlim[0]
        new_xlim = (xlim[0] - x_range * 0.5, xlim[1] + x_range * 0.5)
        ax.set_xlim(max(0, new_xlim[0]), new_xlim[1])
    fig.canvas.draw_idle()


def zoom_in_y(event):
    """Zoom in vertically on all plots"""
    for ax in [ax1, ax2, ax3, ax4]:
        ylim = ax.get_ylim()
        y_range = ylim[1] - ylim[0]
        new_ylim = (ylim[0] + y_range * 0.1, ylim[1] - y_range * 0.1)
        ax.set_ylim(new_ylim)
    fig.canvas.draw_idle()


def zoom_out_y(event):
    """Zoom out vertically on all plots"""
    for ax in [ax1, ax2, ax3, ax4]:
        ylim = ax.get_ylim()
        y_range = ylim[1] - ylim[0]
        new_ylim = (max(0, ylim[0] - y_range * 0.5), ylim[1] + y_range * 0.5)
        ax.set_ylim(new_ylim)
    fig.canvas.draw_idle()


# Create zoom buttons
ax_zoom_in_x = plt.axes([0.05, 0.30, 0.08, 0.03])
ax_zoom_out_x = plt.axes([0.05, 0.25, 0.08, 0.03])
ax_zoom_in_y = plt.axes([0.05, 0.20, 0.08, 0.03])
ax_zoom_out_y = plt.axes([0.05, 0.15, 0.08, 0.03])

btn_zoom_in_x = Button(ax_zoom_in_x, 'Zoom In X')
btn_zoom_out_x = Button(ax_zoom_out_x, 'Zoom Out X')
btn_zoom_in_y = Button(ax_zoom_in_y, 'Zoom In Y')
btn_zoom_out_y = Button(ax_zoom_out_y, 'Zoom Out Y')

btn_zoom_in_x.on_clicked(zoom_in_x)
btn_zoom_out_x.on_clicked(zoom_out_x)
btn_zoom_in_y.on_clicked(zoom_in_y)
btn_zoom_out_y.on_clicked(zoom_out_y)


# Zoom reset function
def reset_zoom(event):
    """Reset all plots to original zoom levels"""
    for ax, (xlim, ylim) in original_limits.items():
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    fig.canvas.draw_idle()


# Zoom to data function
def zoom_to_data(event):
    """Zoom each plot to show only the relevant data range"""
    p = slider_p.val
    n = int(slider_n.val)
    lambda_val = slider_lambda.val

    # Geometric
    geom_data = geom.pmf(x_geom, p)
    valid_indices = geom_data > 0.001
    if np.any(valid_indices):
        ax1.set_xlim(0, min(50, np.max(x_geom[valid_indices]) + 2))
        ax1.set_ylim(0, min(1, np.max(geom_data) * 1.2))

    # Binomial
    binom_data = binom.pmf(x_binom[:n + 1], n, p)
    ax2.set_xlim(-0.5, n + 0.5)
    ax2.set_ylim(0, min(1, np.max(binom_data) * 1.2))

    # Poisson
    poisson_data = poisson.pmf(x_poisson, lambda_val)
    valid_indices = poisson_data > 0.001
    if np.any(valid_indices):
        ax3.set_xlim(0, min(50, np.max(x_poisson[valid_indices]) + 2))
        ax3.set_ylim(0, min(1, np.max(poisson_data) * 1.2))

    # Comparison
    max_val = max(np.max(geom_data), np.max(binom_data), np.max(poisson_data))
    ax4.set_ylim(0, min(1, max_val * 1.2))
    ax4.set_xlim(0, max(n, lambda_val * 2) + 2)

    fig.canvas.draw_idle()


# Connect zoom buttons
reset_zoom_button.on_clicked(reset_zoom)
zoom_all_button.on_clicked(zoom_to_data)


# Update function
def update(val=None):
    p = slider_p.val
    n = int(slider_n.val)
    lambda_val = slider_lambda.val

    # Update geometric distribution
    geom_pmf = geom.pmf(x_geom, p)
    for i, bar in enumerate(geom_bars):
        if i < len(geom_pmf):
            bar.set_height(geom_pmf[i])
        else:
            bar.set_height(0)

    # Update binomial distribution
    binom_pmf = binom.pmf(x_binom[:n + 1], n, p)
    for i, bar in enumerate(binom_bars):
        if i < len(binom_pmf):
            bar.set_height(binom_pmf[i])
            bar.set_x(i)
        else:
            bar.set_height(0)

    # Update Poisson distribution
    poisson_pmf = poisson.pmf(x_poisson, lambda_val)
    for i, bar in enumerate(poisson_bars):
        if i < len(poisson_pmf):
            bar.set_height(poisson_pmf[i])
        else:
            bar.set_height(0)

    # Update comparison plot
    geom_comp = np.zeros_like(x_comparison, dtype=float)
    geom_pmf_comp = geom.pmf(x_comparison[1:], p)
    geom_comp[1:len(geom_pmf_comp) + 1] = geom_pmf_comp

    binom_comp = binom.pmf(x_comparison, n, p)
    poisson_comp = poisson.pmf(x_comparison, lambda_val)

    comparison_line1.set_ydata(geom_comp)
    comparison_line2.set_ydata(binom_comp)
    comparison_line3.set_ydata(poisson_comp)

    # Update titles with current values
    ax1.set_title(f'Geometric Distribution (p={p:.2f})', fontweight='bold')
    ax2.set_title(f'Binomial Distribution (n={n}, p={p:.2f})', fontweight='bold')
    ax3.set_title(f'Poisson Distribution (λ={lambda_val:.1f})', fontweight='bold')
    ax4.set_title(f'Comparison (p={p:.2f}, n={n}, λ={lambda_val:.1f})', fontweight='bold')

    fig.canvas.draw_idle()


# Connect sliders to update function (FIXED: use on_changed for all sliders)
slider_p.on_changed(update)
slider_n.on_changed(update)
slider_lambda.on_changed(update)


# Animation function
def animate_parameters(event):
    # Create animation that cycles through different parameter values
    p_values = np.linspace(0.1, 0.9, 20)
    n_values = np.linspace(10, 40, 20).astype(int)
    lambda_values = np.linspace(3, 15, 20)

    def animate_frame(i):
        slider_p.set_val(p_values[i % len(p_values)])
        slider_n.set_val(n_values[i % len(n_values)])
        slider_lambda.set_val(lambda_values[i % len(lambda_values)])
        return []

    ani = animation.FuncAnimation(fig, animate_frame, frames=50,
                                  interval=300, blit=False, repeat=True)
    plt.show()


# Connect button to animation
animate_button.on_clicked(animate_parameters)

# Initial update
update()

# Add explanation text with zoom instructions
explanation_text = """
🎮 INTERACTIVE CONTROLS:

SLIDERS:
• Probability (p): Success probability (0.05-0.95)
• Trials (n): Number of binomial trials (5-50)
• Lambda (λ): Poisson rate parameter (1-20)

ZOOM BUTTONS:
← Left side buttons control zoom:
• Zoom In/Out X: Adjust horizontal scale
• Zoom In/Out Y: Adjust vertical scale
• Reset Zoom: Return to original view
• Zoom to Data: Auto-zoom to relevant data

ANIMATION:
• Animate Parameters: Auto-cycle through values

📊 DISTRIBUTION TIPS:
• Use zoom to see distribution details
• Watch how shapes change with parameters
• Compare distributions at different scales
"""

plt.figtext(0.02, 0.02, explanation_text, fontsize=8,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.9))


# Add keyboard shortcuts for zoom
def on_key_press(event):
    if event.key == 'x':
        zoom_in_x(event)
    elif event.key == 'X':
        zoom_out_x(event)
    elif event.key == 'y':
        zoom_in_y(event)
    elif event.key == 'Y':
        zoom_out_y(event)
    elif event.key == 'r':
        reset_zoom(event)
    elif event.key == 'z':
        zoom_to_data(event)


fig.canvas.mpl_connect('key_press_event', on_key_press)

plt.show()

# Print keyboard shortcuts
print("Keyboard Shortcuts:")
print("x / X - Zoom In/Out X-axis")
print("y / Y - Zoom In/Out Y-axis")
print("r - Reset Zoom")
print("z - Zoom to Data")