## First step 

```bash
uv init
uv add fastapi uvicorn pydantic
```

## passwordManager.py

Creating the password Manager class in order to simply to word 

```python
import string
import random
import re
```

## Building the API
I decided to build a home page for the API and to render the HTML Jinja must be installed.
Now that I'm thinking of it it's usually installed when we install Flask or Django

```bash
uv add jinja2
```
### Use a bit of tailwindCSS

Learned tailwind css recently so I decided to see if I could use it without installing complete setup  

```html
<script src="https://cdn.tailwindcss.com"></script>
```
And it works but I'm not sure it's the best solution

## Deploying on vercel

```bash
 npm i -g vercel
```
