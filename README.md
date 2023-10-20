# Einleitung

* Dieses Repo dient zum schnellen einrichten eines Python-Repositories mit VSCODE mit src-Ordnerstruktur

# Anleitung

## Vorbereitung für VSCODE

* Entweder kopieren Sie alle Ordner und Dateien des Repos in Ihren neuen Python-Projekt Ordner (ggf. erst herunterladen)
  * https://github.com/rw-haw/23W-AINF-3a/archive/refs/heads/main.zip
* oder Sie clonen das Repo mit git und löschen danach die Repo-Informationen
  * Bash-Variante mit SSH-Authentifizierung
  ```Bash
  git clone git@github.com:rw-haw/empty-python-vscode.git meinProjekt # Clone des Repos wird im Ordner <meinProjekt> erzeugt
  cd meinProjekt # Wechseln in den Repo Ordner
  rm -rf .git # löscht vorhandenen GIT-conntent
  ```
  * Bash-Variante mit SSH-Authentifizierung
  ```Bash
  git clone https://github.com/rw-haw/empty-python-vscode.git meinProjekt # Clone des Repos wird im Ordner <meinProjekt> erzeugt
  cd meinProjekt # Wechseln in den Repo Ordner
  rm -rf .git # löscht vorhandenen GIT-conntent
  ```

## Projekt mit VSCODE

* Öffen Sie den Ordner *meinProjekt* mit VSCODE

### Aufsetzen einer virtuellen Umgebung

* Ggf. zunächst Python Extensions installieren, z.B. *Python Extension Pack*

#### Powershell

* Bestimmen Sie den absoluten Pfad zu Ihrer Python-Executable, z.B. C:\Python311\python.exe

* Öffnen Sie ein Powershell Terminal in VSCODE und führen Sie folgende Befehle aus (Python Pfad ggf. anpassen)

  ```PowerShell
  C:\Python311\python.exe -m venv ENV
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
    python -m pip install pytest numpy matplotlib scipy scikit-image
    ```

  * Für Matplotlib-Arbeiten mit dem PyQt-Backend installieren Sie ebenfalls PyQt5 oder PyQt6

    ```PowerShell
    python -m pip install PyQt6
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


## Clean-Up

* Passen Sie die README.md für Ihr Projekt and und löschen Sie den Ordner docs mit den Screenshots für diese README.

