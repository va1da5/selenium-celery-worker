# Selenium + Celery

This is a minimal project to test possibility of running Selenium with Firefox in a container and expose this functionality as Celery task.

The current setup contains simple capture of rendered HTML page content by loaded Javascript. Additionally, it uses a different User-Agent with each request. Lastly, the page is opened in a private tab meaning that cookies and other data do not persist between requests.

## Get Started

1. Install local Python dependencies

    ```bash
    make install
    ```

2. Create local variables files

    ```bash
    make .env
    ```

3. Pull required container images

    ```bash
    make pull
    ```

4. Build Celery worker container image

    ```bash
    make build
    ```

5. Start containers

    ```bash
    make start
    ```

6. Test task execution on a remote worker

    ```bash
    python exec_remote_task.py -u http://google.com
    ```

## References

-   [Selenium with Python](https://selenium-python.readthedocs.io/)
-   [SeleniumHQ/docker-selenium](https://github.com/SeleniumHQ/docker-selenium)
-   [Celery.send_task()](https://docs.celeryproject.org/en/stable/reference/celery.html#celery.Celery.send_task)
