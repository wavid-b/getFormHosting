# Check if Python is installed
try {
    $pythonVersion = python --version
    Write-Host "Python is installed. Version: $pythonVersion"
} catch {
    Write-Host "Python is not installed."
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe" -OutFile "$env:TEMP\python_installer.exe"
    Start-Process -Wait -FilePath "$env:TEMP\python_installer.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"
}

# Check if pip is installed
try {
    $pipVersion = pip --version
    Write-Host "Pip is installed. Version: $pipVersion"
} catch {
    Write-Host "Pip is not installed."
    Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "$env:TEMP\get-pip.py"
    Start-Process -Wait -FilePath "python" -ArgumentList "$env:TEMP\get-pip.py"
}

Write-Host "Python and pip are installed"

# Check if main.py and getForm.py in src folder
if (!(Test-Path "./src/main.py")) {
    Write-Host "main.py not found in src folder. Exiting..."
    exit
}
if (!(Test-Path "./src/getForm.py")) {
    Write-Host "getForm.py not found in src folder. Exiting..."
    exit
}

#install dependencies
Write-Host "Installing dependencies..."
#installing pandas
pip3 install pandas
#installing numpy
pip3 install numpy
#installing flask
pip3 install flask
#installing unidecode
pip3 install unidecode

#run the main.py function
python3 ./src/main.py

#open the browser to localhost:8000
Write-Host "Opening browser to app"
Start-Process "http://localhost:8000"