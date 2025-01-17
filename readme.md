# MNCD - Visualization

This application exposed as a web api is used for different visualizations used in [MNCD application](https://github.com/matejkubinec/mncd-app) and can be also used for different purposes.

## Visualizations

The following charts are supported (ilustrated on the [Florentine dataset](networkdata.ics.uci.edu/netdata/html/florentine.html)):

| Charts                         |                                         |                                             |                                         |
| :----------------------------- | :-------------------------------------: | :-----------------------------------------: | :-------------------------------------: |
| **Single Layer - Network**     |                 Spring                  |                  Circular                   |                 Spiral                  |
|                                |   ![spring](./docs/images/spring.svg)   |   ![circular](./docs/images/circular.svg)   |   ![spiral](./docs/images/spiral.svg)   |
| **Single Layer - Communities** |                 Spring                  |                  Circular                   |                 Spiral                  |
|                                | ![spring-c](./docs/images/spring-c.svg) | ![circular-c](./docs/images/circular-c.svg) | ![spiral-c](./docs/images/spiral-c.svg) |
| **Multi Layer**                |                 Slices                  |                                             |                                         |
|                                |   ![slices](./docs/images/slices.svg)   |                                             |                                         |
| **Multi Layer - Communities**  |                 Slices                  |                                             |                                         |
|                                | ![slices-c](./docs/images/slices-c.svg) |                                             |                                         |
| **Common Charts**              |                 Barplot                 |                   Treemap                   |                                         |
|                                |  ![barplot](./docs/images/barplot.svg)  |    ![treemap](./docs/images/treemap.svg)    |                                         |

## Usage

You can run the application as docker container with the following command:

```sh
docker run --name mncd-viz -p 5050:5050 ghcr.io/matejkubinec/mncd-viz:edge
```

or alternatively with compose:

```yaml
services:
  mncd-viz:
    container_image: mncd-viz
    image: ghcr.io/matejkubinec/mncd-viz:edge
    restart: unless-stopped
    ports:
      - "5050:5050"
```

## Development

To setup the development environment use the following commands:

```sh
# 1. Create virtual environment
make venv

# 2. Install dependencies
make deps

# 3. Run the application
make run
```

## Building docker image

Run the following command to build the docker image:

```sh
make image
```

## License

Licensed under [MIT](./license.txt)
