I am trying to use a minimized LLM mode to convert a bunch of address text into its State, City, Zip Code
I found this postal library which is very cool and does the job.

- I used my Windows WSL System to do this.
  
***Instructions***

- Open PowerShell as Administrator and run:
wsl --install

- Install Dependencies in WSL:
sudo apt update
sudo apt install -y curl autoconf automake libtool pkg-config build-essential

- Build and Install libpostal
  
git clone https://github.com/openvenues/libpostal

cd libpostal

./bootstrap.sh

./configure

make

sudo make install

sudo ldconfig


- pip install postal


  

