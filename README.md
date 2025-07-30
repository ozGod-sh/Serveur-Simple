# 🌐 Serveur-Simple - Serveur HTTP Minimal

**Créé par ozGod-sh**

## Description

Serveur-Simple est un serveur HTTP minimal basé sur la bibliothèque standard Python qui permet de partager rapidement des fichiers locaux via HTTP. Idéal pour les tests de développement, le partage de fichiers temporaire et les démonstrations.

## Fonctionnalités

### 🚀 Serveur HTTP complet
- **Partage de fichiers** : Sert tous les fichiers du répertoire courant
- **Navigation web** : Interface de navigation dans les dossiers
- **Configuration flexible** : Host et port personnalisables
- **Arrêt propre** : Gestion du Ctrl+C

### 🔧 Simplicité d'utilisation
- **Aucune configuration** : Fonctionne immédiatement
- **Interface claire** : Affichage des informations de connexion
- **Réutilisation d'adresse** : Redémarrage rapide possible
- **Multi-interface** : Écoute sur toutes les interfaces ou spécifique

## Installation

### Prérequis
- Python 3.6+
- Aucune dépendance externe (utilise la bibliothèque standard)

### Installation
```bash
cd Serveur-Simple
# Aucune installation requise - utilise uniquement la stdlib Python
```

## Utilisation

### Syntaxe de base
```bash
python serveur_simple.py [OPTIONS]
```

### Options disponibles
- `-H, --host HOST` : Adresse IP d'écoute (défaut: 0.0.0.0)
- `-p, --port PORT` : Port d'écoute (défaut: 8000)
- `-h, --help` : Affiche l'aide

### Exemples d'utilisation

#### 1. Serveur basique (port 8000)
```bash
python serveur_simple.py
```

#### 2. Port personnalisé
```bash
python serveur_simple.py -p 9000
```

#### 3. Écoute locale uniquement
```bash
python serveur_simple.py -H 127.0.0.1 -p 8080
```

#### 4. Configuration complète
```bash
python serveur_simple.py --host 192.168.1.100 --port 3000
```

## Structure des fichiers

```
Serveur-Simple/
├── serveur_simple.py    # Script principal
└── README.md           # Cette documentation
```

## Cas d'usage

### Développement web
- **Tests locaux** : Servir des fichiers HTML/CSS/JS
- **Prototypage** : Tester rapidement des sites statiques
- **Debug** : Vérifier le comportement des ressources
- **Démonstrations** : Présenter des projets web

### Partage de fichiers
- **Transfert rapide** : Partager des fichiers sur le réseau local
- **Collaboration** : Permettre l'accès à des ressources
- **Backup temporaire** : Accès distant aux fichiers
- **Distribution** : Distribuer des fichiers sans serveur complexe

### Tests de sécurité
- **Serveur de test** : Héberger des payloads de test
- **Simulation** : Créer des environnements de test
- **Callback server** : Recevoir des callbacks HTTP
- **Hosting temporaire** : Héberger des preuves de concept

## Exemple de sortie

### Démarrage du serveur
```
╔══════════════════════════════════════════════════════════╗
║                                                              ║
║  🌐 Serveur-Simple v1.0.0                                ║
║                                                              ║
║  Serveur HTTP minimal pour le partage de fichiers locaux.   ║
║  Créé par ozGod                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════╝

[*] Serveur démarré à l'adresse http://0.0.0.0:8000
[*] Le serveur sert les fichiers du répertoire courant.
[*] Appuyez sur Ctrl+C pour arrêter le serveur.
```

### Arrêt du serveur
```
^C
[*] Arrêt du serveur.
```

## Fonctionnalités du serveur

### Navigation web
- **Listing de répertoires** : Affiche le contenu des dossiers
- **Navigation** : Liens cliquables pour naviguer
- **Téléchargement** : Clic droit pour télécharger les fichiers
- **Retour parent** : Lien pour remonter dans l'arborescence

### Types de fichiers supportés
- **HTML/CSS/JS** : Servis avec les bons Content-Types
- **Images** : JPG, PNG, GIF, SVG affichées dans le navigateur
- **Documents** : PDF, TXT, MD accessibles
- **Archives** : ZIP, TAR téléchargeables
- **Tous formats** : Aucune restriction sur les types de fichiers

## Configuration réseau

### Adresses d'écoute
- **0.0.0.0** : Toutes les interfaces (défaut)
- **127.0.0.1** : Localhost uniquement
- **IP spécifique** : Interface réseau particulière

### Ports recommandés
- **8000** : Port par défaut (non-privilégié)
- **8080** : Alternative courante
- **3000-9000** : Plage de développement
- **80** : Port HTTP standard (nécessite privilèges root)

## Sécurité et limitations

