#### Basic procedure for using this:
1. Create a new git repository on github.com, using this repository as a template, navigate to the new directory
2. Modify ./docker-compose.yml and docker-compose.prod.yml to update image: my_project_python to project name
3. Build the Docker image using docker-compose build
4. Use docker-compose up jupyter to launch a jupyter lab session, the token is default set to "local".
5. Call docker-compose run shell in order to launch a command line within the container
6. Use conda env export --from-history in order to build new environment.yml, copy into docker/environment.yml outside of the container.
7. Call docker-compose build again to test if newly installed packages fix the issue.

#### To create python executable scripts for running remotely
1. docker-compose run shell
2. jupyter nbconvert --to python notebooks/*.ipynb --output-dir code/
3. exit
4. Modify docker-compose.prod.yml to include desired python scripts
5. Build into a package using the following commands
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml push

#### On remote deployment location
1. docker pull cdalldorf/my_project_python:latest
2. docker run -v $(pwd)/output:/output cdalldorf/my_project_python:latest python /code/1_test.py
3. Now this depends on architecture, but it seems like you can just run this as any normal docker container

#### to do's in the future:
1. Figure out the Channing server and create a different docker-compose-prod file in order to properly prepare things to be sent and run there.
2. Create two environments, test and production, as you will likely not want to bother generating plots and installing visualization depndencies when running large computational projects.



# Below is the text from the original branch:

Example template to use Conda + Docker for reproducible, easy to deploy models.

Blog post goes into more detail - find it here:

https://binal.pub/2018/10/data-science-with-docker-and-conda/

#### How to Use This All

As an example - here's my normal development process. Using it I can get from development to production with little friction, knowing that my code will work as expected, and that it won't negatively affect other processes on the production server.

##### Developing and Packaging

1. Clone the template down. Update the `environment.yml` as needed with packages I know I'll need, and run `docker-compose build`. This will build the development image with all the packages I defined installed within it.
2. Create a `.env_dev` file with development environment variables
3. Run `docker-compose up` and navigate to JupyterLab, which will be running on [http://localhost:8888](http://localhost:8888). We can access it by entering in the token `local_dev`.
4. From there prototype and develop a model/process using Jupyter Notebooks, saving any notebooks I create along the way into `/notebooks` as a development diary. Any final artifacts/models I plan on using in production I save within `/code`.
5. Once I have a final version of my code, save it (and any models it relies on) into `/code`.
6. Update the `docker-compose.prod.yml` file's `command` section to point to the my scripts' name, and the `image` section to point to my docker registry (something like my_registry/my_project:0.1).
7. Run `docker-compose -f docker-compose.prod.yml build` - this builds the production version of the image, packaging everything in the `/code` and `/notebooks` directories directly onto the image.
8. Run `docker-compose -f docker-compose.prod.yml push` which pushes that packaged image into my organizations docker registry.

At this point I now have an image that contains all my code, models, and other artifacts I need, that's preinstalled with exact versions of the Python packages and dependencies I require. It's stored in a central location where I can easily pull it down onto other servers.
