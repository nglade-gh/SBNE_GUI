import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['MPLBACKEND'] = 'Agg'
import pygame
from Environnement import Simulation, PARAMS

sim = Simulation(PARAMS, headless=False, max_steps=0, outdir='test_buttons')
for i in range(10):
    sim.step()
# Sélectionner 3 agents pour tester les onglets cerveau
for idx in range(3):
    sim._handle_world_click(int(sim.agents[idx].x), int(sim.agents[idx].y))
sim.handle_events()
sim.render()

# Sauvegarder la capture
pygame.image.save(sim.screen, '/tmp/sbne_buttons.png')
print('Capture OK:', sim.screen.get_size())

# Vérifier les pixels des boutons
checks = [
    (55, 86, 'btn_pause'),
    (155, 86, 'btn_stop'),
    (255, 86, 'btn_restart'),
    (355, 86, 'btn_graphics'),
    (600, 86, 'slider'),
    (695, 86, 'label_refresh'),
    (1380, 86, 'btn_prev'),
    (1470, 86, 'btn_next'),
    (20, 20, 'dashboard'),
    (900, 400, 'world'),
]
for x, y, name in checks:
    print(f'{name} ({x},{y}):', sim.screen.get_at((x, y))[:3])
