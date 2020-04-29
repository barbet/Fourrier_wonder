import matplotlib as mpl

def export_animation_to_mp4(animation, name):
    Writer = mpl.animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='TristanBarbe'), bitrate=1800)
    animation.save(f'./videos/{name}.mp4', writer=writer)