### ⚠️ Avertissements de sécurité
- **Pas d'authentification** : Accès libre à tous les fichiers
- **Pas de chiffrement** : Trafic en clair (HTTP)
- **Exposition complète** : Tous les fichiers du répertoire sont accessibles
- **Pas de logs** : Aucun enregistrement des accès

### Limitations techniques
- **Mono-thread** : Une requête à la fois
- **Pas de cache** : Pas de gestion de cache HTTP
- **Pas de compression** : Pas de gzip/deflate
- **Basique** : Fonctionnalités HTTP minimales

## Intégration avec d'autres outils

### Tests de développement
```bash
# Servir un site statique
cd /path/to/website
python /path/to/serveur_simple.py -p 8000

# Tester avec curl
curl http://localhost:8000/index.html
```

### Partage de fichiers
```bash
# Partager des documents
cd ~/Documents/shared
python serveur_simple.py -H 0.0.0.0 -p 9000
# Accessible via http://IP_MACHINE:9000
```

### Scripts d'automatisation
```python
import subprocess
import time
import requests

# Démarrer le serveur en arrière-plan
server = subprocess.Popen(['python', 'serveur_simple.py', '-p', '8001'])
time.sleep(1)  # Attendre le démarrage

# Tester la connectivité
response = requests.get('http://localhost:8001')
print(f"Server status: {response.status_code}")

# Arrêter le serveur
server.terminate()
```

## Alternatives et comparaisons

### Serveurs Python similaires
```bash
# Module http.server standard
python -m http.server 8000

# Avec répertoire spécifique
python -m http.server 8000 --directory /path/to/files

# Serveur HTTPS
python -m http.server 8000 --bind 127.0.0.1
```

### Avantages de Serveur-Simple
- **Interface claire** : Messages informatifs
- **Gestion d'erreurs** : Arrêt propre avec Ctrl+C
- **Personnalisation** : Code modifiable facilement
- **Pédagogique** : Code source simple à comprendre

### Serveurs plus avancés
- **nginx** : Serveur web professionnel
- **Apache** : Serveur web complet
- **Node.js http-server** : Serveur Node.js simple
- **Python Flask** : Framework web avec plus de fonctionnalités

## Utilisation avancée

### Serveur HTTPS (modification possible)
```python
import ssl

# Ajouter le support SSL/TLS
httpd.socket = ssl.wrap_socket(httpd.socket, 
                              certfile='./server.pem', 
                              server_side=True)
```

### Authentification basique (extension)
```python
import base64

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header or not self.check_auth(auth_header):
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="Restricted"')
            self.end_headers()
            return
        super().do_GET()
    
    def check_auth(self, auth_header):
        # Vérifier les credentials
        pass
```

### Logs personnalisés
```python
import logging

logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(message)s')

class LoggingHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info(f"{self.client_address[0]} - {format % args}")
```

## Dépannage

### Problèmes courants

#### Port déjà utilisé
```bash
# Erreur: [Errno 98] Address already in use
# Solution: Utiliser un autre port
python serveur_simple.py -p 8001

# Ou trouver le processus utilisant le port
netstat -tulpn | grep :8000
kill <PID>
```

#### Permissions insuffisantes
```bash
# Erreur: Permission denied (port < 1024)
# Solution: Utiliser sudo ou un port > 1024
sudo python serveur_simple.py -p 80
# Ou
python serveur_simple.py -p 8080
```

#### Accès depuis d'autres machines
```bash
# Problème: Pas d'accès depuis le réseau
# Solution: Utiliser 0.0.0.0 au lieu de 127.0.0.1
python serveur_simple.py -H 0.0.0.0

# Vérifier le firewall
sudo ufw allow 8000
```

## Bonnes pratiques

### Sécurité
- **Répertoire dédié** : Ne pas servir depuis des répertoires sensibles
- **Réseau local** : Utiliser uniquement sur des réseaux de confiance
- **Durée limitée** : Arrêter le serveur après utilisation
- **Surveillance** : Monitorer les accès si nécessaire

### Performance
- **Fichiers légers** : Éviter de servir de très gros fichiers
- **Réseau local** : Utiliser sur le même réseau pour de meilleures performances
- **Répertoire organisé** : Structurer les fichiers pour faciliter la navigation

## Extensions possibles

### Interface web améliorée
- CSS personnalisé pour le listing
- Icônes par type de fichier
- Barre de recherche
- Upload de fichiers

### Fonctionnalités avancées
- Authentification utilisateur
- Logs détaillés
- Compression gzip
- Cache HTTP
- Support WebDAV

## Sécurité et éthique

⚠️ **Utilisation responsable**
- Ne pas exposer de fichiers sensibles
- Utiliser sur des réseaux de confiance uniquement
- Arrêter le serveur après utilisation
- Respecter les politiques de sécurité de l'organisation

## Licence

MIT License - Voir le fichier LICENSE pour plus de détails.

---

**Serveur-Simple v1.0.0** | Créé par ozGod-sh