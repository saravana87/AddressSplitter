Using libpostal with WSL (Windows Subsystem for Linux)
To convert a bunch of address text into its State, City, and Zip Code, I recommend using the libpostal library, which simplifies the task efficiently. This guide walks you through installing and using the libpostal library on your Windows machine using WSL (Windows Subsystem for Linux).

Step 1: Install WSL (Windows Subsystem for Linux)
Open PowerShell as Administrator and run the following command to install WSL:

powershell
Copy code
wsl --install
This will set up WSL on your machine with Ubuntu as the default distribution. Once the installation is complete, restart your computer.

Step 2: Install Required Dependencies in WSL
After installing WSL, you'll need to install some essential dependencies. Open a WSL terminal (you can open it by typing wsl in the PowerShell window or searching for Ubuntu in your start menu) and run the following commands:

bash
Copy code
sudo apt update
sudo apt install -y curl autoconf automake libtool pkg-config build-essential
Step 3: Build and Install libpostal
Now, clone the libpostal repository, compile, and install it using the following steps:

Clone the repository:
bash
Copy code
git clone https://github.com/openvenues/libpostal
Change into the libpostal directory:
bash
Copy code
cd libpostal
Run the build commands to compile and install libpostal:
bash
Copy code
./bootstrap.sh
./configure
make
sudo make install
Refresh the system's library cache:
bash
Copy code
sudo ldconfig
Step 4: Install the postal Python Package
Once libpostal is successfully installed on your WSL system, you can install the Python wrapper for libpostal:

bash
Copy code
pip install postal
Now you're ready to use libpostal for parsing and extracting useful information from addresses such as State, City, and Zip Code.

Sample Python Code
Here's a sample Python code that uses the postal library to parse an address:

python
Copy code
from postal.parser import parse_address

# Example address
address = "6450 Wheatstone Ct, Maumee, OH 43537"

# Parse the address
parsed = parse_address(address)

# Display parsed components
for component in parsed:
    print(component)
This will give you a parsed version of the address with labels for the components like house_number, road, city, state, postcode, etc.

