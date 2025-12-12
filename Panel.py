import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def generer_plan_arcade():
    # --- 1. PARAMÈTRES DU KIT (Selon votre guide) ---
    largeur_totale = 600      # Largeur standard 2 joueurs
    epaisseur_bois = 19       # SPÉCIFIQUE À VOTRE KIT (Mélaminé 19mm)
    
    # Calcul de la largeur des pièces internes (T1, T2, T5, T10, T11)
    largeur_interne = largeur_totale - (2 * epaisseur_bois) 
    
    # --- 2. COORDONNÉES DU PROFIL (Pièces M1 et M2) ---
    # Format: (Profondeur X, Hauteur Y)
    # Origine (0,0) = Coin Bas-Arrière
    
    profil_coords = [
        (0, 0),        # A: Bas Arrière
        (0, 620),      # B: Haut Arrière (Hauteur totale)
        (240, 620),    # C: Haut du Fronton (Toit)
        (260, 480),    # D: Bas du Fronton (Sous le Marquee)
        (260, 200),    # E: Jonction Écran/Panel
        (520, 140),    # F: Nez du Panel (Où on pose les mains)
        (520, 0),      # G: Pied Avant
        (0, 0)         # H: Retour au début
    ]

    # --- AFFICHAGE ---
    fig = plt.figure(figsize=(14, 8))

    # === VUE 3D (À Gauche) ===
    ax = fig.add_subplot(121, projection='3d')
    
    # Création des murs (Joues M1/M2)
    verts_gauche = [[(0, y, z) for y, z in profil_coords]] # X=0
    verts_droite = [[(largeur_totale, y, z) for y, z in profil_coords]] # X=600
    
    # Création des pièces internes (Simplifié)
    pieces_internes = []
    
    # On relie les points correspondants gauche/droite pour simuler les planches
    # C'est une visualisation simplifiée des traverses T1, T2, etc.
    for i in range(len(profil_coords)-1):
        p1 = profil_coords[i]
        p2 = profil_coords[i+1]
        
        # On ne dessine pas l'ouverture avant (entre G et F par exemple pour les jambes)
        # Mais on dessine le toit, le dos, le panel
        piece = [
            (epaisseur_bois, p1[0], p1[1]),
            (epaisseur_bois, p2[0], p2[1]),
            (largeur_totale - epaisseur_bois, p2[0], p2[1]),
            (largeur_totale - epaisseur_bois, p1[0], p1[1])
        ]
        pieces_internes.append(piece)

    # Ajout des polygones
    ax.add_collection3d(Poly3DCollection(verts_gauche, facecolors='#8B4513', edgecolors='k', alpha=0.8, linewidths=1))
    ax.add_collection3d(Poly3DCollection(verts_droite, facecolors='#8B4513', edgecolors='k', alpha=0.8, linewidths=1))
    ax.add_collection3d(Poly3DCollection(pieces_internes, facecolors='#DEB887', edgecolors='k', alpha=0.6))

    # Config Axes 3D
    ax.set_xlim(0, largeur_totale)
    ax.set_ylim(0, 600)
    ax.set_zlim(0, 650)
    ax.set_xlabel('Largeur (mm)')
    ax.set_title(f"Vue 3D (Bois {epaisseur_bois}mm)")
    ax.view_init(elev=20, azim=-50)

    # === VUE 2D PATRON DE DÉCOUPE (À Droite) ===
    ax2 = fig.add_subplot(122)
    
    # Extraction X et Y pour le tracé 2D
    x_vals = [p[0] for p in profil_coords]
    y_vals = [p[1] for p in profil_coords]
    
    ax2.plot(x_vals, y_vals, 'o-', color='black', linewidth=2)
    ax2.fill(x_vals, y_vals, color='#DEB887', alpha=0.5)
    
    # Annotations des cotes sur le plan 2D
    lettres = ['A', 'B (T2)', 'C (T3)', 'D', 'E', 'F (T6)', 'G', 'H']
    for i, txt in enumerate(lettres):
        ax2.annotate(f"{txt}\n{profil_coords[i]}", 
                     (x_vals[i], y_vals[i]), 
                     textcoords="offset points", 
                     xytext=(10,-10), 
                     ha='left',
                     fontsize=9,
                     fontweight='bold',
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.8))

    ax2.set_title("PATRON DE DÉCOUPE (Pièces M1 & M2)")
    ax2.set_xlabel("Profondeur (mm)")
    ax2.set_ylabel("Hauteur (mm)")
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.set_aspect('equal')

    # --- RAPPORT TEXTE ---
    print("="*40)
    print(f"  DIMENSIONS DE DÉCOUPE (Bois {epaisseur_bois}mm)")
    print("="*40)
    print(f"LARGEUR TOTALE BORNE : {largeur_totale} mm")
    print(f"LARGEUR DES PIÈCES INTERNES : {largeur_interne} mm")
    print("-" * 40)
    print("LISTE DE DÉBIT SUGGÉRÉE :")
    print(f"1. FLANCS (M1/M2) x2 : Découper selon le patron (Approx 620x520 mm)")
    print(f"2. FOND (T10)        : {largeur_interne} x 480 mm")
    print(f"3. TOIT (T2)         : {largeur_interne} x 240 mm")
    print(f"4. PORTE ARRIÈRE     : {largeur_interne} x 450 mm")
    print(f"5. SUPPORT ÉCRAN (T5): {largeur_interne} x 400 mm (Ajuster selon l'écran)")
    print(f"6. PANEL (T6/T7)     : {largeur_totale} x 250 mm (Recouvre les côtés)")
    print("-" * 40)
    print("NB: Pour les arrondis (Marquee et Nez), utilisez un bol ou")
    print("    une boite de conserve pour tracer l'angle entre les points.")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generer_plan_arcade()