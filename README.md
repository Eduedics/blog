Blog API

A Django-powered RESTful API that delivers blog post data to a React frontend. It fetches content in real-time from Twitter using the Twitter API, enabling dynamic blog post previews and detailed views.
GitHub

Features

    Fetches blog posts with:

        Title

        Content preview

        Author

        Publish date


    Real-time data retrieval from Twitter posts using the Twitter API

    Supports filtering by keyword and author

    Pagination support for efficient data handling
API Endpoint

GET /api/posts/
Query Parameters

    search: Filter posts by keyword in title or content

    author: Filter posts by author

    page: Pagination support

Response:
    [
  {
    "id": 1,
    "title": "Understanding Django REST Framework",
    "content_preview": "An introduction to DRF and how it simplifies API development...",
    "author": "Jane Doe",
    "publish_date": "2025-05-15",
    "slug": "understanding-django-rest-framework"
  },
  ...
]

Prerequisites

    Python 3.8+

    pip

    Twitter Developer Account (for API keys)
Installation

    Clone the repository:
        git clone https://github.com/Eduedics/blog.git
        cd blog
    Create and activate a virtual environment:
        python -m venv venv
        source venv/bin/activate 
    Install dependencies:
        pip install -r requirements.txt
    Configure Twitter API credentials:
        Create a .env file in the project root and add your Twitter API keys:
        TWITTER_API_KEY=your_api_key
        TWITTER_API_SECRET=your_api_secret
        TWITTER_ACCESS_TOKEN=your_access_token
        TWITTER_ACCESS_SECRET=your_access_secret
    Apply migrations:
        python manage.py makemigrations
        python manage.py migrate
    Run the development server:
        python manage.py runserver
    Access the API at http://127.0.0.1:8000/api/posts/.
Frontend Integration

    This API is designed to be consumed by a React frontend. Each blog post includes essential information such as title, content preview, author, publish date, and id for detailed view navigation.
    Example Usage
        Display post previews on the homepage or blog listing page.
        Use the slug to fetch a single post via /api/posts/{id}/ for the blog detail page.
Testing:
    python manage.py test
Contributing
    Contributions are welcome! Please fork the repository and submit a pull request.
License
    This project is licensed under the MIT License.
For more information, visit the Eduedics/blog GitHub repository.

