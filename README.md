# Classwork Display App
https://dev.to/ysmnikhil/how-to-build-with-react-or-vue-with-vite-and-docker-1a3l
## Introduction

This monolithic application is a showcase of advanced programming techniques and architectural choices, reflecting years of experience in software development. It is designed to display computer information systems (CIS) homework in an interactive manner using a combination of a comprehensive API and a React frontend.

## Technologies

### Frontend

- **NPM**: Node Package Manager for dependency management.
- **Chakra UI, Emotion, and Framer Motion**: For modern, responsive UI design.
- **Vite**: Next-generation frontend tooling for faster development.

### Backend

- **FastAPI**: High-performance web framework for building APIs, with automatic Swagger documentation, and hot-reloading.
- **SQLAlchemy**: SQL toolkit and ORM for database interactions.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Features

### API

- Built with FastAPI, leveraging its asynchronous capabilities for high performance.
- Automatic Swagger documentation is generated from docstrings, ensuring up-to-date and accessible API documentation.
- Example of an endpoint definition:

    ```python
    @app.post("/create-store")
    def create_store_endpoint(store: StoreSchema, db: Session = Depends(get_db)):
        # Endpoint logic here
    ```

### React Frontend

- Developed with React, utilizing Vite for efficient bundling and hot-reload.
- Styling with Chakra UI and Emotion for a polished, interactive UI.
- Example of a React component:

    ```javascript
    function StoreComponent() {
        // Component logic here
    }
    ```

## Installation

Ensure you have Python 3 and NPM installed.

```bash
# Run the start-up script
./start.sh
```

### Development Setup

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Backend:

```bash
cd backend
source ./env/bin/activate
# Install dependencies
npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion
```

## Access URLs

- **React App**: [http://localhost:5173](http://localhost:5173)
- **Fast API**: [http://localhost:8000/](http://localhost:8000/)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

## Architecture and Design Patterns

The application's architecture showcases a sophisticated blend of design patterns and development principles, aiming to create a robust, maintainable, and user-friendly system:

### Facade Design Pattern
I've strategically incorporated the Facade design pattern to simplify interactions with complex subsystems. This pattern acts as a unified interface to a range of interfaces within these subsystems, effectively reducing dependencies and simplifying their usage. By abstracting the underlying complexity, we offer a more straightforward experience for both developers and end-users. This approach not only enhances the system's usability but also significantly improves its maintainability and scalability.

### RESTful API Design
The API is designed with a strong emphasis on RESTful principles, ensuring an intuitive and consistent interaction model. This is further augmented by comprehensive documentation generated through detailed docstrings, integrated seamlessly with Swagger. This documentation strategy not only makes the API more accessible to developers but also aligns with modern web development standards, facilitating ease of use and implementation.

### Advanced Session Management
In handling database interactions, especially crucial in concurrent environments, we employ `db: Session` within our FastAPI endpoints. This usage is pivotal for maintaining data integrity and efficient transaction management. Each request is handled with a distinct database session, provided by SQLAlchemy's session management, ensuring that transactions are isolated and secure. This approach guarantees that any modifications are transactionally consistent and that the database's integrity is upheld, even in the face of concurrent access.


## Future Enhancements

- Integration of a robust authentication system, with a focus on Single Sign-On (SSO) capabilities, potentially using Microsoft technologies.
