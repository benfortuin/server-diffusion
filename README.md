# server-diffusion

Goal: Get Stable Diffusion running on a server as an API to query.

## Fast setup:

1) Run the app locally with uvicorn using `uvicorn main:app`, which should open locally. 
2) Go to url `/docs` to use OpenAPI's template to try POST requests.
3) Click "Try it Out" on the corresponding request and fill in the fields on the right of each colon as formatted.

## TODO:
- Implement Stable Diffusion
- Understand how to return images
- GUI with Jinja2 ?
- Validation with pydantic?

## Sources:
- Documentation: `https://fastapi.tiangolo.com/`
- Main: `https://www.youtube.com/playlist?list=PL0lYY7rL__yJKvrhuIae-SHY7bZm9Vasb`
- Images: `https://medium.com/@chodvadiyasaurabh/building-an-image-conversion-and-serving-api-with-fastapi-c000b0725e2b`
- Rendering: `https://medium.com/featurepreneur/fastapi-render-template-redirection-c98a26ae1e2a`
