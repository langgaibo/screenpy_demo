FROM python:3.10.6

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get update && apt-get install -y \
    default-jre \
    google-chrome-stable \
    python3-pip \
    sudo \
    unzip \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Allure
ENV ALLURE_VER=2.17.2
RUN curl -o allure-commandline-${ALLURE_VER}.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VER}/allure-commandline-${ALLURE_VER}.tgz && \
    tar -zxvf allure-commandline-${ALLURE_VER}.tgz -C /opt/ && \
    ln -s /opt/allure-commandline-${ALLURE_VER}/bin/allure /usr/bin/allure
ENV PATH="$PATH:/opt/allure-$ALLURE_VER/bin"

# Install sops
RUN curl -sSL https://github.com/mozilla/sops/releases/download/v3.7.1/sops-v3.7.1.linux \
    -o /usr/bin/sops && \
    chmod +x /usr/bin/sops

# Chrome refuses to run as root without the --no-sandbox option.
# So, let's give it a different account to run with.
# This account is given sudo access so it can start Xvfb as root.
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser -G root appuser  && \
    echo "appuser ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/appuser && \
    chmod 0440 /etc/sudoers.d/appuser && \
    mkdir /home/appuser && \
    chown -R appuser:appuser /home/appuser

USER appuser

ARG PROJECT

COPY --chown=appuser:appuser requirements.txt .env_* /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY --chown=appuser:appuser ${PROJECT} /app/${PROJECT}

WORKDIR /app/${PROJECT}

RUN echo "Configured for the ${PROJECT} project." && mkdir -p /app/${PROJECT}/allure-results
