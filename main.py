
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crown & Country")
clock = pygame.time.Clock()

game_state = "menu"

# Fonts
menu_font = pygame.font.SysFont("arial", 48)

# Main menu title
title = menu_font.render("CROWN & COUNTRY", True, (255, 255, 255))
title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))

# New Game button
new_game_text = menu_font.render("New Game", True, (255, 255, 255))
new_game_button = pygame.Rect(500, 260, 280, 60)
new_game_text_rect = new_game_text.get_rect(center=new_game_button.center)

# Settings button
settings_text = menu_font.render("Settings", True, (255, 255, 255))
settings_button = pygame.Rect(500, 340, 280, 60)
settings_text_rect = settings_text.get_rect(center=settings_button.center)

# Exit button
exit_text = menu_font.render("Exit", True, (255, 255, 255))
exit_game_button = pygame.Rect(500, 420, 280, 60)
exit_text_rect = exit_text.get_rect(center=exit_game_button.center)

# Settings screen
settings_heading_text = menu_font.render("Settings", True, (255, 255, 255))
settings_heading_text_rect = settings_heading_text.get_rect(
    center=(SCREEN_WIDTH // 2, 100)
)

# Back button
back_text = menu_font.render("Back", True, (255, 255, 255))
back_button = pygame.Rect(960, 620, 280, 60)
back_text_rect = back_text.get_rect(center=back_button.center)

# Kingdom Management screen
kingdom_text = menu_font.render("Kingdom Management", True, (255, 255, 255))
kingdom_text_rect = kingdom_text.get_rect(
    center=(SCREEN_WIDTH // 2, 100)
)

# Main game loop
running = True

while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if game_state == "menu":
                    if new_game_button.collidepoint(event.pos):
                        game_state = "playing"

                    elif settings_button.collidepoint(event.pos):
                        game_state = "settings"

                    elif exit_game_button.collidepoint(event.pos):
                        running = False

                elif game_state == "settings":
                    if back_button.collidepoint(event.pos):
                        game_state = "menu"

    # Draw background
    screen.fill((15, 20, 30))

    # Main menu
    if game_state == "menu":
        screen.blit(title, title_rect)

        pygame.draw.rect(screen, (70, 80, 100), new_game_button)
        screen.blit(new_game_text, new_game_text_rect)

        pygame.draw.rect(screen, (70, 80, 100), settings_button)
        screen.blit(settings_text, settings_text_rect)

        pygame.draw.rect(screen, (70, 80, 100), exit_game_button)
        screen.blit(exit_text, exit_text_rect)

    # Kingdom Management screen
    elif game_state == "playing":
        screen.fill((20, 45, 30))
        screen.blit(kingdom_text, kingdom_text_rect)

    # Settings screen
    elif game_state == "settings":
        screen.blit(settings_heading_text, settings_heading_text_rect)

        pygame.draw.rect(screen, (70, 80, 100), back_button)
        screen.blit(back_text, back_text_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
