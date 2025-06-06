# Einleitung

* Dieses Repo dient zum schnellen Einrichten eines Python-Repositories mit VSCODE mit src-Ordnerstruktur und pytest unit-Testing

# Anleitung

## Prerequisites Windows

* Das Aktivieren von virtuellen Python-Umgebungen und Ausführen von Powershell-Skripten muss einmalig aktiviert werden
* Öffnen eine Powershell, führen Sie folgenden Befehl aus und bestätigen Sie mit *J*:
  ```Powershell
    # Ausführen in Powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    # Bestätigen mit "J"
  ```

## Vorbereitung für VSCODE

### Vorbereitung per Skript

* Erstellen Sie Ihren Projekt-Ordner und wechseln Sie dahin mit einer Powershell (Windows) oder Terminal/Bash (MacOS/ Linux) und kopieren Sie dahin die Dateien `setup-project-root.ps1` (Windows) `setup-project-root.sh` (MacOS/ Linux)
* Führen Sie das entsprechende Skript aus
  * Windows
  ```Powershell
    # Ausführen in Powershell
    ./setup-project-root.ps1
  ```
  * Terminal/Bash
  ```bash
    # Execute in Terminal
    ./setup-project-root.sh
  ```
### Manuelle Vorbereitung
* Entweder kopieren Sie alle Ordner und Dateien des Repos in Ihren neuen Python-Projekt Ordner (ggf. erst herunterladen)
  * https://github.com/rw-haw/empty-python-vscode/archive/refs/heads/main.zip
* oder Sie clonen das Repo mit git und löschen danach die Repo-Informationen
  * Bash-Variante mit SSH-Authentifizierung
  ```Bash
  git clone git@github.com:rw-haw/empty-python-vscode.git meinProjekt # Clone des Repos wird im Ordner <meinProjekt> erzeugt
  cd meinProjekt # Wechseln in den Repo Ordner
  rm -rf .git # löscht vorhandenen GIT-conntent
  ```
  * Bash-Variante mit Web-Authentifizierung
  ```Bash
  git clone https://github.com/rw-haw/empty-python-vscode.git meinProjekt # Clone des Repos wird im Ordner <meinProjekt> erzeugt
  cd meinProjekt # Wechseln in den Repo Ordner
  rm -rf .git # löscht vorhandenen GIT-conntent
  ```

## Projekt mit VSCODE

* Öffen Sie den Ordner *meinProjekt* mit VSCODE

### Aufsetzen einer virtuellen Umgebung

* Ggf. zunächst Python Extensions installieren, z.B. *Python Extension Pack*

#### Terminal

* Bestimmen Sie den absoluten Pfad zu Ihrer Python-Executable, z.B. C:\Python311\python.exe

  * Mac/ Linux: `python3`

* Öffnen Sie ein Powershell Terminal in VSCODE und führen Sie folgende Befehle aus (Python Pfad ggf. anpassen)

  * Windows
    ```PowerShell
    C:\Python311\python.exe -m venv ENV
    ```
  * Mac/ Linux
    ```PowerShell
    python3 -m venv ENV
    ```

  ![](./docs/ENV_01.png)

* Öffnen Sie `dummy.py` im Editor
  
  ![](./docs/ENV_02.png)

  * ENV sollte jetzt in der Powershell erkannt werden. Machen Sie ein Relaunch der Powershell oder schließen Sie das Terminal und öffnen ein neues
  
    ![](./docs/ENV_03.png)

  * Verifizieren Sie die ENV im Terminal

    ```PowerShell
    python -c "import sys;print(sys.executable)"
    ```
    Dies sollte den Pfad zu der ENV-Umgebung enthalten.

    ![](./docs/ENV_05.png)

  * Installieren Sie benötigte Python-Pakete in der Umgebung über das Terminal mit dem Paketmanager *pip*

    ```PowerShell
    # pytest
    python -m pip install pytest
    ```

  * Für Matplotlib-Arbeiten mit dem PyQt-Backend installieren Sie ebenfalls PyQt5 oder PyQt6

    ```PowerShell
    # Optional für Anwendungen mit Matplotlib
    python -m pip install matplotlib pyqt5
    ```

    * Ggf. benötigen Sie weitere build-Tools. Beachten Sie Hiweise in der Ausgabe bei gescheiterten Installationen des Pakets

#### Python-Dateien

* Öffnen Sie `dummy.py` im Editor
* Selektieren Sie ENV, falls noch nicht automatisch erkannt

  ![](./docs/ENV_04.png)

* Definieren Sie den Ordner *src* als Basis Ordner Ihrer Module, indem Sie *RENAMEMETO.env* umbenennen in *.env* oder verschieben Sie die Datei mit

  ```PowerShell
  mv .\RENAMETO.env .env
  ```

  * Mac/ Linux: 
    * Die .env Datei sollte `PYTHONPATH=src` enthalten oder den absoluten Pfad zu src: `PYTHONPATH=/.../src` ('...' entsprechend anpassen)
    * Zusätzlich erstellen Sie im Projektordner einen Ordner `.vscode` und darin eine Datei `settings.json` mit folgendem Inhalt:
    
      ```bash
      {
      "terminal.integrated.env.osx": {
        "PYTHONPATH": "${workspaceFolder}/src",
      },
      "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}/src",
      },
      "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src",
      },
      "python.envFile": "${workspaceFolder}/.env"
      }
      ```

  In der Datei `dummy.py` sollten jetzt das Modul `myModule` auch erkannt werden.

  ![](./docs/ENV_06.png)

