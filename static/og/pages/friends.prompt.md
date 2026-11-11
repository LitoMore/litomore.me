# Friends

- Image: [Page cover](friends.png)
- Page: [Source](../../../content/pages/friends.md).
- Coverage: one text-free image for the Friends page.
- Generation method: built-in image_gen tool; new generation.
- Prompt template: [OpenGraph documentation](../../../docs/opengraph.md).
- Reference images attached to generation: none.
- Prompt customization: page title and summary only.
- Requested dimensions: 1200 × 630.
- Native dimensions: 1731 × 909.
- Exported dimensions: 1200 × 630.
- Transparent background: false.
- Initial export: ImageMagick point filtering (nearest neighbor), resize to cover, centered crop, strip metadata. Follow-up eye correction recorded below.
- Page publication status: published.

## Exact Generation Prompt

```text
Create a blog cover in the style of a pixel-art video game, with anime-inspired
visual elements and a vibrant, joyful dopamine color palette.

Article: Friends
Summary: A personal blog's collection of links to friends who share writing about analysis, flash fiction, full-stack development, and life, with a warm thank-you to all of them. Evoke friendship, connection, and a welcoming gathering.

Let the article guide the subject, setting, and composition.

Output an opaque landscape image around 1200 × 630, with no text, logos,
or watermark.
```

## Follow-up Edit: Rightmost Girl's Eyes

- Generation method: built-in image_gen tool; edit.
- Edit target: the original 1200 × 630 export of `friends.png` from the generation above, before this correction.
- Edit target SHA-256: `d08874b7e2fbb94020478519feaa398a0c0867b21f821f7c602d152f13f5dd21`.
- Source artwork: original built-in generation `exec-7352ed13-e4ef-44b3-a98a-134cad102d81.png`, exported as described above.
- Reference images attached: the original page cover as the edit target; no additional references.
- Requested dimensions: 1200 × 630.
- Native edit dimensions: 1731 × 909.
- Exported dimensions: 1200 × 630.
- Transparent background: false.
- Export: ImageMagick point filtering (nearest neighbor), resize to cover, centered crop, strip metadata; replaced the page cover with the corrected version.

### Exact Edit Prompt

```text
Use case: precise-object-edit.
Edit the supplied Friends pixel-art cover. Change only the eyes of the purple-haired girl at the far right, who has a pink flower in her hair and holds a notebook. Correct her mismatched, oddly shaped eyes into a natural, consistent pair of anime-style purple eyes, with matching pupils and highlights, aligned to the perspective of her face and looking toward her friends to the left. Keep her happy expression, face shape, mouth, hair, flower, pose, clothing, and notebook unchanged. Preserve every other character, object, background, composition, vivid colors, lighting, and crisp pixel-art style. Make the smallest possible localized correction around her two eyes. Keep the same opaque landscape format, ideally 1200 × 630. Add no text, logos, or watermark.
```


