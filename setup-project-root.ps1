# Define the URL for the file to download
$url = "https://github.com/rw-haw/empty-python-vscode/archive/refs/heads/main.zip"

# Define the name of the zip file
$zipFile = "main.zip"

# Download the file
Invoke-WebRequest -Uri $url -OutFile $zipFile

# Unzip the file
Expand-Archive -Path $zipFile -DestinationPath "."

# Move the contents from the extracted directory
Get-ChildItem -Path "empty-python-vscode-main\*" | Move-Item -Destination "."

# Remove the extracted directory
Remove-Item -Path "empty-python-vscode-main" -Recurse

# Delete the zip file
Remove-Item -Path $zipFile

# Rename 'RENAMETO.env' to '.env'
Rename-Item -Path "RENAMETO.env" -NewName ".env"