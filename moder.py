import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 8))

# Function to create boxes
def create_box(ax, text, xy, boxstyle="round,pad=0.3", fc="violet", ec="black"):
    bbox_props = dict(boxstyle=boxstyle, facecolor=fc, edgecolor=ec)
    t = ax.text(xy[0], xy[1], text, ha="center", va="center", rotation=0,
                size=12, bbox=bbox_props, zorder=10)
    return t

# Creating boxes
user = create_box(ax, "User", [0.5, 0.9])
interaction = create_box(ax, "User Interaction", [0.5, 0.75])
frontend = create_box(ax, "Frontend", [0.5, 0.6])
backend = create_box(ax, "Backend", [0.5, 0.45])
crime_data = create_box(ax, "Crime Data Input", [0.2, 0.3])
feature_extraction = create_box(ax, "Feature Extraction", [0.4, 0.3])
crime_recognition = create_box(ax, "Crime Recognition Model", [0.6, 0.3])
insights_generator = create_box(ax, "Investigation Insights Generator", [0.8, 0.3])
results_display = create_box(ax, "Results Display", [0.5, 0.1])

# Drawing arrows
def draw_arrow(ax, start, end):
    ax.annotate("", xy=end, xycoords='data', xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", color="black", lw=2))

draw_arrow(ax, [0.5, 0.85], [0.5, 0.78])  # User to User Interaction
draw_arrow(ax, [0.5, 0.72], [0.5, 0.63])  # User Interaction to Frontend
draw_arrow(ax, [0.5, 0.57], [0.5, 0.48])  # Frontend to Backend

draw_arrow(ax, [0.35, 0.3], [0.45, 0.3])  # Crime Data Input to Feature Extraction
draw_arrow(ax, [0.55, 0.3], [0.65, 0.3])  # Feature Extraction to Crime Recognition Model
draw_arrow(ax, [0.75, 0.3], [0.85, 0.3])  # Crime Recognition Model to Insights Generator
draw_arrow(ax, [0.5, 0.41], [0.5, 0.36])  # Backend to Insights Generator
draw_arrow(ax, [0.5, 0.25], [0.5, 0.15])  # Insights Generator to Results Display

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save the visualization
visualization_path = "/Users/ahmedmostafa/PycharmProjects/problem_solving/crime_recognition_pipeline.png"
plt.savefig(visualization_path, bbox_inches='tight')
plt.show(), visualization_path
