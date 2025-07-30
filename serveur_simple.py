# -*- coding: utf-8 -*-
# Auteur: ozGod

import argparse
import http.server
import socketserver

def display_banner():
    """Affiche une bannière stylisée pour l'outil."""
    VERSION = "1.0.0"
    AUTHOR = "ozGod"
    banner = f"""
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🌐 Serveur-Simple v{VERSION}                                ║
║                                                              ║
║  Serveur HTTP minimal pour le partage de fichiers locaux.   ║
║  Créé par {AUTHOR}                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝
"""
    print(banner)

def run_server(host, port):
    """Lance un serveur HTTP simple."""
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Permet la réutilisation rapide de l'adresse
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer((host, port), Handler) as httpd:
        print(f"[*] Serveur démarré à l'adresse http://{host}:{port}")
        print("[*] Le serveur sert les fichiers du répertoire courant.")
        print("[*] Appuyez sur Ctrl+C pour arrêter le serveur.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[*] Arrêt du serveur.")
            httpd.server_close()

def main():
    display_banner()
    parser = argparse.ArgumentParser(
        description="Lance un serveur HTTP simple pour servir les fichiers du répertoire courant.",
        epilog=f"Créé par ozGod."
    )
    parser.add_argument("-H", "--host", default="0.0.0.0", help="L'adresse IP sur laquelle écouter (par défaut: 0.0.0.0 pour toutes les interfaces).")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Le port sur lequel écouter (par défaut: 8000).")

    args = parser.parse_args()

    run_server(args.host, args.port)

if __name__ == "__main__":
    main()
