# Python Development Environment Template

This is a template repository for setting up a Python development environment with Docker. It provides a consistent development environment that can be easily shared across team members.

## Features

- 🐳 Docker-based development environment
- 🔄 Hot-reloading for development
- 🐍 Python 3.11 with essential development tools
- 🔍 Debugging support with VS Code
- 📦 Dependency management with requirements.txt
- 🧪 Testing environment setup

## Project Structure

```
.
├── src/                    # Source code directory
├── tests/                  # Test files
├── .vscode/                # VS Code configuration
├── .gitignore              # Git ignore rules
├── Dockerfile              # Development environment configuration
├── docker-compose.yml      # Docker services configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Getting Started

1. Clone this repository
2. Start the development environment:
   ```bash
   # First time setup or after configuration changes
   docker-compose up --build
   
   # Subsequent runs
   docker-compose up
   ```
3. Connect VS Code to the container:
   - Install the "Dev Containers" extension in VS Code
   - Press F1 or Ctrl+Shift+P to open the command palette
   - Type "Remote-Containers: Attach to Running Container"
   - Select the running container from the list
   - VS Code will open a new window connected to the container
4. Access the application at http://localhost:8000

## Development Workflow

### Running the Application
```bash
docker-compose up
```

### Running Tests
```bash
docker-compose exec web pytest
```

### Debugging
- The environment is configured for VS Code debugging
- Debug port is exposed on 5678
- Use the VS Code "Python: Remote Attach" configuration
- Add the following configuration to your `.vscode/launch.json`:
  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Python: Remote Attach",
        "type": "python",
        "request": "attach",
        "connect": {
          "host": "localhost",
          "port": 5678
        },
        "pathMappings": [
          {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/app"
          }
        ],
        "justMyCode": true
      }
    ]
  }
  ```

### Adding Dependencies
1. Add new packages to `requirements.txt`
2. Rebuild the container:
   ```bash
   docker-compose build
   ```

### Adding Platform Dependencies
1. Add new system packages to the `apt-get install` section in the `Dockerfile`
2. Rebuild the container:
   ```bash
   docker-compose build
   ```

## Environment Configuration

- Development server runs on port 8000
- Debug port is 5678
- Redis service is available on port 6379
- Source code is mounted as a volume for live updates

## License

This template is available under the MIT License.
