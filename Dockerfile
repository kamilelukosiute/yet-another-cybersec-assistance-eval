FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    sudo \
    build-essential \
    gcc \
    curl \
    xclip \
    sqlite3 \
    gdb \
    libssl-dev \
    python3.12 \
    python3.12-venv \
    python3.12-dev \
    python3-pip \
    git \
    x11-apps \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Remove the EXTERNALLY-MANAGED file if it exists
RUN rm -f /usr/lib/python3.12/EXTERNALLY-MANAGED

# Create a virtual environment and activate it
RUN python3.12 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy scipy numba Pillow python-chess requests

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Ensure Rust binaries are in PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Set Python 3.12 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1

# Set the working directory in the container
WORKDIR /usr/src/app

# Command to run when the container launches
CMD ["/bin/bash"]

ENV DISPLAY=:99

# Start Xvfb when container launches
CMD Xvfb :99 -screen 0 1024x768x16 & \
    tail -f /dev/null
