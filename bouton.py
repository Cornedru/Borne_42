import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generer_plans_final_ultime():
    # --- CONFIGURATION ---
    largeur_panel = 600
    hauteur_panel = 250
    epaisseur_bois_cote = 19
    
    # Diamètres de perçage
    diametre_bouton = 24    # Trou standard
    diametre_joystick = 24  # Passage tige
    diametre_hp = 80
    
    fig = plt.figure(figsize=(15, 12))
    fig.suptitle('PLAN DÉFINITIF - J1 EXTRÊME GAUCHE & FAÇADE DÉCALÉE', fontsize=16, fontweight='bold', color='darkred')

    # ==========================================================
    # 1. LE PANEL DE CONTRÔLE (J1 à 70mm)
    # ==========================================================
    ax1 = fig.add_subplot(311)
    ax1.set_title(f"1. PANEL MANETTES (Dessus) - J1 à 70mm / J2 à 370mm", fontsize=12)
    
    # Planche Panel
    rect = patches.Rectangle((0, 0), largeur_panel, hauteur_panel, linewidth=2, edgecolor='black', facecolor='#DEB887')
    ax1.add_patch(rect)
    
    # Visualisation du Mur Gauche (Zone de danger)
    ax1.add_patch(patches.Rectangle((0, 0), epaisseur_bois_cote, hauteur_panel, color='black', alpha=0.3, hatch='XX'))
    ax1.text(10, 200, "MUR\n19mm", fontsize=7, color='white', ha='center', fontweight='bold')

    # --- POSITIONS JOYSTICKS ---
    j1_x, j1_y = 70, 125  # POSITION EXTRÊME
    j2_x = j1_x + 300     # = 370mm (Ecart standard)
    j2_y = 125

    # --- DESSIN JOUEUR 1 ---
    ax1.add_patch(patches.Circle((j1_x, j1_y), diametre_joystick/2, color='black', fill=False, hatch='//'))
    ax1.text(j1_x, j1_y-32, "JOY 1", ha='center', fontsize=8, fontweight='bold')
    
    # Alerte Plaque de montage (95mm large)
    # Elle va de (70 - 47.5 = 22.5mm) à (70 + 47.5 = 117.5mm)
    # Le mur finit à 19mm. Marge = 3.5mm. ÇA PASSE !
    rect_plaque = patches.Rectangle((j1_x - 47.5, j1_y - 30), 95, 60, fill=False, edgecolor='red', linestyle='--')
    ax1.add_patch(rect_plaque)
    ax1.text(j1_x, j1_y + 35, "Plaque Métal (OK)", color='red', fontsize=6, ha='center')

    # Layout boutons (Standard courbe)
    offset_boutons = [
        (65, 10), (93, 15), (125, 15),   # Bas
        (60, 45), (88, 55), (122, 55)    # Haut
    ]
    
    for dx, dy in offset_boutons:
        bx, by = j1_x + dx, j1_y - 20 + dy
        ax1.add_patch(patches.Circle((bx, by), diametre_bouton/2, color='red', alpha=0.6))
        ax1.plot(bx, by, '+', color='black')

    # --- DESSIN JOUEUR 2 ---
    ax1.add_patch(patches.Circle((j2_x, j2_y), diametre_joystick/2, color='black', fill=False, hatch='//'))
    ax1.text(j2_x, j2_y-32, "JOY 2", ha='center', fontsize=8, fontweight='bold')

    for dx, dy in offset_boutons:
        bx, by = j2_x + dx, j2_y - 20 + dy
        ax1.add_patch(patches.Circle((bx, by), diametre_bouton/2, color='blue', alpha=0.6))
        ax1.plot(bx, by, '+', color='black')

    # Cotations Panel
    ax1.annotate(f"{j1_x}mm", xy=(j1_x, 0), xytext=(j1_x, -20), arrowprops=dict(arrowstyle="->", color='red'), ha='center', color='red')
    ax1.annotate(f"{j2_x}mm", xy=(j2_x, 0), xytext=(j2_x, -20), arrowprops=dict(arrowstyle="->", color='blue'), ha='center', color='blue')
    
    # Espace restant
    limite_j2 = j2_x + 145 + 15
    marge = largeur_panel - limite_j2
    ax1.text(560, 125, f"Marge\n~{int(marge)}mm", ha='center', color='green', fontsize=9, fontweight='bold')

    ax1.set_xlim(-20, largeur_panel + 20)
    ax1.set_ylim(-30, hauteur_panel + 20)
    ax1.set_aspect('equal')

    # ==========================================================
    # 2. FAÇADE AVANT (Décalée Droite +50mm)
    # ==========================================================
    ax2 = fig.add_subplot(312)
    ax2.set_title("2. FAÇADE AVANT (Boutons décalés sous la main droite)")
    
    rect_facade = patches.Rectangle((0, 0), largeur_panel, 120, linewidth=2, edgecolor='black', facecolor='#D2B48C')
    ax2.add_patch(rect_facade)
    
    service_y = 60
    
    # --- CALCUL DÉCALAGE (+50mm par rapport à l'ancien centrage) ---
    # Centrage théorique sous Joystick : J1 - 30mm
    # Nouveau centrage : (J1 - 30) + 50
    
    # JOUEUR 1
    # J1 est à 70mm
    sel1_x = (70 - 30) + 50   # = 90mm
    sta1_x = (70 + 30) + 50   # = 150mm
    
    ax2.add_patch(patches.Circle((sel1_x, service_y), diametre_bouton/2, color='white', ec='black'))
    ax2.text(sel1_x, service_y, "SEL 1", ha='center', va='center', fontsize=7)
    
    ax2.add_patch(patches.Circle((sta1_x, service_y), diametre_bouton/2, color='white', ec='black'))
    ax2.text(sta1_x, service_y, "STA 1", ha='center', va='center', fontsize=7)

    # Axe Joystick 1 (Pour visualiser le décalage)
    ax2.plot([70, 70], [0, 120], 'k:', alpha=0.3)
    ax2.text(70, 10, "Axe Joy1", fontsize=6, color='gray', ha='center')

    # HOTKEY (Toujours au centre)
    ax2.add_patch(patches.Circle((300, service_y), diametre_bouton/2, color='yellow', ec='black'))
    ax2.text(300, service_y, "HOTKEY", ha='center', va='center', fontsize=6)

    # JOUEUR 2
    # J2 est à 370mm
    sel2_x = (370 - 30) + 50  # = 390mm
    sta2_x = (370 + 30) + 50  # = 450mm
    
    ax2.add_patch(patches.Circle((sel2_x, service_y), diametre_bouton/2, color='white', ec='black'))
    ax2.text(sel2_x, service_y, "SEL 2", ha='center', va='center', fontsize=7)
    
    ax2.add_patch(patches.Circle((sta2_x, service_y), diametre_bouton/2, color='white', ec='black'))
    ax2.text(sta2_x, service_y, "STA 2", ha='center', va='center', fontsize=7)

    # Axe Joystick 2
    ax2.plot([370, 370], [0, 120], 'k:', alpha=0.3)
    ax2.text(370, 10, "Axe Joy2", fontsize=6, color='gray', ha='center')

    # Cotes de perçage Façade
    ax2.annotate(f"{sel1_x}", xy=(sel1_x, service_y+20), xytext=(sel1_x, service_y+40), 
                 arrowprops=dict(arrowstyle="->", color='red'), ha='center', color='red', fontsize=8, fontweight='bold')
    ax2.annotate(f"{sel2_x}", xy=(sel2_x, service_y+20), xytext=(sel2_x, service_y+40), 
                 arrowprops=dict(arrowstyle="->", color='blue'), ha='center', color='blue', fontsize=8, fontweight='bold')

    ax2.set_xlim(-20, largeur_panel + 20)
    ax2.set_ylim(0, 130)
    ax2.set_aspect('equal')

    # ==========================================================
    # 3. PLANCHE HAUT-PARLEURS (Standard)
    # ==========================================================
    ax3 = fig.add_subplot(313)
    ax3.set_title("3. PLANCHE HAUT-PARLEURS (Interne)")
    largeur_interne = 600 - (2 * epaisseur_bois_cote) # = 562
    rect_hp = patches.Rectangle((0, 0), largeur_interne, 120, linewidth=2, edgecolor='black', facecolor='#DEB887')
    ax3.add_patch(rect_hp)
    
    hp_y = 60
    ax3.add_patch(patches.Circle((largeur_interne/4, hp_y), diametre_hp/2, color='gray', alpha=0.5, hatch='..'))
    ax3.text(largeur_interne/4, hp_y, "HP GAUCHE", ha='center', va='center')
    ax3.add_patch(patches.Circle((largeur_interne*3/4, hp_y), diametre_hp/2, color='gray', alpha=0.5, hatch='..'))
    ax3.text(largeur_interne*3/4, hp_y, "HP DROIT", ha='center', va='center')
    
    ax3.set_xlim(-20, largeur_interne + 20)
    ax3.set_ylim(0, 140)
    ax3.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generer_plans_final_ultime()