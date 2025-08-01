# ShareCode

ShareCode enables multiple participants to work in the code editor online without delays.

## Features

- Collaborative code editing
- No registration required
- Supports Python language
- High performance

## Getting Started

### Installation

```bash
docker pull botersk2023/sharecode
touch docker-compose.yml .env .pg_service.conf .pgpass
```

### Running the App

You need to correctly fill in the following files: docker-compose.yml, .env.
.env example you can find in .env.example.
docker-compose.yml has to have several services: django, postgresql, redis, rabbitmq, prometheus, grafana.

```bash
docker-compose up & docker-compose run
```

The app will be available at [http://localhost:8001](http://localhost:8001).

## Usage

1. Create new room
2. Share your room number with other

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
