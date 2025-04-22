# blog
Description: This endpoint returns a list of blog posts to be consumed by a React frontend. Each blog post includes essential information such as title, content preview, author, publish date, and slug for detailed view navigation.  
Method: GET

Response:


Optional Query Parameters:

    ?search= – filter posts by keyword in title or content

    ?author= – filter posts by author

    ?page= – pagination support

Frontend Usage Example:

    Display post previews on the homepage or blog listing page.

    Use the id to fetch a single post via /api/posts/{id}/ for the blog detail page.
