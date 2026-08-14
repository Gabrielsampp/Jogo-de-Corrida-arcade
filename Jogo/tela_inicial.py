def tela_inicial (TELA):
    running = True

    BG_INIT = pygame.image.load("Imagens/bg-tela-inicial.png").convert()
    BG_INIT = pygame.transform.scale(BG_INIT, (500, 700))

    while running:
        #eventos de entrada
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == k_KP_ENTER or event.key == K_RETURN:
                    running = False
            
            TELA.blit(BG_INIT, (0,0))
            pygame.display.flip()