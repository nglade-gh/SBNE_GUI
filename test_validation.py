import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['MPLBACKEND'] = 'Agg'
from Environnement import Simulation, PARAMS

print('Création simulation...')
sim = Simulation(PARAMS, headless=False, max_steps=0, outdir='test_validation')

print('30 pas de simulation...')
for i in range(30):
    sim.step()
print(f'  pop={len(sim.agents)}, steps={sim.total_steps}')

print('Sélection de 4 agents...')
for idx in range(4):
    sim._handle_world_click(int(sim.agents[idx].x), int(sim.agents[idx].y))
print(f'  sélectionnés: {sim.selected_agents}')
assert len(sim.selected_agents) == 4, f'Attendu 4, eu {len(sim.selected_agents)}'

print('Tentative 5e sélection (MAX_SELECTED_SBN=5)...')
sim._handle_world_click(int(sim.agents[4].x), int(sim.agents[4].y))
print(f'  sélectionnés après 5e: {len(sim.selected_agents)}')
assert len(sim.selected_agents) == 5

print('Tentative 6e sélection (doit être refusée)...')
sim._handle_world_click(int(sim.agents[5].x), int(sim.agents[5].y))
print(f'  sélectionnés après 6e: {len(sim.selected_agents)}')
assert len(sim.selected_agents) == 5, 'La limite MAX_SELECTED_SBN ne fonctionne pas!'
# Vérifier que le message d'erreur est dans la console
err_msgs = [m for m in sim.console.messages if m[1] == (230, 70, 70)]
assert err_msgs, 'Pas de message rouge dans la console'
print(f'  message rouge: {err_msgs[-1][0][:60]}...')

print('Désélection agent 2...')
sim._handle_world_click(int(sim.agents[1].x), int(sim.agents[1].y))
print(f'  sélectionnés: {sim.selected_agents}')
assert len(sim.selected_agents) == 4

print('Test _reset_simulation...')
sim._reset_simulation()
assert len(sim.agents) == PARAMS['NUM_AGENTS']
assert sim.total_steps == 0
assert len(sim.selected_agents) == 0
print(f'  pop={len(sim.agents)}, steps={sim.total_steps}, sélectionnés={len(sim.selected_agents)}')

print('Test render...')
sim.render()
print('  render OK')

print('Test handle_events avec événements factices...')
import pygame
pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(500, 500)))
pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
sim.handle_events()
print('  handle_events OK')

print('\n=== TOUS LES TESTS PASSENT ===')
