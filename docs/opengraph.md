# OpenGraph Image Style and Generation Prompt

Each article on litomore.me uses one text-free pixel game cover, shared by its Chinese and English versions. Save one complete English prompt beside each image. Generate a new illustration for each article's subject, rather than duplicating images for translations.

## Files and Article Metadata

Use the article slug for both files, without language or style suffixes:

```text
static/og/posts/example-post.png
static/og/posts/example-post.prompt.md
```

Both language versions reference the same image in their TOML front matter. Merge the field into an existing `[extra]` table:

```toml
[extra]
images = ["/og/posts/example-post.png"]
```

The prompt file records the image and article source links, generation method, exact submitted prompt, any attached references, requested and returned dimensions, transparency setting, and export or editing steps. Keep prompt records in English. Files under `static/`, including prompt records, are published with the site.

## Visual Direction

The shared visual style has three elements: pixel game artwork, a vivid dopamine color palette, and anime-inspired visual elements.

Let the article determine the subject, setting, and composition. Leave the game genre, era, camera angle, lighting, character presence, and individual colors open. Choose each article's visual idea independently.

Existing image prompt files record what was actually used to generate those images. They are historical records, not the shared style template for future covers.

Generate new covers from the reusable text prompt and article content, without example images or existing covers as style references.

## Reusable Prompt

Fill in the article title and summary in the English prompt below, then submit it once per article. Add article-specific details only when they help communicate its subject. Save the exact submitted version in that image's prompt file.

```text
Create a blog cover in the style of a pixel-art video game, with anime-inspired
visual elements and a vibrant, joyful dopamine color palette.

Article: {title}
Summary: {short summary}

Let the article guide the subject, setting, and composition.

Output an opaque landscape image around 1200 × 630, with no text, logos,
or watermark.
```

## Generate and Export Covers

1. Read the article and choose a visual idea that fits its subject. Keep drafts as drafts. If a draft has no body, use its title as the concept without inventing claims about the article.
2. Generate one cover with the built-in image generation tool using the reusable text prompt and article-specific details. Do not attach reference images. Reuse the selected artwork for every translation.
3. Save the exact submitted English prompt and generation details beside the image. If editing an image, also record the source artwork and exact follow-up instruction.
4. Export an opaque 1200 × 630 PNG using point filtering to retain crisp pixel edges. Center-crop only as needed to fill the canvas, and record these steps.
5. Point every language version's `extra.images` field at the shared image path.
6. Run `zola build` and `zola check --skip-external-links`. Inspect the images and verify that generated OG and Twitter image links use the shared files.

Example export command, run from the project root:

```sh
magick /path/to/generated-image.png -filter point -resize '1200x630^' \
  -gravity center -extent 1200x630 -strip static/og/posts/example-post.png
```

The image generation tool may return a native size different from the requested dimensions. Record the returned size and the final exported size. The prompt captures the generation instructions; export steps describe how the production asset was prepared.