### Python Unit-Testing mit pytest

* Wechseln Sie zum Unit-Test Menü von VSCODE (Reagenzglas)

  ![](./docs/unit-tests_01.png)

* Wählen Sie *Configure Python Tests* aus und wählen Sie dann pytest als Framework aus

  ![](./docs/unit-tests_02.png)

Und wählen Sie das *root*-directory aus

* Verifizieren Sie, dass es keine Fehler bei der Suche nach Tests gibt:

  ![](./docs/unit-tests_03.png)

  * Starten Sie einen Test mittels *Play*-Button

    ![](./docs/unit-tests_04.png)
    ![](./docs/unit-tests_05.png)

    Grüne Haken zeigen an, dass der Test ohne Fehler ausgeführt wurde.
#### Probleme

* pytest import-Fehler - Paket mit Modul in src können nicht gefunden werden
  
  * Mac/ Linux: Verwendung absoluter Pfade in .env-Datei kann helfen; ggf. Umgebungvariable `PYTHONPATH` bereits in der eigenen `.bashrc`

  * ggf. cache-Dateien löschen

    * `.pytest_cache`-Ordner
  
  * ggf. python.testing settings aus der `.vscode/settings.json` löschen

  * ggf. Neustart von VSCODE, insbesondere, wenn Umgebungsvariablen angepasst wurden in .bashrc oder in .env

Weitere Ansätze:

* https://pytest-with-eric.com/

* https://pytest-with-eric.com/introduction/pytest-pythonpath/

### Run-And-Debug Python-Dateien mit VSCODE einrichten

* Wechseln Sie zum Debug-Menü
  
  ![](./docs/debug_01.png)

* Wählen Sie *create a launch.json file* und selektieren Sie *Python File*
  
  ![](./docs/debug_02.png)

* Wechseln Sie auf `dummy.py`, setzen Sie einen Breakpoint und starten Sie den Debugger mit dem *Play*-Button

  ![](./docs/debug_03.png)
* Es sollte nun möglich sein, Ihr Skript zu debuggen
  
  ![](./docs/debug_04.png)

  * Es sollte möglich sein in die Funktion `dummy_method` (im Ordner src) hinein zu wechseln:

    ![](./docs/debug_05.png)

### ENV in interaktiven Python-Skripten und Konsolen

* Öffnen Sie `dummy_interactive.py` und führen Sie die erste Cell aus

  ![](./docs/interactive_01.png)

* ENV sollte automatisch erkannt werden. Installieren Sie das *ipykernel* Paket

  ![](./docs/interactive_02.png)

### ENV in Jupyter-Notebook-Dateien

* Öffnen Sie `dummy.ipynb` und wählen Sie den richtigen Kernel aus

  ![](./docs/ipynb_01.png)

* Wählen Sie *Python Environments* und selektieren Sie ENV aus der Liste

  ![](./docs/ipynb_02.png)
  ![](./docs/ipynb_03.png)

* Verifizieren Sie ENV indem Sie die Cell fehlerfrei ausführen lassen
  ![](./docs/ipynb_04.png)


# Clean-Up

* Passen Sie die README.md für Ihr Projekt and und löschen Sie den Ordner **docs** mit den Screenshots für diese README.

# Installation des Moduls

* Dieses Dummy-Repository ist darauf ausgelegt, dass man die in *src* liegenden Module (z.B. `my_package`) mittels pip auch installieren kann.

## Lokale Installation in eine neue ENV

* Erstellen einer ENV
* Aktivieren der ENV
* Installation von *meinProjekt*-Paketen
  * `pip install -e` installiert im Developer*in-Modus, d.h. die Module können am Ursprungsort noch nachträglich verändert werden. Ist der Developer*in-Modus nicht gewünscht, dann die Option `-e` einfach weglassen.
* Testen des `my_package`
    
  ```PowerShell
  C:\Python311\python.exe -m venv ENV
  .\ENV\Scripts\Activate.ps1
  python -m pip install -e ..\meinProjekt\
  python -c "import my_package.dummy_module as d; d.dummy_method()"
  ```

  * Mac/ Linux:

  ```bash
  python3 -m venv ENV
  source ./ENV/bin/activate
  python -m pip install -e ..\meinProjekt\
  python -c "import my_package.dummy_module as d; d.dummy_method()"
  ```

  ![](./docs/install_myModule_01.png)

**Hinweise:**

* Informationen zu Autor*innen und Lizenzen sollten vor einer Verbreitung entsprechend angepasst werden.

# Weiterführende Informationen und Hinweise

* Das src-Layout ist nicht-flach. Mehr Informationen dazu [https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
